"""
Módulo: Guia de Desenvolvimento - O Nerd
==========================================

Este guia fornece instruções para desenvolvedores que desejam
contribuir ou estender a funcionalidade do O Nerd.

Conteúdo:
- Arquitetura da aplicação
- Padrões de código
- Como adicionar novos comandos
- Configuração de desenvolvimento
"""

# =============================================================================
# ARQUITETURA DO PROJETO
# =============================================================================

"""
O Nerd segue uma arquitetura modular e bem estruturada:

config.py
├── Configurações centralizadas
├── Constantes globais
├── API keys
└── Dicionários de aplicativos e comandos

commands.py
├── Execução de comandos do sistema
├── Abertura de aplicativos
├── Pesquisas
└── Validação de segurança

voice.py
├── Reconhecimento de fala (input)
├── Síntese de voz (output)
└── Gerenciamento de áudio

chat.py
├── Interface de texto puro
└── Loop de conversação

o_nerd.py / start.py
├── Interface completa (texto + voz)
├── Detecção de comandos
└── Loop principal

automation.py
└── Automação avançada (cliques, digitação, etc)
"""

# =============================================================================
# PADRÕES DE CÓDIGO
# =============================================================================

"""
Siga estas convenções ao adicionar código:

1. DOCSTRINGS (Obrigatório)
   ✓ Use docstrings em todas as funções
   ✓ Descreva parâmetros e retorno
   ✓ Use formato Google-style
   
   Exemplo:
   def minha_funcao(param1: str, param2: int) -> str:
       \"\"\"Descrição breve.
       
       Descrição mais longa se necessário.
       
       Args:
           param1: Descrição do primeiro parâmetro
           param2: Descrição do segundo parâmetro
           
       Returns:
           Descrição do retorno
       \"\"\"
       return "resultado"

2. TYPE HINTS (Obrigatório)
   ✓ Use type hints em todos os parâmetros
   ✓ Use type hints no retorno
   ✓ Importe de typing se necessário
   
   from typing import Optional, List, Dict
   def funcao(lista: List[str], opcao: Optional[str] = None) -> Dict[str, int]:
       ...

3. NOMES DE VARIÁVEIS (Importante)
   ✓ Use snake_case para variáveis e funções
   ✓ Use UPPER_CASE para constantes
   ✓ Nomes descritivos e significativos
   
   ✓ CORRETO:
     user_input = input()
     MAX_HISTORY_SIZE = 20
     
   ✗ ERRADO:
     ui = input()
     max = 20

4. TRATAMENTO DE ERROS
   ✓ Use try/except específicos
   ✓ Sempre forneça mensagens de erro úteis
   ✓ Nunca engula exceções silenciosamente
   
   try:
       resultado = executar_operacao()
   except ValueError as error:
       print(f"[ERRO] Valor inválido: {error}")
   except Exception as error:
       print(f"[ERRO] Problema inesperado: {error}")

5. COMENTÁRIOS
   ✓ Use comentários para explicar "por quê", não "o quê"
   ✓ Mantenha comentários limpos e atualizados
   ✓ Use separadores para seções
   
   # =========== Seção de Inicialização ===========
   # Calibra o microfone com duração de 0.5s para
   # evitar problemas com ruído ambiente
   recognizer.adjust_for_ambient_noise(source, duration=0.5)
"""

# =============================================================================
# COMO ADICIONAR NOVOS COMANDOS
# =============================================================================

"""
Passo 1: Defina a função em commands.py

def meu_comando(parametro: str) -> str:
    \"\"\"
    Descrição breve.
    
    Args:
        parametro: Descrição
        
    Returns:
        Mensagem de resultado
    \"\"\"
    try:
        # Implementação
        resultado = fazer_algo(parametro)
        return f"✓ Sucesso: {resultado}"
    except Exception as error:
        return f"❌ Erro: {error}"


Passo 2: Registre em execute_command()

def execute_command(command_type: str, args: Optional[str] = None) -> Optional[str]:
    commands = {
        "open_website": lambda: open_website(args),
        "meu_comando": lambda: meu_comando(args),  # ← Adicione aqui
        ...
    }
    if command_type in commands:
        return commands[command_type]()
    return None


Passo 3: Adicione detecção em o_nerd.py

def detect_command(user_input: str) -> tuple:
    text = user_input.lower().strip()
    
    # Comando existente
    if "abrir youtube" in text:
        return ("open_website", "youtube")
    
    # Seu novo comando
    if "meu comando" in text:
        parametro = text.replace("meu comando", "").strip()
        return ("meu_comando", parametro)
    
    return ("chat", None)
"""

# =============================================================================
# CONFIGURAÇÃO DE DESENVOLVIMENTO
# =============================================================================

"""
Ambiente de Desenvolvimento Recomendado:

1. Instale as ferramentas de desenvolvimento:
   pip install -r requirements.txt
   pip install pytest black pylint mypy

2. Configure seu IDE (VS Code recomendado):
   - Extensão: Python
   - Extensão: Pylance
   - Extensão: Black Formatter

3. Estruture seu fluxo de trabalho:
   - Faça uma branch para cada feature
   - Escreva testes antes do código (TDD)
   - Use git commits descritivos
   
   git checkout -b feature/novo-comando
   # ... desenvolvimento ...
   git commit -m "feat: add novo comando de demonstração"
   git push origin feature/novo-comando

4. Antes de fazer push:
   - Formate com Black: black .
   - Verifique com Pylint: pylint *.py
   - Execute testes: pytest
   - Verifique types: mypy commands.py

5. Padrão de commit:
   feat: novo comando/feature
   fix: correção de bug
   refactor: reorganização de código
   docs: atualização de documentação
   test: adicionar testes
"""

# =============================================================================
# ESTRUTURA DE CLASSES PROFISSIONAL
# =============================================================================

"""
Use orientação a objetos para funcionalidades complexas:

class MinhaFuncionalidade:
    \"\"\"Descrição da classe.\"\"\"
    
    def __init__(self, parametro: str):
        \"\"\"Inicializa a classe.
        
        Args:
            parametro: Descrição
        \"\"\"
        self.parametro = parametro
        self.estado = None
    
    def processar(self) -> str:
        \"\"\"Processa algo.
        
        Returns:
            Resultado do processamento
        \"\"\"
        try:
            self.estado = "processando"
            resultado = self._implementacao_interna()
            self.estado = "concluído"
            return resultado
        except Exception as error:
            self.estado = "erro"
            raise
    
    def _implementacao_interna(self) -> str:
        \"\"\"Método privado com implementação interna.\"\"\"
        return f"Resultado: {self.parametro}"
"""

# =============================================================================
# TESTES UNITÁRIOS
# =============================================================================

"""
Exemplo de teste com pytest:

# test_commands.py
import pytest
from commands import is_dangerous_command, execute_command

def test_dangerous_command():
    \"\"\"Testa se comandos perigosos são detectados.\"\"\"
    assert is_dangerous_command("deletar arquivo") == True
    assert is_dangerous_command("pesquisar python") == False

def test_execute_command():
    \"\"\"Testa execução de comando.\"\"\"
    resultado = execute_command("get_time")
    assert resultado is not None
    assert "horas" in resultado

@pytest.fixture
def setup_test():
    \"\"\"Configuração para testes.\"\"\"
    yield  # Teste rodar aqui
    # Limpeza após teste

def test_com_fixture(setup_test):
    \"\"\"Teste usando fixture.\"\"\"
    ...
"""

# =============================================================================
# BOAS PRÁTICAS
# =============================================================================

"""
✓ SEMPRE:
  - Escreva código legível e bem documentado
  - Use type hints
  - Trate exceções apropriadamente
  - Mantenha funções pequenas (single responsibility)
  - Teste seu código antes de fazer commit
  - Use variáveis significativas
  - Respeite limites de linha (~100 caracteres)

✗ NUNCA:
  - Use variáveis globais (use classes/funções)
  - Ingira exceções silenciosamente
  - Deixe código comentado para sempre
  - Use print() para debugging (use logging)
  - Comita código quebrado
  - Use nomes de variáveis curtos (a, b, x)
  - Deixe código duplicado (refatore)

⚠️  CUIDADO COM:
  - Imports circulares
  - Modificação de listas/dicts durante iteração
  - Manutenção de estado em variáveis globais
  - Performance em loops aninhados
  - Vazamento de memória
"""

# =============================================================================
# RECURSOS ÚTEIS
# =============================================================================

"""
Documentação:
- Python: https://docs.python.org/3/
- Google Gemini: https://ai.google.dev/
- SpeechRecognition: https://github.com/Uberi/speech_recognition
- PyAutoGUI: https://pyautogui.readthedocs.io/

Tutoriais:
- Type Hints: https://pep257.pycqa.org/
- docstring: https://www.python.org/dev/peps/pep-0257/
- PEP 8: https://pep8.org/

Ferramentas:
- Black (Formatter): https://github.com/psf/black
- Pylint (Linter): https://www.pylint.org/
- Mypy (Type Checker): https://www.mypy-lang.org/
- Pytest (Testing): https://pytest.org/
"""
