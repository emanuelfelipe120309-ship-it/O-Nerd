# Calculadora Java Profissional

Projeto: calculadora em Java com suporte a expressões, funções científicas, histórico, GUI (Swing) e testes.

Funcionalidades principais
- Avaliação de expressões com operadores `+ - * / ^` e parênteses
- Funções: `sin`, `cos`, `tan`, `asin`, `acos`, `atan`, `sqrt`, `log` (base 10), `ln`, `abs`
- Fatorial: `!` (aplicado a inteiros não-negativos)
- Suporte a operador unário negativo
- Histórico em memória e visualizável pela GUI
- Interface gráfica com Swing e execução via linha de comando
 - Suporte a operador unário negativo
 - Histórico em memória e persistente (salvar/carregar em arquivo)
 - Interface gráfica com Swing e execução via linha de comando

Como compilar e executar

Requisitos: JDK 17 e Maven.

Compilar e executar testes:

```powershell
mvn test
```

Executar a GUI (padrão):

```powershell
mvn -Dexec.mainClass="com.calculator.Main" exec:java
```

Executar uma expressão pela linha de comando:

```powershell
mvn -Dexec.mainClass="com.calculator.Main" -Dexec.args="\"2+2*3\"" exec:java
```

Arquitetura
- `com.calculator.core.Calculator` — parser e avaliador
- `com.calculator.history.HistoryManager` — histórico simples em memória
- `com.calculator.ui.SwingCalculator` — interface gráfica básica
- `com.calculator.Main` — ponto de entrada (lança GUI ou avalia expressão passada por argumento)

Extras implementados
- Salvar/Carregar histórico em `~/.java-calculator/history.txt`
- Constantes `pi` e `e`
- Funções adicionais: `sinh`, `cosh`, `tanh`, `ceil`, `floor`
- Gerar JAR executável com `mvn package` (usando `maven-shade-plugin`)

Contribuições
- Melhorias possíveis: modo programação, temas da UI, suporte a variáveis e script.

