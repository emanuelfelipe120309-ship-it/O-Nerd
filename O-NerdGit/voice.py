"""
O Nerd - Módulo de Voz
=======================

Gerencia entrada de áudio por microfone e saída de áudio sintetizado.
Responsável pelo reconhecimento de fala e síntese de voz.

Autor: O Nerd Development Team
Versão: 2.0
"""

import sys
from typing import Optional

try:
    import speech_recognition as sr
    SPEECH_RECOGNITION_AVAILABLE = True
except ImportError:
    SPEECH_RECOGNITION_AVAILABLE = False
    print("[AVISO] speech_recognition não instalado. Voz desabilitada.")

try:
    import pyttsx3
    TEXT_TO_SPEECH_AVAILABLE = True
except ImportError:
    TEXT_TO_SPEECH_AVAILABLE = False
    print("[AVISO] pyttsx3 não instalado. Síntese de voz desabilitada.")

from config import LANGUAGE, VOICE_RATE, VOICE_VOLUME, ASSISTANT_NAME


class VoiceAssistant:
    """
    Gerenciador de entrada e saída de voz.
    
    Encapsula a funcionalidade de:
    - Reconhecimento de fala via microfone
    - Síntese de texto em fala
    """
    
    AUDIO_TIMEOUT = 5
    AUDIO_PHRASE_LIMIT = 10
    
    def __init__(self):
        """Inicializa o assistente de voz e tenta configurar microfone e TTS."""
        self.recognizer: Optional[sr.Recognizer] = None
        self.microphone: Optional[sr.Microphone] = None
        self.engine: Optional[pyttsx3.engine.Engine] = None
        
        self._initialize_speech_recognition()
        self._initialize_text_to_speech()
    
    def _initialize_speech_recognition(self) -> None:
        """Inicializa o reconhecedor de fala e microfone."""
        if not SPEECH_RECOGNITION_AVAILABLE:
            return
        
        try:
            self.recognizer = sr.Recognizer()
            self.microphone = sr.Microphone()
            
            # Calibra o microfone para ruído ambiente
            with self.microphone as source:
                self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
            
            print("[✓] Microfone configurado com sucesso")
        
        except Exception as error:
            print(f"[AVISO] Erro ao configurar microfone: {error}")
            self.microphone = None
    
    def _initialize_text_to_speech(self) -> None:
        """Inicializa o motor de síntese de voz."""
        if not TEXT_TO_SPEECH_AVAILABLE:
            return
        
        try:
            self.engine = pyttsx3.init()
            
            # Configura propriedades de voz
            self.engine.setProperty('rate', VOICE_RATE)
            self.engine.setProperty('volume', VOICE_VOLUME)
            
            # Tenta encontrar voz em português
            voices = self.engine.getProperty('voices')
            portuguese_voice_found = False
            
            for voice in voices:
                voice_name = voice.name.lower()
                if 'brazil' in voice_name or 'português' in voice_name or 'portuguese' in voice_name:
                    self.engine.setProperty('voice', voice.id)
                    portuguese_voice_found = True
                    break
            
            if portuguese_voice_found:
                print("[✓] Voz em português configurada")
            else:
                print("[AVISO] Voz em português não encontrada. Usando voz padrão.")
        
        except Exception as error:
            print(f"[AVISO] Erro ao configurar TTS: {error}")
            self.engine = None
    
    def speak(self, text: str) -> None:
        """
        Fala um texto em voz alta.
        
        Args:
            text: Texto a ser falado
        """
        # Exibe o texto no console
        print(f"\n{ASSISTANT_NAME}: {text}")
        
        # Tenta sintetizar a voz
        if not self.engine:
            return
        
        try:
            self.engine.say(text)
            self.engine.runAndWait()
        except Exception as error:
            print(f"[AVISO] Erro ao falar: {error}")
    
    def listen(self) -> Optional[str]:
        """
        Ouve áudio do microfone e converte para texto.
        
        Returns:
            Texto reconhecido ou None se houver erro
        """
        if not self.recognizer or not self.microphone:
            print("[ERRO] Microfone não disponível")
            return None
        
        try:
            with self.microphone as source:
                print("[🎤 Ouvindo...]")
                
                # Captura áudio com timeout
                audio = self.recognizer.listen(
                    source,
                    timeout=self.AUDIO_TIMEOUT,
                    phrase_time_limit=self.AUDIO_PHRASE_LIMIT
                )
            
            # Tenta reconhecer a fala
            try:
                text = self.recognizer.recognize_google(
                    audio,
                    language=LANGUAGE
                )
                print(f"✓ Você disse: {text}")
                return text.lower()
            
            except sr.UnknownValueError:
                print("[AVISO] Não consegui entender. Pode repetir?")
                return None
            
            except sr.RequestError as error:
                print(f"[ERRO] Problema com serviço de reconhecimento: {error}")
                return None
        
        except sr.WaitTimeoutError:
            print("[AVISO] Tempo limite excedido. Nenhuma fala detectada.")
            return None
        
        except Exception as error:
            print(f"[ERRO] Problema ao ouvir: {error}")
            return None
    
    def is_voice_available(self) -> bool:
        """Verifica se reconhecimento de voz está disponível."""
        return SPEECH_RECOGNITION_AVAILABLE and self.microphone is not None
    
    def is_tts_available(self) -> bool:
        """Verifica se síntese de voz está disponível."""
        return TEXT_TO_SPEECH_AVAILABLE and self.engine is not None


def get_voice_assistant() -> VoiceAssistant:
    """
    Cria e retorna uma instância do assistente de voz.
    
    Returns:
        Instância de VoiceAssistant pronta para uso
    """
    return VoiceAssistant()

