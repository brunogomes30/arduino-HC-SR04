#include <Arduino.h>
#include <arduino-timer.h>

enum State{
  RECEIVE_INPUT,
  WAITING,
  SEND_OUTPUT
};

const int trigPin = 10;
const int echoPin = 9;
Timer<1, micros> timer;

int distance;
long duration;
State state = RECEIVE_INPUT;

bool calculateDistance(void *arg){
  duration = pulseIn(echoPin, HIGH);
  distance = duration * 0.034/2;
  state = SEND_OUTPUT;
  return false;
}

void startCalculateDistance() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);

  digitalWrite(trigPin, HIGH);
  timer.in(10, calculateDistance);
  state = WAITING;
}


int main(){
  init();
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  Serial.begin(9600);
  int valueread;
  while(true){
    timer.tick();
    switch(state){
      case RECEIVE_INPUT:
        if (Serial.available() > 0) {
          valueread = Serial.read();
          startCalculateDistance();
        }
        break;
      case WAITING:
        break;
      case SEND_OUTPUT:
      if(distance < 1000){
        Serial.println(distance);
      }
        
        state = RECEIVE_INPUT;
        break;
    }
  }
}


