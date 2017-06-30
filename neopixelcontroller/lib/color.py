

class Color:
    red = None
    green = None
    blue = None
    white = None
    bit_color = None

    def __init__(self, red, green, blue, white=0):
        self.red = red
        self.green = green
        self.blue = blue
        self.white = white

    def get_rgb(self):
        return 'rgb(%d,%d,%d)' % (self.red, self.green, self.blue)

    def get_hex(self):
        return '#%02x%02x%02x' % (self.red, self.green, self.blue)

    def get_hsv(self):
        red = self.red / 255.0
        green = self.green / 255.0
        blue = self.blue / 255.0

        median_max = max(red, green, blue)
        median_min = min(red, green, blue)
        difference = median_max - median_min

        if median_max == median_min:
            hue = 0
        elif median_max == red:
            hue = (60 * ((green - blue) / difference) + 360) % 360
        elif median_max == green:
            hue = (60 * ((blue - red) / difference) + 120) % 360
        elif median_max == blue:
            hue = (60 * ((red - green) / difference) + 240) % 360
        else:
            hue = 0

        if median_max == 0:
            saturation = 0
        else:
            saturation = difference / median_max

        value = median_max

        return 'hsv(%d,%d,%d)' % (hue, saturation, value)

    def get_bit(self):
        return (self.white << 24) | (self.red << 16) | (self.green << 8) | self.blue

    def __str__(self):
        return '%d,%d,%d' % (self.red, self.green, self.blue)
