from sense_hat import SenseHat
import time

#naming variable
sense = SenseHat() 

def main():
    while True:
        results = sense.get_orientation_degrees()
        yaw = results['yaw']
        pitch = results['pitch']
        roll = results['roll']


        sense.show_message("YAW: " + yaw)
        sense.show_message("PITCH: " + pitch)
        sense.show_message("ROLL: " + roll)

        time.sleep(0.5)
    return

if __name__ == "__main__":
    main()
