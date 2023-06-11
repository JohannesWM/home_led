import time

from flask import Flask
import subprocess
from app import app
import psutil


# Get the current process ID
pid = psutil.Process()



if __name__ == '__main__':
    # Start the LED control script as a separate process

    led_process = subprocess.Popen(['python', 'leds.py'])

    # Start the Flask application
    app.run(debug=True, port=8000, host="0.0.0.0")

    # Terminate the LED control process when the Flask application exits
    led_process.terminate()
