import matplotlib.pyplot as plt
import numpy as np
import math

import sys
plt.rcParams["font.sans-serif"]=["SimHei"]
plt.rcParams["axes.unicode_minus"]=False


num = 10
node = np.zeros((num, num), dtype=int)

np.fill_diagonal(node, 0)

for i in range(num):
    for j in range(i + 1, num):
        node[i, j] = np.random.randint(50, 100)

node = node + node.T - np.diag(node.diagonal())
encourage = [0]*num
AllC = [100] * num
def findID(id):
    AllC[id] = AllC[id] - 5
    C = [0]*(num-1)
    jj = 0
    for i in range(len(AllC)):
        if i!=id:
            C[jj] = 1/AllC[i]
            jj = jj + 1
    # print(C)
    RSUID = [0]*(num-1)
    findRSUID = [0]*(int(num/2))

    distance = [0]*(num-1)
    jj = 0
    for i in range(len(node[id])):
        if i!=id:
            distance[jj] = node[id][i]
            RSUID[jj] = i
            jj = jj+1
    d = np.sum(node, axis=1)
    E = [distance,C]

    f = [[0] * len(distance),[0]* len(distance)]
    for j in range(2):
        for t in range(len(distance)):
            f[j][t] = E[j][t] / np.sum(E[j])
    k = 1 / (math.log(len(distance)))
    H = [0] * 2
    r = [0.0] * 2
    for i in range(2):
        sum = 0
        for j in range(len(distance)):
            sum = sum + f[i][j] * math.log(f[i][j])
        H[i] = -1 * k * sum
    for i in range(len(r)):
        r[i] = (1 - H[i]) / (2 - np.sum(H))
    # print(r)
    w = [0.0] * len(distance)
    for i in range(len(w)):
        if max(distance) == min(distance):
            distancei = 0
        else:
            distancei = (distance[i] - min(distance)) / (max(distance) - min(distance))
        if max(C) == min(C):
            ci = 0
        else:
            ci = (C[i] - min(C)) / (max(C) - min(C))

        w[i] = r[0]*distancei+r[1] * ci
    w2 = sorted(w)
    jj = len(w2)-1
    while jj>=0:
        if w2[jj] == 0:
            w2[jj] = w2[jj+1]/2
            for i in range(len(w)):
                if w[i] == 0:
                    w[i] = w2[jj+1]/2
        jj = jj-1
    jj = 0
    for i in range(len(w2)):
        for j in range(len(w)):
            if (w[j] == w2[i]) & (jj<len(findRSUID)):
                findRSUID[jj] = RSUID[j]
                encourage[RSUID[j]] = encourage[RSUID[j]]+w[j]
                jj = jj + 1
    return findRSUID

def findID2(id):
    C = [0]*(num-1)
    jj = 0
    for i in range(len(AllC)):
        if i!=id:
            C[jj] = 1/AllC[i]
            jj = jj + 1
    RSUID = [0]*(num-1)
    findRSUID = [0]*(int(num/2))

    distance = [0]*(num-1)
    jj = 0
    for i in range(len(node[id])):
        if i!=id:
            distance[jj] = node[id][i]
            RSUID[jj] = i
            jj = jj+1
    d = np.sum(node, axis=1)
    E = [distance,C]

    f = [[0] * len(distance),[0]* len(distance)]
    for j in range(2):
        for t in range(len(distance)):
            f[j][t] = E[j][t] / np.sum(E[j])
    k = 1 / (math.log(len(distance)))
    H = [0] * 2
    r = [0.0] * 2
    for i in range(2):
        sum = 0
        for j in range(len(distance)):
            sum = sum + f[i][j] * math.log(f[i][j])
        H[i] = -1 * k * sum
    for i in range(len(r)):
        r[i] = (1 - H[i]) / (2 - np.sum(H))
    w = [0.0] * len(distance)
    for i in range(len(w)):
        if max(distance) == min(distance):
            distancei = 0
        else:
            distancei = (distance[i] - min(distance)) / (max(distance) - min(distance))
        if max(C) == min(C):
            ci = 0
        else:
            ci = (C[i] - min(C)) / (max(C) - min(C))

        w[i] = r[0]*distancei+r[1] * ci
    w2 = sorted(w)
    jj = len(w2)-1
    while jj>=0:
        if w2[jj] == 0:
            w2[jj] = w2[jj+1]/2
            for i in range(len(w)):
                if w[i] == 0:
                    w[i] = w2[jj+1]/2
        jj = jj-1
    jj = 0
    for i in range(len(w2)):
        for j in range(len(w)):
            if (w[j] == w2[i]) & (jj<len(findRSUID)):
                findRSUID[jj] = RSUID[j]
                encourage[RSUID[j]] = encourage[RSUID[j]]+w[j]
                jj = jj + 1
    return findRSUID

def changeIDstorage(id,rr,changeid):
    storageCopy = AllC.copy()
    storageCopy[changeid] = storageCopy[changeid]+rr*100
    C = [0]*(num-1)
    jj = 0
    for i in range(len(storageCopy)):
        if i!=id:
            C[jj] = 1/storageCopy[i]
            jj = jj + 1
    RSUID = [0]*(num-1)
    findRSUID = [0]*(int(num/2))

    distance = [0]*(num-1)
    jj = 0
    for i in range(len(node[id])):
        if i!=id:
            distance[jj] = node[id][i]
            RSUID[jj] = i
            jj = jj+1
    d = np.sum(node, axis=1)
    E = [distance,C]

    f = [[0] * len(distance),[0]* len(distance)]
    for j in range(2):
        for t in range(len(distance)):
            f[j][t] = E[j][t] / np.sum(E[j])
    k = 1 / (math.log(len(distance)))
    H = [0] * 2
    r = [0.0] * 2
    for i in range(2):
        sum = 0
        for j in range(len(distance)):
            sum = sum + f[i][j] * math.log(f[i][j])
        H[i] = -1 * k * sum
    for i in range(len(r)):
        r[i] = (1 - H[i]) / (2 - np.sum(H))
    # print(r)
    w = [0.0] * len(distance)
    for i in range(len(w)):
        if max(distance) == min(distance):
            distancei = 0
        else:
            distancei = (distance[i] - min(distance)) / (max(distance) - min(distance))
        if max(C) == min(C):
            ci = 0
        else:
            ci = (C[i] - min(C)) / (max(C) - min(C))

        w[i] = r[0]*distancei+r[1] * ci
    w2 = sorted(w)
    jj = len(w2)-1
    while jj>=0:
        if w2[jj] == 0:
            w2[jj] = w2[jj+1]/2
            for i in range(len(w)):
                if w[i] == 0:
                    w[i] = w2[jj+1]/2
        jj = jj-1
    jj = 0
    for i in range(len(w2)):
        for j in range(len(w)):
            if (w[j] == w2[i]) & (jj<len(findRSUID)):
                findRSUID[jj] = RSUID[j]
                encourage[RSUID[j]] = encourage[RSUID[j]]+w[j]
                jj = jj + 1
    return findRSUID
def delStorage():
    timesid = [0]*num
    for i in range(len(AllC)):
        findRSUID = findID2(i)
        for j in range(len(findRSUID)):
            timesid[findRSUID[j]] = timesid[findRSUID[j]] + 1
    for x in range(len(timesid)):
        if AllC[x] <100:
            if timesid[x]<=(0.3*num):
                unloadRSUNum[x] = unloadRSUNum[x] + 1
                rr = 0
                times = 0
                while times<=(0.8*num):
                    rr = rr + 0.05
                    times = 0
                    for i in range(len(AllC)):
                        findRSUID = changeIDstorage(i,rr,x)
                        if x in findRSUID:
                            times = times+1
                if (AllC[x] + rr*100)<=100:
                    AllC[x] = AllC[x] + rr*100
                else:
                    AllC[x] = 100

piecenum = [50,75,100,125,150,175,200]
unloadNum = [[0]*num]*len(piecenum)

for a in range(len(piecenum)):
    unloadRSUNum = [0]*num
    for b in range(piecenum[a]):

        id = np.random.randint(num)
        findRSUID = findID(id)
        for i in range(len(findRSUID)):
            AllC[findRSUID[i]] = AllC[findRSUID[i]] - 5
        delStorage()
    unloadNum[a] = unloadRSUNum
    unloadNum = np.array(unloadNum)
print(unloadNum.sum(axis=1))




