# Raspberry Pi Python neopixel controller

A project to create a NeoPixel controller on a Raspberry Pi using a Web Server and GPIO.

## Requirements

This package requires the following system packages to be installed:

- python-dev
- build-essential
- python-pip
- python-smbus
- scons
- swig

## Installation

Begin by installing this packages requirements:

    pip install -e .
    
Finally copy the example configuration file `example.config.py`, and save it as `config.py`

    cp neopixelcontroller/example.config.py neopixelcontroller/config.py

## Configuration

You can now configure Neopixel-Controller in a few simple steps. Open `neopixelcontroller/config.py` and update the options as needed.

- `leds` - The number of NeoPixel LED's.
- `neopixel_gpio_pin` - The GPIO pin connected to the NeoPixels.
- `neopixel_frequency` - The NeoPixel signal frequency in hertz.
- `neopixel_dma` - The DMA channel to use for generating signal.
- `neopixel_invert` - Invert the signal sent to the NeoPixels.
- `neopixel_brightness` - The brightness for the NeoPixel's.
- `neopixel_channel` - The PWM channel to use.
- `neopixel_strip` - The NeoPixel strip type.
   
## Usage

It's really as simple as using the Mapper class

    sudo python neopixelcontroller/main.py
    
### License

Neopixel-Controller is open-sourced software licensed under the [MIT license](http://opensource.org/licenses/MIT)