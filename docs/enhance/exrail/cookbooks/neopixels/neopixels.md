# Setting neopixels

The NEOPIXEL macro provides the ability to set neopixels on or off change the colour. either individually or over a range of pixels.

```cpp
NEOPIXEL([-]vpin, red, green, blue [,count])
```

vpin = pin number of the individual pixel in the range defined by the [HAL(NeoPixel...) command](index.md).
red = 0..255 intensity of the red channel
green = 0..255 intensity of the green channel
blue = 0..255 intensity of the blue channel
count = numver of pixels to set, starting at vpin. Default =1.

 Setting pixels on or off (without colour change) can be done with SET/RESET.

Because the pixels obey SET/RESET, the BLINK command can also be used to control blinking a pixel.
