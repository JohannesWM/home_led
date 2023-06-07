from app import app
import threading
from leds import leds_active


def start_led_control():
    led_thread = threading.Thread(target=leds_active)
    led_thread.daemon = True
    led_thread.start()


if __name__ == '__main__':
    start_led_control()
    app.run(debug=True, port=8000, host="0.0.0.0")
