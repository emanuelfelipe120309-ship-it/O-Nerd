# O Nerd - Assistente de IA para Windows

<div align="center">

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

**Um assistente virtual inteligente e completo para Windows que combina IA com automação de sistema.**

[Features](#features) • [Instalação](#instalação) • [Uso](#como-usar) • [Configuração](#configuração) • [Suporte](#suporte)

</div>

---

## 📋 Sobre

**O Nerd** é um assistente de IA alimentado por Google Gemini que transforma seu PC em um assistente virtual inteligente. Com suporte a texto e voz, pode executar comandos, abrir aplicativos, fazer pesquisas e muito mais.

### Construído Com
- **Google Gemini 1.5 Flash** - Motor de IA avançado
- **Python 3.9+** - Linguagem principal
- **Speech Recognition** - Reconhecimento de fala em português
- **pyttsx3** - Síntese de voz natural
- **PyAutoGUI** - Automação inteligente de sistema

---

## ✨ Features

### 🤖 Inteligência Artificial
✅ Conversas naturais em português brasileiro
✅ Responde a qualquer tipo de pergunta
✅ Referências geek e piadas inteligentes
✅ Histórico de conversa mantido
✅ Personalidade única e divertida

### 💻 Controle Completo do Sistema
✅ Abrir qualquer aplicativo instalado
✅ Abrir websites e fazer pesquisas
✅ Consultar data e hora
✅ Detalhes do sistema
✅ Controle de volume do PC

### 🎤 Entrada de Voz
✅ Reconhecimento de fala via microfone
✅ Síntese de fala em português
✅ Modo texto puro
✅ Configuração de velocidade de fala

### ⚡ Automação Avançada
✅ Digitar texto automaticamente
✅ Pressionar teclas especiais
✅ Clicar em posições da tela
✅ Automação completa de aplicativos

### 🔒 Segurança Robusta
✅ Validação de comandos perigosos
✅ Lista de bloqueio inteligente
✅ Isolamento de processos
✅ Confirmações de ações críticas

---

## 🚀 Instalação

1. **Execute o instalador:**
   ```
   SETUP_AUTOINICIO.bat
   ```
   Isto irá:
   - ✅ Instalar todas as dependências
   - ✅ Configurar a chave da API
   - ✅ Registrar O Nerd para iniciar com Windows

2. **Pronto!** O Nerd está instalado e rodará automaticamente na próxima vez que você ligar o PC

### Opção 2: Instalação Manual

```powershell
# 1. Abra PowerShell na pasta do O Nerd

# 2. Instale as dependências
pip install -r requirements.txt

# 3. Configure a variável de ambiente (já vem pre-configurada)
$env:GOOGLE_API_KEY='AIzaSyB-LMlukCeYQ3fHlGVJiwaKRCCahZ6aJBw'

# 4. Inicie o daemon
python daemon.py
```

---

## 🎤 Como Usar

### Modo Texto
```
python o_nerd.py
```
Depois digite suas perguntas ou comandos

### Modo Voz (Daemon)
```
python daemon.py
```
Ou use os atalhos:
- `START_ONERD.bat` - Iniciar O Nerd
- `run_voice_mode.bat` - Modo voz
- `run_text_mode.bat` - Modo texto

---

## ⚠️ IMPORTANTE: Chave da API Google Gemini

O projeto usa a **API Google Generative AI (Gemini)** que funciona com um limite gratuito.

### Se receber erro "Quota Exceeded":

1. **Obtenha sua chave gratuita:**
   - Acesse: https://aistudio.google.com/app/apikey
   - Clique em "Get API Key"
   - Selecione "Create API key in existing project"

2. **Configure sua chave:**
   
   **Windows (Permanente):**
   - Abra "Variáveis de Ambiente do Sistema"
   - Clique em "Variáveis de Ambiente"
   - Nova → Nome: `GOOGLE_API_KEY` Valor: `sua_chave_aqui`
   - Restart o PC

   **Ou temporário (Command Prompt/PowerShell):**
   ```
   set GOOGLE_API_KEY=sua_chave_aqui
   python o_nerd.py
   ```

3. **Use uma chave maior se precisar:**
   - Ative o plano pago em https://ai.google.dev/dashboard
   - Crie um projeto no Google Cloud
   - Configure billing

---

## 🎤 Como Usar

### Ativar O Nerd

Diga em voz alta: **"O Nerd"** ou **"Oi Nerd"**

O Nerd vai responder: "Sim? Como posso ajudar?"

### Exemplos de Comandos

#### Abrir Aplicativos
```
"O Nerd, abra o Discord"
"O Nerd, abre o YouTube"
"O Nerd, abra o VSCode"
"O Nerd, abre o Notepad"
```

Aplicativos suportados:
- **Discord** - Chat e voz
- **YouTube** - Vídeos
- **Chrome/Firefox** - Navegadores
- **VSCode** - Editor de código
- **Notepad** - Bloco de notas
- **Calculadora** - Cálculos
- **PowerShell** - Terminal
- **Explorer** - Gerenciador de arquivos
- ...e muito mais!

#### Executar Ações Automáticas
```
"O Nerd, abra YouTube e pesquise sobre células moleculares"
"O Nerd, abra Google e busque inteligência artificial"
"O Nerd, pesquise Machine Learning no YouTube"
```

Assim o O Nerd irá:
1. Abrir o aplicativo (YouTube/Google)
2. Buscar automaticamente pelo termo
3. Mostrar os resultados

#### Informações do Sistema
```
"O Nerd, que horas são?"
"O Nerd, qual é a data de hoje?"
"O Nerd, informações do sistema"
```

#### Perguntas Gerais
```
"O Nerd, o que é inteligência artificial?"
"O Nerd, qual é a capital da França?"
"O Nerd, me conte uma piada"
```

---

## ⚙️ Configuração

### Variáveis de Ambiente

A chave da API do Gemini já está configurada:
```
GOOGLE_API_KEY=AIzaSyB-LMlukCeYQ3fHlGVJiwaKRCCahZ6aJBw
```

Se precisar alterar, edite `run_daemon.bat` ou `run_onerd.bat`

### Personalização

Edite `config.py` para:
- Adicionar mais aplicativos em `WINDOWS_APPS`
- Adicionar mais websites em `SAFE_APPS`
- Alterar a personalidade em `SYSTEM_PROMPT`
- Mudar o wake word em `WAKE_WORD`

---

## 📂 Estrutura de Arquivos

```
O Nerd/
├── daemon.py                 # Gerencia O Nerd como serviço
├── o_nerd.py                # Núcleo do assistente
├── config.py                # Configurações e APIs
├── commands.py              # Executores de comandos
├── voice.py                 # Entrada/saída de áudio
├── automation.py            # Automação de aplicativos
├── wake_word.py            # Detecção de "O Nerd"
├── requirements.txt         # Dependências Python
├── run_daemon.bat          # Inicia O Nerd em background
├── run_onerd.bat           # Inicia O Nerd interativo
├── SETUP_AUTOINICIO.bat    # Configuração automática
├── START_ONERD.bat         # Instalação + execução
└── README.md               # Este arquivo
```

---

## 🔧 Troubleshooting

### O Nerd não escuta meu microfone
- Verifique se o Windows tem permissão para acessar o microfone
- Teste o microfone em outro app (Discord, WhatsApp, etc)
- Reinicie o O Nerd

### Não reconhece minha voz
- Fale mais claramente em português
- Reduz ruído de fundo
- Tente treinar o reconhecimento do Windows

### API não funciona
- Verifique a chave em `run_daemon.bat`
- Teste a conexão de internet
- Verifique se a chave é válida em `test_gemini.py`

### Aplicativo não abre
- Verifique se o app está instalado
- Tente abrir pelo nome em português ou inglês
- Adicione o app em `config.py` se não estiver listado

---

## 📚 Exemplos Avançados

### Sequência de Ações
```
"O Nerd, abra o YouTube e pesquise sobre Python"
```
Resultado:
1. YouTube abre
2. Campo de busca fica ativo
3. "Python" é digitado automaticamente
4. Pesquisa é executada

### Integração com Desktop
O Nerd roda como um serviço Windows e pode ser:
- Chamado de qualquer lugar na tela
- Integrado com outras aplicações
- Usado como atalho para tarefas repetitivas

---

## 🔐 Segurança

O Nerd possui proteção contra comandos perigosos:
- ❌ Não executa comandos de exclusão (delete, apagar)
- ❌ Não formata drives
- ❌ Não executa operações de sistema crítico
- ❌ Não modifica registry

---

## 🎯 Roadmap Futuro

- [ ] Suporte a mais idiomas
- [ ] Controle de smart home
- [ ] Integração com Google Calendar
- [ ] Envio de emails por voz
- [ ] Suporte a múltiplos usuários
- [ ] Interface gráfica
- [ ] Histórico de conversas

---

## 💬 Feedback

Encontrou um bug? Tem uma sugestão?
Sinta-se livre para contribuir e melhorar O Nerd!

---

**Desenvolvido por:** Dev Manu o Nerd  
**Versão:** 1.0 (December 2025)  
**Licença:** MIT

---

## 🎓 Aprenda Mais

- [Google Gemini API](https://ai.google.dev/)
- [SpeechRecognition Library](https://github.com/Uberi/speech_recognition)
- [PyAutoGUI Docs](https://pyautogui.readthedocs.io/)

---

**Happy coding! 🚀**
#   O - N e r d 
 
 #   O - N e r d  
 #   O - N e r d  
 