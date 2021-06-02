import os
import math


os.chdir("/Users/inoue/Documents/CAD_ref/py")
file = open('WAVEGUIDE!!!' + '.scr', 'w')
file.write('rotate' + '\n')
file.write('all' + '\n')
file.write('' + '\n')
file.write('0,0' + '\n')
file.write(str(60) + '\n')


file.close()