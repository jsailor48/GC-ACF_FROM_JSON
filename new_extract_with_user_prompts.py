import numpy as np
from numpy import gradient
import matplotlib.pyplot as plt
import json
File_path = input("Enter File Path, and or name if in the same Directory")
with open(File_path , 'r') as file:
  data=json.load(file)
  gk_integral = data["Conductivity"] ["GK_Integral"]
  time = data ["Conductivity"]["Time"]
  #print (gk_integral)
  #print (time)
  stored_gk_integral_data = np.array(gk_integral)
  stored_time_data = np.array(time)
  # numerical approximation
  Time_step = input("Enter time step between trajectory frames; eg 1000fs (enter numerical values only)")
  dt = int(Time_step)
  auto_derivative = gradient(stored_gk_integral_data, dt)
Graph_Title = input("Enter Graph Title... EG ACF for 0.70 S/m run: ")
Time_units = input("Enter the units of time eg fs,s,ns....")
plt.plot(stored_time_data,auto_derivative, label = Graph_Title )
plt.xlabel('Time ('+Time_units+')')
plt.ylabel('Intensity')
plt.legend()
plt.show()

#print(data)


