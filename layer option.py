import os
import math

# hajime
os.chdir("/Users/inoue/Documents/CAD_ref/py")
file = open('WAVEGUIDE!!!' + '.scr', 'w')
file.write('-layer' + '\n')
file.write('new' + '\n')
file.write('1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33' + '\n')
file.write('' + '\n')
file.write('-layer' + '\n')  # レイヤーコマンドの起動
file.write('color' + '\n')
file.write('191' + '\n')
file.write('30' + '\n' + '\n')
file.write('-layer' + '\n')  # レイヤーコマンドの起動
file.write('color' + '\n')
file.write('241' + '\n')
file.write('31' + '\n' + '\n')

chip_type = 2

a=410
honey = 0
incident_m_s = 0.5 * a
S = 3
dummy = 0
check_grid = 0

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



y=10000
x1 = 107250
x2 = 2177500
x3 = 3282500

file.write('zoom' + '\n')
file.write('W' + '\n')
file.write('-371000,278000' + '\n')
file.write('2260000,-774000' + '\n')

if chip_type == 1:
    x1 = 1072500
    x2 = 2177500
    x3 = 3282500
    file.write('change' + '\n')
    file.write('fence' + '\n')
    file.write('9000,-720000'+ '\n')
    file.write('9000,-520000'+ '\n')
    file.write('' + '\n')
    file.write('fence' + '\n')
    file.write('1110000,-720000'+ '\n')
    file.write('1110000,-520000'+ '\n')
    file.write('' + '\n')
    file.write('fence' + '\n')
    file.write('2210000,-720000'+ '\n')
    file.write('2210000,-520000'+ '\n')
    file.write('' + '\n')
elif chip_type == 2:
    x1 = 1030000
    x2 = 2135000
    x3 = 3240000
    file.write('change' + '\n')
    file.write('fence' + '\n')
    file.write('-34000,-720000'+ '\n')
    file.write('-34000,-520000'+ '\n')
    file.write('' + '\n')
    file.write('fence' + '\n')
    file.write('1070000,-720000'+ '\n')
    file.write('1070000,-520000'+ '\n')
    file.write('' + '\n')
    file.write('fence' + '\n')
    file.write('2170000,-720000'+ '\n')
    file.write('2170000,-520000'+ '\n')
    file.write('' + '\n')

file.write('' + '\n')
file.write('properties' + '\n')
file.write('layer' + '\n')
file.write('30' + '\n')
file.write('' + '\n')

file.write('change' + '\n')
file.write('fence' + '\n')
file.write('-42000,0' + '\n')
file.write('-40000,0' + '\n')
file.write('' + '\n')
file.write('' + '\n')
file.write('properties' + '\n')
file.write('layer' + '\n')
file.write('31' + '\n')
file.write('' + '\n')

# make the first W1WG for reference
file.write('zoom' + '\n')
file.write('W' + '\n')
file.write(str(x1-30000) + ',' + str(y-100000) + '\n')
file.write(str(x1+30000) + ',' + str(y+100000) + '\n')

file.write('erase' + '\n')
file.write('crossing' + '\n')
file.write(str(x1-1000) + ',' + str(y-100) + '\n')
file.write(str(x1+1000) + ',' + str(y+50000+1000) + '\n')
file.write('' + '\n')



# insert new Si-wires for reference WG
Si_width = 700
a = 410
incident_m_s = 0.5 * a

R_c = 104
S = 3
hole_type = 'C'
wg_type = '1_1'
valley = 0

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
x = x1 - 0.5 * x_phc + S * a / math.sqrt(3) / 4
# symbol lines/holes
file.write('zoom' + '\n')
file.write('W' + '\n')
file.write(str(x - 10000) + ',' + str(y - 10000) + '\n')
file.write(str(x + x_phc + 10000) + ',' + str(y + y_phc_s + 10000) + '\n')
sp1 = str(x + 100) + ',' + str(y - 16 * a)  # 穴を配置する位置のx軸方向に+100nmずらした部分
sm1 = str(x - 100) + ',' + str(y - 16 * a)  # 穴を配置する位置のx軸方向に-100nmずらした部分

file.write('POLYGON' + '\n')
file.write('8' + '\n')
file.write(str(x) + ',' + str(y - 16 * a) + '\n')
file.write('I' + '\n')
file.write(str(R_c) + '\n')  # 半径rを指定
# start making bulk lattice with rectangular arrays
file.write('_Array' + '\n')
file.write('box' + '\n')
file.write(str(x + 1000) + ',' + str(y + 1000 - 16 * a) + '\n')
file.write(str(x - 1000) + ',' + str(y - 1000 - 16 * a) + '\n')
file.write('' + '\n')
file.write('Rectangular' + '\n')
file.write(str(Ny_s + 32) + '\n')
file.write(str(Nx) + '\n')
file.write(str(a) + '\n')
file.write(str(math.sqrt(3) * a) + '\n')
file.write('copy' + '\n')
file.write('box' + '\n')
file.write(str(x + Nx * math.sqrt(3) * a + 20) + ',' + str(y + Ny_s * a + 20 + 16 * a) + '\n')
file.write(str(x - 1.01 * math.sqrt(3) * a) + ',' + str(y - 20 - 16 * a) + '\n')
file.write('' + '\n')
file.write('0,0' + '\n')
file.write(str(math.sqrt(3) * a / 2) + ',' + str(a / 2) + '\n')
file.write('erase' + '\n')
file.write('crossing' + '\n')
file.write(str(x + 0.5 * x_phc - a * math.sqrt(3) / 4) + ',' + str(y + y_phc_s + 16 * a) + '\n')
file.write(str(x) + ',' + str(y - 16 * a) + '\n')
file.write('' + '\n')
# start making the waveguide

"""file.write('rectangle' + '\n')
file.write(str(x + 0.5 * x_phc) + ',' + str(y + y_phc_s+10*a) + '\n')
file.write(str(x) + ',' + str(y-10*a) + '\n')"""

# make domain 1 bulk lattice in Y- area
file.write('zoom' + '\n')
file.write('W' + '\n')
file.write(str(x - 10000) + ',' + str(-y + 10000) + '\n')
file.write(str(x + x_phc + 10000) + ',' + str(-y - y_phc_s - 10000) + '\n')

file.write('POLYGON' + '\n')
file.write('8' + '\n')
file.write(str(x) + ',' + str(-y + 16 * a) + '\n')
file.write('I' + '\n')
file.write(str(R_c) + '\n')  # 半径rを指定

file.write('_Array' + '\n')
file.write('box' + '\n')
file.write(str(x + 1000) + ',' + str(-(y + 1000 - 16 * a)) + '\n')
file.write(str(x - 1000) + ',' + str(-(y - 1000 - 16 * a)) + '\n')
file.write('' + '\n')
file.write('Rectangular' + '\n')
file.write(str(Ny_s + 32) + '\n')
file.write(str(Nx) + '\n')
file.write(str(-a) + '\n')
file.write(str(math.sqrt(3) * a) + '\n')
file.write('copy' + '\n')
file.write('box' + '\n')
file.write(str(x + Nx * math.sqrt(3) * a + 20) + ',' + str(-(y + Ny_s * a + 20 + 16 * a)) + '\n')
file.write(str(x - 1.01 * math.sqrt(3) * a) + ',' + str(-(y - 20 - 16 * a)) + '\n')
file.write('' + '\n')
file.write('0,0' + '\n')
file.write(str(math.sqrt(3) * a / 2) + ',' + str(-a / 2) + '\n')

"""file.write('rectangle' + '\n')
file.write(str(x + 1 * x_phc) + ',' + str(-y - y_phc_s - 16 * a) + '\n')
file.write(str(x + 0.5 * x_phc + a * math.sqrt(3) / 4) + ',' + str(
    -y + 16 * a) + '\n')"""

file.write('erase' + '\n')
file.write('crossing' + '\n')
file.write(str(x + 1 * x_phc) + ',' + str(-y - y_phc_s - 16 * a) + '\n')
file.write(str(x + 0.5 * x_phc + a * math.sqrt(3) / 4) + ',' + str(
    -y + 16 * a) + '\n')
file.write('' + '\n')
file.write('mirror' + '\n')
file.write('crossing' + '\n')
file.write(str(x + 0.5 * x_phc - a * math.sqrt(3) / 4) + ',' + str(-(y + y_phc_s + 16 * a)) + '\n')
file.write(str(x) + ',' + str(-y + 16 * a) + '\n')
file.write('' + '\n')
file.write('0,0' + '\n')
file.write('1,0' + '\n')
file.write('yes' + '\n')

file.write('zoom' + '\n')
file.write('W' + '\n')
file.write(str(x - 10000) + ',' + str(y - 10000) + '\n')
file.write(str(x + x_phc + 10000) + ',' + str(y + y_phc_s + 10000) + '\n')
# separate domain layer
if valley == 1:
    file.write('change' + '\n')
    file.write('crossing' + '\n')
    file.write(str(x + 0.5 * x_phc - a * math.sqrt(3) / 4) + ',' + str(y + y_phc_s + 16 * a) + '\n')
    file.write(str(x) + ',' + str(y - 16 * a) + '\n')
    file.write('' + '\n')
    file.write('properties' + '\n')
    file.write('layer' + '\n')
    file.write('1' + '\n')
    file.write('' + '\n')
# domain shift
file.write('move' + '\n')
file.write('crossing' + '\n')
file.write(str(x + 0.5 * x_phc - a * math.sqrt(3) / 4) + ',' + str(y + y_phc_s + 16 * a) + '\n')
file.write(str(x) + ',' + str(y - 16 * a) + '\n')
file.write('' + '\n')
file.write('0,0' + '\n')
file.write(str(S * a / math.sqrt(3)) + '<' + '120' + '\n')
# delete redundant part of the PhC lattice
file.write('erase' + '\n')
file.write('window' + '\n')
file.write(str(x + x_phc + 5 * math.sqrt(3) * a) + ',' + str(y + y_phc_s + 20.5 * a) + '\n')
file.write(str(x - 5 * math.sqrt(3) * a) + ',' + str(y + y_phc_s + 0.1 * a) + '\n')
file.write('remove' + '\n')
file.write('fence' + '\n')
file.write(str(x - 5 * math.sqrt(3) * a) + ',' + str(y + y_phc_s + 0 * a) + '\n')
file.write(str(x + x_phc + 5 * math.sqrt(3) * a) + ',' + str(y + y_phc_s + 0 * a) + '\n')
file.write('' + '\n')
file.write('' + '\n')
file.write('erase' + '\n')
file.write('window' + '\n')
file.write(str(x + x_phc + x_phc + 5 * math.sqrt(3) * a) + ',' + str(y - 0.1 * a) + '\n')
file.write(str(x - x_phc + 5 * math.sqrt(3) * a) + ',' + str(y - 20.5 * a) + '\n')
file.write('remove' + '\n')
file.write('fence' + '\n')
file.write(str(x - 5 * math.sqrt(3) * a) + ',' + str(y) + '\n')
file.write(str(x + x_phc + 5 * math.sqrt(3) * a) + ',' + str(y) + '\n')
file.write('' + '\n')
file.write('\n')
# delete some in/out region holes according to WG mode type
x_si_f = x + 0.5 * x_phc - S * a / math.sqrt(3) / 4 + incident_shift() * a * math.sqrt(3)  # final Si wire position
if wg_type == "1_6":
    file.write('erase' + '\n')
    file.write('fence' + '\n')
    file.write(str(x_si_f) + ',' + str(y + 0 * a) + '\n')
    file.write(str(x_si_f - math.sqrt(3) * a / 4) + ',' + str(y + 0 * a) + '\n')
    file.write('' + '\n')
    file.write('\n')
    file.write('erase' + '\n')
    file.write('fence' + '\n')
    file.write(str(x_si_f) + ',' + str(y + 1 * a) + '\n')
    file.write(str(x_si_f - math.sqrt(3) * a / 4) + ',' + str(y + 1 * a) + '\n')
    file.write('' + '\n')
    file.write('\n')

    file.write('erase' + '\n')
    file.write('fence' + '\n')
    file.write(str(x_si_f) + ',' + str(y + y_phc_s - 0 * a) + '\n')
    file.write(str(x_si_f - math.sqrt(3) * a / 4) + ',' + str(y + y_phc_s - 0 * a) + '\n')
    file.write('' + '\n')
    file.write('\n')
    file.write('erase' + '\n')
    file.write('fence' + '\n')
    file.write(str(x_si_f) + ',' + str(y + y_phc_s - 1 * a) + '\n')
    file.write(str(x_si_f - math.sqrt(3) * a / 4) + ',' + str(y + y_phc_s - 1 * a) + '\n')
    file.write('' + '\n')
    file.write('\n')
if wg_type == "1_3":
    file.write('erase' + '\n')
    file.write('fence' + '\n')
    file.write(str(x_si_f - math.sqrt(3) * a / 12) + ',' + str(y + y_phc_s - 4 * a) + '\n')
    file.write(str(x_si_f - math.sqrt(3) * a / 12) + ',' + str(y + y_phc_s - 3 * a) + '\n')
    file.write(str(x_si_f - math.sqrt(3) * a / 12) + ',' + str(y + y_phc_s - 2 * a) + '\n')
    file.write(str(x_si_f - math.sqrt(3) * a / 12) + ',' + str(y + y_phc_s - a) + '\n')
    file.write(str(x_si_f - math.sqrt(3) * a / 12) + ',' + str(y + y_phc_s) + '\n')
    file.write(str(x_si_f - 5 * math.sqrt(3) * a / 12) + ',' + str(y + y_phc_s) + '\n')
    file.write('' + '\n')
    file.write('\n')

    file.write('erase' + '\n')
    file.write('fence' + '\n')
    file.write(str(x_si_f - math.sqrt(3) * a / 12) + ',' + str(y + 4 * a) + '\n')
    file.write(str(x_si_f - math.sqrt(3) * a / 12) + ',' + str(y + 3 * a) + '\n')
    file.write(str(x_si_f - math.sqrt(3) * a / 12) + ',' + str(y + 2 * a) + '\n')
    file.write(str(x_si_f - math.sqrt(3) * a / 12) + ',' + str(y + a) + '\n')
    file.write(str(x_si_f - math.sqrt(3) * a / 12) + ',' + str(y) + '\n')
    file.write(str(x_si_f - 5 * math.sqrt(3) * a / 12) + ',' + str(y) + '\n')
    file.write('' + '\n')
    file.write('\n')

if wg_type == "2_3":
    file.write('erase' + '\n')
    file.write('fence' + '\n')
    file.write(str(x_si_f - math.sqrt(3) * a / 3) + ',' + str(y) + '\n')
    file.write(str(x_si_f + math.sqrt(3) * a / 3) + ',' + str(y) + '\n')
    file.write('' + '\n')
    file.write('\n')
    file.write('erase' + '\n')
    file.write('fence' + '\n')
    file.write(str(x_si_f - math.sqrt(3) * a / 3) + ',' + str(y + y_phc_s) + '\n')
    file.write(str(x_si_f + math.sqrt(3) * a / 3) + ',' + str(y + y_phc_s) + '\n')
    file.write('' + '\n')
    file.write('\n')
if wg_type == "5_6":
    file.write('erase' + '\n')
    file.write('fence' + '\n')
    file.write(str(x_si_f) + ',' + str(y + 0 * a) + '\n')
    file.write(str(x_si_f + 5 * math.sqrt(3) * a / 12) + ',' + str(y + 0 * a) + '\n')
    file.write('' + '\n')
    file.write('\n')
    file.write('erase' + '\n')
    file.write('fence' + '\n')
    file.write(str(x_si_f) + ',' + str(y + y_phc_s + 0 * a) + '\n')
    file.write(str(x_si_f + 5 * math.sqrt(3) * a / 12) + ',' + str(y + y_phc_s + 0 * a) + '\n')
    file.write('' + '\n')
    file.write('\n')
# make the contour
if check_grid == 0:
    dummy = dummy + 1
else:
    file.write('rectangle' + '\n')
    file.write(str(x + 0.5 * x_phc - S * a / math.sqrt(3) / 4) + ',' + str(y + y_phc_s) + '\n')
    file.write(str(x - S * a / math.sqrt(3) / 2) + ',' + str(y) + '\n')
    file.write('' + '\n')
    file.write(str(x + 1 * x_phc) + ',' + str(y + y_phc_s) + '\n')
    file.write(str(x + 0.5 * x_phc - S * a / math.sqrt(3) / 4) + ',' + str(y) + '\n')

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

file.write('-layer' + '\n')
file.write('set' + '\n')
file.write('5' + '\n')
file.write('' + '\n')
file.write('rectangle' + '\n')
file.write(str(x + 0.5 * x_phc - S * a / math.sqrt(3) / 4 + incident_shift() * a * math.sqrt(3)
               - 1000 - (Si_width / 2)) + ',' + str(y - incident_m_s) + '\n')
file.write(str(x + math.sqrt(3) * a / 2) + ',' + str(y - incident_m_s - 2000) + '\n')
file.write('' + '\n')
file.write(str(x + 0.5 * x_phc - S * a / math.sqrt(3) / 4 + incident_shift() * a * math.sqrt(3)
               + 1000 + (Si_width / 2)) + ',' + str(y - incident_m_s) + '\n')
file.write(str(x + x_phc - math.sqrt(3) * a / 2) + ',' + str(y - incident_m_s - 2000) + '\n')
file.write('' + '\n')
file.write(str(x + 0.5 * x_phc - S * a / math.sqrt(3) / 4 + incident_shift() * a * math.sqrt(3)
               - 1000 - (Si_width / 2)) + ',' + str(y + y_phc_s + incident_m_s) + '\n')
file.write(str(x + math.sqrt(3) * a / 2) + ',' + str(y + y_phc_s + incident_m_s + 2000) + '\n')
file.write('' + '\n')
file.write(str(x + 0.5 * x_phc - S * a / math.sqrt(3) / 4 + incident_shift() * a * math.sqrt(3)
               + 1000 + (Si_width / 2)) + ',' + str(y + y_phc_s + incident_m_s) + '\n')
file.write(str(x + x_phc - math.sqrt(3) * a / 2) + ',' + str(y + y_phc_s + incident_m_s + 2000) + '\n')
file.write('-layer' + '\n')
file.write('set' + '\n')
file.write('0' + '\n')
file.write('' + '\n')

file.write('erase' + '\n')
file.write('crossing' + '\n')
file.write(str(-10000+1000)+','+str(0+1000) + '\n')
file.write(str(-10000-1000)+','+str(0-1000) + '\n')
file.write('' + '\n')






















# make the 2nd W1WG for reference
file.write('zoom' + '\n')
file.write('W' + '\n')
file.write(str(x2-30000) + ',' + str(y-100000) + '\n')
file.write(str(x2+30000) + ',' + str(y+100000) + '\n')

file.write('erase' + '\n')
file.write('crossing' + '\n')
file.write(str(x2-1000) + ',' + str(y-100) + '\n')
file.write(str(x2+1000) + ',' + str(y+50000+1000) + '\n')
file.write('' + '\n')



# insert new Si-wires for reference WG
Si_width = 500
a = 410
incident_m_s = 0.5 * a

R_c = 104
S = 3
hole_type = 'C'
wg_type = '1_1'
valley = 0

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
x = x2 - 0.5 * x_phc + S * a / math.sqrt(3) / 4
# symbol lines/holes
file.write('zoom' + '\n')
file.write('W' + '\n')
file.write(str(x - 10000) + ',' + str(y - 10000) + '\n')
file.write(str(x + x_phc + 10000) + ',' + str(y + y_phc_s + 10000) + '\n')
sp1 = str(x + 100) + ',' + str(y - 16 * a)  # 穴を配置する位置のx軸方向に+100nmずらした部分
sm1 = str(x - 100) + ',' + str(y - 16 * a)  # 穴を配置する位置のx軸方向に-100nmずらした部分

file.write('POLYGON' + '\n')
file.write('8' + '\n')
file.write(str(x) + ',' + str(y - 16 * a) + '\n')
file.write('I' + '\n')
file.write(str(R_c) + '\n')  # 半径rを指定
# start making bulk lattice with rectangular arrays
file.write('_Array' + '\n')
file.write('box' + '\n')
file.write(str(x + 1000) + ',' + str(y + 1000 - 16 * a) + '\n')
file.write(str(x - 1000) + ',' + str(y - 1000 - 16 * a) + '\n')
file.write('' + '\n')
file.write('Rectangular' + '\n')
file.write(str(Ny_s + 32) + '\n')
file.write(str(Nx) + '\n')
file.write(str(a) + '\n')
file.write(str(math.sqrt(3) * a) + '\n')
file.write('copy' + '\n')
file.write('box' + '\n')
file.write(str(x + Nx * math.sqrt(3) * a + 20) + ',' + str(y + Ny_s * a + 20 + 16 * a) + '\n')
file.write(str(x - 1.01 * math.sqrt(3) * a) + ',' + str(y - 20 - 16 * a) + '\n')
file.write('' + '\n')
file.write('0,0' + '\n')
file.write(str(math.sqrt(3) * a / 2) + ',' + str(a / 2) + '\n')
file.write('erase' + '\n')
file.write('crossing' + '\n')
file.write(str(x + 0.5 * x_phc - a * math.sqrt(3) / 4) + ',' + str(y + y_phc_s + 16 * a) + '\n')
file.write(str(x) + ',' + str(y - 16 * a) + '\n')
file.write('' + '\n')
# start making the waveguide

"""file.write('rectangle' + '\n')
file.write(str(x + 0.5 * x_phc) + ',' + str(y + y_phc_s+10*a) + '\n')
file.write(str(x) + ',' + str(y-10*a) + '\n')"""

# make domain 1 bulk lattice in Y- area
file.write('zoom' + '\n')
file.write('W' + '\n')
file.write(str(x - 10000) + ',' + str(-y + 10000) + '\n')
file.write(str(x + x_phc + 10000) + ',' + str(-y - y_phc_s - 10000) + '\n')

file.write('POLYGON' + '\n')
file.write('8' + '\n')
file.write(str(x) + ',' + str(-y + 16 * a) + '\n')
file.write('I' + '\n')
file.write(str(R_c) + '\n')  # 半径rを指定

file.write('_Array' + '\n')
file.write('box' + '\n')
file.write(str(x + 1000) + ',' + str(-(y + 1000 - 16 * a)) + '\n')
file.write(str(x - 1000) + ',' + str(-(y - 1000 - 16 * a)) + '\n')
file.write('' + '\n')
file.write('Rectangular' + '\n')
file.write(str(Ny_s + 32) + '\n')
file.write(str(Nx) + '\n')
file.write(str(-a) + '\n')
file.write(str(math.sqrt(3) * a) + '\n')
file.write('copy' + '\n')
file.write('box' + '\n')
file.write(str(x + Nx * math.sqrt(3) * a + 20) + ',' + str(-(y + Ny_s * a + 20 + 16 * a)) + '\n')
file.write(str(x - 1.01 * math.sqrt(3) * a) + ',' + str(-(y - 20 - 16 * a)) + '\n')
file.write('' + '\n')
file.write('0,0' + '\n')
file.write(str(math.sqrt(3) * a / 2) + ',' + str(-a / 2) + '\n')

"""file.write('rectangle' + '\n')
file.write(str(x + 1 * x_phc) + ',' + str(-y - y_phc_s - 16 * a) + '\n')
file.write(str(x + 0.5 * x_phc + a * math.sqrt(3) / 4) + ',' + str(
    -y + 16 * a) + '\n')"""

file.write('erase' + '\n')
file.write('crossing' + '\n')
file.write(str(x + 1 * x_phc) + ',' + str(-y - y_phc_s - 16 * a) + '\n')
file.write(str(x + 0.5 * x_phc + a * math.sqrt(3) / 4) + ',' + str(
    -y + 16 * a) + '\n')
file.write('' + '\n')
file.write('mirror' + '\n')
file.write('crossing' + '\n')
file.write(str(x + 0.5 * x_phc - a * math.sqrt(3) / 4) + ',' + str(-(y + y_phc_s + 16 * a)) + '\n')
file.write(str(x) + ',' + str(-y + 16 * a) + '\n')
file.write('' + '\n')
file.write('0,0' + '\n')
file.write('1,0' + '\n')
file.write('yes' + '\n')

file.write('zoom' + '\n')
file.write('W' + '\n')
file.write(str(x - 10000) + ',' + str(y - 10000) + '\n')
file.write(str(x + x_phc + 10000) + ',' + str(y + y_phc_s + 10000) + '\n')
# separate domain layer
if valley == 1:
    file.write('change' + '\n')
    file.write('crossing' + '\n')
    file.write(str(x + 0.5 * x_phc - a * math.sqrt(3) / 4) + ',' + str(y + y_phc_s + 16 * a) + '\n')
    file.write(str(x) + ',' + str(y - 16 * a) + '\n')
    file.write('' + '\n')
    file.write('properties' + '\n')
    file.write('layer' + '\n')
    file.write('1' + '\n')
    file.write('' + '\n')
# domain shift
file.write('move' + '\n')
file.write('crossing' + '\n')
file.write(str(x + 0.5 * x_phc - a * math.sqrt(3) / 4) + ',' + str(y + y_phc_s + 16 * a) + '\n')
file.write(str(x) + ',' + str(y - 16 * a) + '\n')
file.write('' + '\n')
file.write('0,0' + '\n')
file.write(str(S * a / math.sqrt(3)) + '<' + '120' + '\n')
# delete redundant part of the PhC lattice
file.write('erase' + '\n')
file.write('window' + '\n')
file.write(str(x + x_phc + 5 * math.sqrt(3) * a) + ',' + str(y + y_phc_s + 20.5 * a) + '\n')
file.write(str(x - 5 * math.sqrt(3) * a) + ',' + str(y + y_phc_s + 0.1 * a) + '\n')
file.write('remove' + '\n')
file.write('fence' + '\n')
file.write(str(x - 5 * math.sqrt(3) * a) + ',' + str(y + y_phc_s + 0 * a) + '\n')
file.write(str(x + x_phc + 5 * math.sqrt(3) * a) + ',' + str(y + y_phc_s + 0 * a) + '\n')
file.write('' + '\n')
file.write('' + '\n')
file.write('erase' + '\n')
file.write('window' + '\n')
file.write(str(x + x_phc + x_phc + 5 * math.sqrt(3) * a) + ',' + str(y - 0.1 * a) + '\n')
file.write(str(x - x_phc + 5 * math.sqrt(3) * a) + ',' + str(y - 20.5 * a) + '\n')
file.write('remove' + '\n')
file.write('fence' + '\n')
file.write(str(x - 5 * math.sqrt(3) * a) + ',' + str(y) + '\n')
file.write(str(x + x_phc + 5 * math.sqrt(3) * a) + ',' + str(y) + '\n')
file.write('' + '\n')
file.write('\n')
# delete some in/out region holes according to WG mode type
x_si_f = x + 0.5 * x_phc - S * a / math.sqrt(3) / 4 + incident_shift() * a * math.sqrt(3)  # final Si wire position
if wg_type == "1_6":
    file.write('erase' + '\n')
    file.write('fence' + '\n')
    file.write(str(x_si_f) + ',' + str(y + 0 * a) + '\n')
    file.write(str(x_si_f - math.sqrt(3) * a / 4) + ',' + str(y + 0 * a) + '\n')
    file.write('' + '\n')
    file.write('\n')
    file.write('erase' + '\n')
    file.write('fence' + '\n')
    file.write(str(x_si_f) + ',' + str(y + 1 * a) + '\n')
    file.write(str(x_si_f - math.sqrt(3) * a / 4) + ',' + str(y + 1 * a) + '\n')
    file.write('' + '\n')
    file.write('\n')

    file.write('erase' + '\n')
    file.write('fence' + '\n')
    file.write(str(x_si_f) + ',' + str(y + y_phc_s - 0 * a) + '\n')
    file.write(str(x_si_f - math.sqrt(3) * a / 4) + ',' + str(y + y_phc_s - 0 * a) + '\n')
    file.write('' + '\n')
    file.write('\n')
    file.write('erase' + '\n')
    file.write('fence' + '\n')
    file.write(str(x_si_f) + ',' + str(y + y_phc_s - 1 * a) + '\n')
    file.write(str(x_si_f - math.sqrt(3) * a / 4) + ',' + str(y + y_phc_s - 1 * a) + '\n')
    file.write('' + '\n')
    file.write('\n')
if wg_type == "1_3":
    file.write('erase' + '\n')
    file.write('fence' + '\n')
    file.write(str(x_si_f - math.sqrt(3) * a / 12) + ',' + str(y + y_phc_s - 4 * a) + '\n')
    file.write(str(x_si_f - math.sqrt(3) * a / 12) + ',' + str(y + y_phc_s - 3 * a) + '\n')
    file.write(str(x_si_f - math.sqrt(3) * a / 12) + ',' + str(y + y_phc_s - 2 * a) + '\n')
    file.write(str(x_si_f - math.sqrt(3) * a / 12) + ',' + str(y + y_phc_s - a) + '\n')
    file.write(str(x_si_f - math.sqrt(3) * a / 12) + ',' + str(y + y_phc_s) + '\n')
    file.write(str(x_si_f - 5 * math.sqrt(3) * a / 12) + ',' + str(y + y_phc_s) + '\n')
    file.write('' + '\n')
    file.write('\n')

    file.write('erase' + '\n')
    file.write('fence' + '\n')
    file.write(str(x_si_f - math.sqrt(3) * a / 12) + ',' + str(y + 4 * a) + '\n')
    file.write(str(x_si_f - math.sqrt(3) * a / 12) + ',' + str(y + 3 * a) + '\n')
    file.write(str(x_si_f - math.sqrt(3) * a / 12) + ',' + str(y + 2 * a) + '\n')
    file.write(str(x_si_f - math.sqrt(3) * a / 12) + ',' + str(y + a) + '\n')
    file.write(str(x_si_f - math.sqrt(3) * a / 12) + ',' + str(y) + '\n')
    file.write(str(x_si_f - 5 * math.sqrt(3) * a / 12) + ',' + str(y) + '\n')
    file.write('' + '\n')
    file.write('\n')

if wg_type == "2_3":
    file.write('erase' + '\n')
    file.write('fence' + '\n')
    file.write(str(x_si_f - math.sqrt(3) * a / 3) + ',' + str(y) + '\n')
    file.write(str(x_si_f + math.sqrt(3) * a / 3) + ',' + str(y) + '\n')
    file.write('' + '\n')
    file.write('\n')
    file.write('erase' + '\n')
    file.write('fence' + '\n')
    file.write(str(x_si_f - math.sqrt(3) * a / 3) + ',' + str(y + y_phc_s) + '\n')
    file.write(str(x_si_f + math.sqrt(3) * a / 3) + ',' + str(y + y_phc_s) + '\n')
    file.write('' + '\n')
    file.write('\n')
if wg_type == "5_6":
    file.write('erase' + '\n')
    file.write('fence' + '\n')
    file.write(str(x_si_f) + ',' + str(y + 0 * a) + '\n')
    file.write(str(x_si_f + 5 * math.sqrt(3) * a / 12) + ',' + str(y + 0 * a) + '\n')
    file.write('' + '\n')
    file.write('\n')
    file.write('erase' + '\n')
    file.write('fence' + '\n')
    file.write(str(x_si_f) + ',' + str(y + y_phc_s + 0 * a) + '\n')
    file.write(str(x_si_f + 5 * math.sqrt(3) * a / 12) + ',' + str(y + y_phc_s + 0 * a) + '\n')
    file.write('' + '\n')
    file.write('\n')
# make the contour
if check_grid == 0:
    dummy = dummy + 1
else:
    file.write('rectangle' + '\n')
    file.write(str(x + 0.5 * x_phc - S * a / math.sqrt(3) / 4) + ',' + str(y + y_phc_s) + '\n')
    file.write(str(x - S * a / math.sqrt(3) / 2) + ',' + str(y) + '\n')
    file.write('' + '\n')
    file.write(str(x + 1 * x_phc) + ',' + str(y + y_phc_s) + '\n')
    file.write(str(x + 0.5 * x_phc - S * a / math.sqrt(3) / 4) + ',' + str(y) + '\n')

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

file.write('-layer' + '\n')
file.write('set' + '\n')
file.write('5' + '\n')
file.write('' + '\n')
file.write('rectangle' + '\n')
file.write(str(x + 0.5 * x_phc - S * a / math.sqrt(3) / 4 + incident_shift() * a * math.sqrt(3)
               - 1000 - (Si_width / 2)) + ',' + str(y - incident_m_s) + '\n')
file.write(str(x + math.sqrt(3) * a / 2) + ',' + str(y - incident_m_s - 2000) + '\n')
file.write('' + '\n')
file.write(str(x + 0.5 * x_phc - S * a / math.sqrt(3) / 4 + incident_shift() * a * math.sqrt(3)
               + 1000 + (Si_width / 2)) + ',' + str(y - incident_m_s) + '\n')
file.write(str(x + x_phc - math.sqrt(3) * a / 2) + ',' + str(y - incident_m_s - 2000) + '\n')
file.write('' + '\n')
file.write(str(x + 0.5 * x_phc - S * a / math.sqrt(3) / 4 + incident_shift() * a * math.sqrt(3)
               - 1000 - (Si_width / 2)) + ',' + str(y + y_phc_s + incident_m_s) + '\n')
file.write(str(x + math.sqrt(3) * a / 2) + ',' + str(y + y_phc_s + incident_m_s + 2000) + '\n')
file.write('' + '\n')
file.write(str(x + 0.5 * x_phc - S * a / math.sqrt(3) / 4 + incident_shift() * a * math.sqrt(3)
               + 1000 + (Si_width / 2)) + ',' + str(y + y_phc_s + incident_m_s) + '\n')
file.write(str(x + x_phc - math.sqrt(3) * a / 2) + ',' + str(y + y_phc_s + incident_m_s + 2000) + '\n')
file.write('-layer' + '\n')
file.write('set' + '\n')
file.write('0' + '\n')
file.write('' + '\n')

file.write('erase' + '\n')
file.write('crossing' + '\n')
file.write(str(-10000+1000)+','+str(0+1000) + '\n')
file.write(str(-10000-1000)+','+str(0-1000) + '\n')
file.write('' + '\n')



# make the pure Si WG
file.write('zoom' + '\n')
file.write('W' + '\n')
file.write(str(x3-30000) + ',' + str(y-100000) + '\n')
file.write(str(x3+30000) + ',' + str(y+100000) + '\n')

file.write('erase' + '\n')
file.write('crossing' + '\n')
file.write(str(x3-1000) + ',' + str(y-100) + '\n')
file.write(str(x3+1000) + ',' + str(y+50000+1000) + '\n')
file.write('' + '\n')





W_futoi_Si = 8000
L_futoi_Si = 5000000
W_air = 2000
file.write('-layer' + '\n')
file.write('set' + '\n')
file.write('4' + '\n')
file.write('' + '\n')

file.write('rectangle' + '\n')
file.write(str(x3 + W_futoi_Si / 2) + ',' + str(y + L_futoi_Si / 2) + '\n')
file.write(str(x3 + W_futoi_Si / 2 + W_air) + ',' + str(y - L_futoi_Si / 2) + '\n')
file.write('' + '\n')
file.write(str(x3 - W_futoi_Si / 2) + ',' + str(y - L_futoi_Si / 2) + '\n')
file.write(str(x3 - W_futoi_Si / 2 - W_air) + ',' + str(y + L_futoi_Si / 2) + '\n')




print('-----FINISH !-----')
file.close()

