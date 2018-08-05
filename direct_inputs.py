import ctypes
import time

SendInput = ctypes.windll.user32.SendInput

keys = {
    "W":0x11,
    "A":0x1E,
    "S":0x1F,
    "D":0x20,
    "ROLL":0x42,
    "CAMUP":0x68,
    "CAMDN":0x62,
    "CAMLFT":0x64,
    "CAMRGT":0x66,
    "ATK":0x37,
    "STRAT":0x38,
    "JUMP":0x20,
    "LOCK":0x51,
    "CHITEM":0x28,
    "SWTWEPR":0x27,
    "SWTWEPL":0x25,
    "ITEM":0x52,
    "INTR":0x45,
    "TWOH":0x46,
}


# C struct redefinitions
PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time",ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                 ("mi", MouseInput),
                 ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

# Actuals Functions

def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


# This was for the mouse. Could never get it to work. Has something to do with the hex codes being generated on each press.
# def set_pos(x, y):
#     x = 1 + int(x * 65536. / 1920.)
#     y = 1 + int(y * 65536. / 1080.)
#     extra = ctypes.c_ulong(0)
#     ii_ = Input_I()
#     ii_.mi = MouseInput(x, y, 0, (0x0001 | 0x8000), 0, ctypes.pointer(extra))
#     command = Input(ctypes.c_ulong(0), ii_)
#     ctypes.windll.user32.SendInput(1, ctypes.pointer(command), ctypes.sizeof(command))
#
#
# def left_click():
#     extra = ctypes.c_ulong(0)
#     ii_ = Input_I()
#     ii_.mi = MouseInput(0, 0, 0, 0x0002, 0, ctypes.pointer(extra))
#     x = Input(ctypes.c_ulong(0), ii_)
#     ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))
#
#     extra = ctypes.c_ulong(0)
#     ii_ = Input_I()
#     ii_.mi = MouseInput(0, 0, 0, 0x0004, 0, ctypes.pointer(extra))
#     x = Input(ctypes.c_ulong(0), ii_)
#     ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))