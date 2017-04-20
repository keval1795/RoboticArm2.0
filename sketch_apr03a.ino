#include <Servo.h>

Servo myservo;
Servo myservo1;
Servo myservo2;
Servo myservo3;
Servo myservo4;
String inString = "";

int pos=90;
int pos1=150;
int pos2=90;
int pos3=90;
int pos4=90;

int incoming;

void setup() {
  // Open serial communications and wait for port to open:
  Serial.begin(9600);

//pinMode(ledPin, OUTPUT);
myservo.attach(3);
myservo1.attach(5);
myservo2.attach(6);
myservo3.attach(10);
myservo4.attach(11);

myservo.write(pos);
myservo1.write(pos1);
myservo2.write(pos2);
myservo3.write(pos3);
myservo4.write(pos4);
}

void loop() {
  while (Serial.available() > 0) 
  {
    int inChar = Serial.read();
    
    
    if (isDigit(inChar)) 
 {
      
      inString += (char)inChar;
    
 }   
                  if (inChar == '\n') 
                          {
                            
                            inString="";
                           }

 
if (inChar =='r')
    {      
      if (pos + inString.toInt() <= 180)
      {
    myservo.write(pos + inString.toInt());
    Serial.println(pos + inString.toInt());
    pos = pos + inString.toInt();
    }
    }
else if (inChar =='l')
    {      
      if (pos - inString.toInt() >= 0)
      {
    myservo.write(pos - inString.toInt());
    Serial.println(pos - inString.toInt());
    pos = pos - inString.toInt();
    }
    }
else if (inChar =='u')
    {      
      if (pos1 + inString.toInt() <= 180)
      {
    myservo1.write(pos1 + inString.toInt());
    Serial.println(pos1 + inString.toInt());
    pos1 = pos1 + inString.toInt();
    }
    }
else if (inChar =='d')
    {      
      if (pos1 - inString.toInt() >= 0)
      {
    myservo1.write(pos1 - inString.toInt());
    Serial.println(pos1 - inString.toInt());
    pos1 = pos1 - inString.toInt();
    }
    }    
else if (inChar =='b')
    {      
      if (pos2 + inString.toInt() <= 180)
      {
    myservo2.write(pos2 + inString.toInt());
    delay(30);
    Serial.println(pos2 + inString.toInt());
    pos2 = pos2 + inString.toInt();
    }
    }   
else if (inChar =='f')
    {      
      if (pos2 - inString.toInt() >= 0)
      {
    myservo2.write(pos2 - inString.toInt());
    delay(30);
    Serial.println(pos2 - inString.toInt());
    pos2 = pos2 - inString.toInt();
    }
    }         
else if (inChar =='c')
    {      
      if (pos3 + inString.toInt() <= 180)
      {
    myservo3.write(pos3 + inString.toInt());
    Serial.println(pos3 + inString.toInt());
    pos3 = pos3 + inString.toInt();
    }
    }
else if (inChar =='a')
    {      
      if (pos3 - inString.toInt() >= 0)
      {
    myservo3.write(pos3 - inString.toInt());
    Serial.println(pos3 - inString.toInt());
    pos3 = pos3 - inString.toInt();
    }
    }    
else if (inChar =='g')
    {      
      if (pos4 + inString.toInt() <= 180)
      {
    myservo4.write(pos4 + inString.toInt());
    Serial.println(pos4 + inString.toInt());
    pos4 = pos4 + inString.toInt();
    }
    }
else if (inChar =='t')
    {      
      if (pos4 - inString.toInt() >= 0)
      {
    myservo4.write(pos4 - inString.toInt());
    Serial.println(pos4 - inString.toInt());
    pos4 = pos4 - inString.toInt();
    }
    }        
    
  }
}
  

