import netCDF4
import numpy as np
from datetime import datetime


time= datetime(2012,3,5)
time= datetime(2014,8,12)
lat,lon= 39 , -70
depth = 20

temp1 = get_espresso_temp1(time,lat,lon,depth)
temp = get_esptesso_temp(time,lat,lon,depth)
print(temp1)
print(temp2)
