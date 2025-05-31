# Create an animation extension
from kmk.extensions.display import ImageEntry
from kmk.scheduler import create_task
import displayio



class Animation(ImageEntry):
    def __init__(self, images, x=0, y=0, layer=None, side=None, period=1000):
        super().__init__(x=x, y=y, image=images[0], layer=layer, side=side)
        self.images = [displayio.OnDiskBitmap(img) for img in images]
        self.frame = 0
        self.period = period  # default update every 1000ms - avoid display updating too often, or else it wil compete with encoder updates
        self.keyboard = None  # set during bootup
        self.display = None



    def during_bootup(self, keyboard):
        self.keyboard = keyboard
        for extension in keyboard.extensions:
            if hasattr(extension, 'display'):
                self.display = extension
                break
        if self.display is None:
            raise RuntimeError("No display found")
        
        # built in scheduler creates a task that runs every 100ms to update the animation
        self._task = create_task(self.update, period_ms=self.period)
        
    def update(self):
        self.frame = (self.frame + 1) % len(self.images)
        self.image = self.images[self.frame]

        # refresh display - extension[2] is the oled display
        if self.keyboard:
            self.display.render(self.keyboard.active_layers[0])