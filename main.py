import os
import adafruit_connection_manager
import wifi
import adafruit_requests

 

import time
import adafruit_display_text.label
import board
import displayio
import framebufferio
import rgbmatrix
import terminalio
import datetime
displayio.release_displays()

matrix = rgbmatrix.RGBMatrix(
    width=64, height=32, bit_depth=1,
    rgb_pins=[board.IO1, board.IO2, board.IO3, board.IO5, board.IO4, board.IO6],
    addr_pins=[board.IO8, board.IO7, board.IO10, board.IO9],
    clock_pin=board.IO12, latch_pin=board.IO11, output_enable_pin=board.IO13)

display = framebufferio.FramebufferDisplay(matrix, auto_refresh=False)
SCALE = 1
b1 = displayio.Bitmap(display.width//SCALE, display.height//SCALE, 2)
b2 = displayio.Bitmap(display.width//SCALE, display.height//SCALE, 2)
palette = displayio.Palette(2)

bitmap1 = displayio.OnDiskBitmap("car1.bmp")
bitmap2 = displayio.OnDiskBitmap("car2.bmp")
bitmap3 = displayio.OnDiskBitmap("car3.bmp")
bitmap4 = displayio.OnDiskBitmap("car4.bmp")


bitmaps = [bitmap1, bitmap4, bitmap2, bitmap3]

hour = int(datetime.datetime.now().hour)

image_duration = 0.1
tile_grid = displayio.TileGrid(bitmaps[0], pixel_shader=bitmaps[0].pixel_shader)
group = displayio.Group()
group.append(tile_grid)
display.root_group = group
start = 8
end = 23
hour = datetime.datetime.now().hour

def update_clock():
    time = datetime.datetime.now().strftime("%H:%M:%S")

    if 8<= hour < 12:
        color = 0xF38C16
    elif 12 <= hour < 5:
        color = 0x38C93D
    elif 5 <= hour < 8:
        color = 0x23485A
    else:
        color = 0x202021
        
    clock_display = adafruit_display_text.label.Label(
        font = terminalio.FONT,
        text = time,
        color = color,
        x = 15,
        y = 5
    )
    while len(group) > 1:
        group.pop()

       
    group.append(clock_display)

while True :
    if start <= hour < end:
        update_clock ()
    
        for bitmap in bitmaps:
            tile_grid.bitmap = bitmap
            tile_grid.pixel_shader = bitmap.pixel_shader
            time.sleep(0.2)    
            display.refresh(minimum_frames_per_second=0)
        
    else:
        time.sleep(60)


