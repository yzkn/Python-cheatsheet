import sys
import time
for num, i in enumerate(range(100)):
    sys.stdout.write("\r%d" % num)
    sys.stdout.flush()
    time.sleep(0.01)
