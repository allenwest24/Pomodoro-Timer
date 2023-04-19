import sys
import time
import subprocess
cheering = "mixkit-small-group-cheer-and-applause-518.wav"
break_over = "mixkit-classic-alarm-995.wav"
ding = "mixkit-cowbell-sharp-hit-1743.wav"

def main(work_duration, rest_duration):
    while True:
        print("WORK WORK WORK!!")
        subprocess.run(["afplay", ding])
        time.sleep(work_duration * 60)

        print("Time to rest!")
        subprocess.run(["afplay", ding])
        time.sleep(rest_duration * 60)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python work_rest_timer.py <work_duration> <rest_duration>")
        sys.exit(1)

    work_duration = int(sys.argv[1])
    rest_duration = int(sys.argv[2])

    main(work_duration, rest_duration)
