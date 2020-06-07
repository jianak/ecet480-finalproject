#!/bin/bash

python wifi_tx.py 1.75 jx_sig_iq_1.dat rx_sig_iq_1.dat wifi_rx_1.pcap &> msg_tx_1.txt
python wifi_tx.py 1.65 jx_sig_iq_2.dat rx_sig_iq_2.dat wifi_rx_2.pcap &> msg_tx_2.txt
python wifi_tx.py 1.45 jx_sig_iq_3.dat rx_sig_iq_3.dat wifi_rx_3.pcap &> msg_tx_3.txt
python wifi_tx.py 1.15 jx_sig_iq_4.dat rx_sig_iq_4.dat wifi_rx_4.pcap &> msg_tx_4.txt
python wifi_tx.py 0.75 jx_sig_iq_5.dat rx_sig_iq_5.dat wifi_rx_5.pcap &> msg_tx_5.txt
python wifi_tx.py 0.25 jx_sig_iq_6.dat rx_sig_iq_6.dat wifi_rx_6.pcap &> msg_tx_6.txt
python wifi_tx.py 0.05 jx_sig_iq_7.dat rx_sig_iq_7.dat wifi_rx_7.pcap &> msg_tx_7.txt
python wifi_tx.py 0.025 jx_sig_iq_8.dat rx_sig_iq_8.dat wifi_rx_8.pcap &> msg_tx_8.txt
python wifi_tx.py 0.01 jx_sig_iq_9.dat rx_sig_iq_9.dat wifi_rx_9.pcap &> msg_tx_9.txt
python wifi_tx.py 0.005 jx_sig_iq_10.dat rx_sig_iq_10.dat wifi_rx_10.pcap &> msg_tx_10.txt
python wifi_tx.py 0.0025 jx_sig_iq_11.dat rx_sig_iq_11.dat wifi_rx_11.pcap &> msg_tx_11.txt
python wifi_tx.py 0.001 jx_sig_iq_12.dat rx_sig_iq_12.dat wifi_rx_12.pcap &> msg_tx_12.txt
python wifi_tx.py 0.0005 jx_sig_iq_13.dat rx_sig_iq_13.dat wifi_rx_13.pcap &> msg_tx_13.txt
