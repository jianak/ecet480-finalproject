import pickle
import numpy as np
import matplotlib.pyplot as plt

noise = "noise=0.13"
DIR = noise + "/"
with open("per_16_qam_with_{}_interleaving.pkl".format(noise), "rb") as fin:
    per_1 = np.array(list(pickle.load(fin).values()))

with open(DIR + "sjrs.pkl", "rb") as fin:
    sjrs = pickle.load(fin)

plt.plot(list(sjrs.values()), per_1 * 100, marker="o")
plt.xlabel("SJR (dB)")
plt.ylabel("Packet Error Rate (%)")
plt.grid(b=True, which="major", color="#d3d3d3", linestyle="-")
plt.grid(b=True, which="minor", color="#d3d3d3", linestyle="-")
plt.savefig("16q_{}_interleaving.pdf".format(noise), dpi=800)
