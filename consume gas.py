import matplotlib.pyplot as plt
import numpy as np
import math

import sys

node = [[ 0, 75, 81, 85, 63, 79, 94, 81, 76, 78, 79, 73, 90, 62, 95],
 [75,  0, 76, 94, 51, 65, 51, 77, 72, 55, 64, 81, 95, 84, 81],
 [81, 76,  0, 53, 54, 98, 59, 97, 94, 84, 77, 79, 73, 88, 63],
 [85, 94, 53,  0, 53, 83, 88, 82, 64, 80, 85, 69, 73, 81, 56],
 [63, 51, 54, 53,  0, 64, 92, 59, 77, 55, 70, 59, 61, 69, 77],
 [79, 65, 98, 83, 64,  0, 62, 95, 85, 76, 99, 56, 72, 83, 84],
 [94, 51, 59, 88, 92, 62,  0, 61, 76, 87, 63, 72, 91, 53, 63],
 [81, 77, 97, 82, 59, 95, 61,  0, 52, 54, 98, 88, 86, 70, 76],
 [76, 72, 94, 64, 77, 85, 76, 52,  0, 51, 92, 79, 72, 88, 54],
 [78, 55, 84, 80, 55, 76, 87, 54, 51,  0, 76, 62, 76, 88, 97],
 [79, 64, 77, 85, 70, 99, 63, 98, 92, 76,  0, 58, 91, 92, 55],
 [73, 81, 79, 69, 59, 56, 72, 88, 79, 62, 58,  0, 70, 87, 85],
 [90, 95, 73, 73, 61, 72, 91, 86, 72, 76, 91, 70,  0, 89, 67],
 [62, 84, 88, 81, 69, 83, 53, 70, 88, 88, 92, 87, 89,  0, 70],
 [95, 81, 63, 56, 77, 84, 63, 76, 54, 97, 55, 85, 67, 70,  0],]
num = 15
encourage = [150]*num
encourage2 = [150]*num
AllC = [100] * num

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
            if timesid[x]<=0.3*num:
                rr = 0
                times = 0
                while times<=0.8*num:
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


blocknum = [30,60,90,120,150]
for a in range(len(blocknum)):
    encourage = [150] * num
    encourage2 = [150] * num
    AllC = [100] * num
    for b in range(blocknum[a]):

        id = np.random.randint(num)
        findRSUID = findID(id)
        for i in range(len(findRSUID)):
            AllC[findRSUID[i]] = AllC[findRSUID[i]] - 5
        delStorage()

    print(encourage)








