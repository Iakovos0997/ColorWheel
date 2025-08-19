from graphics import *
from button import *
import math, colorsys

# Assume Button class is imported here

class ColorWheel:
    def __init__(self, window, step=1):
        self.window = window
        self.width = window.getWidth()
        self.height = window.getHeight()
        self.cx = self.width // 2
        self.cy = self.height // 2
        self.radius = int(min(self.width, self.height) * 0.4)
        self.step = step

        # UI elements
        self.colorPreview = None
        self.text_rgb = None
        self.marker = None
        self.quit = None

        self._makeColorWheel()

    # ---------- Utility Methods ----------

    def _hsv_to_rgb(self, hue: float, sat: float, val: float):
        rr, gg, bb = colorsys.hsv_to_rgb(hue / 360.0, sat, val)
        return int(rr * 255), int(gg * 255), int(bb * 255)

    def _draw_pixel(self, x: int, y: int, color):
        pix = Rectangle(Point(x, y), Point(x + self.step, y + self.step))
        pix.setFill(color)
        pix.setOutline(color)
        pix.draw(self.window)

    # ---------- Wheel Construction ----------

    def _makeColorWheel(self):
        self._drawOutlineCircle()
        self._addColors()
        self._addLabels()
        self._addMarker()

    def _drawOutlineCircle(self):
        Circle(Point(self.cx, self.cy), self.radius).draw(self.window)

    def _addColors(self):
        update(0)
        for y in range(self.cy - self.radius, self.cy + self.radius, self.step):
            for x in range(self.cx - self.radius, self.cx + self.radius, self.step):
                dx, dy = x - self.cx, y - self.cy
                r = math.hypot(dx, dy)
                if r <= self.radius:
                    hue = (math.degrees(math.atan2(dy, dx)) + 360) % 360
                    s = r / self.radius
                    R8, G8, B8 = self._hsv_to_rgb(hue, s, 1.0)
                    self._draw_pixel(x, y, color_rgb(R8, G8, B8))
        update()

    def _addLabels(self):
        dataCircle = Circle(Point(self.cx, self.cy), self.radius // 1.75)
        dataCircle.setOutline("gray")
        dataCircle.setFill("white")
        dataCircle.draw(self.window)

        self.colorPreview = Rectangle(Point(240, 320), Point(360, 360))
        self.colorPreview.setOutline("black")
        self.colorPreview.setFill("white")
        self.colorPreview.draw(self.window)

        Text(Point(self.cx, self.cy - 30), "Selected Color").draw(self.window)
        self.text_rgb = Text(Point(self.cx, self.cy), "RGB: (—, —, —)")
        self.text_rgb.draw(self.window)

    def _addMarker(self):
        self.marker = Circle(Point(self.cx, self.cy), 6)
        self.marker.setOutline("white")
        self.marker.setWidth(2)

    def _draw_marker(self, point: Point):
        if self.marker:
            self.marker.undraw()
        self.marker = Circle(point, 6)
        self.marker.setOutline("white")
        self.marker.setWidth(2)
        self.marker.draw(self.window)

    def _quit(self):
        self.quit = True

    # ---------- Interaction Loop ----------

    def run(self):
        self.quit = False
        while True:
            p = self.window.getMouse()
            if p is None:
                break

            # Check quit button first
            if self.quit:
                break

            x, y = p.getX(), p.getY()
            dx, dy = x - self.cx, y - self.cy
            r = math.hypot(dx, dy)

            if r <= self.radius:
                hue = (math.degrees(math.atan2(dy, dx)) + 360) % 360
                s = r / self.radius
                R8, G8, B8 = self._hsv_to_rgb(hue, s, 1.0)

                col = color_rgb(R8, G8, B8)
                self.colorPreview.setFill(col)
                self.text_rgb.setText(f"RGB: ({R8}, {G8}, {B8})")
                self._draw_marker(p)

        self.window.close()

    def handle_click(self, p: Point):
        """Handle a click inside the wheel area."""
        x, y = p.getX(), p.getY()
        dx, dy = x - self.cx, y - self.cy
        r = math.hypot(dx, dy)

        if r <= self.radius:
            hue = (math.degrees(math.atan2(dy, dx)) + 360) % 360
            s = r / self.radius
            R8, G8, B8 = self._hsv_to_rgb(hue, s, 1.0)

            col = color_rgb(R8, G8, B8)
            self.colorPreview.setFill(col)
            self.text_rgb.setText(f"RGB: ({R8}, {G8}, {B8})")
            self._draw_marker(p)
