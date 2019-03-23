import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Qt4Agg')
import matplotlib.pyplot as plt


data1 = pd.read_csv('/Users/fateh/Documents/20190318/20190318-215906_radar_data_.csv',) 
data1.dtypes
rd1_data = data1.iloc[:,0:-1]

a = np.asarray(rd1_data)
print(np.shape(a))
arr = []
#print(type(a),len(a),len(a[0]))
i = 0
for v in a:
    arr.append([])
    for x in v:
        arr[i].append(abs(complex(x)))
    i+=1
print(arr)
df=pd.DataFrame(arr)
print(df)

radarResolution = 0.0522
radarDataTimes = data1.iloc[:,0]
print(radarDataTimes)

# plot raw data
fs = np.floor((len(radarDataTimes)-1)/(radarDataTimes.iloc[-1]- radarDataTimes[0]))
print(fs)
ts=1/fs
print(ts)


t = len((df.iloc[:,0])-1)
print(np.shape(t))
t1=np.arange(0,t)/fs
print(np.shape(t1))
print(t1)

dist_rd1 = len((df.iloc[0,:])-1)
print(np.shape(dist_rd1))
dist_rd2=np.arange(0,dist_rd1)*radarResolution
print(np.shape(dist_rd2))
print(dist_rd2)

plt.contourf(dist_rd2,t1,df);

#matplotlib.pyplot.pcolormesh(dist_rd2,t1,df);
plt.title('Radar 1 raw data plot')
plt.savefig("/Users/fateh/Documents/my_file_stack15.png")
plt.ylabel('Time (s)')
plt.xlabel('Distance (m)')
