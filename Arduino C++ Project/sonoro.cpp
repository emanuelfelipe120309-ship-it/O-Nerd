// sonoro.cpp
// Controle sonoro com botão: sons intercalados por toque curto; toque longo ativa modo automático.
// Materiais: Arduino Uno (ou compatível), botão momentâneo com resistor pull-down ou usar INPUT_PULLUP,
// buzzer piezo, jumpers, breadboard, LED opcional.

#include <Arduino.h>

// Pinos
const int BUTTON_PIN = 7;   // botão conectado (use INPUT_PULLUP se preferir)
const int BUZZER_PIN = 9;   // buzzer piezo
const int LED_PIN = 13;     // LED indicador

// Temporizações
const unsigned long DEBOUNCE_MS = 50;
const unsigned long LONG_PRESS_MS = 500;
const unsigned long AUTO_INTERVAL_MS = 300; // intervalo entre sons no modo automático

// Sequência de tons (Hz) que serão intercalados
const int tonesSeq[] = { 440, 660, 550, 880 }; // A4, E5-ish, C#5-ish, A5
const int tonesCount = sizeof(tonesSeq) / sizeof(tonesSeq[0]);

// Estado
bool lastRawButton = HIGH; // se usar INPUT_PULLUP, botão não-pressionado = HIGH
unsigned long lastDebounceTime = 0;
unsigned long pressStartTime = 0;
int currentToneIndex = 0;
bool autoMode = false;
unsigned long lastAutoToggle = 0;

void playToneShort(int freq) {
  tone(BUZZER_PIN, freq, 180);
  delay(220);
  noTone(BUZZER_PIN);
}

void setup() {
  pinMode(BUTTON_PIN, INPUT_PULLUP); // usando pull-up interno -> botão ao GND
  pinMode(BUZZER_PIN, OUTPUT);
  pinMode(LED_PIN, OUTPUT);
  digitalWrite(LED_PIN, LOW);
}

void loop() {
  int raw = digitalRead(BUTTON_PIN);

  // debouncing
  if (raw != lastRawButton) {
    lastDebounceTime = millis();
    lastRawButton = raw;
  }

  if ((millis() - lastDebounceTime) > DEBOUNCE_MS) {
    static int stableState = HIGH;
    if (stableState != raw) {
      stableState = raw;
      if (stableState == LOW) {
        // borda de descida (com INPUT_PULLUP, LOW = botão pressionado)
        pressStartTime = millis();
      } else {
        // borda de subida: botão liberado
        unsigned long duration = millis() - pressStartTime;
        if (duration >= LONG_PRESS_MS) {
          // toque longo: alterna modo automático
          autoMode = !autoMode;
          digitalWrite(LED_PIN, autoMode ? HIGH : LOW);
          // feedback sonoro rápido
          tone(BUZZER_PIN, autoMode ? 1000 : 600, 120);
          delay(140);
          noTone(BUZZER_PIN);
        } else {
          // toque curto: toca próximo tom da sequência (intercalado)
          playToneShort(tonesSeq[currentToneIndex]);
          currentToneIndex = (currentToneIndex + 1) % tonesCount;
        }
      }
    }
  }

  // se modo automático, alterna sons periodicamente
  if (autoMode) {
    unsigned long now = millis();
    if (now - lastAutoToggle >= AUTO_INTERVAL_MS) {
      lastAutoToggle = now;
      playToneShort(tonesSeq[currentToneIndex]);
      currentToneIndex = (currentToneIndex + 1) % tonesCount;
    }
  }
}

/*
  Uso / conexões:
  - BUTTON_PIN (7) com `INPUT_PULLUP`: ligue um lado do botão ao pino 7 e o outro ao GND.
  - BUZZER_PIN (9) -> buzzer piezo (positivo no pino, negativo ao GND)
  - LED_PIN (13) -> LED com resistor 220Ω ao GND (opcional)

  Comportamento:
  - Pressão curta (<500 ms): toca o próximo som da sequência (intercalando).
  - Pressão longa (>=500 ms): alterna modo automático; no modo automático os sons
    são tocados sequencialmente a cada `AUTO_INTERVAL_MS` ms até que uma pressão longa desligue o modo.

  Se preferir que o botão funcione com pull-down em vez de pull-up, ajuste `pinMode(BUTTON_PIN, INPUT)`
  e conecte o outro lado do botão ao VCC com um resistor pull-down externo.
*/
