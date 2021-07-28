
/* rawSend.ino Example sketch for IRLib2
 *  Illustrates how to send a code Using raw timings which were captured
 *  from the "rawRecv.ino" sample sketch.  Load that sketch and
 *  capture the values. They will print in the serial monitor. Then you
 *  cut and paste that output into the appropriate section below.
 */
#include <IRLibSendBase.h>    //We need the base code
#include <IRLib_HashRaw.h>    //Only use raw sender
#include <dht.h>

//set dht 22 pin
const int dataPin = 8;

dht DHT;

IRsendRaw mySender;

void setup() {
  Serial.begin(9600);
  delay(2000);
  while (!Serial); //delay for Leonardo
}


#define CHECK_TIME 300000  // 5 minutes


#define RAW_DATA_LEN_ON 144

uint16_t rawDataOn[RAW_DATA_LEN_ON]={
  1206, 482, 1206, 482, 362, 1330, 362, 1326,
  362, 1354, 334, 1322, 366, 1326, 362, 1326,
  362, 1330, 358, 1354, 338, 1350, 1182, 7234,
  1206, 486, 1202, 486, 362, 1354, 334, 1326,
  362, 1326, 362, 1354, 334, 1330, 358, 1354,
  334, 1354, 334, 1326, 366, 1354, 1178, 7262,
  1178, 510, 1178, 482, 366, 1354, 334, 1354,
  334, 1354, 334, 1354, 334, 1354, 334, 1354,
  334, 1358, 334, 1354, 330, 1358, 1178, 7266,
  1178, 510, 1174, 486, 362, 1354, 334, 1354,
  334, 1354, 334, 1354, 334, 1326, 366, 1354,
  334, 1354, 334, 1326, 362, 1354, 1178, 7266,
  1178, 482, 1206, 510, 334, 1354, 334, 1354,
  334, 1354, 334, 1354, 334, 1358, 330, 1358,
  334, 1354, 334, 1354, 334, 1354, 1178, 7266,
  1178, 510, 1178, 510, 334, 1354, 334, 1354,
  334, 1358, 330, 1358, 334, 1354, 334, 1354,
  334, 1354, 334, 1354, 334, 1354, 1178, 1000};


void loop() {

   int static status_vent = 0; //shutdown by default

    if(status_vent == 0){
    mySender.send(rawDataOn,RAW_DATA_LEN_ON,36);//Pass the buffer,length, optionally frequency
    Serial.println(F("FAN Switched On"));
    status_vent = 1;
    }

     delay(CHECK_TIME);

}