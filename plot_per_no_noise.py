import pickle
import numpy as np
import matplotlib.pyplot as plt
from IPython.core.debugger import set_trace

TOP_DIR1 = "16qam/"
TOP_DIR2 = "16qam_with_noise/"

noise = "noise=0.1"
NOISE_DIR2 = TOP_DIR2 + noise + "/"
with open(TOP_DIR1 + "per_16_qam_single_no_noise.pkl", "rb") as fin:
    per_1 = np.array(list(pickle.load(fin).values()))

#with open(TOP_DIR2 + "per_16_qam_with_{}_single.pkl".format(noise), "rb") as fin:
#    per_2 = np.array(list(pickle.load(fin).values()))

with open(TOP_DIR1 + "sjrs.pkl", "rb") as fin:
    sjrs_1 = pickle.load(fin)

#with open(NOISE_DIR2 + "sjrs.pkl", "rb") as fin:
#    sjrs_2 = pickle.load(fin)

plt.plot(list(sjrs_1.values()), per_1 * 100, marker="o")
plt.xlabel("SJR (dB)")
plt.ylabel("Packet Error Rate (%)")
plt.grid(b=True, which="major", color="#d3d3d3", linestyle="-")
plt.grid(b=True, which="minor", color="#d3d3d3", linestyle="-")
plt.savefig("16q_single_no_noise.png".format(noise), dpi=200)
