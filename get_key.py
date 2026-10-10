import termios, tty, sys

def get_key():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)

    try:
        tty.setraw(fd)

        key = sys.stdin.read(1)

        # Arrow keys begin with ESC
        if key == "\x1b":
            key += sys.stdin.read(2)

        return key

    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
