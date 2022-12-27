#include <ESP32Servo.h>
//#define DEBUG_ARRAY(a) {for (int index = 0; index < sizeof(a) / sizeof(a[0]); index++)    {Serial.print(a[index]); Serial.print('\t');} Serial.println();};
Servo servo1;
Servo servo2;
Servo servo3;
Servo servo4;
//----------------
String str = "";
const char separator = ',';
const int dataLength = 4;
int retiro[dataLength];
int aux = 0;
String texto_monedas = "";
//----------------
//Cantidades de monedas
int monedas[dataLength];
//int cant_05 = 0;
//int cant_10 = 0;
//int cant_20 = 0;
//int cant_50 = 0;
int help05 = 0;
int help10 = 0;
int help20 = 0;
int help50 = 0;

const int pinServo1=21;
const int pinServo2=19;
const int pinServo3=18;
const int pinServo4=5;
const int sensorPin1 = 23;
const int sensorPin2 = 22;
const int sensorPin3 = 4;
const int sensorPin4 = 15;
const int ang_init = 120;

void setup () {
      attachInterrupt(digitalPinToInterrupt(sensorPin1), aumento_moneda, FALLING);
      attachInterrupt(digitalPinToInterrupt(sensorPin2), aumento_moneda, FALLING);
      attachInterrupt(digitalPinToInterrupt(sensorPin3), aumento_moneda, FALLING);
      attachInterrupt(digitalPinToInterrupt(sensorPin4), aumento_moneda, FALLING);
      servo1.attach(pinServo1, 500, 2500);
      servo2.attach(pinServo2, 500, 2500);
      servo3.attach(pinServo3, 500, 2500);
      servo4.attach(pinServo4, 500, 2500);
      servo1.write(ang_init);
      servo2.write(ang_init);
      servo3.write(ang_init);
      servo4.write(ang_init);
      pinMode(2, OUTPUT); //Led para saber que todo esta corriendo correctamente
      Serial.begin(9600);
}

void loop () {
 if (help05 == 1) {monedas[0] ++; help05 =0;}
 if (help10 == 1) {monedas[1] ++; help10 =0;}
 if (help20 == 1) {monedas[2] ++; help20 =0;}
 if (help50 == 1) {monedas[3] ++; help50 =0;}

/*
 //Solo para ver cuantas monedas hay, luego se quiará
 Serial.println("CANTIDADES:");
 Serial.println(monedas[0]);
 Serial.println(monedas[1]);
 Serial.println(monedas[2]);
 Serial.println(monedas[3]);
 delay(100);
*/
 if (Serial.available()>0){
  String dato = Serial.readStringUntil('\n');
  
  if(dato.indexOf("PASAME EL DATO")!=-1){aux=1;}
  else if(dato.indexOf(",")!=-1){
     for (int i = 0; i < dataLength ; i++){
           int index = dato.indexOf(separator);
           retiro[i] = dato.substring(0, index).toInt();
           dato = dato.substring(index + 1);
        }
     monedas[0] = monedas[0] - retiro[0];
     monedas[1] = monedas[1] - retiro[1];
     monedas[2] = monedas[2] - retiro[2];
     monedas[3] = monedas[3] - retiro[3];
     aux=2;
   }
}
if (aux == 1){/*MANDA DATO "cant_05,cant_10,cant_20,cant_50"*/
  for(int i = 0; i < dataLength ; i++){
    texto_monedas.concat(monedas[i]);
    if(i < dataLength-1) texto_monedas.concat(",");
  }
  Serial.println(texto_monedas);
  texto_monedas = "";
  aux = 0;
  }
if (aux == 2){
      while (retiro[0]>0 || retiro[1]>0 || retiro[2]>0|| retiro[3]>0){
        if(retiro[0]>0) servo1.write(0);
        if(retiro[1]>0) servo2.write(0);
        if(retiro[2]>0) servo3.write(0);
        if(retiro[3]>0) servo4.write(0);
        delay(300);
        servo1.write(ang_init);
        servo2.write(ang_init);
        servo3.write(ang_init);
        servo4.write(ang_init);
        delay(300);
        retiro[0]--;
        retiro[1]--;
        retiro[2]--;
        retiro[3]--;
        }
    aux = 0;
    Serial.println("LISTO");
}

 //QUITAR AL FINAL
 digitalWrite(2, HIGH); // enciende el LED.
 delay(500); // retardo en milisegundos
 digitalWrite(2, LOW); // apaga el LED.
 delay(500);

}

/*
// Aumento moneda de 0.5 soles
void aumento_05(){
  help05=1;
}
// Aumento moneda de 1 sol
void aumento_10(){
  help10=1;
}
// Aumento moneda de 2 soles
void aumento_20(){
  help20=1;
}
// Aumento moneda de 5 soles
void aumento_50(){
  help50=1;
}
*/

// Aumento de moneda RESUMIDO
void aumento_moneda(){
  if (!digitalRead(sensorPin1)) {help05=1;}     // Aumento moneda de 0.5 soles
  else if (!digitalRead(sensorPin2)) {help10=1;}// Aumento moneda de 1   sol
  else if (!digitalRead(sensorPin3)) {help20=1;}// Aumento moneda de 2   soles
  else if (!digitalRead(sensorPin4)) {help50=1;}// Aumento moneda de 3   soles
}
