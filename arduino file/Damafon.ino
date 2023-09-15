#include <SPI.h>
#include <MFRC522.h>
int flag;
int data;
int flag1;
String lastc;
#define SS_PIN 10
#define RST_PIN 9
MFRC522 mfrc522(SS_PIN, RST_PIN); // Create MFRC522 instance.
byte uidCard[4] = {0x93, 0x48, 0x67, 0x9A}; 
void setup() {
 Serial.begin(9600); // Initialize serial communications with the PC
 SPI.begin();   // Init SPI bus
 mfrc522.PCD_Init(); // Init MFRC522 card
 
 
}

void loop() {
  String c;
  flag1++;
  
 if ( ! mfrc522.PICC_IsNewCardPresent()) {
  return;
 }

 // Select one of the cards
 if ( ! mfrc522.PICC_ReadCardSerial()) {
  return;
 }

  for (byte  i =0; i < mfrc522.uid.size; i++){
    c = c + String(mfrc522.uid.uidByte[i],HEX);
    
    }
    c.toUpperCase();
  if(c != lastc){
    Serial.println(c);
    lastc = c;
    flag1 = 0;
  }
  else if(flag1 > 50){
    Serial.println(c);
    flag1 = 0;
  }
  
  
}
