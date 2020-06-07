import os
import dpkt
import pickle
from IPython.core.debugger import set_trace

subdirs = [f.path + "/" for f in os.scandir(os.getcwd()) if f.is_dir()]
for sd in subdirs:
    # parse pcap file and count total number of packets received
    packets_rx = {i:0 for i in range(1,14)}
    for i in range(1,14):
        pcap = sd + "wifi_rx_{}.pcap".format(i)
        packets_rx[i] = len([_ for _ in dpkt.pcap.Reader(open(pcap, "rb"))])

    # get total number of packets sent
    with open(sd + "msgs_snt.pkl", "rb") as fin:
        packets_tx = pickle.load(fin)

    # calculate packet error rate (PER) for each trial
    per = {i:0 for i in range(1,14)}
    for i in range(1,14):
        per[i] = 1 - (packets_rx[i] / packets_tx[i])

    nf = sd[sd[:-1].rfind("/"):][1:-1]
    with open("per_16_qam_with_{}_single.pkl".format(nf), "wb") as fout:
        pickle.dump(per, fout)
