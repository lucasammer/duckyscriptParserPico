# duckyscriptParserPico
a duckyscript adaptation for pico

Some features wont work yet!
this is a work in progress!

# installation
1. download [CircuitPython for rasberry pi pico](https://circuitpython.org/board/raspberry_pi_pico/)
2. plug in your pico whilst holding the BOOTSEL button (the white one)
3. make sure your pico has nothing on it by uploading the [flash_nuke.uf2](https://datasheets.raspberrypi.com/soft/flash_nuke.uf2)
4. upload your circuitpython .uf2 file to your pico once it reconnects
5. alter the code.py file to be the code.py file from this repository
6. upload your payload.dd this can be any duckyscript file

You can know that the code is running when the green light on your pico is on. The light turns on when the code starts running and turns off once it finishes.

If you do not want the pico to show up as a storage device, do what [this guy on reddit](https://www.reddit.com/r/raspberrypipico/comments/mu73rq/comment/hxpftwl/?utm_source=share&utm_medium=web2x&context=3) said.
