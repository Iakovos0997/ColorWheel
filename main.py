from graphics import *
from button import Button
from ColorWheel import ColorWheel
from colorMixer import ColorMixer

def main():
    win = GraphWin("Color Wheel", 600, 600, autoflush=False)

    # Make the wheel
    wheel = ColorWheel(win, step=3)

    # Add buttons
    closeButton = Button(win, Point(win.getWidth() // 2 - 70, int(win.getHeight() * 0.95)), 100, 30, "Quit")
    closeButton.activate()

    mixerButton = Button(win, Point(win.getWidth() // 2 + 70, int(win.getHeight() * 0.95)), 100, 30, 'Color Mixer')
    mixerButton.activate()

    while True:
        p = win.getMouse()
        if p is None:
            break

        # check buttons first
        if closeButton.clicked(p):
            break
        elif mixerButton.clicked(p):
            win.close()
            win = GraphWin("Color Mixer", 600, 600, autoflush=False)
            mixer = ColorMixer(win)
            choice = mixer.run()
            if choice == "back":
                win.close()
                main()  # restart ColorWheel
                break

        # otherwise let the wheel handle the click
        wheel.handle_click(p)

    win.close()

if __name__ == "__main__":
    main()