'''To take input from key press'''


class _GetchUnix(object):

    '''Code'''

    def __init__(self):
        pass
        # import tty, sys

    def __call__(self):
        import sys
        import tty
        import termios
        filedescription = sys.stdin.fileno()
        old_settings = termios.tcgetattr(filedescription)
        try:
            tty.setraw(sys.stdin.fileno())
            char = sys.stdin.read(1)
        finally:
            termios.tcsetattr(filedescription, termios.TCSADRAIN, old_settings)
        return char
