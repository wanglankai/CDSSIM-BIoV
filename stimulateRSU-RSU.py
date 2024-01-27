import matplotlib.pyplot as plt
import numpy as np
import math
from mpl_toolkits.mplot3d import Axes3D
import sys

plt.rcParams["font.sans-serif"]=["SimHei"]
plt.rcParams["axes.unicode_minus"]=False
node = [[ 0, 87, 78, 53, 90, 55, 72, 55, 52, 80],
            [87,  0, 72, 64, 53, 95, 88, 68, 93, 59],
            [78, 72,  0, 93, 69, 83, 65, 62, 52, 92],
            [53, 64, 93,  0, 80, 94, 63, 66, 96, 97],
            [90, 53, 69, 80,  0, 82, 99, 97, 79, 95],
            [55, 95, 83, 94, 82,  0, 96, 51, 71, 62],
            [72, 88, 65, 63, 99, 96,  0, 70, 56, 77],
            [55, 68, 62, 66, 97, 51, 70,  0, 93, 53],
            [52, 93, 52, 96, 79, 71, 56, 93,  0, 58],
            [80, 59, 92, 97, 95, 62, 77, 53, 58,  0]]
num = 10
encourage = [1000]*num
encourage2 = [1000]*num
AllC = [100] * num
RRencoutagetime = [[0]*num,[0]*num,[0]*num,[0]*num,[0]*num,[0]*num,[0]*num,[0]*num,[0]*num,[0]*num]

def findID(id):
    AllC[id] = AllC[id] - 5
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
                RRencoutagetime[id][RSUID[j]] = RRencoutagetime[id][RSUID[j]] + 1
                encourage[RSUID[j]] = encourage[RSUID[j]]+w[j]
                encourage[id] = encourage[id] - w[j]
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
            if timesid[x]<=3:
                rr = 0
                times = 0
                while times<=8:
                    rr = rr + 0.05
                    times = 0
                    for i in range(len(AllC)):
                        findRSUID = changeIDstorage(i,rr,x)
                        if x in findRSUID:
                            times = times+1
                if (AllC[x] + rr*100)<=100:
                    AllC[x] = AllC[x] + rr*100
                    encourage[x] = encourage[x]-(encourage[x]-encourage2[x])*rr
                    encourage2[x] = encourage[x]
                else:
                    encourage[x] = encourage[x] - (encourage[x] - encourage2[x]) * (100-AllC[x])/100
                    encourage2[x] = encourage[x]
                    AllC[x] = 100
for a in range(50):
    id = np.random.randint(num)
    findRSUID = findID(id)
    for i in range(len(findRSUID)):
        AllC[findRSUID[i]] = AllC[findRSUID[i]] - 5
    delStorage()
print(RRencoutagetime)






