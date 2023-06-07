from app import app
import multiprocessing
from leds import leds_active


def start_led_control():
    process = multiprocessing.Process(target=leds_active)
    process.start()


if __name__ == '__main__':
    start_led_control()
    app.run(debug=True, port=8000, host="0.0.0.0")
