import os
import dpkt
import pickle
from IPython.core.debugger import set_trace

# parse pcap file and count total number of packets received
packets_rx = {i:0 for i in range(1,14)}
for i in range(1,14):
    pcap = "wifi_rx_{}.pcap".format(i)
    packets_rx[i] = len([_ for _ in dpkt.pcap.Reader(open(pcap, "rb"))])

# get total number of packets sent
with open("msgs_snt.pkl", "rb") as fin:
    packets_tx = pickle.load(fin)

# calculate packet error rate (PER) for each trial
per = {i:0 for i in range(1,14)}
for i in range(1,14):
    per[i] = 1 - (packets_rx[i] / packets_tx[i])

with open("per_16_qam_single_no_noise.pkl", "wb") as fout:
    pickle.dump(per, fout)
