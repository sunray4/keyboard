print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

from kmk.modules.layers import Layers
from kmk.extensions.media_keys import MediaKeys
from kmk.oled import Oled, OledData, OledReactionType, OledDisplayMode
from kmk.modules.lock_status import LockStatus

keyboard = KMKKeyboard()

keyboard.modules.append(Layers())
keyboard.extensions.append(MediaKeys())

keyboard.col_pins = (board.GP28, board.GP17, board.GP26, board.GP22, board.GP19, board.GP20, board.GP21, board.GP11, board.GP9, board.GP8, board.GP7, board.GP6, board.GP5, board.GP4, board.GP3, board.GP10, board.GP16, board.GP2)
keyboard.row_pins = (board.GP27, board.GP18, board.GP12, board.GP13, board.GP14, board.GP15)
keyboard.diode_orientation = keyboard.DIODE_ROW2COL

BASE = [
    KC.ESC,  KC.BRID, KC.BRIU, KC.MCTL, KC.SLCK, KC.DICT, KC.DND,  KC.MPRV, KC.MPLY, KC.MNXT, KC.MUTE, KC.VOLD, KC.VOLU, KC.NO,   KC.INS,  KC.HOME, KC.PGUP, KC.PMNS,
    KC.GRV,  KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,   KC.N6,   KC.N7,   KC.N8,   KC.N9,   KC.N0,   KC.MINS, KC.EQL,  KC.BSPC, KC.DEL,  KC.END,  KC.PGDN, KC.PPLS,
    KC.TAB,  KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,    KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,    KC.LBRC, KC.RBRC, KC.BSLS, KC.NLCK, KC.PSLS, KC.PAST, KC.P6,
    KC.CAPSLOCK,   KC.A,    KC.S,    KC.D,    KC.F,    KC.G,    KC.H,    KC.J,    KC.K,    KC.L,    KC.SCLN, KC.QUOT, KC.ENT,  KC.UP,   KC.P7,   KC.P8,   KC.P9,   KC.PENT,
    KC.LSFT, KC.NO,   KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,    KC.N,    KC.M,    KC.COMM, KC.DOT,  KC.SLSH, KC.RSFT, KC.DOWN, KC.P4,   KC.P5,   KC.P0,   KC.PDOT,
    KC.MO(1),KC.NO,   KC.LCTL, KC.LALT, KC.LCMD, KC.NO,   KC.NO,   KC.SPC,  KC.NO,   KC.RALT, KC.RCMD, KC.RCTL, KC.LEFT, KC.RIGHT,KC.P1,   KC.P2,   KC.P3,   KC.NO,
]

FN = [
    KC.RESET, KC.F1,   KC.F2,   KC.F3,   KC.F4,   KC.F5,   KC.F6,   KC.F7,   KC.F8,   KC.F9,   KC.F10,  KC.F11,  KC.F12,  KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
    KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.DEL, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, 
    KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, 
    KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, 
    KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, 
    KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, 
]

keyboard.keymap = [BASE, FN]

# OLED display
keyboard.SCL=board.GP0
keyboard.SDA=board.GP1

#placeholder animation
animation_frames = [
    "   *   ",
    "  *    ", 
    " *     ", 
    "*      ",  
    " *     ",  
]


class OLEDAnimation(LockStatus):
    def __init__(self):
        self.animation_frame = 0  # first frame

    def update_animation(self):
        if self.get_caps_lock():
            oled._views[2] = {0: OledReactionType.STATIC, 1: ["CapsLock"]}
        else:
            oled._views[2] = {0: OledReactionType.STATIC, 1: [animation_frames[self.animation_frame]]}
            self.animation_frame = (self.animation_frame + 1) % len(animation_frames)  

        keyboard.sandbox.lock_update = 1  

    def after_hid_send(self, sandbox):
        super().after_hid_send(sandbox)
        self.update_animation()

oled_animation = OLEDAnimation()
keyboard.modules.append(oled_animation)


if __name__ == "__main__":
    keyboard.go()