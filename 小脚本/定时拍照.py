import os
import time

name = './Pictures/' + time.strftime('%m-%d_%H:%M:%S') + '.jpg'
os.system(f'raspistill -o {name}')
