import arduino_communication as ac
import distance_ui as ui
import time
import sys

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print('Please provide a port, e.g: python main.py COM7')
        sys.exit(1)
    port = sys.argv[1]
        
    # Create the UI
    ui = ui.DistanceUI()

    # Create the Arduino Communication
    arduino = ac.ArduinoCommunication(port, 9600)

    # Start the UI
    ui.start()

    while(True):
        # Update the Arduino Communication
        arduino.update()

        # Update the UI
        if(arduino.value_was_read()):
            ui.update(arduino.value)
        time.sleep(0.1)
    ui.close()


