
/*
 * Blink - makes a single LED blink on and off
 */

void setup() {
  pinMode(13, OUTPUT); // pin 13 - change value if you have LED on diff pin
}

void loop() {
  digitalWrite(13, HIGH);  // set pin 13 to high voltage, turning LED on
  delay(1000);             // wait 1000 milliseconds, or one second.
  digitalWrite(13, LOW);   // set pin 13 to low voltage, or zero. LED off.
  delay(1000);             //wait one second before starting the loop again.
}

// (c) 2018 Let's Start Coding. License: www.letsstartcoding.com/bsdlicense
