## Installation
For ubuntu you may need to add user to gpio group:

```bash
sudo groupadd -f --system gpio
sudo usermod -a -G gpio ubuntu
```

Install packages:
```bash
sudo apt install python3-gpiozero
sudo pip3 install rpi.gpio --upgrade
sudo pip3 install rpi_ws281x adafruit-circuitpython-neopixel
sudo python3 -m pip install --force-reinstall adafruit-blinka
```

Clone repository:
```bash
https://github.com/LoSk-p/rpi-leds.git
```

## Run

Connect button to 5V and to GPIO 4 pin.

Connect WS2812B:
* power (V) - 5V
* ground (G) - Ground
* signal (DI) - GPIO 18 pin

Run the script:
```bash
cd rpi-leds
python3 button_leds.py
```