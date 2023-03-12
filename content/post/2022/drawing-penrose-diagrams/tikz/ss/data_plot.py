# M = 1/2, horizon is at r=1
import numpy as np
from scipy.special import lambertw      # For the tortoise coordinate

def kruskal_coords(r, t):
    # https://en.wikipedia.org/wiki/Kruskal%E2%80%93Szekeres_coordinates#Definition
    # With G=1, M=1/2 (dimensionless coordinates)
    # height = -2*np.sqrt(r) + np.log( (np.sqrt(r)+1)/(np.sqrt(r)-1) ) # Gullstrand-Painleve
    # r_tort = r + np.log(r-1); height = np.sqrt(1+r_tort**2) # hyperbolic in tortoise
    height = r + 2*np.log(r) - np.log(r - 1) - 2 # minimal gauge
    # height = 0.
    rho = np.sqrt(r-1)*np.exp(r/2)*np.cosh((t+height)/2)
    tau = np.sqrt(r-1)*np.exp(r/2)*np.sinh((t+height)/2)
    R = 2./np.pi*(np.arctan(tau+rho)-np.arctan(tau-rho))
    T = 2./np.pi*(np.arctan(tau+rho)+np.arctan(tau-rho))
    return R, T

# Array of constant values for t 
t_vals = np.linspace(-3., 3, 7)
# Tortoise coordinate on domain (-\infty, \infty)
r_tort = np.tan(np.pi/2*np.cos(np.pi * np.arange(0, 100+1) / 100))[::-1][2:-1]
# Schwarzschild-Droste radial coordinate r (the inverse of the tortoise coordinate)
r_schw = np.real(lambertw(np.exp(r_tort-1))+1)

for i, t_val in enumerate(t_vals):
    R, T = kruskal_coords(r_schw, t_val)
    fn = 'data/ss'+str(i)+'.csv'
    np.savetxt(fn, np.stack((R, T)).T,
               delimiter=',', fmt='%f', header="R,T", comments="")
    print('{'+fn+'},')



