import pickle

msgs_snt = {}
for i in range(1,14):
    with open("msg_tx_{}.txt".format(i), "r") as fin:
        txt = fin.readlines()

    s = "******* MESSAGE DEBUG PRINT ********\n"

    cnt = 0
    for l in txt:
        if l == s: cnt += 1

    msgs_snt[i] = cnt

print(msgs_snt)
with open("msgs_snt.pkl", "wb") as fout:
    pickle.dump(msgs_snt, fout)
