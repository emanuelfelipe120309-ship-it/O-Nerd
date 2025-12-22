# LED Modes — Arduino UNO

Resumo rápido: sketch para controlar 3 LEDs com modos OFF / STATIC / BLINK / BREATH / CHASE.
Entrada por botão (ciclo de modos) e por Serial (configurações e troca de modo).

Componentes recomendados
- Arduino UNO
- 3 LEDs (qualquer cor)
- 3 resistores 220Ω a 470Ω
- 1 botão push-button
- Protoboard
- Jumpers (fios)

Pinout padrão no sketch
- LEDs: pinos PWM 3, 5, 6 (consulte `project.cpp` para alterar)
- Botão: pino digital 2 (usa `INPUT_PULLUP`)

Ligação (breadboard)
1. LEDs:
   - Coloque cada LED na protoboard (anodo e catodo). Anodo (+, perna maior) vai ao resistor, resistor ao pino PWM do Arduino (3, 5, 6).
   - Catodo (-, perna menor) do LED vai ao GND comum do Arduino.
   - Use resistores de 220Ω a 470Ω em série com cada LED para limitar corrente.

   Exemplo (LED na primeira linha da protoboard):
   - Arduino D3 -> resistor 220Ω -> anodo LED -> catodo LED -> GND

2. Botão (usando `INPUT_PULLUP` no código):
   - Conecte um lado do botão ao pino digital 2 do Arduino.
   - Conecte o outro lado do botão ao GND do Arduino.
   - Observação: a orientação do botão na protoboard importa; normalmente as duas pernas do mesmo lado da fileira são conectadas — verifique com multímetro ou teste visual.
   - Com `INPUT_PULLUP`, o pino lê `HIGH` quando solto e `LOW` quando pressionado.

Dicas de hardware
- Verifique polaridade dos LEDs (anodo/catodo).
- Use uma fonte USB que forneça corrente suficiente para os LEDs; 3 LEDs com resistores 220Ω consomem pouco, mas atenção se usar muitos ou LEDs de alta potência.
- Se quiser mais LEDs ou efeitos, prefira usar transistores ou drivers em vez de ligar muitos LEDs diretamente ao Arduino.

Uso do sketch
- Arquivo: `project.cpp` (copie para um sketch Arduino ou renomeie para `project.ino` no Arduino IDE).
- Portas PWM: se quiser mudar LEDs para outros pinos PWM no UNO, atualize a constante `LED_PINS` em `project.cpp`.

Comandos Serial (via Monitor Serial ou `arduino-cli`):
- `help` — lista comandos
- `mode <name|index>` — define modo (OFF, STATIC, BLINK, BREATH, CHASE)
   - Ex: `mode blink` ou `mode 2`
- `brightness <0-255>` — define brilho global
- `blink <ms>` — define intervalo de piscar (ms)
- `breath <ms>` — define período da respiração (ms)
- `chase <ms>` — define intervalo do chase (ms)

Exemplos rápidos
- Mudar para modo BREATH:
  - Enviar `mode breath` pelo Monitor Serial
- Diminuir brilho:
  - `brightness 100`

Upload (Arduino IDE)
1. Abra o Arduino IDE.
2. Copie o conteúdo de `project.cpp` para um novo sketch e salve como `project.ino` (opcional) no mesmo diretório.
3. Em Ferramentas -> Placa selecione `Arduino/Genuino UNO`.
4. Selecione a porta COM correta.
5. Clique em Upload.

Upload (arduino-cli — Windows PowerShell exemplo)
```powershell
arduino-cli compile --fqbn arduino:avr:uno path\to\sketch_folder
arduino-cli upload -p COM3 --fqbn arduino:avr:uno path\to\sketch_folder
```
Substitua `COM3` e `path\to\sketch_folder` conforme seu sistema.

Resolução de problemas
- Monitor Serial não mostra mensagens: verifique taxa (115200 bps).
- Botão não altera modo: confira ligação do botão (pino 2 ao botão, outro lado do botão a GND).
- LEDs sempre apagados: confirme resistores, polaridade e pinos PWM corretos.

Quer que eu:
- converta o `project.cpp` para `project.ino` automaticamente?
- adicione suporte a mais LEDs (ex.: 8 canais) ou controle via botão longo/curto?
