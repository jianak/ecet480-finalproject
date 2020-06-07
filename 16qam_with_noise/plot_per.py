import pickle
import numpy as np
import matplotlib.pyplot as plt

noise = "noise=0.1"
DIR = noise + "/"
with open("per_16_qam_with_{}_single.pkl".format(noise), "rb") as fin:
    per_1 = np.array(list(pickle.load(fin).values()))

with open(DIR + "sjrs.pkl", "rb") as fin:
    sjrs = pickle.load(fin)
#with open("per_16_qam_with_noise=0.2_single.pkl", "rb") as fin:
#    per_2 = pickle.load(fin)

#with open("per_16_qam_with_noise=0.13_single.pkl", "rb") as fin:
#    per_3 = pickle.load(fin)

plt.plot(list(sjrs.values()), per_1 * 100, marker="o")
plt.xlabel("SJR (dB)")
plt.ylabel("Packet Error Rate (%)")
plt.grid(b=True, which="major", color="#d3d3d3", linestyle="-")
plt.grid(b=True, which="minor", color="#d3d3d3", linestyle="-")
plt.savefig("16q_{}.png".format(noise), dpi=200)
