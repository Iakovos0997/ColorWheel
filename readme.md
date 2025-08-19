# Color Wheel and Color Mixer GUI

This project provides an interactive **Color Wheel** and **Color Mixer** GUI using Python's `graphics.py` module. Users can select colors visually from a color wheel or mix custom colors using RGBK values in a real-time interactive interface.

---

## Features

### Color Wheel
- Displays a full HSV-based color wheel.
- Click anywhere inside the wheel to select a color.
- Shows a preview of the selected color along with its RGB values.
- Real-time marker indicates the selected color on the wheel.

### Color Mixer
- Allows the user to mix two colors using **R, G, B, K** values.
- **K** acts as a weighting factor for mixing.
- Real-time color preview updates as the values are changed.
- Displays the resulting mixed color along with updated RGBK values.
- Back button to return to the color wheel interface.

---

## Files

- `button.py` — Defines the `Button` class for GUI buttons.
- `colorMixer.py` — Implements the `ColorMixer` class for mixing colors with RGBK values.
- `ColorWheel.py` — Implements the `ColorWheel` class for selecting colors visually.
- `main.py` — Runs the main application combining the Color Wheel and Color Mixer interfaces.

---

## Requirements

- Python 3.x
- [`graphics.py`](https://mcsp.wartburg.edu/zelle/python/)

Make sure `graphics.py` is in the same directory as the project files.

---

## Usage

1. Run the main application:

```bash
python main.py
