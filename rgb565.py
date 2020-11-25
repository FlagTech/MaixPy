import sensor, image, time, lcd

lcd.init(freq=15000000)
sensor.reset()                      # Reset and initialize the sensor. It will
                                    # run automatically, call sensor.run(0) to stop
sensor.set_pixformat(sensor.RGB565) # Set pixel format to RGB565 (or GRAYSCALE)
sensor.set_framesize(sensor.QVGA)   # Set frame size to QVGA (320x240)
sensor.skip_frames(time = 2000)     # Wait for settings take effect.
clock = time.clock()                # Create a clock object to track the FPS.

while(True):
    img = sensor.snapshot()         # Take a picture and return the image.
    bi = img.to_bytes()
    a = img.get_pixel(0, 0)
    print(a[0], a[1], a[2])         # show  RGB
    print(                          # show RGB in binary format
        "{:08b}".format(a[0]),
        "{:08b}".format(a[1]),
        "{:08b}".format(a[2]))
    print(                          # show RGB565 in binary format
        "{:08b}".format(bi[0]),
        "{:08b}".format(bi[1], "b"))
    r = (bi[0] & 0xF8) >> 3         # get R from RGB565
    r1 = (r << 3) | (r >> 2)        # convert R back to RGB888 format
    b = bi[1] & 0x1F                # get B from RGB565
    b1 = (b << 3) | (b >> 2)        # convert B back to RGB888 format
    g = ((bi[0] & 0x07) << 3) | ((bi[1] & 0xE0)>>5) # get G from RGB565
    g1 = (g << 2) | (g >> 4)        # convert G back to RGB888 format
    print(                          # show not converted RGB888 in binary format before converting
        "{:08b}".format(r),
        "{:08b}".format(g),
        "{:08b}".format(b))
    print(                          # show RGB88 converted from RGB565 in binary format
        "{:08b}".format(r1),
        "{:08b}".format(g1),
        "{:08b}".format(b1))
    print(r1, g1, b1)               # show RGB88 converted from RGB565
    lcd.display(img)                # Display on LCD
    print("--------------------------")
