import time
import leds
from app import app
import psutil
import multiprocessing as mp


ledFunc = mp.Process(target=leds.lights_server_link)

if __name__ == '__main__':

    ledFunc.start()

    # Start the Flask application
    app.run(debug=False, port=8000, host="0.0.0.0")

    # Keyboard interrupt occurred, terminate the process
    ledFunc.terminate()
