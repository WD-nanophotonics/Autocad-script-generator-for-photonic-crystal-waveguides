import os
import math
from termcolor import colored

# hajime

os.chdir("/Users/inoue/Documents/CAD_ref/py")
check_grid = 0  # 0=off 1=on , plot PhC contours
symbol_line = 0  # 0=off 1=on , plot symbol lines instead of holes
valley = 1  # 0=off 1=on , separate domain layers for valley PhCWGs
hole_type = 'T'
wg_type = '1_3'
a_type = 'A3'
chip = 13
a = 500
d = 360
d2 = 140
S = -2
R_c = 120
LayerNum = 0
Si_width = 300
honey = 0
r_c = 94
y_plus = 200000
chip_type700=[1,4,5]
chip_type500=[2,3,11,14,15]
chip_type300=[12,13]

if chip in chip_type700 :
    Si_width=700
if chip in chip_type500 :
    Si_width=500
if chip in chip_type300 :
    Si_width=300

print('CHIP NUMBER='+str(chip))
print('Si_width='+str(Si_width))


if hole_type == 'C':
    valley = 0
    print('valley='+str(valley))

elif hole_type == 'H':
    valley = 1
    print('valley='+str(valley))
elif hole_type == 'T':
    valley = 1
    print('valley='+str(valley))

else:
    print(colored('WARNING: INVALID HOLE TYPE', 'red'))


if hole_type == 'Ho':
    honey = 1
else:
    honey = 0

if wg_type == '1_6':
    S = -2
    if hole_type == 'TT':
        d = 360
        if a_type == 'A1':
            a = 431
        if a_type == 'A2':
            a = 445
        if a_type == 'A3':
            a = 459
    if hole_type == 'C':
        R_c = 104
        if a_type == 'A1':
            a = 400
        if a_type == 'A2':
            a = 414
        if a_type == 'A3':
            a = 428
    if hole_type == 'T':
        d = 352
        d2 = 96
        if a_type == 'A1':
            a = 432
        if a_type == 'A2':
            a = 446
        if a_type == 'A3':
            a = 460
if wg_type == '1_3':
    S = -1
    if hole_type == 'TT':
        d = 276
        if a_type == 'A1':
            a = 386
        if a_type == 'A2':
            a = 400
        if a_type == 'A3':
            a = 414
    if hole_type == 'C':
        R_c = 104
        if a_type == 'A1':
            a = 391
        if a_type == 'A2':
            a = 405
        if a_type == 'A3':
            a = 419
    if hole_type == 'T':
        d = 352
        d2 = 144
        if a_type == 'A1':
            a = 452
        if a_type == 'A2':
            a = 466
        if a_type == 'A3':
            a = 480
if wg_type == '2_3':
    S = 1
    if hole_type == 'TT':
        d = 332
        if a_type == 'A1':
            a = 413
        if a_type == 'A2':
            a = 427
        if a_type == 'A3':
            a = 441
    if hole_type == 'C':
        R_c = 120
        if a_type == 'A1':
            a = 413
        if a_type == 'A2':
            a = 427
        if a_type == 'A3':
            a = 441
    if hole_type == 'T':
        d = 352
        d2 = 156
        if a_type == 'A1':
            a = 452
        if a_type == 'A2':
            a = 466
        if a_type == 'A3':
            a = 480
if wg_type == '5_6':
    S = 2
    if hole_type == 'TT':
        d = 300
        if a_type == 'A1':
            a = 420
        if a_type == 'A2':
            a = 434
        if a_type == 'A3':
            a = 448
    if hole_type == 'C':
        R_c = 120
        if a_type == 'A1':
            a = 413
        if a_type == 'A2':
            a = 427
        if a_type == 'A3':
            a = 441
    if hole_type == 'T':
        d = 352
        d2 = 144
        if a_type == 'A1':
            a = 452
        if a_type == 'A2':
            a = 466
        if a_type == 'A3':
            a = 480
if wg_type == '1_1':
    S = 3
    if hole_type == 'T':
        d = 240
        if a_type == 'A1':
            a = 395
        if a_type == 'A2':
            a = 402
        if a_type == 'A3':
            a = 409
    if hole_type == 'C':
        R_c = 104
        if a_type == 'A1':
            a = 396
        if a_type == 'A2':
            a = 410
        if a_type == 'A3':
            a = 424
    if hole_type == 'H':   # not really
        R_c = 156
        r_c = 94
        if a_type == 'A1':
            a = 446
        if a_type == 'A2':
            a = 460
        if a_type == 'A3':
            a = 474




dummy = 0
W12WG = 0
if wg_type == '1_1':
    if hole_type == 'H':
        W12WG =1
    else:
        dummy = dummy + 1
else:
    dummy = dummy + 1








def script_writing():
    if a_type == 'A1':
        return 'w'

    else:
        return 'a'


if a == 500:
    print(colored('WARNING: lattice constant not assigned', 'red'))



incident_m_s = 0.5 * a
if wg_type == '2_3':
    incident_m_s = 0.0 * a
else:
    incident_m_s = 0.5 * a



def i_lr():
    if S == -1:
        return -1
    elif S == 2:
        return -1
    else:
        return 1


def incident_shift():  # Si wire x-direction shift for some WGs ( bearded and W1/3WG )
    if S == 2:
        return 0
    elif S == -2:
        return 0.25
    elif S == -1:
        return 0.25
    else:
        return 0


print('incident_shift='+str(incident_shift()))

r = d / math.sqrt(3)
r2 = d2 / math.sqrt(3)
Iv = 85000  # WG intervals
x_initial = 10000

if chip % 2 == 0:
    if a_type == 'A1':
        x_initial = 10000
    elif a_type == 'A2':
        x_initial = 10000 + 13 * Iv
    elif a_type == 'A3':
        x_initial = 10000 + 26 * Iv
elif chip % 2 == 1:
    if a_type == 'A1':
        x_initial = 10000 + 85000 / 2
    elif a_type == 'A2':
        x_initial = 10000 + 13 * Iv + 85000 / 2
    elif a_type == 'A3':
        x_initial = 10000 + 26 * Iv + 85000 / 2

Nx = 22  # bulk lattice thickness
n1 = 100
n2 = 30
n3 = 0
n4 = 0
n5 = 0
n6 = 0
n7 = 100
Nx_z = Nx + (n2 + n4 + n6) / 2
Ny_s = n1 + n2 + n3 + n4 + n5 + n6 + n7  # PhC length param of Straight WG
Ny_z = n1 + n3 + n5 + n7 - (n2 + n4 + n6) / 2  # PhC length param of Z-shaped WG
x_phc = 0.5 * math.sqrt(3) * (2 * Nx - 1) * a
x_phc_z = 0.5 * math.sqrt(3) * (2 * Nx - 1 + n2 + n4 + n6) * a
y_phc_s = (Ny_s - 0.0) * a
y_phc_z = (Ny_z - 0.0) * a
file = open('WAVEGUIDE!!!' + '.scr', str(script_writing()))
if a_type == 'A1':
    file.write('-layer' + '\n')
    file.write('new' + '\n')
    file.write('1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33' + '\n')
    file.write('' + '\n')
else:
    print('not first wg arrays')

file.write('-layer' + '\n')
file.write('set' + '\n')
file.write('0' + '\n')
file.write('' + '\n')
file.write('insunits' + '\n')
file.write('12' + '\n')



# insert Si waveguides
file.write('zoom' + '\n')
file.write('W' + '\n')
file.write('0,1000' + '\n')
file.write('-20000,-1000' + '\n')
file.write('-insertcontent' + '\n')
file.write('/Users/inoue/Documents/CAD_ref/Si_' + str(Si_width) + '.dwg' + '\n')
file.write(str(Si_width) + '\n')
file.write('-10000,-100' + '\n')
file.write('1' + '\n')
file.write('1' + '\n')
file.write('0' + '\n')
file.write('mirror' + '\n')
file.write('fence' + '\n')
file.write('-11000,-110' + '\n')
file.write('-9000,-110' + '\n')
file.write('' + '\n')
file.write('' + '\n')
file.write('0,0' + '\n')
file.write('1,0' + '\n')
file.write('No' + '\n')

file.write('-layer' + '\n')
file.write('set' + '\n')
file.write('5' + '\n')
file.write('' + '\n')
file.write('rectangle' + '\n')
file.write(str(-40000 - Si_width / 2 - 1000) + ',' + str(-8000) + '\n')
file.write(str(-40000 - 9.5 * math.sqrt(3) * a - incident_shift() * a * math.sqrt(3)) + ',' + str(
    -8000 - 2000) + '\n')
file.write('' + '\n')
file.write(str(-40000 + Si_width / 2 + 1000) + ',' + str(-8000) + '\n')
file.write(str(-40000 + 9.5 * math.sqrt(3) * a - incident_shift() * a * math.sqrt(3)) + ',' + str(
    -8000 - 2000) + '\n')
file.write('rotate' + '\n')
file.write('fence' + '\n')
file.write(str(-40000 - 9.5 * math.sqrt(3) * a) + ',' + str(-8000 - 2000) + '\n')
file.write(str(-40000 + 9.5 * math.sqrt(3) * a) + ',' + str(-8000 - 2000) + '\n')
file.write('' + '\n')
file.write('' + '\n')
file.write('-40000,-8000' + '\n')
file.write('60' + '\n')
file.write('mirror' + '\n')
file.write('previous' + '\n')
file.write('' + '\n')
file.write('0,0' + '\n')
file.write('1,0' + '\n')
file.write('No' + '\n')
file.write('-layer' + '\n')
file.write('set' + '\n')
file.write('0' + '\n')
file.write('' + '\n')

file.write('zoom' + '\n')
file.write('W' + '\n')
file.write('-30000,1000' + '\n')
file.write('-50000,-1000' + '\n')
file.write('-insertcontent' + '\n')
file.write('/Users/inoue/Documents/CAD_ref/Si_' + str(Si_width) + '_b.dwg' + '\n')
file.write(str(Si_width) + 'b' + '\n')
file.write('-40000,-8000' + '\n')
file.write('1' + '\n')
file.write('1' + '\n')
file.write('0' + '\n')
file.write('mirror' + '\n')
file.write('fence' + '\n')
file.write('-41000,-8100' + '\n')
file.write('-39000,-8100' + '\n')
file.write('' + '\n')
file.write('' + '\n')
file.write('0,0' + '\n')
file.write('1,0' + '\n')
file.write('No' + '\n')





x = x_initial - 0.5 * x_phc + S * a / math.sqrt(3) / 4
y = 10000

file.write('zoom' + '\n')
file.write('W' + '\n')
file.write('0,1000' + '\n')
file.write('-20000,-1000' + '\n')
file.write('copy' + '\n')
file.write('fence' + '\n')
file.write('-11000,-110' + '\n')
file.write('-9000,-110' + '\n')
file.write('' + '\n')
file.write('' + '\n')
file.write('D' + '\n')
file.write(
    str(x + 0.5 * x_phc - S * a / math.sqrt(3) / 4 + 10000 + incident_shift() * a * math.sqrt(3)) + ','
    + str(y + 100 - incident_m_s) + '\n')
file.write('\n')
file.write('fence' + '\n')
file.write('-11000,110' + '\n')
file.write('-9000,110' + '\n')
file.write('' + '\n')
file.write('' + '\n')
file.write('D' + '\n')
file.write(
    str(x + 0.5 * x_phc - S * a / math.sqrt(3) / 4 + 10000 + incident_shift() * a * math.sqrt(3)) + ','
    + str(y + y_phc_s + incident_m_s - 100) + '\n')

# finish making the 1st of 13 WGs
x = 1 * Iv + x_initial - 0.5 * x_phc_z + S * a / math.sqrt(3) / 4



file.write('zoom' + '\n')
file.write('W' + '\n')
file.write('0,1000' + '\n')
file.write('-20000,-1000' + '\n')
file.write('copy' + '\n')
file.write('fence' + '\n')
file.write('-11000,-110' + '\n')
file.write('-9000,-110' + '\n')
file.write('' + '\n')
file.write('' + '\n')
file.write('D' + '\n')
file.write(str(x + 0.5 * x_phc - S * a / math.sqrt(3) / 4 + 10000 + incident_shift() * a * math.sqrt(
    3)) + ',' + str(y + 100 - incident_m_s) + '\n')
file.write('\n')
file.write('fence' + '\n')
file.write('-11000,110' + '\n')
file.write('-9000,110' + '\n')
file.write('' + '\n')
file.write('' + '\n')
file.write('D' + '\n')
file.write(str(x + x_phc_z - 0.5 * x_phc - S * a / math.sqrt(3) / 4 + 10000 +
               incident_shift() * a * math.sqrt(3)) + ',' + str(y + y_phc_z - 100 + incident_m_s) + '\n')
# finish making the 2nd WG




# start making the 3rd of 13 waveguides i.e. straight counterpart of 4 bends Z-shaped WG
Nx = 22  # bulk lattice thickness
n1 = 100
n2 = 30
n3 = 30
n4 = 30
n5 = 0
n6 = 0
n7 = 100
Nx_z = Nx + (n2 + n4 + n6) / 2
Ny_s = n1 + n2 + n3 + n4 + n5 + n6 + n7  # PhC length param of Straight WG
Ny_z = n1 + n3 + n5 + n7 - (n2 + n4 + n6) / 2  # PhC length param of Z-shaped WG
x_phc = 0.5 * math.sqrt(3) * (2 * Nx - 1) * a
x_phc_z = 0.5 * math.sqrt(3) * (2 * Nx - 1 + n2 + n4 + n6) * a
y_phc_s = (Ny_s - 0.0) * a
y_phc_z = (Ny_z - 0.0) * a
x = 2 * Iv + x_initial - 0.5 * x_phc + S * a / math.sqrt(3) / 4
file.write('zoom' + '\n')
file.write('W' + '\n')
file.write('0,1000' + '\n')
file.write('-20000,-1000' + '\n')
file.write('copy' + '\n')
file.write('fence' + '\n')
file.write('-11000,-110' + '\n')
file.write('-9000,-110' + '\n')
file.write('' + '\n')
file.write('' + '\n')
file.write('D' + '\n')
file.write(
    str(x + 0.5 * x_phc - S * a / math.sqrt(3) / 4 + 10000 + incident_shift() * a * math.sqrt(3)) + ','
    + str(y + 100 - incident_m_s) + '\n')
file.write('\n')
file.write('fence' + '\n')
file.write('-11000,110' + '\n')
file.write('-9000,110' + '\n')
file.write('' + '\n')
file.write('' + '\n')
file.write('D' + '\n')
file.write(
    str(x + 0.5 * x_phc - S * a / math.sqrt(3) / 4 + 10000 + incident_shift() * a * math.sqrt(3)) + ','
    + str(y + y_phc_s - 100 + incident_m_s) + '\n')


# start making the 4th of 13 WGs, i.e. 4 bends Z-shaped WG
x = 3 * Iv + x_initial - 0.5 * x_phc_z + S * a / math.sqrt(3) / 4

file.write('zoom' + '\n')
file.write('W' + '\n')
file.write('0,1000' + '\n')
file.write('-20000,-1000' + '\n')
file.write('copy' + '\n')
file.write('fence' + '\n')
file.write('-11000,-110' + '\n')
file.write('-9000,-110' + '\n')
file.write('' + '\n')
file.write('' + '\n')
file.write('D' + '\n')
file.write(str(x + 0.5 * x_phc - S * a / math.sqrt(3) / 4 + 10000 + incident_shift() * a * math.sqrt(
    3)) + ',' + str(y + 100 - incident_m_s) + '\n')
file.write('\n')
file.write('fence' + '\n')
file.write('-11000,110' + '\n')
file.write('-9000,110' + '\n')
file.write('' + '\n')
file.write('' + '\n')
file.write('D' + '\n')
file.write(str(x + x_phc_z - 0.5 * x_phc - S * a / math.sqrt(3) / 4 + 10000 +
               incident_shift() * a * math.sqrt(3)) + ',' + str(y + y_phc_z - 100 + incident_m_s) + '\n')


# finish making the 4th WG

# start making the 5th of 13 waveguides i.e. straight counterpart of 6 bends Z-shaped WG
Nx = 22  # bulk lattice thickness
n1 = 100
n2 = 30
n3 = 30
n4 = 30
n5 = 30
n6 = 30
n7 = 100
Nx_z = Nx + (n2 + n4 + n6) / 2
Ny_s = n1 + n2 + n3 + n4 + n5 + n6 + n7  # PhC length param of Straight WG
Ny_z = n1 + n3 + n5 + n7 - (n2 + n4 + n6) / 2  # PhC length param of Z-shaped WG
x_phc = 0.5 * math.sqrt(3) * (2 * Nx - 1) * a
x_phc_z = 0.5 * math.sqrt(3) * (2 * Nx - 1 + n2 + n4 + n6) * a
y_phc_s = (Ny_s - 0.0) * a
y_phc_z = (Ny_z - 0.0) * a
x = 4 * Iv + x_initial - 0.5 * x_phc + S * a / math.sqrt(3) / 4

file.write('zoom' + '\n')
file.write('W' + '\n')
file.write('0,1000' + '\n')
file.write('-20000,-1000' + '\n')
file.write('copy' + '\n')
file.write('fence' + '\n')
file.write('-11000,-110' + '\n')
file.write('-9000,-110' + '\n')
file.write('' + '\n')
file.write('' + '\n')
file.write('D' + '\n')
file.write(
    str(x + 0.5 * x_phc - S * a / math.sqrt(3) / 4 + 10000 + incident_shift() * a * math.sqrt(3)) + ','
    + str(y + 100 - incident_m_s) + '\n')
file.write('\n')
file.write('fence' + '\n')
file.write('-11000,110' + '\n')
file.write('-9000,110' + '\n')
file.write('' + '\n')
file.write('' + '\n')
file.write('D' + '\n')
file.write(
    str(x + 0.5 * x_phc - S * a / math.sqrt(3) / 4 + 10000 + incident_shift() * a * math.sqrt(3)) + ','
    + str(y + y_phc_s - 100 + incident_m_s) + '\n')
# finish making the 5th of 13 WGs

# start making the 6th of 13 WGs, i.e. 6 bends Z-shaped WG
x = 5 * Iv + x_initial - 0.5 * x_phc_z + S * a / math.sqrt(3) / 4

file.write('zoom' + '\n')
file.write('W' + '\n')
file.write('0,1000' + '\n')
file.write('-20000,-1000' + '\n')
file.write('copy' + '\n')
file.write('fence' + '\n')
file.write('-11000,-110' + '\n')
file.write('-9000,-110' + '\n')
file.write('' + '\n')
file.write('' + '\n')
file.write('D' + '\n')
file.write(str(x + 0.5 * x_phc - S * a / math.sqrt(3) / 4 + 10000 + incident_shift() * a * math.sqrt(
    3)) + ',' + str(y + 100 - incident_m_s) + '\n')
file.write('\n')
file.write('fence' + '\n')
file.write('-11000,110' + '\n')
file.write('-9000,110' + '\n')
file.write('' + '\n')
file.write('' + '\n')
file.write('D' + '\n')
file.write(str(x + x_phc_z - 0.5 * x_phc - S * a / math.sqrt(3) / 4 + 10000 +
               incident_shift() * a * math.sqrt(3)) + ',' + str(y + y_phc_z - 100 + incident_m_s) + '\n')




# finish making the 6th WG











# start making the 7th of 13 waveguides i.e. straight counterpart of 7 bends Z-shaped WG
Nx = 22  # bulk lattice thickness
n1 = 30
n2 = 30
n3 = 30
n4 = 30
n5 = 30
n6 = 30
n7 = 30
n8 = 30
n9 = 0
n10 = 0
n_max = max(n1, n2, n3, n4, n5, n6, n7, n8, n9, n10)

Nx_z = Nx + n_max / 2
Ny_s = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9 + n10  # PhC length param of Straight WG
Ny_z = (n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9 + n10) / 2  # PhC length param of zigzag WG
x_phc = 0.5 * math.sqrt(3) * (2 * Nx - 1) * a
x_phc_z = 0.5 * math.sqrt(3) * (2 * Nx - 1 + n_max) * a
y_phc_s = (Ny_s - 0.0) * a
y_phc_z = (Ny_z - 0.5) * a
x = 6 * Iv + x_initial - 0.5 * x_phc + S * a / math.sqrt(3) / 4

file.write('zoom' + '\n')
file.write('W' + '\n')
file.write('0,1000' + '\n')
file.write('-20000,-1000' + '\n')
file.write('copy' + '\n')
file.write('fence' + '\n')
file.write('-11000,-110' + '\n')
file.write('-9000,-110' + '\n')
file.write('' + '\n')
file.write('' + '\n')
file.write('D' + '\n')
file.write(
    str(x + 0.5 * x_phc - S * a / math.sqrt(3) / 4 + 10000 + incident_shift() * a * math.sqrt(3)) + ','
    + str(y + 100 - incident_m_s) + '\n')
file.write('\n')
file.write('fence' + '\n')
file.write('-11000,110' + '\n')
file.write('-9000,110' + '\n')
file.write('' + '\n')
file.write('' + '\n')
file.write('D' + '\n')
file.write(
    str(x + 0.5 * x_phc - S * a / math.sqrt(3) / 4 + 10000 + incident_shift() * a * math.sqrt(3)) + ','
    + str(y + y_phc_s - 100 + incident_m_s) + '\n')

# start making the 8th of 13 WGs, i.e. 7 bends Z-shaped WG

x = 7 * Iv + x_initial - 0.5 * x_phc_z + S * a / math.sqrt(3) / 2

W_shift = 1.5
C_shift = 2


x_dsi = x + 0.5 * x_phc_z + (n1 * a / 2) * math.sqrt(3) / 2 - W_shift * a / math.sqrt(
    3) / 2 - S * a / math.sqrt(3) / 2
y_dsi = y
x_usi = x + 0.5 * x_phc_z + (n8 - n7 + n6 - n5 + n4 - n3 + n2 - n1 / 2 - 0) * a * math.sqrt(
    3) / 2 - W_shift * a / math.sqrt(3) / 2 - S * a / math.sqrt(3) / 2
y_usi = y + (n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 - 0) * a / 2
l_barrier = 10 * math.sqrt(3) * a



check1124 = 0

incident_n_s = 0 * a

if S == -2:
    incident_n_s = 0.75 * a
if S == -1:
    incident_n_s = 0.5 * a
if S == 1:
    incident_n_s = 0.5 * a
if S == 2:
    incident_n_s = 0.75 * a
if S == 3:
    incident_n_s = 0.5 * a

if check1124 == 1:
    file.write('line' + '\n')
    file.write(str(x_dsi + l_barrier / 2 - incident_n_s* math.sqrt(3) / 2) + ',' + str(y_dsi + math.sqrt(3) * l_barrier / 2 + incident_n_s / 2) + '\n')
    file.write(str(x_dsi - l_barrier / 2 - incident_n_s * math.sqrt(3) / 2) + ',' + str(y_dsi - math.sqrt(3) * l_barrier / 2 + incident_n_s / 2) + '\n')
    file.write('' + '\n')
    file.write('line' + '\n')
    file.write(str(x_usi + l_barrier / 2 - incident_n_s * math.sqrt(3) / 2) + ',' + str(
        y_usi - math.sqrt(3) * l_barrier / 2 - incident_n_s / 2) + '\n')
    file.write(str(x_usi - l_barrier / 2 - incident_n_s * math.sqrt(3) / 2) + ',' + str(
        y_usi + math.sqrt(3) * l_barrier / 2 - incident_n_s / 2) + '\n')
    file.write('' + '\n')
    file.write('fox' + '\n')

file.write('zoom' + '\n')
file.write('W' + '\n')
file.write('-30000,20000' + '\n')
file.write('-50000,-20000' + '\n')
file.write('copy' + '\n')
file.write('crossing' + '\n')
file.write('-30000,0' + '\n')
file.write('-50000,-20000' + '\n')
file.write('' + '\n')
file.write('D' + '\n')
file.write(str(
    x_dsi - (incident_n_s - 0.5 * a) * math.sqrt(3) / 2 + 40000 + 0.5 * incident_shift() * a * math.sqrt(
        3)) +
           ',' + str(
    y_dsi + (incident_n_s - 0.5 * a) / 2 + 8000 + incident_shift() * a * math.sqrt(3) * math.sqrt(
        3) / 2) + '\n')
file.write('\n')
file.write('crossing' + '\n')
file.write('-50000,20000' + '\n')
file.write('-30000,0' + '\n')
file.write('' + '\n')
file.write('D' + '\n')
file.write(str(
    x_usi - (incident_n_s - 0.5 * a) * math.sqrt(3) / 2 + 40000 + 0.5 * incident_shift() * a * math.sqrt(
        3)) + ','
           + str(
    y_usi - (incident_n_s - 0.5 * a) / 2 - 8000 - incident_shift() * a * math.sqrt(3) * math.sqrt(
        3) / 2) + '\n')
# finish making the 8th WG



# start making the 9th of 13 WGs, i.e. uneven 7 bends Z-shaped WG
Nx = 22  # bulk lattice thickness
n1 = 34
n2 = 32
n3 = 29
n4 = 27
n5 = 26
n6 = 28
n7 = 31
n8 = 33
n9 = 0
n10 = 0
n_max = max(n1, n2, n3, n4, n5, n6, n7, n8, n9, n10)

Nx_z = Nx + n_max / 2
Ny_s = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9 + n10  # PhC length param of Straight WG
Ny_z = (n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9 + n10) / 2  # PhC length param of zigzag WG
x_phc = 0.5 * math.sqrt(3) * (2 * Nx - 1) * a
x_phc_z = 0.5 * math.sqrt(3) * (2 * Nx - 1 + n_max) * a
y_phc_s = (Ny_s - 0.0) * a
y_phc_z = (Ny_z - 0.5) * a
x = 8 * Iv + x_initial - 0.5 * x_phc_z + S * a / math.sqrt(3) / 2


W_shift = -4.5
C_shift = 5

x_dsi = x + 0.5 * x_phc_z + (n1 * a / 2) * math.sqrt(3) / 2 - W_shift * a / math.sqrt(
    3) / 2 - S * a / math.sqrt(3) / 2
y_dsi = y
x_usi = x + 0.5 * x_phc_z + (n8 - n7 + n6 - n5 + n4 - n3 + n2 - n1 / 2 - 0) * a * math.sqrt(
    3) / 2 - W_shift * a / math.sqrt(3) / 2 - S * a / math.sqrt(3) / 2
y_usi = y + (n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 - 0) * a / 2
l_barrier = 10 * math.sqrt(3) * a


# start making incident Si wires
check1124 = 0

if check1124 == 1:
    file.write('line' + '\n')
    file.write(str(x_dsi + l_barrier / 2 - incident_n_s * math.sqrt(3) / 2) + ',' + str(
        y_dsi + math.sqrt(3) * l_barrier / 2 + incident_n_s / 2) + '\n')
    file.write(str(x_dsi - l_barrier / 2 - incident_n_s * math.sqrt(3) / 2) + ',' + str(
        y_dsi - math.sqrt(3) * l_barrier / 2 + incident_n_s / 2) + '\n')
    file.write('' + '\n')
    file.write('line' + '\n')
    file.write(str(x_usi + l_barrier / 2 - incident_n_s * math.sqrt(3) / 2) + ',' + str(
        y_usi - math.sqrt(3) * l_barrier / 2 - incident_n_s / 2) + '\n')
    file.write(str(x_usi - l_barrier / 2 - incident_n_s * math.sqrt(3) / 2) + ',' + str(
        y_usi + math.sqrt(3) * l_barrier / 2 - incident_n_s / 2) + '\n')
    file.write('' + '\n')

file.write('zoom' + '\n')
file.write('W' + '\n')
file.write('-30000,20000' + '\n')
file.write('-50000,-20000' + '\n')
file.write('copy' + '\n')
file.write('crossing' + '\n')
file.write('-30000,0' + '\n')
file.write('-50000,-20000' + '\n')
file.write('' + '\n')
file.write('D' + '\n')
file.write(str(
    x_dsi - (incident_n_s - 0.5 * a) * math.sqrt(3) / 2 + 40000 + 0.5 * incident_shift() * a * math.sqrt(
        3)) +
           ',' + str(
    y_dsi + (incident_n_s - 0.5 * a) / 2 + 8000 + incident_shift() * a * math.sqrt(3) * math.sqrt(
        3) / 2) + '\n')
file.write('\n')
file.write('crossing' + '\n')
file.write('-50000,20000' + '\n')
file.write('-30000,0' + '\n')
file.write('' + '\n')
file.write('D' + '\n')
file.write(str(
    x_usi - (incident_n_s - 0.5 * a) * math.sqrt(3) / 2 + 40000 + 0.5 * incident_shift() * a * math.sqrt(
        3)) + ','
           + str(
    y_usi - (incident_n_s - 0.5 * a) / 2 - 8000 - incident_shift() * a * math.sqrt(3) * math.sqrt(
        3) / 2) + '\n')


# finish making the 9th WG

# start making the 10th of 13 waveguides i.e. straight counterpart of 9 bends Z-shaped WG
Nx = 22  # bulk lattice thickness
n1 = 30
n2 = 30
n3 = 30
n4 = 30
n5 = 30
n6 = 30
n7 = 30
n8 = 30
n9 = 30
n10 = 30
n_max = max(n1, n2, n3, n4, n5, n6, n7, n8, n9, n10)

Nx_z = Nx + n_max / 2
Ny_s = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9 + n10  # PhC length param of Straight WG
Ny_z = (n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9 + n10) / 2  # PhC length param of zigzag WG
x_phc = 0.5 * math.sqrt(3) * (2 * Nx - 1) * a
x_phc_z = 0.5 * math.sqrt(3) * (2 * Nx - 1 + n_max) * a
y_phc_s = (Ny_s - 0.0) * a
y_phc_z = (Ny_z - 0.5) * a
x = 9 * Iv + x_initial - 0.5 * x_phc + S * a / math.sqrt(3) / 4

file.write('zoom' + '\n')
file.write('W' + '\n')
file.write('0,1000' + '\n')
file.write('-20000,-1000' + '\n')
file.write('copy' + '\n')
file.write('fence' + '\n')
file.write('-11000,-110' + '\n')
file.write('-9000,-110' + '\n')
file.write('' + '\n')
file.write('' + '\n')
file.write('D' + '\n')
file.write(
    str(x + 0.5 * x_phc - S * a / math.sqrt(3) / 4 + 10000 + incident_shift() * a * math.sqrt(3)) + ','
    + str(y + 100 - incident_m_s) + '\n')
file.write('\n')
file.write('fence' + '\n')
file.write('-11000,110' + '\n')
file.write('-9000,110' + '\n')
file.write('' + '\n')
file.write('' + '\n')
file.write('D' + '\n')
file.write(
    str(x + 0.5 * x_phc - S * a / math.sqrt(3) / 4 + 10000 + incident_shift() * a * math.sqrt(3)) + ','
    + str(y + y_phc_s - 100 + incident_m_s) + '\n')


# finish making the 10th of 13 WGs

# start making the 11th of 13 WGs, i.e. 9 bends Z-shaped WG

x = 10 * Iv + x_initial - 0.5 * x_phc_z + S * a / math.sqrt(3) / 2




W_shift = 1.5
C_shift = 2


x_dsi = x + 0.5 * x_phc_z + (n1 * a / 2) * math.sqrt(3) / 2 - W_shift * a / math.sqrt(
    3) / 2 - S * a / math.sqrt(3) / 2
y_dsi = y
x_usi = x + 0.5 * x_phc_z + (n10 - n9 + n8 - n7 + n6 - n5 + n4 - n3 + n2 - n1 / 2 - 0) * a * math.sqrt(
    3) / 2 - W_shift * a / math.sqrt(3) / 2 - S * a / math.sqrt(3) / 2
y_usi = y + (n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9 + n10 - 0) * a / 2
l_barrier = 10 * math.sqrt(3) * a


# start making incident Si wires
check1124 = 0


if check1124 == 1:
    file.write('line' + '\n')
    file.write(str(x_dsi + l_barrier / 2 - incident_n_s * math.sqrt(3) / 2) + ',' + str(
        y_dsi + math.sqrt(3) * l_barrier / 2 + incident_n_s / 2) + '\n')
    file.write(str(x_dsi - l_barrier / 2 - incident_n_s * math.sqrt(3) / 2) + ',' + str(
        y_dsi - math.sqrt(3) * l_barrier / 2 + incident_n_s / 2) + '\n')
    file.write('' + '\n')
    file.write('line' + '\n')
    file.write(str(x_usi + l_barrier / 2 - incident_n_s * math.sqrt(3) / 2) + ',' + str(
        y_usi - math.sqrt(3) * l_barrier / 2 - incident_n_s / 2) + '\n')
    file.write(str(x_usi - l_barrier / 2 - incident_n_s * math.sqrt(3) / 2) + ',' + str(
        y_usi + math.sqrt(3) * l_barrier / 2 - incident_n_s / 2) + '\n')
    file.write('' + '\n')

file.write('zoom' + '\n')
file.write('W' + '\n')
file.write('-30000,20000' + '\n')
file.write('-50000,-20000' + '\n')
file.write('copy' + '\n')
file.write('crossing' + '\n')
file.write('-30000,0' + '\n')
file.write('-50000,-20000' + '\n')
file.write('' + '\n')
file.write('D' + '\n')
file.write(str(
    x_dsi - (incident_n_s - 0.5 * a) * math.sqrt(3) / 2 + 40000 + 0.5 * incident_shift() * a * math.sqrt(
        3)) +
           ',' + str(
    y_dsi + (incident_n_s - 0.5 * a) / 2 + 8000 + incident_shift() * a * math.sqrt(3) * math.sqrt(
        3) / 2) + '\n')
file.write('\n')
file.write('crossing' + '\n')
file.write('-50000,20000' + '\n')
file.write('-30000,0' + '\n')
file.write('' + '\n')
file.write('D' + '\n')
file.write(str(
    x_usi - (incident_n_s - 0.5 * a) * math.sqrt(3) / 2 + 40000 + 0.5 * incident_shift() * a * math.sqrt(
        3)) + ','
           + str(
    y_usi - (incident_n_s - 0.5 * a) / 2 - 8000 - incident_shift() * a * math.sqrt(3) * math.sqrt(
        3) / 2) + '\n')


# finish making the 11th WG

# start making the 12th of 13 WGs, i.e. uneven 9 bends Z-shaped WG



file.write('-layer' + '\n')
file.write('set' + '\n')
file.write('0' + '\n')
file.write('' + '\n')
Nx = 22  # bulk lattice thickness
n1 = 35
n2 = 33
n3 = 31
n4 = 28
n5 = 26
n6 = 25
n7 = 27
n8 = 29
n9 = 32
n10 = 34
n_max = max(n1, n2, n3, n4, n5, n6, n7, n8, n9, n10)

Nx_z = Nx + n_max / 2
Ny_s = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9 + n10  # PhC length param of Straight WG
Ny_z = (n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9 + n10) / 2  # PhC length param of zigzag WG
x_phc = 0.5 * math.sqrt(3) * (2 * Nx - 1) * a
x_phc_z = 0.5 * math.sqrt(3) * (2 * Nx - 1 + n_max) * a
y_phc_s = (Ny_s - 0.0) * a
y_phc_z = (Ny_z - 0.5) * a
x = 11 * Iv + x_initial - 0.5 * x_phc_z + S * a / math.sqrt(3) / 2






W_shift = -7.5
C_shift = 3
x_dsi = x + 0.5 * x_phc_z + (n1 * a / 2) * math.sqrt(3) / 2 - W_shift * a / math.sqrt(
    3) / 2 - S * a / math.sqrt(3) / 2
y_dsi = y
x_usi = x + 0.5 * x_phc_z + (n10 - n9 + n8 - n7 + n6 - n5 + n4 - n3 + n2 - n1 / 2 - 0) * a * math.sqrt(
    3) / 2 - W_shift * a / math.sqrt(3) / 2 - S * a / math.sqrt(3) / 2
y_usi = y + (n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9 + n10 - 0) * a / 2
l_barrier = 10 * math.sqrt(3) * a



# start making incident Si wires
check1124 = 0

if check1124 == 1:
    file.write('line' + '\n')
    file.write(str(x_dsi + l_barrier / 2 - incident_n_s * math.sqrt(3) / 2) + ',' + str(
        y_dsi + math.sqrt(3) * l_barrier / 2 + incident_n_s / 2) + '\n')
    file.write(str(x_dsi - l_barrier / 2 - incident_n_s * math.sqrt(3) / 2) + ',' + str(
        y_dsi - math.sqrt(3) * l_barrier / 2 + incident_n_s / 2) + '\n')
    file.write('' + '\n')
    file.write('line' + '\n')
    file.write(str(x_usi + l_barrier / 2 - incident_n_s * math.sqrt(3) / 2) + ',' + str(
        y_usi - math.sqrt(3) * l_barrier / 2 - incident_n_s / 2) + '\n')
    file.write(str(x_usi - l_barrier / 2 - incident_n_s * math.sqrt(3) / 2) + ',' + str(
        y_usi + math.sqrt(3) * l_barrier / 2 - incident_n_s / 2) + '\n')
    file.write('' + '\n')

file.write('zoom' + '\n')
file.write('W' + '\n')
file.write('-30000,20000' + '\n')
file.write('-50000,-20000' + '\n')
file.write('copy' + '\n')
file.write('crossing' + '\n')
file.write('-30000,0' + '\n')
file.write('-50000,-20000' + '\n')
file.write('' + '\n')
file.write('D' + '\n')
file.write(str(
    x_dsi - (incident_n_s - 0.5 * a) * math.sqrt(3) / 2 + 40000 + 0.5 * incident_shift() * a * math.sqrt(
        3)) +
           ',' + str(
    y_dsi + (incident_n_s - 0.5 * a) / 2 + 8000 + incident_shift() * a * math.sqrt(3) * math.sqrt(
        3) / 2) + '\n')
file.write('\n')
file.write('crossing' + '\n')
file.write('-50000,20000' + '\n')
file.write('-30000,0' + '\n')
file.write('' + '\n')
file.write('D' + '\n')
file.write(str(
    x_usi - (incident_n_s - 0.5 * a) * math.sqrt(3) / 2 + 40000 + 0.5 * incident_shift() * a * math.sqrt(
        3)) + ','
           + str(
    y_usi - (incident_n_s - 0.5 * a) / 2 - 8000 - incident_shift() * a * math.sqrt(3) * math.sqrt(
        3) / 2) + '\n')


# finish making the 12th WG

x = 12 * Iv + x_initial
file.write('zoom' + '\n')
file.write('W' + '\n')
file.write(str(x - 10000) + ',' + str(y - 10000) + '\n')
file.write(str(x + x_phc_z + 10000) + ',' + str(y + y_phc_z + 10000) + '\n')

dummy =0
if a_type == 'A3':
    dummy = 9
else:

    a=410
    incident_m_s = 0.5 * a
    # delete proto-Si-wires
    file.write('zoom' + '\n')
    file.write('W' + '\n')
    file.write('-50000,20000' + '\n')
    file.write('0,-20000' + '\n')
    file.write('erase' + '\n')
    file.write('crossing' + '\n')
    file.write('-50000,20000' + '\n')
    file.write('0,-20000' + '\n')
    file.write('' + '\n')
    #insert new Si-wires for reference WG
    if a_type=='A1':
        Si_width=700
    elif a_type=='A2':
        Si_width=500
    else:
        print("Invalid lattice constant setting")

    R_c=104
    S=3
    hole_type='C'
    wg_type='1_1'
    valley=0

    # insert Si waveguides
    file.write('zoom' + '\n')
    file.write('W' + '\n')
    file.write('0,1000' + '\n')
    file.write('-20000,-1000' + '\n')
    file.write('-insertcontent' + '\n')
    file.write('/Users/inoue/Documents/CAD_ref/Si_' + str(Si_width) + '.dwg' + '\n')
    file.write(str(Si_width) + '\n')
    file.write('-10000,-100' + '\n')
    file.write('1' + '\n')
    file.write('1' + '\n')
    file.write('0' + '\n')
    file.write('mirror' + '\n')
    file.write('fence' + '\n')
    file.write('-11000,-110' + '\n')
    file.write('-9000,-110' + '\n')
    file.write('' + '\n')
    file.write('' + '\n')
    file.write('0,0' + '\n')
    file.write('1,0' + '\n')
    file.write('No' + '\n')

    Nx = 22  # bulk lattice thickness
    n1 = 60
    n2 = 0
    n3 = 0
    n4 = 0
    n5 = 0
    n6 = 0
    n7 = 60
    Nx_z = Nx + (n2 + n4 + n6) / 2
    Ny_s = n1 + n2 + n3 + n4 + n5 + n6 + n7  # PhC length param of Straight WG
    Ny_z = n1 + n3 + n5 + n7 - (n2 + n4 + n6) / 2  # PhC length param of Z-shaped WG
    x_phc = 0.5 * math.sqrt(3) * (2 * Nx - 1) * a
    x_phc_z = 0.5 * math.sqrt(3) * (2 * Nx - 1 + n2 + n4 + n6) * a
    y_phc_s = (Ny_s - 0.0) * a
    y_phc_z = (Ny_z - 0.0) * a
    x = 12 * Iv + x_initial - 0.5 * x_phc + S * a / math.sqrt(3) / 4

    # start making incident Si wires
    file.write('zoom' + '\n')
    file.write('W' + '\n')
    file.write('0,1000' + '\n')
    file.write('-20000,-1000' + '\n')
    file.write('copy' + '\n')
    file.write('fence' + '\n')
    file.write('-11000,-110' + '\n')
    file.write('-9000,-110' + '\n')
    file.write('' + '\n')
    file.write('' + '\n')
    file.write('D' + '\n')
    file.write(
        str(x + 0.5 * x_phc - S * a / math.sqrt(3) / 4 + 10000 + incident_shift() * a * math.sqrt(3)) + ','
        + str(y + 100 - incident_m_s) + '\n')
    file.write('\n')
    file.write('fence' + '\n')
    file.write('-11000,110' + '\n')
    file.write('-9000,110' + '\n')
    file.write('' + '\n')
    file.write('' + '\n')
    file.write('D' + '\n')
    file.write(
        str(x + 0.5 * x_phc - S * a / math.sqrt(3) / 4 + 10000 + incident_shift() * a * math.sqrt(3)) + ','
        + str(y + y_phc_s - 100 + incident_m_s) + '\n')

# delete proto-Si-wires
file.write('zoom' + '\n')
file.write('W' + '\n')
file.write('-50000,20000' + '\n')
file.write('0,-20000' + '\n')
file.write('erase' + '\n')
file.write('crossing' + '\n')
file.write('-50000,20000' + '\n')
file.write('0,-20000' + '\n')
file.write('' + '\n')

if a_type == 'A3':
    file.write('-layer' + '\n')
    file.write('set' + '\n')
    file.write('31' + '\n')
    file.write('' + '\n')
    # make rectangle contour for the 1/3 device area
    Iv_wg = 51000
    l_area = 3230000  # 横サイズ
    w_area = 4000000  # 縦サイズ
    file.write('rectangle' + '\n')
    file.write(str(-Iv_wg + 10000) + ',' + str(-w_area / 2) + '\n')
    file.write(str(l_area + Iv_wg + 10000) + ',' + str(w_area / 2) + '\n')

    file.write('-layer' + '\n')
    file.write('set' + '\n')
    file.write('0' + '\n')
    file.write('' + '\n')
print('-----FINISH !-----')
file.close()




