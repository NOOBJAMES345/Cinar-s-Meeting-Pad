import board
import busio
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners.keypad import KeysScanner
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.display import Display, TextEntry
from kmk.extensions.media_keys import MediaKeys

keyboard = KMKKeyboard()
keyboard.modules.append(MediaKeys())

# 1. BUTON AYARLARI (Verdiğin kesin pin listesi)
keyboard.matrix = KeysScanner(
    pins=[
        board.GP1,   # SW1
        board.GP2,   # SW2
        board.GP4,   # SW3
        board.GP3,   # SW4
        board.GP0,   # SW5
        board.GP28,  # SW6
    ],
    value_when_pressed=False,
    pull=True,
)


encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

# Encoder Pinleri: A=GPIO27, B=GPIO29.
encoder_handler.pins = ((board.GP27, board.GP29, None, False),)


encoder_handler.map = [
    ((KC.VOLU, KC.VOLD),), 
]

# SCL: GPIO7, SDA: GPIO6
i2c_bus = busio.I2C(board.GP7, board.GP6)

display = Display(
    display_ssd1306=None,
    width=128,
    height=32,
    brightness=0.8,
)

display.entries = [
    TextEntry(text='HackPad v1.0', x=0, y=0),
    TextEntry(text='Encoder: Aktif', x=0, y=12),
]

display_driver = display.ssd1306(i2c_bus, device_address=0x3C)
display.display = display_driver
keyboard.extensions.append(display)

# 4. TUŞ HARİTASI
keyboard.keymap = [
    [
        KC.A,           KC.B,           KC.C,           # Üst Butonlar
        KC.LCTRL(KC.C), KC.LCTRL(KC.V), KC.ENTER        # Alt Butonlar
    ]
]

if __name__ == '__main__':
    keyboard.go()
