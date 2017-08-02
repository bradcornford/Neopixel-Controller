from Tkinter import *
import threading


class AdafruitNeopixelMock(threading.Thread):

    LEDS = 16

    LED_GPIO_PIN = 18
    LED_FREQUENCY_HZ = 800000
    LED_DMA = 5
    LED_INVERT = False
    LED_BRIGHTNESS = 255
    LED_CHANNEL = 0
    LED_STRIP = 0x00081000

    PIXELS = []

    DEFAULT_COLOR = '#000000'

    thread = None

    tkinter = None

    def __init__(self, leds, gpio_pin, requenzy_hz, dma, invert, brightness, channel, strip):
        print("[AdafruitNeopixelMock][info] Initialising")

        self.LEDS = leds

        self.LED_GPIO_PIN = gpio_pin
        self.LED_FREQUENCY_HZ = requenzy_hz
        self.LED_DMA = dma
        self.LED_INVERT = invert
        self.LED_BRIGHTNESS = brightness
        self.LED_CHANNEL = channel
        self.LED_STRIP = strip

        self.tkinter = Tk()

        frame = Frame(self.tkinter)
        frame.pack()

        for i in range(0, self.LEDS):
            self.PIXELS.append(
                {
                    'color': self.DEFAULT_COLOR,
                    'pixel': Button(frame, text=i, height=0, width=0)
                }
            )

            self.PIXELS[i]['pixel'].configure(background=self.DEFAULT_COLOR, highlightbackground=self.DEFAULT_COLOR)
            self.PIXELS[i]['pixel'].pack(side=LEFT)

        threading.Thread.__init__(self)
        self.start()

    def run(self):
        self.tkinter.mainloop()

    def begin(self):
        print("[AdafruitNeopixelMock][info] Begin")

    def setPixelColor(self, pixel, color):
        print("[AdafruitNeopixelMock][info] Set pixel color")

        self.PIXELS[pixel]['color'] = '#%02x%02x%02x' % ((color >> 16) & 255, (color >> 8) & 255, color & 255)

    def setBrightness(self, brightness):
        print("[AdafruitNeopixelMock][info] Set brightness")

        self.LED_BRIGHTNESS = brightness

    def show(self):
        print("[AdafruitNeopixelMock][info] Show")

        for pixel in self.PIXELS:
            pixel['pixel'].configure(background=pixel['color'], highlightbackground=pixel['color'])
            pixel['pixel'].pack(side=LEFT)

        self.tkinter.update()
