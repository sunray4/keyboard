print("Starting")

import board
print(dir(board))

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.macros import Macros, Press, Release, Tap, Delay


from kmk.modules.layers import Layers
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.encoder import EncoderHandler

from kmk.extensions.display.ssd1306 import SSD1306
from kmk.extensions.display import Display, ImageEntry
from animation import Animation

# keyboard setup
keyboard = KMKKeyboard()

keyboard.modules.append(Layers())
keyboard.extensions.append(MediaKeys())

macros = Macros()
keyboard.modules.append(macros)

keyboard.col_pins = (board.GP1, board.GP7, board.GP18, board.GP10, board.GP11, board.GP12, board.GP13, board.GP14, board.GP15, board.GP8, board.GP9, board.GP19, board.GP20, board.GP21, board.GP22, board.GP28)
keyboard.row_pins = (board.GP2, board.GP3, board.GP4, board.GP5, board.GP6, board.GP0)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

SMILE = KC.MACRO(
    Tap(KC.COLN),
    Tap(KC.RPRN),
)

CAPSLOCK = KC.MACRO(
    Press(KC.CAPSLOCK),
    Delay(10),
    Tap(KC.TG(2)),
    Release(KC.CAPSLOCK),
)

BASE = [
    KC.PSLS, KC.PAST, KC.ESC,  KC.BRID, KC.BRIU, SMILE, KC.DEL, KC.RCMD(KC.RCMD), KC.LCMD(KC.LALT(KC.D)),  KC.MPRV, KC.MPLY, KC.MNXT, KC.MUTE, KC.VOLD, KC.VOLU, KC.MUTE, #when encoder switch is pressed
    KC.PMNS, KC.P9, KC.GRV,  KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,   KC.N6,   KC.N7,   KC.N8,   KC.N9,   KC.N0, KC.MINS, KC.EQL,  KC.BSPC,
    KC.P7, KC.P8, KC.TAB,  KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,    KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,    KC.LBRC, KC.RBRC, KC.BSLS, 
    KC.P5, KC.P6, KC.PPLS, CAPSLOCK,   KC.A,    KC.S,    KC.D,    KC.F,    KC.G,    KC.H,    KC.J,    KC.K,    KC.L,    KC.SCLN, KC.QUOT, KC.ENT,
    KC.P4, KC.P1, KC.P2, KC.LSFT, KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,    KC.N,    KC.M,    KC.COMM, KC.DOT,  KC.SLSH, KC.RSFT, KC.UP,
    KC.P0, KC.P3, KC.PDOT, KC.PENT, KC.MO(1) , KC.LCTL, KC.LALT, KC.LCMD, KC.NO, KC.SPC, KC.RCMD, KC.RALT, KC.LEFT, KC.DOWN, KC.RIGHT, KC.NO, #for changing led (lion key)
]

FN = [
    KC.TRNS, KC.TRNS, KC.RESET, KC.F1,   KC.F2,   KC.F3,   KC.F4,   KC.F5,   KC.F6,   KC.F7,   KC.F8,   KC.F9,   KC.F10,  KC.F11,  KC.F12, KC.TRNS,
    KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.DELETE,
    KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
    KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
    KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, 
    KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,

]

CAPS_LAYER = [
    KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
    KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
    KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
    KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
    KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, 
    KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,

]



keyboard.keymap = [BASE, FN, CAPS_LAYER]


# rotary encoder
encoder = EncoderHandler()
keyboard.modules.append(encoder)

encoder.pins = (
    (board.GP16, board.GP17),
    )

encoder.map = [ ((KC.VOLD, KC.VOLU, KC.NO),), # volume control - mute button part of matrix
                ((KC.BRID, KC.BRIU, KC.NO),), # brightness control - when move layer with Fn key
                ]



# OLED display
oled_driver = SSD1306(
    sda=board.GP26,
    scl=board.GP27,
)

oled_entries = [
    Animation(
        images=["mountain_animation/mountain1.bmp", "mountain_animation/mountain2.bmp", 
                "mountain_animation/mountain3.bmp", "mountain_animation/mountain4.bmp", 
                "mountain_animation/mountain5.bmp", "mountain_animation/mountain6.bmp", 
                "mountain_animation/mountain7.bmp"],
        x=0,
        y=0,
        layer=None,  # scene for all layers aside from layer 2
        period=700,
    ),       
    ImageEntry(
        image="mountain_animation/snowflakes.bmp",
        x=0,
        y=0,
        layer=2,  # layer 2 scene
    ),

]

oled = Display(
    display=oled_driver,
    entries=oled_entries,
    width=128,
    height=32,
    brightness=0.2,
    dim_time=20,
    dim_target=0.1,
    off_time=60,
)
print("Adding oled")

keyboard.extensions.append(oled)

for entry in oled_entries:
    if hasattr(entry, 'during_bootup'):
        entry.during_bootup(keyboard)

           
if __name__ == "__main__":
    print("Starting keyboard")
    keyboard.go()
    