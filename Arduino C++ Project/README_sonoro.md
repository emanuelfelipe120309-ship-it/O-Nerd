# Controle Sonoro — `sonoro.cpp`

Descrição rápida:
- Sketch que reproduz sons intercalados com um botão: pressão curta avança o som; pressão longa ativa/desativa modo automático.

Materiais:
- Arduino Uno (ou compatível)
- Botão momentâneo (momentary push-button)
- Buzzer piezo
- LED (opcional) + resistor 220 Ω
- Jumpers e breadboard
- Cabo USB

Conexões (uso de `INPUT_PULLUP` no sketch):
- Botão: um terminal -> pino digital 7 do Arduino; outro terminal -> GND.
  - O sketch usa `pinMode(7, INPUT_PULLUP)`, então o pino lê `LOW` quando o botão é pressionado.
- Buzzer positivo -> pino digital 9
- Buzzer negativo -> GND
- LED -> pino 13 via resistor 220 Ω -> GND (opcional)

Comportamento:
- Pressão curta (<500 ms): toca o próximo tom da sequência (intercalando).
- Pressão longa (>=500 ms): alterna modo automático. No modo automático os sons são tocados sequencialmente a cada 300 ms (configurável).

Como usar:
1. Conecte conforme indicado.
2. Faça upload do sketch `sonoro.cpp` ao Arduino.
3. Pressione o botão brevemente para avançar manualmente pelos sons.
4. Pressione e segure para ativar o modo automático; pressione e segure novamente para desativar.

Personalizações fáceis:
- Alterar sequência de tons: editar `tonesSeq[]` no topo do arquivo.
- Ajustar intervalo automático: alterar `AUTO_INTERVAL_MS`.
- Se preferir usar pull-down em vez de pull-up, ajuste `pinMode(BUTTON_PIN, INPUT)` e adicione um resistor pull-down externo entre o pino e GND.

Testes rápidos:
- Sem carga no pino do buzzer, verifique com multímetro se o pino 9 muda temporariamente ao tocar — isso indica que o sketch está chamando `tone()`.
- Se o botão não responder corretamente, verifique se está ligado a GND e não a VCC (com `INPUT_PULLUP`, botão vai ao GND).
