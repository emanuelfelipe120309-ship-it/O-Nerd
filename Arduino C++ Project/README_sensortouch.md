# Instrumento Tátil — `sensortouchtest.cpp`

Descrição rápida:
- Projeto simples que usa um módulo touch (TTP223) para tocar uma pequena melodia em toque curto e alternar um LED em toque longo.

Materiais:
- Arduino Uno (ou compatível)
- Módulo sensor touch TTP223 (ou um pad capacitivo)
- Buzzer piezo (ou pequeno alto-falante)
- LED + resistor 220 Ω
- Jumpers e breadboard
- Cabo USB para programar o Arduino

Conexões (usando TTP223):
- Módulo TTP223 VCC -> 5V
- Módulo TTP223 GND -> GND
- Módulo TTP223 OUT -> pino digital 2 do Arduino
- Buzzer positivo -> pino digital 9
- Buzzer negativo -> GND
- LED -> pino 13 via resistor 220 Ω -> GND

Resumo do código / comportamento:
- Toque curto: toca 4 notas curtas (melodia).
- Toque longo (>= 500 ms): alterna o LED indicador e emite um bip curto.
- Debounce do sensor incluído para evitar repetições indesejadas.

Upload (Arduino IDE):
1. Abra o Arduino IDE.
2. Selecione a placa correta em `Tools > Board` (ex.: Arduino Uno) e a porta em `Tools > Port`.
3. Abra `sensortouchtest.cpp` (ou cole o conteúdo em um novo sketch) e clique em Upload.

Adaptações possíveis:
- Se você não tiver o módulo TTP223 e quiser usar apenas um pedaço de folha metálica, eu adapto o sketch para usar a biblioteca `CapacitiveSensor`.
- Para ESP32/boards com suporte a pinos touch, posso trocar a leitura para `touchRead()`.

Dicas de depuração:
- Verifique alimentação e GND comuns entre módulo e Arduino.
- Se o sensor estiver muito sensível, mova o pad ou ajuste a posição; para TTP223 há um pot interno em alguns módulos.
- Se não ouvir som, verifique polaridade do buzzer e pino configurado no sketch.
