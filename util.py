import sys
import time


def loading_animation():
    for _ in range(3):
        sys.stdout.write('.')
        sys.stdout.flush()
        time.sleep(0.5)
    print()

