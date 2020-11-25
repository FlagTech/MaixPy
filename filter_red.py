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
    img = img.resize(64,48)         # resize to small image
    bi = img.to_bytes()             # get bytesarray of image object
    for i in range(0, img.size(), 2): # filtering highest 5 bits every 2 bytes
        bi[i] = bi[i] & 0x07
    lcd.display(img)                # Display on LCD
