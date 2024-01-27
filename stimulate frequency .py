import matplotlib.pyplot as plt
import numpy as np
import math

import sys
plt.rcParams["font.sans-serif"]=["SimHei"]
plt.rcParams["axes.unicode_minus"]=False

node = [[ 0, 62, 92, 79, 63, 99, 76, 94, 92, 60, 74, 86, 88, 53, 92, 68, 59, 66,
  82, 72, 75, 64, 70, 80, 94, 74, 78, 53, 61, 89, 87, 56, 84, 81, 52, 56,
  68, 99, 74, 67],
 [62,  0, 72, 55, 51, 54, 93, 63, 66, 89, 81, 63, 67, 80, 59, 56, 63, 52,
  77, 91, 66, 91, 65, 88, 91, 65, 75, 51, 96, 72, 66, 97, 50, 86, 58, 63,
  55, 94, 98, 82],
 [92, 72,  0, 56, 75, 77, 79, 97, 89, 94, 75, 50, 80, 94, 59, 82, 92, 85,
  86, 63, 65, 79, 89, 69, 71, 78, 95, 89, 69, 67, 58, 99, 58, 80, 68, 98,
  97, 94, 94, 94],
 [79, 55, 56,  0, 56, 65, 70, 91, 52, 66, 56, 84, 78, 56, 72, 94, 93, 66,
  65, 54, 87, 84, 51, 92, 51, 72, 85, 95, 67, 98, 93, 56, 64, 92, 64, 50,
  65, 60, 73, 91],
 [63, 51, 75, 56,  0, 69, 55, 52, 82, 91, 96, 52, 64, 87, 92, 56, 73, 75,
  88, 63, 52, 74, 84, 76, 91, 57, 60, 96, 52, 54, 55, 55, 86, 84, 82, 93,
  82, 72, 67, 76],
 [99, 54, 77, 65, 69,  0, 52, 83, 59, 66, 79, 96, 92, 51, 59, 81, 92, 69,
  88, 96, 71, 63, 83, 75, 98, 97, 60, 75, 57, 99, 96, 61, 94, 66, 97, 64,
  86, 70, 57, 77],
 [76, 93, 79, 70, 55, 52,  0, 92, 67, 86, 63, 92, 78, 67, 56, 92, 66, 85,
  86, 97, 98, 96, 91, 84, 87, 98, 70, 70, 96, 71, 91, 59, 69, 87, 89, 99,
  81, 81, 73, 79],
 [94, 63, 97, 91, 52, 83, 92,  0, 50, 87, 86, 77, 82, 51, 86, 67, 96, 70,
  89, 91, 97, 83, 96, 96, 63, 88, 65, 98, 56, 59, 50, 66, 84, 98, 90, 75,
  81, 87, 98, 68],
 [92, 66, 89, 52, 82, 59, 67, 50,  0, 73, 53, 72, 91, 89, 70, 88, 90, 90,
  65, 94, 76, 75, 78, 71, 52, 82, 74, 87, 70, 67, 51, 69, 95, 97, 86, 99,
  50, 90, 52, 92],
 [60, 89, 94, 66, 91, 66, 86, 87, 73,  0, 73, 72, 96, 89, 56, 75, 88, 99,
  74, 72, 78, 95, 54, 99, 83, 70, 78, 73, 61, 75, 70, 65, 86, 62, 65, 94,
  71, 81, 81, 97],
 [74, 81, 75, 56, 96, 79, 63, 86, 53, 73,  0, 89, 63, 83, 70, 58, 56, 95,
  90, 66, 58, 86, 88, 68, 97, 73, 92, 75, 83, 69, 61, 98, 94, 66, 86, 71,
  86, 88, 51, 63],
 [86, 63, 50, 84, 52, 96, 92, 77, 72, 72, 89,  0, 96, 81, 88, 59, 73, 67,
  83, 93, 68, 73, 83, 87, 52, 81, 86, 91, 84, 61, 51, 69, 51, 84, 87, 92,
  56, 96, 65, 71],
 [88, 67, 80, 78, 64, 92, 78, 82, 91, 96, 63, 96,  0, 60, 94, 96, 83, 76,
  93, 63, 57, 89, 62, 60, 54, 97, 75, 61, 58, 84, 99, 74, 82, 63, 93, 50,
  67, 88, 77, 65],
 [53, 80, 94, 56, 87, 51, 67, 51, 89, 89, 83, 81, 60,  0, 63, 87, 82, 66,
  59, 58, 96, 74, 93, 54, 91, 70, 98, 68, 75, 86, 69, 70, 61, 51, 71, 83,
  75, 69, 68, 53],
 [92, 59, 59, 72, 92, 59, 56, 86, 70, 56, 70, 88, 94, 63,  0, 54, 53, 95,
  51, 55, 58, 99, 83, 56, 70, 62, 67, 75, 64, 58, 96, 79, 84, 59, 50, 77,
  75, 64, 55, 65],
 [68, 56, 82, 94, 56, 81, 92, 67, 88, 75, 58, 59, 96, 87, 54,  0, 90, 90,
  59, 91, 53, 98, 96, 54, 74, 95, 99, 55, 70, 54, 60, 99, 65, 98, 65, 52,
  85, 65, 81, 65],
 [59, 63, 92, 93, 73, 92, 66, 96, 90, 88, 56, 73, 83, 82, 53, 90,  0, 89,
  50, 71, 58, 83, 59, 56, 52, 76, 92, 80, 72, 61, 52, 62, 95, 63, 64, 63,
  94, 73, 95, 79],
 [66, 52, 85, 66, 75, 69, 85, 70, 90, 99, 95, 67, 76, 66, 95, 90, 89,  0,
  80, 51, 55, 55, 87, 79, 68, 63, 87, 74, 66, 84, 90, 84, 50, 80, 71, 97,
  64, 65, 51, 82],
 [82, 77, 86, 65, 88, 88, 86, 89, 65, 74, 90, 83, 93, 59, 51, 59, 50, 80,
   0, 62, 93, 81, 61, 66, 96, 56, 59, 79, 68, 87, 69, 82, 85, 81, 97, 64,
  63, 69, 62, 91],
 [72, 91, 63, 54, 63, 96, 97, 91, 94, 72, 66, 93, 63, 58, 55, 91, 71, 51,
  62,  0, 56, 96, 78, 50, 95, 79, 75, 74, 87, 73, 78, 95, 84, 91, 63, 96,
  67, 82, 51, 71],
 [75, 66, 65, 87, 52, 71, 98, 97, 76, 78, 58, 68, 57, 96, 58, 53, 58, 55,
  93, 56,  0, 99, 82, 93, 71, 78, 59, 86, 51, 55, 67, 84, 50, 78, 77, 76,
  55, 93, 60, 94],
 [64, 91, 79, 84, 74, 63, 96, 83, 75, 95, 86, 73, 89, 74, 99, 98, 83, 55,
  81, 96, 99,  0, 93, 88, 71, 50, 71, 82, 95, 90, 62, 54, 91, 84, 90, 83,
  56, 93, 56, 81],
 [70, 65, 89, 51, 84, 83, 91, 96, 78, 54, 88, 83, 62, 93, 83, 96, 59, 87,
  61, 78, 82, 93,  0, 74, 52, 76, 64, 51, 59, 79, 95, 65, 54, 71, 78, 93,
  70, 94, 86, 76],
 [80, 88, 69, 92, 76, 75, 84, 96, 71, 99, 68, 87, 60, 54, 56, 54, 56, 79,
  66, 50, 93, 88, 74,  0, 69, 96, 58, 99, 68, 75, 97, 60, 86, 59, 80, 89,
  60, 74, 51, 79],
 [94, 91, 71, 51, 91, 98, 87, 63, 52, 83, 97, 52, 54, 91, 70, 74, 52, 68,
  96, 95, 71, 71, 52, 69,  0, 81, 84, 74, 88, 74, 90, 76, 58, 91, 65, 99,
  63, 57, 82, 62],
 [74, 65, 78, 72, 57, 97, 98, 88, 82, 70, 73, 81, 97, 70, 62, 95, 76, 63,
  56, 79, 78, 50, 76, 96, 81,  0, 88, 85, 92, 76, 74, 54, 89, 63, 80, 98,
  85, 70, 90, 53],
 [78, 75, 95, 85, 60, 60, 70, 65, 74, 78, 92, 86, 75, 98, 67, 99, 92, 87,
  59, 75, 59, 71, 64, 58, 84, 88,  0, 81, 84, 99, 60, 85, 56, 66, 63, 80,
  93, 61, 67, 54],
 [53, 51, 89, 95, 96, 75, 70, 98, 87, 73, 75, 91, 61, 68, 75, 55, 80, 74,
  79, 74, 86, 82, 51, 99, 74, 85, 81,  0, 98, 94, 90, 69, 58, 51, 64, 61,
  72, 50, 51, 91],
 [61, 96, 69, 67, 52, 57, 96, 56, 70, 61, 83, 84, 58, 75, 64, 70, 72, 66,
  68, 87, 51, 95, 59, 68, 88, 92, 84, 98,  0, 54, 91, 66, 87, 79, 79, 51,
  60, 60, 50, 81],
 [89, 72, 67, 98, 54, 99, 71, 59, 67, 75, 69, 61, 84, 86, 58, 54, 61, 84,
  87, 73, 55, 90, 79, 75, 74, 76, 99, 94, 54,  0, 82, 93, 96, 59, 84, 92,
  84, 50, 82, 97],
 [87, 66, 58, 93, 55, 96, 91, 50, 51, 70, 61, 51, 99, 69, 96, 60, 52, 90,
  69, 78, 67, 62, 95, 97, 90, 74, 60, 90, 91, 82,  0, 66, 97, 83, 65, 91,
  69, 65, 98, 66],
 [56, 97, 99, 56, 55, 61, 59, 66, 69, 65, 98, 69, 74, 70, 79, 99, 62, 84,
  82, 95, 84, 54, 65, 60, 76, 54, 85, 69, 66, 93, 66,  0, 89, 81, 64, 89,
  87, 75, 63, 78],
 [84, 50, 58, 64, 86, 94, 69, 84, 95, 86, 94, 51, 82, 61, 84, 65, 95, 50,
  85, 84, 50, 91, 54, 86, 58, 89, 56, 58, 87, 96, 97, 89,  0, 64, 95, 94,
  91, 66, 53, 69],
 [81, 86, 80, 92, 84, 66, 87, 98, 97, 62, 66, 84, 63, 51, 59, 98, 63, 80,
  81, 91, 78, 84, 71, 59, 91, 63, 66, 51, 79, 59, 83, 81, 64,  0, 58, 85,
  60, 55, 61, 78],
 [52, 58, 68, 64, 82, 97, 89, 90, 86, 65, 86, 87, 93, 71, 50, 65, 64, 71,
  97, 63, 77, 90, 78, 80, 65, 80, 63, 64, 79, 84, 65, 64, 95, 58,  0, 92,
  86, 66, 68, 98],
 [56, 63, 98, 50, 93, 64, 99, 75, 99, 94, 71, 92, 50, 83, 77, 52, 63, 97,
  64, 96, 76, 83, 93, 89, 99, 98, 80, 61, 51, 92, 91, 89, 94, 85, 92,  0,
  84, 58, 87, 98],
 [68, 55, 97, 65, 82, 86, 81, 81, 50, 71, 86, 56, 67, 75, 75, 85, 94, 64,
  63, 67, 55, 56, 70, 60, 63, 85, 93, 72, 60, 84, 69, 87, 91, 60, 86, 84,
   0, 81, 50, 53],
 [99, 94, 94, 60, 72, 70, 81, 87, 90, 81, 88, 96, 88, 69, 64, 65, 73, 65,
  69, 82, 93, 93, 94, 74, 57, 70, 61, 50, 60, 50, 65, 75, 66, 55, 66, 58,
  81,  0, 52, 98],
 [74, 98, 94, 73, 67, 57, 73, 98, 52, 81, 51, 65, 77, 68, 55, 81, 95, 51,
  62, 51, 60, 56, 86, 51, 82, 90, 67, 51, 50, 82, 98, 63, 53, 61, 68, 87,
  50, 52,  0, 68],
 [67, 82, 94, 91, 76, 77, 79, 68, 92, 97, 63, 71, 65, 53, 65, 65, 79, 82,
  91, 71, 94, 81, 76, 79, 62, 53, 54, 91, 81, 97, 66, 78, 69, 78, 98, 98,
  53, 98, 68,  0]]

num = 40
encourage = [0]*num
AllC = [100] * num
getencoutagestorage = [0]*num
uninstallencoutagestorage = [0]*num
def findID(id):
    AllC[id] = AllC[id] - 5
    getencoutagestorage[id] = getencoutagestorage[id] + 1 * 5
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
                getencoutagestorage[RSUID[j]] = getencoutagestorage[RSUID[j]] + 1*5
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
    global sumtime
    timesid = [0]*num
    for i in range(len(AllC)):
        findRSUID = findID2(i)
        for j in range(len(findRSUID)):
            timesid[findRSUID[j]] = timesid[findRSUID[j]] + 1
    for x in range(len(timesid)):
        if AllC[x] <100:
            if timesid[x]<=(0.3*num):
                sumtime = sumtime+1
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
                    uninstallencoutagestorage[x] = uninstallencoutagestorage[x]+rr*100
                else:
                    uninstallencoutagestorage[x] = uninstallencoutagestorage[x] + 100-AllC[x]
                    AllC[x] = 100

sumtime = 0
for b in range(50):

    id = np.random.randint(num)
    findRSUID = findID(id)
    for i in range(len(findRSUID)):
        AllC[findRSUID[i]] = AllC[findRSUID[i]] - 5
    delStorage()
print(getencoutagestorage)
print(uninstallencoutagestorage)




