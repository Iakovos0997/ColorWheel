from graphics import *
from button import Button
import time  # Needed for sleep

class ColorMixer:
    def __init__(self, win):
        self.win = win
        self.make_ui()

    def make_ui(self):
        w, h = self.win.getWidth(), self.win.getHeight()

        # --- Row 1: Color 1 ---
        Text(Point(70, 120), "Color 1:").draw(self.win)
        self.entries1 = self.make_entry_group(200, 120)
        self.preview1 = Rectangle(Point(450, 100), Point(550, 140))
        self.preview1.draw(self.win)

        # --- Row 2: Color 2 ---
        Text(Point(70, 200), "Color 2:").draw(self.win)
        self.entries2 = self.make_entry_group(200, 200)
        self.preview2 = Rectangle(Point(450, 180), Point(550, 220))
        self.preview2.draw(self.win)

        # --- Row 3: Result ---
        Text(Point(70, 300), "Result:").draw(self.win)
        self.resultEntries = self.make_entry_group(200, 300, readonly=True)
        self.resultPreview = Rectangle(Point(450, 280), Point(550, 320))
        self.resultPreview.draw(self.win)

        # --- Buttons ---
        self.backButton = Button(self.win, Point(60, h-30), 80, 25, "Back")
        self.backButton.activate()

    def make_entry_group(self, x, y, readonly=False):
        labels = ["R", "G", "B", "K"]
        entries = []
        for i, lab in enumerate(labels):
            # Draw label slightly above the entry box
            Text(Point(x + i*60, y - 20), lab).draw(self.win)
            e = Entry(Point(x + i*60, y), 5)
            e.setText("0")
            e.setFill("gray30")
            e.setTextColor("white")
            e.draw(self.win)
            if readonly:
                e.setText("0")
                e.setFill("gray30")
                e.setTextColor("white")
            entries.append(e)
        return entries

    def get_rgbk(self, entries):
        values = [int(e.getText()) for e in entries]
        return values

    def set_rgbk(self, entries, values):
        for e, v in zip(entries, values):
            e.setText(str(v))

    def mix_colors(self):
        r1, g1, b1, k1 = self.get_rgbk(self.entries1)
        r2, g2, b2, k2 = self.get_rgbk(self.entries2)

        # Sum applying k as "weight"
        r = min(255, r1*k1 + r2*k2)
        g = min(255, g1*k1 + g2*k2)
        b = min(255, b1*k1 + b2*k2)
        k = k1 + k2

        # Update result
        self.set_rgbk(self.resultEntries, [r, g, b, k])

        self.preview1.setFill(color_rgb(min(255, r1*k1), min(255, g1*k1), min(255, b1*k1)))
        self.preview2.setFill(color_rgb(min(255, r2*k2), min(255, g2*k2), min(255, b2*k2)))
        self.resultPreview.setFill(color_rgb(r, g, b))

    def run(self):
        prev1 = [None]*4
        prev2 = [None]*4

        while True:
            p = self.win.checkMouse()  # Non-blocking mouse check

            # Get current entry values safely (ignore non-integer input)
            try:
                current1 = self.get_rgbk(self.entries1)
            except ValueError:
                current1 = prev1
            try:
                current2 = self.get_rgbk(self.entries2)
            except ValueError:
                current2 = prev2

            # Update previews if values changed
            if current1 != prev1 or current2 != prev2:
                self.mix_colors()
                prev1 = current1
                prev2 = current2

            # Handle button clicks
            if p:
                if self.backButton.clicked(p):
                    return "back"

            time.sleep(0.05)  # Small delay to reduce CPU usage
