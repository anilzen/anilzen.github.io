from scipy.special import lambertw      # For the tortoise coordinate
import numpy as np
import os

# Suppress all warnings
import warnings
warnings.filterwarnings("ignore")

def penrose_coords(r, t):
    condition = r <= 1
    u = np.where(condition, np.sqrt((1-r)/(1+r))*np.exp(t), np.sqrt(-(1-r)/(1+r))*np.exp(-t))
    v = np.where(condition, -np.sqrt((1-r)/(1+r))*np.exp(-t), np.sqrt(-(1-r)/(1+r))*np.exp(t))

    T = 2./np.pi*(np.arctan(v)+np.arctan(u))
    R = 2./np.pi*(np.arctan(v)-np.arctan(u)) + 1

    return R, T

def set_height(surface_type, r):
    condition = r <= 1
    r_tort = np.where(condition, 0.5*(np.log(1+r)-np.log(np.abs(1-r))), 
                      -0.5*(np.log(1+r)-np.log(np.abs(1-r))))
    if surface_type == "standard":
        height = 0
    elif surface_type == "outgoing_null":
        height = -r_tort # Outgoing null surfaces u = t - r
    elif surface_type == "ingoing_null":
        height = r_tort # Ingoing null surfaces v = t + r
    elif surface_type == "future_hyperboloidal":
        # Future hyperboloidal tau = t - \sqrt{L^2+r^2} + L
        # Change value of L_CMC to change K = 3/L_CMC
        L_CMC = 1.0
        height = -(np.sqrt(L_CMC**2 + r_tort**2) - L_CMC)
    elif surface_type == "kerr_schild":
        height = np.where(condition, r - r_tort, -r - r_tort)
    elif surface_type == "misner":
        height = np.where(condition, r - np.sqrt(1+r**2) - r_tort, -(r - np.sqrt(1+r**2)) - r_tort)
    else:
        raise ValueError("Invalid surface_type")
    return height

t = np.tan(np.linspace(-1.1, 1.1, 7, endpoint=True))

nr_points = 100
r_in = 0.5 * (-np.cos((np.arange(nr_points) * np.pi) / (nr_points - 1)) + 1)
nr_points *=3
r_out = 20 * (-np.cos((np.arange(nr_points) * np.pi) / (nr_points - 1)) + 1)+1
r = np.concatenate((r_in, r_out))

height =  set_height("misner", r)

# Create an array to store the data
all_data = np.empty((len(r), 2 * len(t)))
# Iterate over each value of t
for i, t_val in enumerate(t):
    tau = t_val - height # Note the opposite sign due to definition of t vs tau
    R, T = penrose_coords(r, tau)    
    # Store the data in the array
    all_data[:, 2 * i] = R
    all_data[:, 2 * i + 1] = T

# Create data directory if it doesn't exist
if not os.path.exists('data'):
    os.makedirs('data')
# Save the data to a CSV file
column_headers = [f'{axis}_{line}' for line in range(len(t)) for axis in ['R', 'T']]
np.savetxt('data/deSitter.csv', all_data, delimiter=',', header=','.join(column_headers), comments='', fmt='%f')
