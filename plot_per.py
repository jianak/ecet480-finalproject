import pickle
import numpy as np
import matplotlib.pyplot as plt

TOP_DIR1 = "16_qam_with_noise_interleaving/"
TOP_DIR2 = "16qam_with_noise/"

noise = "noise=0.1"
NOISE_DIR1 = TOP_DIR1 + noise + "/"
NOISE_DIR2 = TOP_DIR2 + noise + "/"
with open(TOP_DIR1 + "per_16_qam_with_{}_interleaving.pkl".format(noise), "rb") as fin:
    per_1 = np.array(list(pickle.load(fin).values()))

with open(TOP_DIR2 + "per_16_qam_with_{}_single.pkl".format(noise), "rb") as fin:
    per_2 = np.array(list(pickle.load(fin).values()))

with open(NOISE_DIR1 + "sjrs.pkl", "rb") as fin:
    sjrs_1 = pickle.load(fin)

with open(NOISE_DIR2 + "sjrs.pkl", "rb") as fin:
    sjrs_2 = pickle.load(fin)

plt.plot(list(sjrs_1.values()), per_1 * 100, marker="o", alpha=0.7)
plt.plot(list(sjrs_1.values()), per_2 * 100, marker="o", alpha=0.7)
plt.legend(["Interleaving", "Single"])
plt.xlabel("SJR (dB)")
plt.ylabel("Packet Error Rate (%)")
plt.grid(b=True, which="major", color="#d3d3d3", linestyle="-")
plt.grid(b=True, which="minor", color="#d3d3d3", linestyle="-")
plt.savefig("16q_{}_interleaving_vs_single.png".format(noise), dpi=200)
