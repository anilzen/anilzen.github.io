import numpy as np

def penrose_coords(r, t, K=1):
#    height = 0
    # height = np.sqrt(1./K**2+r**2)-1./K
    height = np.sqrt(1./K**2+r**2)
    tau = t+height
    R = 1./np.pi*(np.arctan(tau+r)-np.arctan(tau-r))
    T = 1./np.pi*(np.arctan(tau+r)+np.arctan(tau-r))
    return R, T

def save_to_file(penrose_c, fn):
    R, T = penrose_c
    np.savetxt(fn, np.stack((R, T)).T,
                delimiter=',', fmt='%f', header="R,T", comments="")
    print('{'+fn+'},')


samp = lambda i: np.tan(0.5 * np.pi * i)
r_values = samp(np.linspace(0.00, 1, 100))

save_to_file(penrose_coords(r_values[:-1], t=0, K=0.5), 'data/Ksma.csv')
save_to_file(penrose_coords(r_values[:-1], t=0, K=2), 'data/Kbig.csv')

# t_values = np.linspace(-3., 3, 7)

# for i, t_val in enumerate(t_values):
#     R, T = penrose_coords(r_values[:-1], t_val)
#     fn = 'data/mink'+str(i)+'.csv'
#     np.savetxt(fn, np.stack((R, T)).T,
#                delimiter=',', fmt='%f', header="R,T", comments="")
#     print('{'+fn+'},')