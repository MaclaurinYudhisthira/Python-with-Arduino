#define echo 13
#define trig 12
#define buz 11
void setup() {
  Serial.begin(9600);
  pinMode(trig,OUTPUT);
  pinMode(echo,INPUT);
//  pinMode(buz,OUTPUT);
}

void loop() {
  digitalWrite(trig,LOW);
  delayMicroseconds(2);
  digitalWrite(trig,HIGH);
  delayMicroseconds(8);
  digitalWrite(trig,LOW);
  int duration=pulseIn(echo,HIGH);
  int dist=duration*0.034/2;
//  Serial.print("Distance : ");
  Serial.println(dist);
  if(dist!=100)
  {
    digitalWrite(buz,HIGH);
    delay(500);
    digitalWrite(buz,LOW);
    delay(400);
  }
  
  delay(100);
  
}
