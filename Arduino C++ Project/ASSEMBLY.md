# Montagem e ligação (Arduino UNO + 3 LEDs)

Este arquivo explica passo-a-passo como montar o circuito na protoboard e quais peças usar para o projeto de 3 LEDs (pisca-pisca) com `project.cpp`.

Peças necessárias
- Arduino UNO (ou compatível)
- 3 LEDs (cores à escolha)
- 3 resistores 220Ω (ou 330Ω a 470Ω)
- 1 botão push-button
- Protoboard
- Jumpers (fios macho-macho)
- Cabo USB para programar o Arduino

Avisos de segurança
- Nunca conecte um LED diretamente ao 5V sem resistor.
- Corrente típica por LED com 220Ω e 5V é segura para usos pequenos. Para muitos LEDs, use driver/transistor.

Pinout usado no sketch
- LED 0 -> Arduino D3 (PWM)
- LED 1 -> Arduino D5 (PWM)
- LED 2 -> Arduino D6 (PWM)
- Botão -> Arduino D2 (com `INPUT_PULLUP` no código)

Esquema de ligação (texto / ASCII)

  Arduino UNO pins
  --------------
  [GND]-----------------------------+-----------------+-----------------+
                                      |                 |                 
                                      |                 |                 
  D3 --------------[resistor220]--->|-> LED0 (anodo)   |                 
                                      |                LED1 (anodo)      
  D5 --------------[resistor220]--->|-> LED1 (anodo)   |                 
                                      |                 |                 
  D6 --------------[resistor220]--->|-> LED2 (anodo)   |                 
                                      |                 |                 
  GND --------------------------------+-------(LED cathodes)--------------

  Botão (push-button):
  - Pino D2 conectado a uma perna do botão.
  - Outra perna do botão conectada ao GND.
  - No código usamos `pinMode(BUTTON_PIN, INPUT_PULLUP)`; portanto, o pino lê HIGH quando solto e LOW quando pressionado.

Dicas para montagem na protoboard
- Coloque os LEDs com a mesma orientação (anodo, catodo). Anodo -> resistor -> pino Arduino; catodo -> GND.
- Use fios curtos para reduzir ruído.
- Confirme que a fileira de GND da protoboard está ligada ao GND do Arduino.

Testes iniciais
1. Conecte o Arduino ao PC via USB.
2. Abra o Monitor Serial (115200 bps). Você verá a mensagem de inicialização do sketch.
3. Pressione o botão para ciclar modos.
4. Envie `help` no Monitor Serial para ver comandos e ajustar frequências.

Exemplo rápido de comandos
- `mode pisca` — muda para o modo pisca-pisca (cada LED com sua frequência)
- `ledfreq 0 150` — define o LED 0 para alternar a cada 150 ms
- `pattern preset1` — aplica sequência predefinida de frequências

Quer que eu gere um diagrama PNG/SVG com as ligações para você? Posso criar um desenho simples SVG aqui e salvá-lo no projeto se desejar.
