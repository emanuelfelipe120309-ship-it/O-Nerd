"""
O Nerd - Exemplos de Uso Avançado
===================================

Demonstrações práticas e casos de uso do O Nerd.
"""

# =============================================================================
# EXEMPLO 1: CONVERSAS COMPLEXAS
# =============================================================================

"""
O Nerd mantém histórico de conversa para conversas mais naturais:

Você: Qual é a capital da França?
O Nerd: A capital da França é Paris, uma das cidades mais belas do mundo...

Você: Quantos habitantes tem?
O Nerd: Paris tem aproximadamente 2,2 milhões de habitantes na cidade...
        (entende que "tem" se refere a Paris)

Você: E qual é a moeda usada lá?
O Nerd: Na França, a moeda é o Euro...
        (mantém contexto de que falamos sobre a França)
"""

# =============================================================================
# EXEMPLO 2: AUTOMAÇÃO PRÁTICA
# =============================================================================

"""
Sequência de comandos para produtividade:

1. Abrir Ambiente de Desenvolvimento
   Você: Abra meu ambiente de trabalho
   O Nerd: Abrindo VS Code, Discord, Spotify...
   
2. Pesquisar Documentação
   Você: Pesquise sobre async await em Python no Google
   O Nerd: Abrindo pesquisa no Google...
   
3. Consultar Sistema
   Você: Como está o desempenho do PC?
   O Nerd: [Mostra informações do sistema]
   
4. Controlar Áudio
   Você: Aumente o volume para 70%
   O Nerd: Volume ajustado para 70%
"""

# =============================================================================
# EXEMPLO 3: DESENVOLVIMENTO COM O NERD
# =============================================================================

"""
Auxílio ao desenvolvimento de código:

Você: Escreva uma função Python que valida email
O Nerd: [Fornece código validado]

```python
import re

def validar_email(email: str) -> bool:
    '''Valida formato de email.'''
    padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(padrao, email) is not None

# Testes
assert validar_email("usuario@example.com") == True
assert validar_email("invalido@") == False
```

Você: Como otimizar este código?
O Nerd: [Oferece sugestões de melhoria]
"""

# =============================================================================
# EXEMPLO 4: APRENDIZADO E CONSULTORIA
# =============================================================================

"""
O Nerd é ótimo para aprendizado:

Você: Explique orientação a objetos em Python para iniciantes
O Nerd: Orientação a Objetos (OOP) é um paradigma que organiza código
        em "objetos" que contêm dados (atributos) e ações (métodos)...

Você: Dê um exemplo prático
O Nerd: [Fornece exemplo com classe Carro]

Você: Como isso é diferente de procedural?
O Nerd: [Explica diferenças]

Você: Qual é melhor?
O Nerd: Depende do contexto, mas OOP é melhor para projetos grandes...
"""

# =============================================================================
# EXEMPLO 5: CRIATIVIDADE E ENTRETENIMENTO
# =============================================================================

"""
O Nerd também é divertido:

Você: Me conte uma piada de programador
O Nerd: Por que programadores preferem o toilet ao banheiro?
        Porque o toilet funciona como esperado! 😄

Você: Faça um acróstico para PROGRAMAÇÃO
O Nerd: 
P - Processamento lógico de dados
R - Rotinas eficientes e rápidas
O - Objetos bem estruturados
G - Gerenciamento inteligente
R - Resoluções criativas
A - Algoritmos otimizados
M - Máquinas que entendem
Ã - Ações precisas
O - Organização perfeita

Você: Qual é a melhor linguagem de programação?
O Nerd: [Resposta equilibrada sobre trade-offs de cada linguagem]
"""

# =============================================================================
# EXEMPLO 6: CUSTOMIZAÇÃO
# =============================================================================

"""
Customize o O Nerd para seus usos específicos:

1. Adicionar seus próprios aplicativos em config.py:

WINDOWS_APPS = {
    ...
    "meu app": "C:/Caminho/Para/Meu/App.exe",
    "projeto": "C:/Meus Documentos/Projeto/",
}

2. Modificar o SYSTEM_PROMPT para diferentes personalidades:

# Modo Formal
SYSTEM_PROMPT = "Você é um assistente profissional e formal..."

# Modo Geek
SYSTEM_PROMPT = "Você é um nerd entusiasmado que adora tecnologia..."

# Modo Tutor
SYSTEM_PROMPT = "Você é um professor paciente que explica tudo..."

3. Adicionar novos comandos em commands.py:

def meu_comando_customizado(parametro: str) -> str:
    return f"Executei meu comando com {parametro}"

Depois registrar em execute_command():
"meu_comando": lambda: meu_comando_customizado(args),
"""

# =============================================================================
# EXEMPLO 7: INTEGRAÇÃO COM OUTROS SCRIPTS
# =============================================================================

"""
Use O Nerd em seus próprios scripts Python:

from commands import execute_command
from voice import get_voice_assistant

# Abrir aplicativo programaticamente
resultado = execute_command("open_app", "discord")
print(resultado)  # "Abrindo Discord..."

# Fazer pesquisa
resultado = execute_command("search_google", "Python async await")
print(resultado)  # "Pesquisando por 'Python async await' no Google..."

# Usar reconhecimento de voz em seu código
voice = get_voice_assistant()
if voice.is_voice_available():
    texto = voice.listen()
    print(f"Usuário disse: {texto}")
    voice.speak("Recebi seu comando!")
"""

# =============================================================================
# EXEMPLO 8: FLUXO DE TRABALHO TÍPICO
# =============================================================================

"""
Rotina matinal com O Nerd:

08:00 - Iniciar O Nerd
        Você: Bom dia, que dia é hoje?
        O Nerd: Hoje é segunda-feira, 21 de dezembro de 2025

08:01 - Abrir ferramentas de trabalho
        Você: Abra Discord, Spotify e VS Code
        O Nerd: Abrindo Discord, Spotify e VS Code...

08:02 - Pesquisar tarefas
        Você: Pesquise sobre REST API Python
        O Nerd: [Abre Google com a pesquisa]

08:30 - Informações do sistema
        Você: Como está o PC?
        O Nerd: [Mostra dados do sistema]

08:45 - Conversa sobre problemas
        Você: Estou com erro 404 no meu código
        O Nerd: 404 significa página/recurso não encontrado...
                [Oferece soluções]

Você: Obrigado, foi útil!
O Nerd: De nada! Fico feliz em ajudar! 😊
"""

# =============================================================================
# EXEMPLO 9: MODO VOTO POR VOZ
# =============================================================================

"""
Interação via voz (fones com microfone):

[Aperta atalho configurado ou diz "Hey Nerd"]

Você: (fala) Que horas são?
O Nerd: (sintetizado) Agora são 14 horas e 32 minutos.

Você: (fala) Abre YouTube
O Nerd: (sintetizado) Abrindo YouTube...

Você: (fala) Pesquise sobre machine learning
O Nerd: (sintetizado) Pesquisando por machine learning no Google...

Você: (fala) Qual é o resultado de 15 vezes 8?
O Nerd: (sintetizado) 15 vezes 8 é igual a 120.
"""

# =============================================================================
# EXEMPLO 10: DEBUGGING E TROUBLESHOOTING
# =============================================================================

"""
O Nerd ajuda a encontrar problemas:

Você: Por que meu código está lento?
O Nerd: Há várias razões comuns:
        1. Loops aninhados ineficientes
        2. Operações de I/O bloqueantes
        3. Estruturas de dados inadequadas
        4. Falta de indexação em bancos
        
        Você pode compartilhar o código para análise?

Você: [Compartilha o código]
O Nerd: Encontrei alguns problemas:
        - Linha 45: Você está iterando para cada item de uma lista
        - Sugestão: Use list comprehension
        - Linha 78: Operação de arquivo está fora do loop
        [Fornece sugestões de otimização]

Você: Como implemento a sugestão?
O Nerd: [Mostra código refatorado com explicações]
"""

# =============================================================================
# DICAS PRO
# =============================================================================

"""
✨ DICAS PARA MELHOR EXPERIÊNCIA:

1. Seja específico
   ✗ "Como faço?"
   ✓ "Como configuro um servidor Flask em Python?"

2. Forneça contexto
   ✗ "Está dando erro"
   ✓ "Quando executo o código, recebo um erro 'ModuleNotFoundError'"

3. Faça perguntas de acompanhamento
   ✗ Pergunta isolada sem conexão
   ✓ Conversa natural com histórico

4. Use comandos quando apropriado
   ✗ "Abra o Chrome por favor" (se estiver em voz)
   ✓ Comando direto sem preamburinhos

5. Aprovite a IA para aprender
   ✗ Aceita respostas sem questionar
   ✓ Questiona, pede exemplos, explora

6. Customize para suas necessidades
   ✗ Use configuração padrão
   ✓ Ajuste SYSTEM_PROMPT para sua personalidade

7. Combine recursos
   ✗ Usa só voz ou só texto
   ✓ Alterna conforme a situação

8. Mantenha histórico
   ✗ Conversas muito longas
   ✓ Reseta quando mudar de contexto
"""

# =============================================================================
# ROADMAP FUTURO
# =============================================================================

"""
Funcionalidades planejadas para próximas versões:

V2.1:
- Suporte a múltiplos idiomas
- Integração com Spotify (controlar música)
- Dashboard web de monitoramento

V2.2:
- Plugins customizáveis
- Scheduler de tarefas
- Integração com calendário

V2.3:
- Offline mode básico
- Modelo IA local (Llama2)
- Sincronização em nuvem

V3.0:
- Arquitetura de microserviços
- Aplicativo mobile nativo
- APIs públicas
"""
