import numpy as np
t = np.linspace(-np.pi/2., np.pi/2, 8, endpoint=False)[1:]
r = np.linspace(0, np.pi/2, 30)

def penrose_coords(r, t):
    R = 1./np.pi*(np.arctan(t+r)-np.arctan(t-r))
    T = 1./np.pi*(np.arctan(t+r)+np.arctan(t-r))
    return R, T

for i, t_val in enumerate(t):
    R, T = penrose_coords(np.tan(r), np.tan(t_val))
    np.savetxt('data/arctan_data'+str(i)+'.csv', np.stack((R, T)).T,
               delimiter=',', fmt='%f', header="R,T", comments="")
