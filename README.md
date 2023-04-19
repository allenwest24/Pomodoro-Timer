# Pomodoro-Timer
A simple Python script to help you manage your work and rest intervals. It plays a sound and displays a message to indicate when it's time to work and when it's time to rest.

## Requirements

- Python 3
- macOS (uses the `afplay` command to play audio)

## Setup

1. Clone or download the repository to your local machine.
2. Download or use your own sound files for the work and rest notifications. In this example, we use the following sound files:

   - `mixkit-small-group-cheer-and-applause-518.wav` for the rest notification
   - `mixkit-classic-alarm-995.wav` for the work notification

3. Update the script to use the appropriate sound file names if you're using different files.

## Usage

To run the script, open a terminal window and navigate to the directory where you saved the script. Then, execute the following command:

```
python work_rest_timer.py <work_duration> <rest_duration>
```
Replace work_duration and rest_duration with the desired durations in minutes.

For example, to set work_duration to 25 minutes and rest_duration to 5 minutes, run:

```
python work_rest_timer.py 25 5
```

The script will play a sound and display "WORK WORK WORK!!" when it's time to work, and play a different sound and display "Time to rest!" when it's time to rest.

Press Ctrl+C to stop the script.