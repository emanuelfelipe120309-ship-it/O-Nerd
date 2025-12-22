// Projeto: Instrumento tátil com sensor touch (módulo TTP223)
// Funcionalidade:
// - Toque curto: toca uma nota curta (melodia)
// - Toque longo (>500 ms): alterna LED indicador
// Materiais sugeridos: Arduino Uno (ou compatível), módulo sensor touch TTP223,
// buzzer piezo (ou pequeno speaker), LED (e resistor 220Ω), jumpers, breadboard, cabo USB.
// Confirme seus materiais para ajustar o código/conexões se necessário.

#include <Arduino.h>

// Pinos (ajuste conforme sua montagem)
const int TOUCH_PIN = 2;     // saída digital do módulo touch (TTP223)
const int BUZZER_PIN = 9;    // pino para o buzzer (pode usar PWM)
const int LED_PIN = 13;      // LED indicador

// Debounce e temporização
const unsigned long DEBOUNCE_MS = 50;
const unsigned long LONG_PRESS_MS = 500;

bool lastTouchState = false;
unsigned long lastDebounceTime = 0;
unsigned long touchStartTime = 0;
bool ledState = false;

// Notas para a melodia (frequências em Hz)
const int melody[] = { 523, 659, 784, 1047 }; // C5, E5, G5, C6
const int melodyLen = sizeof(melody) / sizeof(melody[0]);

void playShortMelody() {
  // toca 4 notas curtas sequenciais
  for (int i = 0; i < melodyLen; ++i) {
    tone(BUZZER_PIN, melody[i], 120);
    delay(150);
  }
  noTone(BUZZER_PIN);
}

void setup() {
  pinMode(TOUCH_PIN, INPUT);
  pinMode(BUZZER_PIN, OUTPUT);
  pinMode(LED_PIN, OUTPUT);
  digitalWrite(LED_PIN, LOW);
}

void loop() {
  bool rawTouch = digitalRead(TOUCH_PIN) == HIGH; // HIGH quando tocado no TTP223

  if (rawTouch != lastTouchState) {
    lastDebounceTime = millis();
    lastTouchState = rawTouch;
  }

  if ((millis() - lastDebounceTime) > DEBOUNCE_MS) {
    static bool stableState = false;
    if (stableState != rawTouch) {
      stableState = rawTouch;
      if (stableState) {
        // borda de subida: início do toque
        touchStartTime = millis();
      } else {
        // borda de descida: fim do toque
        unsigned long pressDuration = millis() - touchStartTime;
        if (pressDuration >= LONG_PRESS_MS) {
          // toque longo: alterna LED
          ledState = !ledState;
          digitalWrite(LED_PIN, ledState ? HIGH : LOW);
          // feedback sonoro curto
          tone(BUZZER_PIN, 880, 120);
          delay(140);
          noTone(BUZZER_PIN);
        } else {
          // toque curto: toca a melodia
          playShortMelody();
        }
      }
    }
  }
}

/*
  Montagem sugerida:
  - TOUCH_PIN (digital)  <- saída D0 do módulo TTP223 (conecte VCC e GND do módulo)
  - BUZZER_PIN (9)      -> buzzer piezo (polo positivo no pino, negativo no GND)
  - LED_PIN (13)        -> LED com resistor 220Ω ao GND

  Observações:
  - Se você não tiver o módulo TTP223 mas tiver apenas um pedaço de folha metálica,
    é possível montar um pad e usar a biblioteca CapacitiveSensor; me diga se for o caso
    que eu adapto o código.
  - Para ESP32/boards com `touchRead()` podemos mudar o código para usar pins capacitivos.
*/
