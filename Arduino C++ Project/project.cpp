#include <Arduino.h>
#include <math.h>

// =========================
// Configuração (ajuste conforme hardware)
// =========================
// LED pins (use PWM-capable pins for brightness/fade)
const uint8_t LED_PINS[] = {3, 5, 6};
const size_t LED_COUNT = sizeof(LED_PINS) / sizeof(LED_PINS[0]);

// Button to cycle modes (uses internal pull-up)
const uint8_t BUTTON_PIN = 2;

// Defaults
uint8_t globalBrightness = 200; // 0-255
unsigned long blinkInterval = 500; // ms
unsigned long breathPeriod = 2000; // ms
unsigned long chaseInterval = 150; // ms

// Button debounce
const unsigned long BUTTON_DEBOUNCE_MS = 50;

// =========================
// Mode enum
// =========================
enum Mode {
  MODE_OFF = 0,
  MODE_STATIC,
  MODE_BLINK,
  MODE_BREATH,
  MODE_CHASE,
  MODE_PISCA, // each LED blinks at its own frequency (pisca-pisca)
  MODE_COUNT
};

Mode currentMode = MODE_STATIC;

// Timing state
unsigned long lastMillisBlink = 0;
bool blinkState = false;

unsigned long lastMillisBreath = 0;

unsigned long lastMillisChase = 0;
size_t chaseIndex = 0;

// --- For MODE_PISCA (per-LED blinking) ---
unsigned long ledToggleInterval[LED_COUNT] = {200, 350, 500}; // ms between toggles for each LED
unsigned long ledLastToggle[LED_COUNT] = {0};
bool ledState[LED_COUNT] = {false};

// Button state
int lastButtonState = HIGH; // using INPUT_PULLUP
unsigned long lastButtonChange = 0;

// Serial command buffer
String serialBuf;

// =========================
// Helper functions
// =========================
void applyBrightnessToAll(uint8_t b) {
  for (size_t i = 0; i < LED_COUNT; ++i) {
    analogWrite(LED_PINS[i], b);
  }
}

void setAllOff() {
  applyBrightnessToAll(0);
}

void setStatic() {
  applyBrightnessToAll(globalBrightness);
}

void updateBlink(unsigned long now) {
  if (now - lastMillisBlink >= blinkInterval) {
    lastMillisBlink = now;
    blinkState = !blinkState;
    applyBrightnessToAll(blinkState ? globalBrightness : 0);
  }
}

void updateBreath(unsigned long now) {
  // Smooth breathing using sine wave
  unsigned long t = now % breathPeriod;
  double phase = (double)t / (double)breathPeriod; // 0..1
  double angle = phase * 2.0 * PI; // 0..2PI
  double v = (sin(angle - PI / 2.0) + 1.0) / 2.0; // 0..1 (starts from low)
  uint8_t b = (uint8_t)(v * (double)globalBrightness + 0.5);
  applyBrightnessToAll(b);
}

void updateChase(unsigned long now) {
  if (now - lastMillisChase >= chaseInterval) {
    lastMillisChase = now;
    chaseIndex = (chaseIndex + 1) % LED_COUNT;
    for (size_t i = 0; i < LED_COUNT; ++i) {
      uint8_t b = (i == chaseIndex) ? globalBrightness : 0;
      analogWrite(LED_PINS[i], b);
    }
  }
}

void updatePisca(unsigned long now) {
  for (size_t i = 0; i < LED_COUNT; ++i) {
    unsigned long interval = ledToggleInterval[i];
    if (interval < 10) interval = 10;
    if (now - ledLastToggle[i] >= interval) {
      ledLastToggle[i] = now;
      ledState[i] = !ledState[i];
      analogWrite(LED_PINS[i], ledState[i] ? globalBrightness : 0);
    }
  }
}

void setMode(Mode m) {
  if (m >= MODE_COUNT) return;
  currentMode = m;
  // Reset timing when switching modes
  lastMillisBlink = millis();
  lastMillisBreath = millis();
  lastMillisChase = millis();
  chaseIndex = 0;
  blinkState = false;

  // Apply immediate effect for some modes
  switch (currentMode) {
    case MODE_OFF: setAllOff(); break;
    case MODE_STATIC: setStatic(); break;
    case MODE_BLINK: applyBrightnessToAll(0); break;
    case MODE_BREATH: applyBrightnessToAll(0); break;
    case MODE_CHASE: applyBrightnessToAll(0); break;
    case MODE_PISCA:
      // init per-led state
      for (size_t i = 0; i < LED_COUNT; ++i) {
        ledLastToggle[i] = millis();
        ledState[i] = false;
        analogWrite(LED_PINS[i], 0);
      }
      break;
    default: break;
  }
}

String modeName(Mode m) {
  switch (m) {
    case MODE_OFF: return "OFF";
    case MODE_STATIC: return "STATIC";
    case MODE_BLINK: return "BLINK";
    case MODE_BREATH: return "BREATH";
    case MODE_CHASE: return "CHASE";
    default: return "UNKNOWN";
  }
}

void handleSerialCommand(const String &cmd) {
  // Simple parsing: commands are space-separated
  // Examples: "mode blink", "mode 2", "brightness 128", "help"
  String s = cmd;
  s.trim();
  s.toLowerCase();
  if (s.length() == 0) return;

  if (s == "help") {
    Serial.println(F("Commands:"));
    Serial.println(F("  mode <name|index>  - set mode (OFF, STATIC, BLINK, BREATH, CHASE)"));
    Serial.println(F("  brightness <0-255> - set global brightness"));
    Serial.println(F("  blink <ms> - set blink interval"));
    Serial.println(F("  breath <ms> - set breath period"));
    Serial.println(F("  chase <ms> - set chase interval"));
    return;
  }

  int firstSpace = s.indexOf(' ');
  String cmdName = (firstSpace == -1) ? s : s.substring(0, firstSpace);
  String arg = (firstSpace == -1) ? String() : s.substring(firstSpace + 1);
  arg.trim();

  if (cmdName == "mode") {
    if (arg.length() == 0) {
      Serial.print(F("Current mode: "));
      Serial.println(modeName(currentMode));
      return;
    }
    // try numeric
    if (arg.charAt(0) >= '0' && arg.charAt(0) <= '9') {
      int idx = arg.toInt();
      if (idx >= 0 && idx < (int)MODE_COUNT) {
        setMode((Mode)idx);
        Serial.print(F("Mode set to "));
        Serial.println(modeName(currentMode));
        return;
      }
    }
    // name match
    if (arg == "off") { setMode(MODE_OFF); }
    else if (arg == "static") { setMode(MODE_STATIC); }
    else if (arg == "blink") { setMode(MODE_BLINK); }
    else if (arg == "breath") { setMode(MODE_BREATH); }
    else if (arg == "chase") { setMode(MODE_CHASE); }
    else {
      Serial.println(F("Unknown mode name"));
      return;
    }
    Serial.print(F("Mode set to "));
    Serial.println(modeName(currentMode));
    return;
  }

  if (cmdName == "brightness") {
    if (arg.length() == 0) return;
    int b = arg.toInt();
    if (b < 0) b = 0; if (b > 255) b = 255;
    globalBrightness = (uint8_t)b;
    Serial.print(F("Brightness set to "));
    Serial.println(globalBrightness);
    return;
  }

  if (cmdName == "blink") {
    if (arg.length() == 0) return;
    unsigned long v = (unsigned long)arg.toInt();
    if (v < 10) v = 10;
    blinkInterval = v;
    Serial.print(F("Blink interval set to "));
    Serial.println(blinkInterval);
    return;
  }

  if (cmdName == "breath") {
    if (arg.length() == 0) return;
    unsigned long v = (unsigned long)arg.toInt();
    if (v < 100) v = 100;
    breathPeriod = v;
    Serial.print(F("Breath period set to "));
    Serial.println(breathPeriod);
    return;
  }

  if (cmdName == "chase") {
    if (arg.length() == 0) return;
    unsigned long v = (unsigned long)arg.toInt();
    if (v < 10) v = 10;
    chaseInterval = v;
    Serial.print(F("Chase interval set to "));
    Serial.println(chaseInterval);
    return;
  }

  if (cmdName == "ledfreq") {
    // ledfreq <index> <ms>  (index: 0..LED_COUNT-1)
    int idx = -1;
    unsigned long v = 0;
    int sp = arg.indexOf(' ');
    if (sp != -1) {
      String sIdx = arg.substring(0, sp);
      String sVal = arg.substring(sp + 1);
      idx = sIdx.toInt();
      v = (unsigned long)sVal.toInt();
    }
    if (idx >= 0 && idx < (int)LED_COUNT) {
      if (v < 10) v = 10;
      ledToggleInterval[idx] = v;
      Serial.print(F("LED frequency set: index "));
      Serial.print(idx);
      Serial.print(F(" -> "));
      Serial.print(v);
      Serial.println(F(" ms"));
    } else {
      Serial.println(F("Usage: ledfreq <index> <ms>"));
    }
    return;
  }

  if (cmdName == "pattern") {
    // pattern preset1|preset2|random
    if (arg == "preset1") {
      unsigned long p[] = {150, 300, 450};
      for (size_t i = 0; i < LED_COUNT; ++i) ledToggleInterval[i] = p[i];
      Serial.println(F("Pattern preset1 applied"));
    } else if (arg == "preset2") {
      unsigned long p[] = {80, 160, 320};
      for (size_t i = 0; i < LED_COUNT; ++i) ledToggleInterval[i] = p[i];
      Serial.println(F("Pattern preset2 applied"));
    } else if (arg == "random") {
      for (size_t i = 0; i < LED_COUNT; ++i) {
        ledToggleInterval[i] = 50 + (unsigned long)(random(100, 800));
      }
      Serial.println(F("Random pattern applied"));
    } else {
      Serial.println(F("pattern <preset1|preset2|random>"));
    }
    return;
  }

  Serial.println(F("Unknown command. Type 'help'"));
}

// =========================
// Setup / Loop
// =========================
void setupPins() {
  for (size_t i = 0; i < LED_COUNT; ++i) {
    pinMode(LED_PINS[i], OUTPUT);
    analogWrite(LED_PINS[i], 0);
  }
  pinMode(BUTTON_PIN, INPUT_PULLUP);
}

void setup() {
  Serial.begin(115200);
  delay(50);
  Serial.println(F("LED Modes sketch starting"));
  setupPins();
  setMode(currentMode);
}

void loop() {
  unsigned long now = millis();

  // --- Button handling (cycle modes on press) ---
  int raw = digitalRead(BUTTON_PIN);
  if (raw != lastButtonState) {
    lastButtonChange = now;
    lastButtonState = raw;
  }
  if ((now - lastButtonChange) > BUTTON_DEBOUNCE_MS) {
    static int stableState = HIGH;
    if (raw != stableState) {
      stableState = raw;
      if (stableState == LOW) { // pressed (because INPUT_PULLUP)
        // advance mode
        Mode next = (Mode)((currentMode + 1) % MODE_COUNT);
        setMode(next);
        Serial.print(F("Button: mode -> "));
        Serial.println(modeName(currentMode));
      }
    }
  }

  // --- Serial handling ---
  while (Serial.available()) {
    char c = (char)Serial.read();
    if (c == '\n' || c == '\r') {
      if (serialBuf.length() > 0) {
        handleSerialCommand(serialBuf);
        serialBuf = String();
      }
    } else {
      serialBuf += c;
      // keep buffer reasonably small
      if (serialBuf.length() > 200) serialBuf = serialBuf.substring(serialBuf.length() - 200);
    }
  }

  // --- Mode updates (non-blocking) ---
  switch (currentMode) {
    case MODE_OFF: /* nothing */ break;
    case MODE_STATIC: /* steady already applied */ break;
    case MODE_BLINK: updateBlink(now); break;
    case MODE_BREATH: updateBreath(now); break;
    case MODE_CHASE: updateChase(now); break;
    default: break;
  }
}
