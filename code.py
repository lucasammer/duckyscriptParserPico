import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
import time

import board
import digitalio

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

led.value = True

time.sleep(3)

kbd = Keyboard(usb_hid.devices)

delay = 0.018
charDelay = 0.018

def sendString(string):
    for i in range(len(string)):
        print("Printing letter " + string[i])
        sendLetter(string[i])
        time.sleep(delay)

def sendLetter(l):
    if l == "a":
        kbd.send(Keycode.A)
    elif l == "A":
        kbd.send(Keycode.SHIFT, Keycode.A)
    elif l == "b":
        kbd.send(Keycode.B)
    elif l == "B":
        kbd.send(Keycode.SHIFT, Keycode.B)
    elif l == "c":
        kbd.send(Keycode.C)
    elif l == "C":
        kbd.send(Keycode.SHIFT, Keycode.C)
    elif l == "d":
        kbd.send(Keycode.D)
    elif l == "D":
        kbd.send(Keycode.SHIFT, Keycode.D)
    elif l == "e":
        kbd.send(Keycode.E)
    elif l == "E":
        kbd.send(Keycode.SHIFT, Keycode.E)
    elif l == "f":
        kbd.send(Keycode.F)
    elif l == "F":
        kbd.send(Keycode.SHIFT, Keycode.F)
    elif l == "g":
        kbd.send(Keycode.G)
    elif l == "G":
        kbd.send(Keycode.SHIFT, Keycode.G)
    elif l == "h":
        kbd.send(Keycode.H)
    elif l == "H":
        kbd.send(Keycode.SHIFT, Keycode.H)
    elif l == "i":
        kbd.send(Keycode.I)
    elif l == "I":
        kbd.send(Keycode.SHIFT, Keycode.I)
    elif l == "j":
        kbd.send(Keycode.J)
    elif l == "J":
        kbd.send(Keycode.SHIFT, Keycode.J)
    elif l == "k":
        kbd.send(Keycode.K)
    elif l == "K":
        kbd.send(Keycode.SHIFT, Keycode.K)
    elif l == "l":
        kbd.send(Keycode.L)
    elif l == "L":
        kbd.send(Keycode.SHIFT, Keycode.L)
    elif l == "m":
        kbd.send(Keycode.M)
    elif l == "M":
        kbd.send(Keycode.SHIFT, Keycode.M)
    elif l == "n":
        kbd.send(Keycode.N)
    elif l == "N":
        kbd.send(Keycode.SHIFT, Keycode.N)
    elif l == "o":
        kbd.send(Keycode.O)
    elif l == "O":
        kbd.send(Keycode.SHIFT, Keycode.O)
    elif l == "p":
        kbd.send(Keycode.P)
    elif l == "P":
        kbd.send(Keycode.SHIFT, Keycode.P)
    elif l == "q":
        kbd.send(Keycode.Q)
    elif l == "Q":
        kbd.send(Keycode.SHIFT, Keycode.Q)
    elif l == "r":
        kbd.send(Keycode.R)
    elif l == "R":
        kbd.send(Keycode.SHIFT, Keycode.R)
    elif l == "s":
        kbd.send(Keycode.S)
    elif l == "S":
        kbd.send(Keycode.SHIFT, Keycode.S)
    elif l == "t":
        kbd.send(Keycode.T)
    elif l == "T":
        kbd.send(Keycode.SHIFT, Keycode.T)
    elif l == "u":
        kbd.send(Keycode.U)
    elif l == "U":
        kbd.send(Keycode.SHIFT, Keycode.U)
    elif l == "v":
        kbd.send(Keycode.V)
    elif l == "V":
        kbd.send(Keycode.SHIFT, Keycode.V)
    elif l == "w":
        kbd.send(Keycode.W)
    elif l == "W":
        kbd.send(Keycode.SHIFT, Keycode.W)
    elif l == "x":
        kbd.send(Keycode.X)
    elif l == "X":
        kbd.send(Keycode.SHIFT, Keycode.X)
    elif l == "y":
        kbd.send(Keycode.Y)
    elif l == "Y":
        kbd.send(Keycode.SHIFT, Keycode.Y)
    elif l == "z":
        kbd.send(Keycode.Z)
    elif l == "Z":
        kbd.send(Keycode.SHIFT, Keycode.Z)
    elif l == "0":
        kbd.send(Keycode.ZERO)
    elif l == "1":
        kbd.send(Keycode.ONE)
    elif l == "2":
        kbd.send(Keycode.TWO)
    elif l == "3":
        kbd.send(Keycode.THREE)
    elif l == "4":
        kbd.send(Keycode.FOUR)
    elif l == "5":
        kbd.send(Keycode.FIVE)
    elif l == "6":
        kbd.send(Keycode.SIX)
    elif l == "7":
        kbd.send(Keycode.SEVEN)
    elif l == "8":
        kbd.send(Keycode.EIGHT)
    elif l == "9":
        kbd.send(Keycode.NINE)
    elif l == " ":
        runKeys(["SPACE"])
    elif l == "!":
        kbd.send(Keycode.SHIFT, Keycode.ONE)
    elif l == "@":
        kbd.send(Keycode.SHIFT, Keycode.TWO)
    elif l == "#":
        kbd.send(Keycode.SHIFT, Keycode.THREE)
    elif l == "$":
        kbd.send(Keycode.SHIFT, Keycode.FOUR)
    elif l == "%":
        kbd.send(Keycode.SHIFT, Keycode.FIVE)
    elif l == "^":
        kbd.send(Keycode.SHIFT, Keycode.SIX)
    elif l == "&":
        kbd.send(Keycode.SHIFT, Keycode.SEVEN)
    elif l == "*":
        kbd.send(Keycode.SHIFT, Keycode.EIGHT)
    elif l == "(":
        kbd.send(Keycode.SHIFT, Keycode.NINE)
    elif l == ")":
        kbd.send(Keycode.SHIFT, Keycode.ZERO)
    elif l == "-":
        kbd.send(Keycode.MINUS)
    elif l == "_":
        kbd.send(Keycode.SHIFT, Keycode.MINUS)
    elif l == "=":
        kbd.send(Keycode.EQUALS)
    elif l == "+":
        kbd.send(Keycode.SHIFT, Keycode.EQUALS)
    elif l == "[":
        kbd.send(Keycode.LEFT_BRACKET)
    elif l == "{":
        kbd.send(Keycode.SHIFT, Keycode.LEFT_BRACKET)
    elif l == "]":
        kbd.send(Keycode.RIGHT_BRACKET)
    elif l == "}":
        kbd.send(Keycode.SHIFT, Keycode.RIGHT_BRACKET)
    elif l == "\\":
        kbd.send(Keycode.BACKSLASH)
    elif l == "|":
        kbd.send(Keycode.SHIFT, Keycode.BACKSLASH)
    elif l == ";":
        kbd.send(Keycode.SEMICOLON)
    elif l == ":":
        kbd.send(Keycode.SHIFT, Keycode.SEMICOLON)
    elif l == "'":
        kbd.send(Keycode.QUOTE)
    elif l == "\"":
        kbd.send(Keycode.SHIFT, Keycode.QUOTE)
    elif l == "`":
        kbd.send(Keycode.GRAVE_ACCENT)
    elif l == "~":
        kbd.send(Keycode.SHIFT, Keycode.GRAVE_ACCENT)
    elif l == ",":
        kbd.send(Keycode.COMMA)
    elif l == "<":
        kbd.send(Keycode.SHIFT, Keycode.COMMA)
    elif l == ".":
        kbd.send(Keycode.PERIOD)
    elif l == ">":
        kbd.send(Keycode.SHIFT, Keycode.PERIOD)
    elif l == "/":
        kbd.send(Keycode.FORWARD_SLASH)
    elif l == "?":
        kbd.send(Keycode.SHIFT, Keycode.FORWARD_SLASH)
    elif l == "\n":
        runKeys(["ENTER"])


def runKeys(string):
    key_string = string[0]
    if key_string == "CTRL" or key_string == "RCTRL":
        kbd.send(Keycode.CONTROL)
    elif key_string == "SHIFT" or key_string == "RSHIFT":
        kbd.send(Keycode.SHIFT)
    elif key_string == "ALT" or key_string == "RALT":
        kbd.send(Keycode.ALT)
    elif key_string == "WINDOWS" or key_string == "RWINDOWS":
        kbd.send(Keycode.GUI)
    elif key_string == "COMMAND" or key_string == "RCOMMAND":
        # On Mac, Command key is equivalent to GUI key
        kbd.send(Keycode.GUI)
    elif key_string == "OPTION" or key_string == "ROPTION":
        # On Mac, Option key is equivalent to ALT key
        kbd.send(Keycode.ALT)
    elif key_string == "ESC":
        kbd.send(Keycode.ESCAPE)
    elif key_string == "ENTER":
        kbd.send(Keycode.ENTER)
    elif key_string == "UP":
        kbd.send(Keycode.UP_ARROW)
    elif key_string == "DOWN":
        kbd.send(Keycode.DOWN_ARROW)
    elif key_string == "LEFT":
        kbd.send(Keycode.LEFT_ARROW)
    elif key_string == "RIGHT":
        kbd.send(Keycode.RIGHT_ARROW)
    elif key_string == "SPACE":
        kbd.send(Keycode.SPACEBAR)
    elif key_string == "BACKSPACE":
        kbd.send(Keycode.BACKSPACE)
    elif key_string == "TAB":
        kbd.send(Keycode.TAB)
    elif key_string == "CAPSLOCK":
        kbd.send(Keycode.CAPS_LOCK)
    elif key_string == "PRINTSCREEN":
        kbd.send(Keycode.PRINT_SCREEN)
    elif key_string == "SCROLLLOCK":
        kbd.send(Keycode.SCROLL_LOCK)
    elif key_string == "PAUSE" or key_string == "BREAK":
        kbd.send(Keycode.PAUSE)
    elif key_string == "INSERT":
        kbd.send(Keycode.INSERT)
    elif key_string == "HOME":
        kbd.send(Keycode.HOME)
    elif key_string == "PAGEUP":
        kbd.send(Keycode.PAGE_UP)
    elif key_string == "PAGEDOWN":
        kbd.send(Keycode.PAGE_DOWN)
    elif key_string == "DELETE":
        kbd.send(Keycode.DELETE)
    elif key_string == "END":
        kbd.send(Keycode.END)
    elif key_string == "MENU":
        kbd.send(Keycode.APPLICATION)
    elif key_string == "POWER":
        # You can use a specific keycode for the power button if available
        pass  # Add the corresponding keycode here
    # Function keys F1 to F24
    elif key_string.startswith("F") and key_string[1:].isdigit():
        f_key = int(key_string[1:])
        if 1 <= f_key <= 24:
            kbd.send(getattr(Keycode, f'F{f_key}'))
    # Media keys
    elif key_string == "MK_VOLUP":
        kbd.send(Keycode.VOLUME_INCREMENT)
    elif key_string == "MK_VOLDOWN":
        kbd.send(Keycode.VOLUME_DECREMENT)
    elif key_string == "MK_MUTE":
        kbd.send(Keycode.MUTE)
    elif key_string == "MK_PREV":
        kbd.send(Keycode.SCAN_PREVIOUS_TRACK)
    elif key_string == "MK_NEXT":
        kbd.send(Keycode.SCAN_NEXT_TRACK)
    elif key_string == "MK_PP":
        kbd.send(Keycode.PLAY_PAUSE)
    # Numpad keys
    elif key_string == "NUMLOCK":
        kbd.send(Keycode.NUMLOCK)
    elif key_string == "KP_SLASH":
        kbd.send(Keycode.KEYPAD_FORWARD_SLASH)
    elif key_string == "KP_ASTERISK":
        kbd.send(Keycode.KEYPAD_ASTERISK)
    elif key_string == "KP_MINUS":
        kbd.send(Keycode.KEYPAD_MINUS)
    elif key_string == "KP_PLUS":
        kbd.send(Keycode.KEYPAD_PLUS)
    elif key_string == "KP_ENTER":
        kbd.send(Keycode.KEYPAD_ENTER)
    elif key_string.isdigit() and int(key_string) >= 0 and int(key_string) <= 9:
        kbd.send(getattr(Keycode, f'KP_{key_string}'))
    elif key_string == "KP_DOT":
        kbd.send(Keycode.KEYPAD_PERIOD)
    elif key_string == "KP_EQUAL":
        kbd.send(Keycode.KEYPAD_EQUALS)
    
    # my commands
    elif(key_string == "RUN"):
        kbd.send(Keycode.GUI, Keycode.R)

def doPart(string):
    if(string[0] == "REM"):
        pass
    elif(string[0] == "DEFAULTDELAY"):
        delay = int(string[1]) / 1000
    elif(string[0] == "DEFAULTCHARDELAY"):
        charDelay = int(string[1]) / 1000
    elif(string[0] == "CHARJITTER"):
        # i aint doing that
        pass
    elif(string[0] == "DELAY"):
        time.sleep(int(string[1])/1000)
    elif(string[0] == "STRING"):
        sendString(" ".join(string[1:]))
    elif(string[0] == "STRINGLN"):
        sendString(" ".join(string[1:]) + "\n")
    elif(string[0] == "REPEAT"):
        # repeat last thing again
        pass # for now
    else:
        runKeys(string)

payload = open("payload.dd")
payload = payload.read()
payload = payload.splitlines()
for i in range(len(payload)):
    payload[i] = payload[i].split(" ")
print(payload)
for line in payload:
    doPart(line)

led.value = False
