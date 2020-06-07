import pickle
import numpy as np
from IPython.core.debugger import set_trace

def rms(x):
    return np.sqrt(np.mean(np.abs(x)**2))

sjrs = {}
for i in range(1,14):
    jx = np.fromfile("jx_sig_iq_{}.dat".format(i), dtype=np.complex64)
    rx = np.fromfile("rx_sig_iq_{}.dat".format(i), dtype=np.complex64)

    jx_pwr = rms(jx)
    rx_pwr = rms(rx)

    sjrs[i] = 20 * np.log10(rx_pwr / jx_pwr)

print(sjrs)
with open("sjrs.pkl", "wb") as fout:
    pickle.dump(sjrs, fout)
