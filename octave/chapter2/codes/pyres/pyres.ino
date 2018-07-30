const int analogIn = A0;
int analogVal = 0;

void setup() {
  Serial.begin(9600);
   pinMode(13,OUTPUT);
}

void loop() {

 digitalWrite(13, HIGH);
 delay(5000);
 digitalWrite(13,LOW);
 delay(5000 );

  
  analogVal = analogRead(analogIn);
  Serial.println(analogVal);
  delay(1000);
}
