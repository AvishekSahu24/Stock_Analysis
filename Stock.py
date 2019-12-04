import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlsxwriter
import math


def movingavg(values, window):
    weights = np.repeat(1.0, window) / window
    smav = np.convolve(values, weights, 'valid')
    return smav


data2 = pd.read_excel("data15.xlsx")


CCI = []
SI = []
DSI = []
datatrue = []
rd = []
rc = []
rb = []
ra = []
nu = []

nd = []
sa = []
sb = []
sc = []
sd = []

CCIGraph = []

maxaOne = []
minaOne = []

maxaTwo = []
minaTwo = []

maxaThree = []
minaThree = []

minaGap = []
maxaGap = []

changeMinMax = []
# print(data2)

changeSlot = []

newminaThree2 = []
newMaxaThree2 = []



for dk in range(0, len(data2)):
    changeMinMax.append(1)

for sdf in range(0, len(data2)):
    changeSlot.append(1)

addCellValue = float(input("enter add value: "))
maxaCellValue = float(input("enter the ratio(Maxa ratio): "))
minaCellValue = 100 - maxaCellValue
max2 = maxaCellValue / 100
min2 = minaCellValue / 100

for s1, e1 in zip(range(0, ((len(data2) - 20) + 1)), range(20, (len(data2) + 1))):
    data = data2[s1:e1]
    period = len(data)

    pc = data.iloc[:, 5]
    lc = data.iloc[:, 4]
    hp = data.iloc[:, 3]

    typical_price = []
    x = s1
    while x < e1:
        tp = (hp[x] + lc[x] + pc[x]) / 3
        typical_price.append(tp)
        x += 1

    mov_av = sum(typical_price) / period

    mean_div = []
    z = 0
    while z < len(data):
        k = (abs(typical_price[z] - mov_av))
        mean_div.append(k)
        z += 1

    md = sum(mean_div) / period

    cc = (typical_price[-1] - mov_av) / (0.015 * md)

    CCI.append(round(cc, 2))




for s2, e2 in zip(range(0, ((len(data2) - 14) + 1)), range(14, (len(data2) + 1))):
    data3 = data2[s2:e2]
    period3 = len(data3)
    

    pc1 = data3.iloc[:, 5]
    lc1 = data3.iloc[:, 4]
    hp1 = data3.iloc[:, 3]

  
    k = ((pc1[e2 - 1] - min(lc1)) / (max(hp1) - min(lc1))) * 100
    SI.append(round(k, 2))



for d1, d2 in zip(range(0, ((len(SI) - 3) + 1)), range(3, (len(SI) + 1))):
    data4 = SI[d1:d2]
    DSI.append(round((sum(data4) / 3), 2))



for p1, p2 in zip(range(0, ((len(data2) - 1) + 1)), range(2, (len(data2) + 1))):

   
    data5 = data2[p1:p2]
    pc2 = data5.iloc[:, 5]
    lc2 = data5.iloc[:, 4]
    hp2 = data5.iloc[:, 3]
  


    pc3 = data5.iloc[0:2, 5]
    lc3 = data5.iloc[0:2, 4]
    hp3 = data5.iloc[0:2, 3]





    if hp3[p1 + 1] < hp3[p1] and lc3[p1 + 1] > lc3[p1]:
        datatrue.append("        .")

    else:
        datatrue.append(" ")



pc4 = data2.iloc[:, 5]
lc4 = data2.iloc[:, 4]
hp4 = data2.iloc[:, 3]
xt = 0
while xt < len(data2):
    rdx = (0.927 * (hp4[xt] - lc4[xt])) + pc4[xt]
    rcx = (0.691 * (hp4[xt] - lc4[xt])) + pc4[xt]
    rbx = (0.545 * (hp4[xt] - lc4[xt])) + pc4[xt]
    rax = (0.309 * (hp4[xt] - lc4[xt])) + pc4[xt]
    nux = (0.073 * (hp4[xt] - lc4[xt])) + pc4[xt]

    ndx = abs((0.073 * (hp4[xt] - lc4[xt])) - pc4[xt])
    sax = abs((0.309 * (hp4[xt] - lc4[xt])) - pc4[xt])
    sbx = abs((0.545 * (hp4[xt] - lc4[xt])) - pc4[xt])
    scx = abs((0.691 * (hp4[xt] - lc4[xt])) - pc4[xt])
    sdx = abs((0.927 * (hp4[xt] - lc4[xt])) - pc4[xt])

    rd.append(round(rdx, 2))
    rc.append(round(rcx, 2))
    rb.append(round(rbx, 2))
    ra.append(round(rax, 2))

    nu.append(round(nux, 2))
    nd.append(round(ndx, 2))
    sa.append(round(sax, 2))
    sb.append(round(sbx, 2))
    sc.append(round(scx, 2))
    sd.append(round(sdx, 2))
    xt += 1

dumbCCI = []
for g1 in range(0, 19):
    dumbCCI.append(" ")

newCCI = dumbCCI + CCI

dumbSI = []
for g2 in range(0, 13):
    dumbSI.append(" ")

newSI = dumbSI + SI

dumbDSI = []
for g3 in range(0, 15):
    dumbDSI.append(" ")

newDSI = dumbDSI + DSI

rt = 0
dotcate = []
pc5 = data2.iloc[:, 5]
lc5 = data2.iloc[:, 4]
hp5 = data2.iloc[:, 3]
high = hp5[0]
low = lc5[0]
while rt < len(data2):

    if high >= hp5[rt] and low <= lc5[rt]:
        dotcate.append("True")
    else:
        dotcate.append("false")
        high = hp5[rt]
        low = lc5[rt]
    rt += 1
dotcate[0] = "flase"

dumbdatatrue = []
for g4 in range(0, 1):
    dumbdatatrue.append(" ")

newdatatrue = dumbdatatrue + datatrue


x11 = 0
while x11 < len(data2):
    if hp4[x11] > ra[x11]:
        maxaOne.append(hp4[x11])
    else:
        maxaOne.append(ra[x11])

    if lc4[x11] < sa[x11]:
        minaOne.append(lc4[x11])
    else:
        minaOne.append(sa[x11])
    x11 += 1

pt = 0
maxaDumb = maxaOne[0]
minadumb = minaOne[0]
while pt < len(dotcate):
    if dotcate[pt] == "false":
        maxaTwo.append(maxaOne[pt])
        minaTwo.append(minaOne[pt])
        maxaDumb = maxaOne[pt]
        minadumb = minaOne[pt]
    else:
        if maxaOne[pt]>maxaDumb:
            maxaTwo.append(maxaOne[pt])
            minaTwo.append(minaOne[pt])
        elif minaOne[pt]<minadumb:
            maxaTwo.append(maxaOne[pt])
            minaTwo.append(minaOne[pt])
        else:
            maxaTwo.append(maxaDumb)
            minaTwo.append(minadumb)
    pt += 1

maxaTwo[0] = " "
minaTwo[0] = " "

x12 = 0
while x12 < len(CCI):
    if CCI[x12] > 100:
        CCIGraph.append("         A")
    elif 100 > CCI[x12] > 0:
        CCIGraph.append("         B")
    elif 0 > CCI[x12] > -100:
        CCIGraph.append("         C")
    elif CCI[x12] < -100:
        CCIGraph.append("         D")
    x12 += 1

dumbCCIGraph = []
for g12 in range(0, 19):
    dumbCCIGraph.append(" ")

newCCIGraph = dumbCCIGraph + CCIGraph

dumbDataPattern = []
for g31 in range(0, len(data2)):
    dumbDataPattern.append(" ")

maxminPattern = []
for g311 in range(0, len(data2)):
    maxminPattern.append(" ")

datamovers = []
for g312 in range(0, len(data2)):
    datamovers.append(" ")

minValue = 0
lowValue = []
ind = []
ran = []

for rtt in range(1, len(maxaTwo)):
    
    frac, whole = math.modf(maxaTwo[rtt])

    if frac < min2:
        newMaxaThree2.append(int(whole +1+ addCellValue))

    elif frac > max2:
        newMaxaThree2.append(int(whole  +2+ addCellValue))

    else:
        newMaxaThree2.append(int(whole + 1 + addCellValue))

dumMaxaThree = []
for a in range(0, 1):
    dumMaxaThree.append(" ")

allMaxaThree = dumMaxaThree + newMaxaThree2

for rff in range(1, len(minaTwo)):
    frac, whole = math.modf(minaTwo[rff])
  

    if frac < min2:
        newminaThree2.append(int(whole - 1 - addCellValue))

    elif frac > max2:
        newminaThree2.append(int(whole - addCellValue))


    else:
        newminaThree2.append(int(whole - addCellValue))




allminaThree = dumMaxaThree + newminaThree2

for p101, p201 in zip(range(0, ((len(CCI) - 1) + 1)), range(1, (len(CCI) + 1))):
    try:
        if CCI[p101] > 100 and 100 > CCI[p201] > 0:
            datamovers[CCI.index(CCI[p201]) + 20] = "A->B"

            if SI[CCI.index(CCI[p201]) + 6] < DSI[CCI.index(CCI[p201]) + 4]:
                changeSlot[CCI.index(CCI[p201]) + 19] = "AB"
            else:
                changeSlot[CCI.index(CCI[p201]) + 19] = "(AB)"

            changeMinMax[CCI.index(CCI[p201]) + 19] = allminaThree[CCI.index(CCI[p201]) + 19]
            if SI[CCI.index(CCI[p201]) + 6] < DSI[CCI.index(CCI[p201]) + 4]:
                try:
                    run37 = 1
                    
                    while run37 != 0:
                        if newCCIGraph[CCI.index(CCI[p201]) + 19 + run37] != "         B":
                            minValue = changeMinMax[CCI.index(CCI[p201]) + 18 + run37]
                            if "(" not in changeSlot[CCI.index(CCI[p201]) + 18 + run37] and minValue > lc5[
                                                CCI.index(CCI[p201]) + 19 + run37]:
                                dumbDataPattern[CCI.index(CCI[p201]) + 19 + run37] = "AB-"
                                changeSlot[CCI.index(CCI[p201]) + 18 + run37] = "AB"
                            run37 == 0
                            break
                        else:

                            minValue = changeMinMax[CCI.index(CCI[p201]) + 18 + run37]

                            if "(" not in changeSlot[CCI.index(CCI[p201]) + 18 + run37] and minValue > lc5[
                                                CCI.index(CCI[p201]) + 19 + run37]:
                                dumbDataPattern[CCI.index(CCI[p201]) + 19 + run37] = "AB-"
                                changeSlot[CCI.index(CCI[p201]) + 18 + run37] = "AB"
                                run37 == 0
                                break
                            else:
                                if SI[CCI.index(CCI[p201]) + 6 + run37] > DSI[CCI.index(CCI[p201]) + 4 + run37]:
                                    # print(SI[CCI.index(CCI[p20]) + 6 + run35])
                                    changeSlot[CCI.index(CCI[p201]) + 19 + run37] = "(AB)"
                                    dumbDataPattern[CCI.index(CCI[p201]) + 19 + run37] = dumbDataPattern[
                                        CCI.index(CCI[p201]) + 18 + run37]
                                    changeMinMax[CCI.index(CCI[p201]) + 19 + run37] = changeMinMax[
                                        CCI.index(CCI[p201]) + 18 + run37]
                                    run37 += 1
                                else:
                                    changeSlot[CCI.index(CCI[p201]) + 19 + run37] = changeSlot[
                                        CCI.index(CCI[p201]) + 18 + run37].strip("()")
                                    changeMinMax[CCI.index(CCI[p201]) + 19 + run37] = changeMinMax[
                                        CCI.index(CCI[p201]) + 18 + run37]

                                    dumbDataPattern[CCI.index(CCI[p201]) + 19 + run37] = dumbDataPattern[
                                        CCI.index(CCI[p201]) + 18 + run37]

                                    if "(" in changeSlot[CCI.index(CCI[p201]) + 18 + run37]:
                                        # print("true at: " + str(allminaThree[CCI.index(CCI[p20]) + 19 + run35]))
                                        if allminaThree[CCI.index(CCI[p201]) + 19 + run37] < changeMinMax[
                                                            CCI.index(CCI[p201]) + 18 + run37]:
                                            changeMinMax[CCI.index(CCI[p201]) + 19 + run37] = allminaThree[
                                                CCI.index(CCI[p201]) + 19 + run37]
                                    run37 += 1

                except:
                    print("leave")
    except:
        print()

minValue = 0
for p102, p202 in zip(range(0, ((len(CCI) - 1) + 1)), range(1, (len(CCI) + 1))):
    try:
        if CCI[p102] > 100 and 0 > CCI[p202] > -100:
            datamovers[CCI.index(CCI[p202]) + 20] = "A->C"

            if SI[CCI.index(CCI[p202]) + 6] < DSI[CCI.index(CCI[p202]) + 4]:
                changeSlot[CCI.index(CCI[p202]) + 19] = "AC"
            else:
                changeSlot[CCI.index(CCI[p202]) + 19] = "(AC)"

            changeMinMax[CCI.index(CCI[p202]) + 19] = allminaThree[CCI.index(CCI[p202]) + 19]
            if SI[CCI.index(CCI[p202]) + 6] < DSI[CCI.index(CCI[p202]) + 4]:
                try:
                    run38 = 1
                    # print(newCCIGraph[CCI.index(CCI[p20]) + 18 + run35])
                    while run38 != 0:
                        if newCCIGraph[CCI.index(CCI[p202]) + 19 + run38] != "         C":
                            minValue = changeMinMax[CCI.index(CCI[p202]) + 18 + run38]
                            if "(" not in changeSlot[CCI.index(CCI[p202]) + 18 + run38] and minValue > lc5[
                                                CCI.index(CCI[p202]) + 19 + run38]:
                                dumbDataPattern[CCI.index(CCI[p202]) + 19 + run38] = "AC-"
                                changeSlot[CCI.index(CCI[p202]) + 18 + run38] = "AC"
                            run38 == 0
                            break
                        else:

                            minValue = changeMinMax[CCI.index(CCI[p202]) + 18 + run38]
                            if "(" not in changeSlot[CCI.index(CCI[p202]) + 18 + run38] and minValue > lc5[
                                                CCI.index(CCI[p202]) + 19 + run38]:
                                dumbDataPattern[CCI.index(CCI[p202]) + 19 + run38] = "AC-"
                                changeSlot[CCI.index(CCI[p202]) + 18 + run38] = "AC"
                                run38 == 0
                                break
                            else:
                                if SI[CCI.index(CCI[p202]) + 6 + run38] > DSI[CCI.index(CCI[p202]) + 4 + run38]:
                                    # print(SI[CCI.index(CCI[p20]) + 6 + run35])
                                    changeSlot[CCI.index(CCI[p202]) + 19 + run38] = "(AC)"
                                    dumbDataPattern[CCI.index(CCI[p202]) + 19 + run38] = dumbDataPattern[
                                        CCI.index(CCI[p202]) + 18 + run38]
                                    changeMinMax[CCI.index(CCI[p202]) + 19 + run38] = changeMinMax[
                                        CCI.index(CCI[p202]) + 18 + run38]
                                    run38 += 1
                                else:
                                    changeSlot[CCI.index(CCI[p202]) + 19 + run38] = changeSlot[
                                        CCI.index(CCI[p202]) + 18 + run38].strip("()")
                                    changeMinMax[CCI.index(CCI[p202]) + 19 + run38] = changeMinMax[
                                        CCI.index(CCI[p202]) + 18 + run38]

                                    dumbDataPattern[CCI.index(CCI[p202]) + 19 + run38] = dumbDataPattern[
                                        CCI.index(CCI[p202]) + 18 + run38]

                                    if "(" in changeSlot[CCI.index(CCI[p202]) + 18 + run38]:
                                        # print("true at: " + str(allminaThree[CCI.index(CCI[p20]) + 19 + run35]))
                                        if allminaThree[CCI.index(CCI[p202]) + 19 + run38] < changeMinMax[
                                                            CCI.index(CCI[p202]) + 18 + run38]:
                                            changeMinMax[CCI.index(CCI[p202]) + 19 + run38] = allminaThree[
                                                CCI.index(CCI[p202]) + 19 + run38]
                                    run38 += 1


                except:
                    print("leave")
    except:
        print()

minValue = 0
for p103, p203 in zip(range(0, ((len(CCI) - 1) + 1)), range(1, (len(CCI) + 1))):
    try:
        if CCI[p103] > 100 and CCI[p203] < -100:
            datamovers[CCI.index(CCI[p203]) + 20] = "A->D"

            if SI[CCI.index(CCI[p203]) + 6] < DSI[CCI.index(CCI[p203]) + 4]:
                changeSlot[CCI.index(CCI[p203]) + 19] = "AD"
            else:
                changeSlot[CCI.index(CCI[p203]) + 19] = "(AD)"

            changeMinMax[CCI.index(CCI[p203]) + 19] = allminaThree[CCI.index(CCI[p203]) + 19]
            if SI[CCI.index(CCI[p203]) + 6] < DSI[CCI.index(CCI[p203]) + 4]:
                try:
                    run39 = 1
                    # print(newCCIGraph[CCI.index(CCI[p20]) + 18 + run35])
                    while run39 != 0:
                        if newCCIGraph[CCI.index(CCI[p203]) + 19 + run39] != "         D":
                            minValue = changeMinMax[CCI.index(CCI[p203]) + 18 + run39]
                            if "(" not in changeSlot[CCI.index(CCI[p203]) + 18 + run39] and minValue > lc5[
                                                CCI.index(CCI[p203]) + 19 + run39]:
                                dumbDataPattern[CCI.index(CCI[p203]) + 19 + run39] = "AD-"
                                changeSlot[CCI.index(CCI[p203]) + 18 + run39] = "AD"
                            run39 == 0
                            break
                        else:

                            minValue = changeMinMax[CCI.index(CCI[p203]) + 18 + run39]
                            if "(" not in changeSlot[CCI.index(CCI[p203]) + 18 + run39] and minValue > lc5[
                                                CCI.index(CCI[p203]) + 19 + run39]:
                                dumbDataPattern[CCI.index(CCI[p203]) + 19 + run39] = "AD-"
                                changeSlot[CCI.index(CCI[p203]) + 18 + run39] = "AD"
                                run39 == 0
                                break
                            else:
                                if SI[CCI.index(CCI[p203]) + 6 + run39] > DSI[CCI.index(CCI[p203]) + 4 + run39]:
                                    # print(SI[CCI.index(CCI[p20]) + 6 + run35])
                                    changeSlot[CCI.index(CCI[p203]) + 19 + run39] = "(AD)"
                                    dumbDataPattern[CCI.index(CCI[p203]) + 19 + run39] = dumbDataPattern[
                                        CCI.index(CCI[p203]) + 18 + run39]
                                    changeMinMax[CCI.index(CCI[p203]) + 19 + run39] = changeMinMax[
                                        CCI.index(CCI[p203]) + 18 + run39]
                                    run39 += 1
                                else:
                                    changeSlot[CCI.index(CCI[p203]) + 19 + run39] = changeSlot[
                                        CCI.index(CCI[p203]) + 18 + run39].strip("()")
                                    changeMinMax[CCI.index(CCI[p203]) + 19 + run39] = changeMinMax[
                                        CCI.index(CCI[p203]) + 18 + run39]

                                    dumbDataPattern[CCI.index(CCI[p203]) + 19 + run39] = dumbDataPattern[
                                        CCI.index(CCI[p203]) + 18 + run39]

                                    if "(" in changeSlot[CCI.index(CCI[p203]) + 18 + run39]:
                                        # print("true at: " + str(allminaThree[CCI.index(CCI[p20]) + 19 + run35]))
                                        if allminaThree[CCI.index(CCI[p203]) + 19 + run39] < changeMinMax[
                                                            CCI.index(CCI[p203]) + 18 + run39]:
                                            changeMinMax[CCI.index(CCI[p203]) + 19 + run39] = allminaThree[
                                                CCI.index(CCI[p203]) + 19 + run39]
                                    run39 += 1


                except:
                    print("leave")
    except:
        print()

minValue = 0
# For B range
for p10, p20 in zip(range(0, ((len(CCI) - 1) + 1)), range(1, (len(CCI) + 1))):
    try:
        if 100 > CCI[p10] > 0 and 0 > CCI[p20] > -100:
            datamovers[CCI.index(CCI[p20]) + 20] = "B->C"
            if SI[CCI.index(CCI[p20]) + 6] < DSI[CCI.index(CCI[p20]) + 4]:
                changeSlot[CCI.index(CCI[p20]) + 19] = "BC"
            else:
                changeSlot[CCI.index(CCI[p20]) + 19] = "(BC)"

            changeMinMax[CCI.index(CCI[p20]) + 19] = allminaThree[CCI.index(CCI[p20]) + 19]
            if SI[CCI.index(CCI[p20]) + 6] < DSI[CCI.index(CCI[p20]) + 4]:
                try:
                    run35 = 1
                    # print(newCCIGraph[CCI.index(CCI[p20]) + 18 + run35])
                    while run35 != 0:
                        if newCCIGraph[CCI.index(CCI[p20]) + 19 + run35]!="         C":
                            minValue = changeMinMax[CCI.index(CCI[p20]) + 18 + run35]
                            if "(" not in changeSlot[CCI.index(CCI[p20]) + 18 + run35] and minValue > lc5[CCI.index(CCI[p20]) + 19 + run35]:
                                dumbDataPattern[CCI.index(CCI[p20]) + 19 + run35] = "BC-"
                                changeSlot[CCI.index(CCI[p20]) + 18 + run35] = "BC"
                            run35 == 0
                            break
                        else:

                            minValue = changeMinMax[CCI.index(CCI[p20]) + 18 + run35]

                            if "(" not in changeSlot[CCI.index(CCI[p20]) + 18 + run35] and minValue > lc5[CCI.index(CCI[p20]) + 19 + run35]:
                                dumbDataPattern[CCI.index(CCI[p20]) + 19 + run35] = "BC-"
                                changeSlot[CCI.index(CCI[p20]) + 18 + run35] = "BC"
                                print(minValue)
                                run35 == 0
                                break
                            else:
                                if SI[CCI.index(CCI[p20]) + 6 + run35] > DSI[CCI.index(CCI[p20]) + 4 + run35]:
                                    # print(SI[CCI.index(CCI[p20]) + 6 + run35])
                                    changeSlot[CCI.index(CCI[p20]) + 19 + run35] = "(BC)"
                                    dumbDataPattern[CCI.index(CCI[p20]) + 19 + run35] = dumbDataPattern[CCI.index(CCI[p20]) + 18 + run35]
                                    changeMinMax[CCI.index(CCI[p20]) + 19 + run35] = changeMinMax[CCI.index(CCI[p20]) + 18 + run35]
                                    run35 += 1
                                else:
                                    changeSlot[CCI.index(CCI[p20]) + 19 + run35] = changeSlot[CCI.index(CCI[p20]) + 18 + run35].strip("()")
                                    changeMinMax[CCI.index(CCI[p20]) + 19 + run35] = changeMinMax[CCI.index(CCI[p20]) + 18 + run35]

                                    dumbDataPattern[CCI.index(CCI[p20]) + 19 + run35] = dumbDataPattern[CCI.index(CCI[p20]) + 18 + run35]

                                    if "(" in changeSlot[CCI.index(CCI[p20]) + 18 + run35]:
                                        # print("true at: " + str(allminaThree[CCI.index(CCI[p20]) + 19 + run35]))
                                        if allminaThree[CCI.index(CCI[p20]) + 19 + run35] < changeMinMax[CCI.index(CCI[p20]) + 18 + run35]:
                                            changeMinMax[CCI.index(CCI[p20]) + 19 + run35] = allminaThree[CCI.index(CCI[p20]) + 19 + run35]
                                    run35 += 1




                except:
                    print("levae")




    except:
        print()

minValue = 0
for p104, p204 in zip(range(0, ((len(CCI) - 1) + 1)), range(1, (len(CCI) + 1))):
    try:
        if 100 > CCI[p104] > 0 and CCI[p204] < -100:
            datamovers[CCI.index(CCI[p204]) + 20] = "B->D"

            if SI[CCI.index(CCI[p204]) + 6] < DSI[CCI.index(CCI[p204]) + 4]:
                changeSlot[CCI.index(CCI[p204]) + 19] = "BD"
            else:
                changeSlot[CCI.index(CCI[p204]) + 19] = "(BD)"

            changeMinMax[CCI.index(CCI[p204]) + 19] = allminaThree[CCI.index(CCI[p204]) + 19]
            if SI[CCI.index(CCI[p204]) + 6] < DSI[CCI.index(CCI[p204]) + 4]:
                try:
                    run40 = 1
                    # print(newCCIGraph[CCI.index(CCI[p20]) + 18 + run35])
                    while run40 != 0:
                        if newCCIGraph[CCI.index(CCI[p204]) + 19 + run40] != "         D":
                            minValue = changeMinMax[CCI.index(CCI[p204]) + 18 + run40]
                            if "(" not in changeSlot[CCI.index(CCI[p204]) + 18 + run40] and minValue > lc5[
                                                CCI.index(CCI[p204]) + 19 + run40]:
                                dumbDataPattern[CCI.index(CCI[p204]) + 19 + run40] = "BD-"
                                changeSlot[CCI.index(CCI[p204]) + 18 + run40] = "BD"
                            run40 == 0
                            break
                        else:

                            minValue = changeMinMax[CCI.index(CCI[p204]) + 18 + run40]
                            if "(" not in changeSlot[CCI.index(CCI[p204]) + 18 + run40] and minValue > lc5[
                                                CCI.index(CCI[p204]) + 19 + run40]:
                                dumbDataPattern[CCI.index(CCI[p204]) + 19 + run40] = "BD-"
                                changeSlot[CCI.index(CCI[p204]) + 18 + run40] = "BD"
                                run40 == 0
                                break
                            else:
                                if SI[CCI.index(CCI[p204]) + 6 + run40] > DSI[CCI.index(CCI[p204]) + 4 + run40]:
                                    # print(SI[CCI.index(CCI[p20]) + 6 + run35])
                                    changeSlot[CCI.index(CCI[p204]) + 19 + run40] = "(BD)"
                                    dumbDataPattern[CCI.index(CCI[p204]) + 19 + run40] = dumbDataPattern[
                                        CCI.index(CCI[p204]) + 18 + run40]
                                    changeMinMax[CCI.index(CCI[p204]) + 19 + run40] = changeMinMax[
                                        CCI.index(CCI[p204]) + 18 + run40]
                                    run40 += 1
                                else:
                                    changeSlot[CCI.index(CCI[p204]) + 19 + run40] = changeSlot[
                                        CCI.index(CCI[p204]) + 18 + run40].strip("()")
                                    changeMinMax[CCI.index(CCI[p204]) + 19 + run40] = changeMinMax[
                                        CCI.index(CCI[p204]) + 18 + run40]

                                    dumbDataPattern[CCI.index(CCI[p204]) + 19 + run40] = dumbDataPattern[
                                        CCI.index(CCI[p204]) + 18 + run40]

                                    if "(" in changeSlot[CCI.index(CCI[p204]) + 18 + run40]:
                                        # print("true at: " + str(allminaThree[CCI.index(CCI[p20]) + 19 + run35]))
                                        if allminaThree[CCI.index(CCI[p204]) + 19 + run40] < changeMinMax[
                                                            CCI.index(CCI[p204]) + 18 + run40]:
                                            changeMinMax[CCI.index(CCI[p204]) + 19 + run40] = allminaThree[
                                                CCI.index(CCI[p204]) + 19 + run40]
                                    run40 += 1



                except:
                    print("levae")
    except:
        print()

minValue = 0
for p105, p205 in zip(range(0, ((len(CCI) - 1) + 1)), range(1, (len(CCI) + 1))):
    try:
        if 0 > CCI[p105] > -100 and CCI[p205] < -100:
            datamovers[CCI.index(CCI[p205]) + 20] = "C->D"

            if SI[CCI.index(CCI[p205]) + 6] < DSI[CCI.index(CCI[p205]) + 4]:
                changeSlot[CCI.index(CCI[p205]) + 19] = "CD"
            else:
                changeSlot[CCI.index(CCI[p205]) + 19] = "(CD)"

            changeMinMax[CCI.index(CCI[p205]) + 19] = allminaThree[CCI.index(CCI[p205]) + 19]
            if SI[CCI.index(CCI[p205]) + 6] < DSI[CCI.index(CCI[p205]) + 4]:
                try:
                    run41 = 1
                    # print(newCCIGraph[CCI.index(CCI[p20]) + 18 + run35])
                    while run41 != 0:
                        if newCCIGraph[CCI.index(CCI[p205]) + 19 + run41] != "         D":
                            minValue = changeMinMax[CCI.index(CCI[p205]) + 18 + run41]
                            if "(" not in changeSlot[CCI.index(CCI[p205]) + 18 + run41] and minValue > lc5[
                                                CCI.index(CCI[p205]) + 19 + run41]:
                                dumbDataPattern[CCI.index(CCI[p205]) + 19 + run41] = "CD-"
                                changeSlot[CCI.index(CCI[p205]) + 18 + run41] = "CD"
                            run41 == 0
                            break
                        else:

                            minValue = changeMinMax[CCI.index(CCI[p205]) + 18 + run41]
                            if "(" not in changeSlot[CCI.index(CCI[p205]) + 18 + run41] and minValue > lc5[
                                                CCI.index(CCI[p205]) + 19 + run41]:
                                dumbDataPattern[CCI.index(CCI[p205]) + 19 + run41] = "CD-"
                                changeSlot[CCI.index(CCI[p205]) + 18 + run41] = "CD"
                                run41 == 0
                                break
                            else:
                                if SI[CCI.index(CCI[p205]) + 6 + run41] > DSI[CCI.index(CCI[p205]) + 4 + run41]:
                                    # print(SI[CCI.index(CCI[p20]) + 6 + run35])
                                    changeSlot[CCI.index(CCI[p205]) + 19 + run41] = "(CD)"
                                    dumbDataPattern[CCI.index(CCI[p205]) + 19 + run41] = dumbDataPattern[
                                        CCI.index(CCI[p205]) + 18 + run41]
                                    changeMinMax[CCI.index(CCI[p205]) + 19 + run41] = changeMinMax[
                                        CCI.index(CCI[p205]) + 18 + run41]
                                    run41 += 1
                                else:
                                    changeSlot[CCI.index(CCI[p205]) + 19 + run41] = changeSlot[
                                        CCI.index(CCI[p205]) + 18 + run41].strip("()")
                                    changeMinMax[CCI.index(CCI[p205]) + 19 + run41] = changeMinMax[
                                        CCI.index(CCI[p205]) + 18 + run41]

                                    dumbDataPattern[CCI.index(CCI[p205]) + 19 + run41] = dumbDataPattern[
                                        CCI.index(CCI[p205]) + 18 + run41]

                                    if "(" in changeSlot[CCI.index(CCI[p205]) + 18 + run41]:
                                        # print("true at: " + str(allminaThree[CCI.index(CCI[p20]) + 19 + run35]))
                                        if allminaThree[CCI.index(CCI[p205]) + 19 + run41] < changeMinMax[
                                                            CCI.index(CCI[p205]) + 18 + run41]:
                                            changeMinMax[CCI.index(CCI[p205]) + 19 + run41] = allminaThree[
                                                CCI.index(CCI[p205]) + 19 + run41]
                                    run41 += 1


                except:
                    print("levae")
    except:
        print()

maxValue = 0
for p106, p206 in zip(range(0, ((len(CCI) - 1) + 1)), range(1, (len(CCI) + 1))):
    try:
        if 100 > CCI[p106] > 0 and CCI[p206] > 100:
            datamovers[CCI.index(CCI[p206]) + 20] = "B->A"

            if SI[CCI.index(CCI[p206]) + 6] > DSI[CCI.index(CCI[p206]) + 4]:
                changeSlot[CCI.index(CCI[p206]) + 19] = "BA"
            else:
                changeSlot[CCI.index(CCI[p206]) + 19] = "(BA)"

            changeMinMax[CCI.index(CCI[p206]) + 19] = allMaxaThree[CCI.index(CCI[p206]) + 19]
            if SI[CCI.index(CCI[p206]) + 6] > DSI[CCI.index(CCI[p206]) + 4]:
                try:
                    run42 = 1
                    # print(newCCIGraph[CCI.index(CCI[p20]) + 18 + run35])
                    while run42 != 0:
                        if newCCIGraph[CCI.index(CCI[p206]) + 19 + run42] != "         A":
                            minValue = changeMinMax[CCI.index(CCI[p206]) + 18 + run42]
                            if "(" not in changeSlot[CCI.index(CCI[p206]) + 18 + run42] and minValue > lc5[
                                                CCI.index(CCI[p206]) + 19 + run42]:
                                dumbDataPattern[CCI.index(CCI[p206]) + 19 + run42] = "BA-"
                                changeSlot[CCI.index(CCI[p206]) + 18 + run42] = "BA"
                            run42 == 0
                            break
                        else:

                            minValue = changeMinMax[CCI.index(CCI[p206]) + 18 + run42]
                            if "(" not in changeSlot[CCI.index(CCI[p206]) + 18 + run42] and minValue < hp5[
                                                CCI.index(CCI[p206]) + 19 + run42]:
                                dumbDataPattern[CCI.index(CCI[p206]) + 19 + run42] = "BA+"
                                changeSlot[CCI.index(CCI[p206]) + 18 + run42] = "BA"
                                run42 == 0
                                break
                            else:
                                if SI[CCI.index(CCI[p206]) + 6 + run42] < DSI[CCI.index(CCI[p206]) + 4 + run42]:
                                    # print(SI[CCI.index(CCI[p20]) + 6 + run35])
                                    changeSlot[CCI.index(CCI[p206]) + 19 + run42] = "(BA)"
                                    dumbDataPattern[CCI.index(CCI[p206]) + 19 + run42] = dumbDataPattern[
                                        CCI.index(CCI[p206]) + 18 + run42]
                                    changeMinMax[CCI.index(CCI[p206]) + 19 + run42] = changeMinMax[
                                        CCI.index(CCI[p206]) + 18 + run42]
                                    run42 += 1
                                else:
                                    changeSlot[CCI.index(CCI[p206]) + 19 + run42] = changeSlot[
                                        CCI.index(CCI[p206]) + 18 + run42].strip("()")
                                    changeMinMax[CCI.index(CCI[p206]) + 19 + run42] = changeMinMax[
                                        CCI.index(CCI[p206]) + 18 + run42]

                                    dumbDataPattern[CCI.index(CCI[p206]) + 19 + run42] = dumbDataPattern[
                                        CCI.index(CCI[p206]) + 18 + run42]

                                    if "(" in changeSlot[CCI.index(CCI[p206]) + 18 + run42]:
                                        # print("true at: " + str(allminaThree[CCI.index(CCI[p20]) + 19 + run35]))
                                        if allminaThree[CCI.index(CCI[p206]) + 19 + run42] < changeMinMax[
                                                            CCI.index(CCI[p206]) + 18 + run42]:
                                            changeMinMax[CCI.index(CCI[p206]) + 19 + run42] = allMaxaThree[
                                                CCI.index(CCI[p206]) + 19 + run42]
                                    run42 += 1

      
                        print("BA")
                except:
                    print("levae")
    except:
        print()

maxValue = 0
for p107, p207 in zip(range(0, ((len(CCI) - 1) + 1)), range(1, (len(CCI) + 1))):
    try:
        if 0 > CCI[p107] > -100 and CCI[p207] > 100:
            datamovers[CCI.index(CCI[p207]) + 20] = "C->A"

            if SI[CCI.index(CCI[p207]) + 6] > DSI[CCI.index(CCI[p207]) + 4]:
                changeSlot[CCI.index(CCI[p207]) + 19] = "CA"
            else:
                changeSlot[CCI.index(CCI[p207]) + 19] = "(CA)"

            changeMinMax[CCI.index(CCI[p207]) + 19] = allMaxaThree[CCI.index(CCI[p207]) + 19]
            if SI[CCI.index(CCI[p207]) + 6] > DSI[CCI.index(CCI[p207]) + 4]:
                try:
                    run43 = 1
                    # print(newCCIGraph[CCI.index(CCI[p20]) + 18 + run35])
                    while run43 != 0:
                        if newCCIGraph[CCI.index(CCI[p207]) + 19 + run43] != "         A":
                            minValue = changeMinMax[CCI.index(CCI[p207]) + 18 + run43]
                            if "(" not in changeSlot[CCI.index(CCI[p207]) + 18 + run43] and minValue > lc5[
                                                CCI.index(CCI[p207]) + 19 + run43]:
                                dumbDataPattern[CCI.index(CCI[p207]) + 19 + run43] = "CA-"
                                changeSlot[CCI.index(CCI[p207]) + 18 + run43] = "CA"
                            run43 == 0
                            break
                        else:

                            minValue = changeMinMax[CCI.index(CCI[p207]) + 18 + run43]
                            if "(" not in changeSlot[CCI.index(CCI[p207]) + 18 + run43] and minValue < hp5[
                                                CCI.index(CCI[p207]) + 19 + run43]:
                                dumbDataPattern[CCI.index(CCI[p207]) + 19 + run43] = "CA+"
                                changeSlot[CCI.index(CCI[p207]) + 18 + run43] = "CA"
                                run43 == 0
                                break
                            else:
                                if SI[CCI.index(CCI[p207]) + 6 + run43] < DSI[CCI.index(CCI[p207]) + 4 + run43]:
                                    # print(SI[CCI.index(CCI[p20]) + 6 + run35])
                                    changeSlot[CCI.index(CCI[p207]) + 19 + run43] = "(CA)"
                                    dumbDataPattern[CCI.index(CCI[p207]) + 19 + run43] = dumbDataPattern[
                                        CCI.index(CCI[p207]) + 18 + run43]
                                    changeMinMax[CCI.index(CCI[p207]) + 19 + run43] = changeMinMax[
                                        CCI.index(CCI[p207]) + 18 + run43]
                                    run43 += 1
                                else:
                                    changeSlot[CCI.index(CCI[p207]) + 19 + run43] = changeSlot[
                                        CCI.index(CCI[p207]) + 18 + run43].strip("()")
                                    changeMinMax[CCI.index(CCI[p207]) + 19 + run43] = changeMinMax[
                                        CCI.index(CCI[p207]) + 18 + run43]

                                    dumbDataPattern[CCI.index(CCI[p207]) + 19 + run43] = dumbDataPattern[
                                        CCI.index(CCI[p207]) + 18 + run43]

                                    if "(" in changeSlot[CCI.index(CCI[p207]) + 18 + run43]:
                                        # print("true at: " + str(allminaThree[CCI.index(CCI[p20]) + 19 + run35]))
                                        if allminaThree[CCI.index(CCI[p207]) + 19 + run43] < changeMinMax[
                                                            CCI.index(CCI[p207]) + 18 + run43]:
                                            changeMinMax[CCI.index(CCI[p207]) + 19 + run43] = allMaxaThree[
                                                CCI.index(CCI[p207]) + 19 + run43]
                                    run43 += 1


                        print("CA")
                except:
                    print("levae")
    except:
        print()

maxValue = 0
for p108, p208 in zip(range(0, ((len(CCI) - 1) + 1)), range(1, (len(CCI) + 1))):
    try:
        if 0 > CCI[p108] > -100 and 100 > CCI[p208] > 0:
            datamovers[CCI.index(CCI[p208]) + 20] = "C->B"

            if SI[CCI.index(CCI[p208]) + 6] > DSI[CCI.index(CCI[p208]) + 4]:
                changeSlot[CCI.index(CCI[p208]) + 19] = "CB"
            else:
                changeSlot[CCI.index(CCI[p208]) + 19] = "(CB)"

            changeMinMax[CCI.index(CCI[p208]) + 19] = allMaxaThree[CCI.index(CCI[p208]) + 19]
            if SI[CCI.index(CCI[p208]) + 6] > DSI[CCI.index(CCI[p208]) + 4]:
                try:
                    run36 = 1
                    while run36 != 0:
                        if newCCIGraph[CCI.index(CCI[p208]) + 19 + run36] != "         B":
                            minValue = changeMinMax[CCI.index(CCI[p208]) + 18 + run36]
                            if "(" not in changeSlot[CCI.index(CCI[p208]) + 18 + run36] and minValue > lc5[
                                                CCI.index(CCI[p208]) + 19 + run36]:
                                dumbDataPattern[CCI.index(CCI[p208]) + 19 + run36] = "CB-"
                                changeSlot[CCI.index(CCI[p208]) + 18 + run36] = "CB"
                            run36 == 0
                            break
                        else:

                            minValue = changeMinMax[CCI.index(CCI[p208]) + 18 + run36]
                            if "(" not in changeSlot[CCI.index(CCI[p208]) + 18 + run36] and minValue < hp5[
                                                CCI.index(CCI[p208]) + 19 + run36]:
                                dumbDataPattern[CCI.index(CCI[p208]) + 19 + run36] = "CB+"
                                changeSlot[CCI.index(CCI[p208]) + 18 + run36] = "CB"
                                run36 == 0
                                break
                            else:
                                if SI[CCI.index(CCI[p208]) + 6 + run36] < DSI[CCI.index(CCI[p208]) + 4 + run36]:
                                    # print(SI[CCI.index(CCI[p20]) + 6 + run35])
                                    changeSlot[CCI.index(CCI[p208]) + 19 + run36] = "(CB)"
                                    dumbDataPattern[CCI.index(CCI[p208]) + 19 + run36] = dumbDataPattern[
                                        CCI.index(CCI[p208]) + 18 + run36]
                                    changeMinMax[CCI.index(CCI[p208]) + 19 + run36] = changeMinMax[
                                        CCI.index(CCI[p208]) + 18 + run36]
                                    run36 += 1
                                else:
                                    changeSlot[CCI.index(CCI[p208]) + 19 + run36] = changeSlot[
                                        CCI.index(CCI[p208]) + 18 + run36].strip("()")
                                    changeMinMax[CCI.index(CCI[p208]) + 19 + run36] = changeMinMax[
                                        CCI.index(CCI[p208]) + 18 + run36]

                                    dumbDataPattern[CCI.index(CCI[p208]) + 19 + run36] = dumbDataPattern[
                                        CCI.index(CCI[p208]) + 18 + run36]

                                    if "(" in changeSlot[CCI.index(CCI[p208]) + 18 + run36]:
                                        # print("true at: " + str(allminaThree[CCI.index(CCI[p20]) + 19 + run35]))
                                        if allminaThree[CCI.index(CCI[p208]) + 19 + run36] < changeMinMax[
                                                            CCI.index(CCI[p208]) + 18 + run36]:
                                            changeMinMax[CCI.index(CCI[p208]) + 19 + run36] = allMaxaThree[
                                                CCI.index(CCI[p208]) + 19 + run36]
                                    run36 += 1

                        print("CB")
                except:
                    print("levae")
    except:
        print()

maxValue = 0
for p109, p209 in zip(range(0, ((len(CCI) - 1) + 1)), range(1, (len(CCI) + 1))):
    try:
        if CCI[p209] > 100 and CCI[p109] < -100:
            datamovers[CCI.index(CCI[p109]) + 20] = "D->A"

            if SI[CCI.index(CCI[p209]) + 6] > DSI[CCI.index(CCI[p209]) + 4]:
                changeSlot[CCI.index(CCI[p209]) + 19] = "DA"
            else:
                changeSlot[CCI.index(CCI[p209]) + 19] = "(DA)"

            changeMinMax[CCI.index(CCI[p209]) + 19] = allMaxaThree[CCI.index(CCI[p209]) + 19]
            if SI[CCI.index(CCI[p209]) + 6] > DSI[CCI.index(CCI[p209]) + 4]:
                try:
                    run44 = 1
                    # print(newCCIGraph[CCI.index(CCI[p20]) + 18 + run35])
                    while run44 != 0:
                        if newCCIGraph[CCI.index(CCI[p209]) + 19 + run44] != "         A":
                            minValue = changeMinMax[CCI.index(CCI[p209]) + 18 + run44]
                            if "(" not in changeSlot[CCI.index(CCI[p209]) + 18 + run44] and minValue > lc5[
                                                CCI.index(CCI[p209]) + 19 + run44]:
                                dumbDataPattern[CCI.index(CCI[p209]) + 19 + run44] = "DA-"
                                changeSlot[CCI.index(CCI[p209]) + 18 + run44] = "DA"
                            run44 == 0
                            break
                        else:

                            minValue = changeMinMax[CCI.index(CCI[p209]) + 18 + run44]
                            if "(" not in changeSlot[CCI.index(CCI[p209]) + 18 + run44] and minValue < hp5[
                                                CCI.index(CCI[p209]) + 19 + run44]:
                                dumbDataPattern[CCI.index(CCI[p209]) + 19 + run44] = "DA+"
                                changeSlot[CCI.index(CCI[p209]) + 18 + run44] = "DA"
                                run44 == 0
                                break
                            else:
                                if SI[CCI.index(CCI[p209]) + 6 + run44] < DSI[CCI.index(CCI[p209]) + 4 + run44]:
                                    # print(SI[CCI.index(CCI[p20]) + 6 + run35])
                                    changeSlot[CCI.index(CCI[p209]) + 19 + run44] = "(DA)"
                                    dumbDataPattern[CCI.index(CCI[p209]) + 19 + run44] = dumbDataPattern[
                                        CCI.index(CCI[p209]) + 18 + run44]
                                    changeMinMax[CCI.index(CCI[p209]) + 19 + run44] = changeMinMax[
                                        CCI.index(CCI[p209]) + 18 + run44]
                                    run44 += 1
                                else:
                                    changeSlot[CCI.index(CCI[p209]) + 19 + run44] = changeSlot[
                                        CCI.index(CCI[p209]) + 18 + run44].strip("()")
                                    changeMinMax[CCI.index(CCI[p209]) + 19 + run44] = changeMinMax[
                                        CCI.index(CCI[p209]) + 18 + run44]

                                    dumbDataPattern[CCI.index(CCI[p209]) + 19 + run44] = dumbDataPattern[
                                        CCI.index(CCI[p209]) + 18 + run44]

                                    if "(" in changeSlot[CCI.index(CCI[p209]) + 18 + run44]:
                                        # print("true at: " + str(allminaThree[CCI.index(CCI[p20]) + 19 + run35]))
                                        if allminaThree[CCI.index(CCI[p209]) + 19 + run44] < changeMinMax[
                                                            CCI.index(CCI[p209]) + 18 + run44]:
                                            changeMinMax[CCI.index(CCI[p209]) + 19 + run44] = allMaxaThree[
                                                CCI.index(CCI[p209]) + 19 + run44]
                                    run44 += 1

                        print("DA")
                except:
                    print("levae")
    except:
        print()

maxValue = 0
for p110, p210 in zip(range(0, ((len(CCI) - 1) + 1)), range(1, (len(CCI) + 1))):
    try:
        if CCI[p110] < -100 and 100 > CCI[p210] > 0:
            datamovers[CCI.index(CCI[p210]) + 20] = "D->B"

            if SI[CCI.index(CCI[p210]) + 6] > DSI[CCI.index(CCI[p210]) + 4]:
                changeSlot[CCI.index(CCI[p210]) + 19] = "DB"
            else:
                changeSlot[CCI.index(CCI[p210]) + 19] = "(DB)"

            changeMinMax[CCI.index(CCI[p210]) + 19] = allMaxaThree[CCI.index(CCI[p210]) + 19]
            if SI[CCI.index(CCI[p210]) + 6] > DSI[CCI.index(CCI[p210]) + 4]:
                try:

                    run45 = 1
                    # print(newCCIGraph[CCI.index(CCI[p20]) + 18 + run35])
                    while run45 != 0:
                        if newCCIGraph[CCI.index(CCI[p210]) + 19 + run45] != "         B":
                            minValue = changeMinMax[CCI.index(CCI[p210]) + 18 + run45]
                            if "(" not in changeSlot[CCI.index(CCI[p210]) + 18 + run45] and minValue > lc5[
                                                CCI.index(CCI[p210]) + 19 + run45]:
                                dumbDataPattern[CCI.index(CCI[p210]) + 19 + run45] = "DB-"
                                changeSlot[CCI.index(CCI[p210]) + 18 + run45] = "DB"
                            run45 == 0
                            break
                        else:

                            minValue = changeMinMax[CCI.index(CCI[p210]) + 18 + run45]
                            if "(" not in changeSlot[CCI.index(CCI[p210]) + 18 + run45] and minValue < hp5[
                                                CCI.index(CCI[p210]) + 19 + run45]:
                                dumbDataPattern[CCI.index(CCI[p210]) + 19 + run45] = "DB+"
                                changeSlot[CCI.index(CCI[p210]) + 18 + run45] = "DB"
                                run45 == 0
                                break
                            else:
                                if SI[CCI.index(CCI[p210]) + 6 + run45] < DSI[CCI.index(CCI[p210]) + 4 + run45]:
                                    # print(SI[CCI.index(CCI[p20]) + 6 + run35])
                                    changeSlot[CCI.index(CCI[p210]) + 19 + run45] = "(DB)"
                                    dumbDataPattern[CCI.index(CCI[p210]) + 19 + run45] = dumbDataPattern[
                                        CCI.index(CCI[p210]) + 18 + run45]
                                    changeMinMax[CCI.index(CCI[p210]) + 19 + run45] = changeMinMax[
                                        CCI.index(CCI[p210]) + 18 + run45]
                                    run45 += 1
                                else:
                                    changeSlot[CCI.index(CCI[p210]) + 19 + run45] = changeSlot[
                                        CCI.index(CCI[p210]) + 18 + run45].strip("()")
                                    changeMinMax[CCI.index(CCI[p210]) + 19 + run45] = changeMinMax[
                                        CCI.index(CCI[p210]) + 18 + run45]

                                    dumbDataPattern[CCI.index(CCI[p210]) + 19 + run45] = dumbDataPattern[
                                        CCI.index(CCI[p210]) + 18 + run45]

                                    if "(" in changeSlot[CCI.index(CCI[p210]) + 18 + run45]:
                                        # print("true at: " + str(allminaThree[CCI.index(CCI[p20]) + 19 + run35]))
                                        if allminaThree[CCI.index(CCI[p210]) + 19 + run45] < changeMinMax[
                                                            CCI.index(CCI[p210]) + 18 + run45]:
                                            changeMinMax[CCI.index(CCI[p210]) + 19 + run45] = allMaxaThree[
                                                CCI.index(CCI[p210]) + 19 + run45]
                                    run45 += 1

                        print("DB")
                except:
                    print("levae")
    except:
        print()

maxValue = 0
for p111, p211 in zip(range(0, ((len(CCI) - 1) + 1)), range(1, (len(CCI) + 1))):
    try:
        if CCI[p111] < -100 and 0 > CCI[p211] > -100:
            datamovers[CCI.index(CCI[p211]) + 20] = "D->C"

            if SI[CCI.index(CCI[p211]) + 6] > DSI[CCI.index(CCI[p211]) + 4]:
                changeSlot[CCI.index(CCI[p211]) + 19] = "DC"
            else:
                changeSlot[CCI.index(CCI[p211]) + 19] = "(DC)"

            changeMinMax[CCI.index(CCI[p211]) + 19] = allMaxaThree[CCI.index(CCI[p211]) + 19]
            # print("maxa two is: " +str(maxaTwo[CCI.index(CCI[p211])+ 19]))
            # print("start from " + str(CCI[p111]) + "end till " + str(CCI[p211]))
            if SI[CCI.index(CCI[p211]) + 6] > DSI[CCI.index(CCI[p211]) + 4]:
                try:
                    run46 = 1
                    # print(newCCIGraph[CCI.index(CCI[p20]) + 18 + run35])
                    while run46 != 0:
                        if newCCIGraph[CCI.index(CCI[p211]) + 19 + run46] != "         C":
                            minValue = changeMinMax[CCI.index(CCI[p211]) + 18 + run46]
                            if "(" not in changeSlot[CCI.index(CCI[p211]) + 18 + run46] and minValue > lc5[
                                                CCI.index(CCI[p211]) + 19 + run46]:
                                dumbDataPattern[CCI.index(CCI[p211]) + 19 + run46] = "DC-"
                                changeSlot[CCI.index(CCI[p211]) + 18 + run46] = "DC"
                            run46 == 0
                            break
                        else:

                            minValue = changeMinMax[CCI.index(CCI[p211]) + 18 + run46]
                            if "(" not in changeSlot[CCI.index(CCI[p211]) + 18 + run46] and minValue < hp5[
                                                CCI.index(CCI[p211]) + 19 + run46]:
                                dumbDataPattern[CCI.index(CCI[p211]) + 19 + run46] = "DC+"
                                changeSlot[CCI.index(CCI[p211]) + 18 + run46] = "DC"
                                run46 == 0
                                break
                            else:
                                if SI[CCI.index(CCI[p211]) + 6 + run46] < DSI[CCI.index(CCI[p211]) + 4 + run46]:
                                    # print(SI[CCI.index(CCI[p20]) + 6 + run35])
                                    changeSlot[CCI.index(CCI[p211]) + 19 + run46] = "(DC)"
                                    dumbDataPattern[CCI.index(CCI[p211]) + 19 + run46] = dumbDataPattern[
                                        CCI.index(CCI[p211]) + 18 + run46]
                                    changeMinMax[CCI.index(CCI[p211]) + 19 + run46] = changeMinMax[
                                        CCI.index(CCI[p211]) + 18 + run46]
                                    run46 += 1
                                else:
                                    changeSlot[CCI.index(CCI[p211]) + 19 + run46] = changeSlot[
                                        CCI.index(CCI[p211]) + 18 + run46].strip("()")
                                    changeMinMax[CCI.index(CCI[p211]) + 19 + run46] = changeMinMax[
                                        CCI.index(CCI[p211]) + 18 + run46]

                                    dumbDataPattern[CCI.index(CCI[p211]) + 19 + run46] = dumbDataPattern[
                                        CCI.index(CCI[p211]) + 18 + run46]

                                    if "(" in changeSlot[CCI.index(CCI[p211]) + 18 + run46]:
                                        # print("true at: " + str(allminaThree[CCI.index(CCI[p20]) + 19 + run35]))
                                        if allminaThree[CCI.index(CCI[p211]) + 19 + run46] < changeMinMax[
                                                            CCI.index(CCI[p211]) + 18 + run46]:
                                            changeMinMax[CCI.index(CCI[p211]) + 19 + run46] = allMaxaThree[
                                                CCI.index(CCI[p211]) + 19 + run46]
                                    run46 += 1

                        print("DC")
                except:
                    print("levae")
    except:
        print()

     
for t56 in range(0, len(dumbDataPattern)):
    if dumbDataPattern[t56] == " ":
        dumbDataPattern[t56] = dumbDataPattern[t56 - 1]

freeCell = []
for g35 in range(0, len(data2)):
    freeCell.append(" ")

for df in changeMinMax:
    if df == 1:
        changeMinMax[changeMinMax.index(df)] = " "

for gfd in changeSlot:
    if gfd == 1:
        changeSlot[changeSlot.index(gfd)] = " "


lumsum=[]
for dsa in range(0,len(dumbDataPattern)):
    try:
        if dumbDataPattern[dsa]==dumbDataPattern[dsa+1]:
            lumsum.append("True")
        else:
            lumsum.append("False")

    except:
        print(" ")


commonDataChunks=[]
for rew in range(0,len(lumsum)):
    if lumsum[rew] =="False":
        commonDataChunks.append(rew)

# for tre1, tre2 in zip(commonDataChunks[0::], commonDataChunks[1::]):
#     print(str(tre1)+ "the " + str(tre2))
#     for cat22 in range(tre1,tre2):
#         tempchangeslot = changeSlot[cat22]
#         try:
#             looper = 1
#             while looper !=tre2-tre1:
#                 # if changeSlot[cat22 + looper] == tempchangeslot or  changeSlot[cat22 + looper].strip("()") == tempchangeslot:
#                 #     print(changeMinMax[cat22])
#                 #     if changeMinMax[cat22]<changeMinMax[cat22 + looper]:
#                 #         changeMinMax[cat22 + looper] =changeMinMax[cat22]
#                 #         break
#                 #     looper==0
#                 # else:
#                 #     looper+=1
#
#                 print(changeSlot[cat22 + looper])
#                 looper+=1
#
#
#
#
#         except:
#             print(" ")


for tre1, tre2 in zip(commonDataChunks[0::], commonDataChunks[1::]):
    print(str(tre1) + "the " + str(tre2))
    for cat22 in range(tre1, tre2):
        tempchangeslot = changeSlot[cat22]
        try:
            for cat23 in range(tre1+1,tre2+1):
                if changeSlot[cat23] == tempchangeslot or changeSlot[cat23].strip("()") == tempchangeslot:
                    if changeMinMax[cat22] < changeMinMax[cat23]:
                        changeMinMax[cat23] = changeMinMax[cat22]
        except:
            print(" ")




# catch22 = 1
# while dumbDataPattern:
#     if dumbDataPattern[catch22 -1] == dumbDataPattern[catch22]:
#         print(str(dumbDataPattern[catch22 -1]) + "till" + str(dumbDataPattern[catch22]))
#         catch22+=1
#     else:
#         catch22=catch22


# for dsa in range(0, len(dumbDataPattern)):
#     if dumbDataPattern[dsa]==" ":
#         break
#     else:
#         if dumbDataPattern[dsa] == dumbDataPattern[dsa+1]:
#             print("true")
#         else:
#             print("false")



# get data from last cell of date
# print(data2.iat[-1,0])



# dat7 = pd.DataFrame(result3)
# dat8 = pd.DataFrame(newdatatrue)
# dat8.columns = ['Data True']
# result4 = dat7.join(dat8)


# for few in changeSlot:
#     if few == " ":
#         print(" ")
#     else:
#         if dumbDataPattern[changeSlot.index(few)] ==dumbDataPattern[changeSlot.index(few)-1]:
#             changeSlot[changeSlot.index(few)+1]= changeSlot[changeSlot.index(few)]






dat7 = pd.DataFrame(data2)
dat8 = pd.DataFrame(newdatatrue)
dat8.columns = ['Data true']
result1A = dat7.join(dat8)

dat9a = pd.DataFrame(result1A)
dat10a = pd.DataFrame(freeCell)
dat10a.columns = [' ']
result2A = dat9a.join(dat10a)

dat11a = pd.DataFrame(result2A)
dat12a = pd.DataFrame(newCCI)
dat12a.columns = ['CCI']
result3A = dat11a.join(dat12a)

dat13a = pd.DataFrame(result3A)
dat14a = pd.DataFrame(freeCell)
dat14a.columns = ['  ']
result4A = dat13a.join(dat14a)

dat15a = pd.DataFrame(result4A)
dat16a = pd.DataFrame(newSI)
dat16a.columns = ['K']
result5A = dat15a.join(dat16a)

dat17a = pd.DataFrame(result5A)
dat18a = pd.DataFrame(newDSI)
dat18a.columns = ['D']
result6a = dat17a.join(dat18a)

dat19a = pd.DataFrame(result6a)
dat20a = pd.DataFrame(freeCell)
dat20a.columns = ['    ']
result7A = dat19a.join(dat20a)

dat9 = pd.DataFrame(result7A)
dat10 = pd.DataFrame(rd)
dat10.columns = ['RD']
result5 = dat9.join(dat10)

dat11 = pd.DataFrame(result5)
dat12 = pd.DataFrame(rc)
dat12.columns = ['RC']
result6 = dat11.join(dat12)

dat13 = pd.DataFrame(result6)
dat14 = pd.DataFrame(rb)
dat14.columns = ['RB']
result7 = dat13.join(dat14)

dat15 = pd.DataFrame(result7)
dat16 = pd.DataFrame(ra)
dat16.columns = ['RA']
result8 = dat15.join(dat16)

dat17 = pd.DataFrame(result8)
dat18 = pd.DataFrame(nu)
dat18.columns = ['NU']
result9 = dat17.join(dat18)

dat19 = pd.DataFrame(result9)
dat20 = pd.DataFrame(nd)
dat20.columns = ['ND']
result10 = dat19.join(dat20)

dat21 = pd.DataFrame(result10)
dat22 = pd.DataFrame(sa)
dat22.columns = ['SA']
result11 = dat21.join(dat22)

dat23 = pd.DataFrame(result11)
dat24 = pd.DataFrame(sb)
dat24.columns = ['SB']
result12 = dat23.join(dat24)

dat25 = pd.DataFrame(result12)
dat26 = pd.DataFrame(sc)
dat26.columns = ['SC']
result13 = dat25.join(dat26)

dat27 = pd.DataFrame(result13)
dat28 = pd.DataFrame(sd)
dat28.columns = ['SD']
result14 = dat27.join(dat28)

dat21a = pd.DataFrame(result14)
dat22a = pd.DataFrame(freeCell)
dat22a.columns = ['     ']
result8A = dat21a.join(dat22a)

dat29 = pd.DataFrame(result8A)
dat30 = pd.DataFrame(maxaOne)
dat30.columns = ['Maxa One']
result15 = dat29.join(dat30)

dat31 = pd.DataFrame(result15)
dat32 = pd.DataFrame(minaOne)
dat32.columns = ['Mina One']
result16 = dat31.join(dat32)

# dat23a = pd.DataFrame(result16)
# dat24a = pd.DataFrame(freeCell)
# dat24a.columns = ['      ']
# result9A = dat23a.join(dat24a)



dat37 = pd.DataFrame(result16)
dat38 = pd.DataFrame(maxaTwo)
dat38.columns = ['Maxa Two']
result19 = dat37.join(dat38)

dat39 = pd.DataFrame(result19)
dat40 = pd.DataFrame(minaTwo)
dat40.columns = ['Mina Two']
result20 = dat39.join(dat40)

dat43 = pd.DataFrame(result20)
dat44 = pd.DataFrame(allMaxaThree)
dat44.columns = ['Maxa Two new']
result22 = dat43.join(dat44)

dat45 = pd.DataFrame(result22)
dat46 = pd.DataFrame(allminaThree)
dat46.columns = ['Mina Two new']
result23 = dat45.join(dat46)

dat25a = pd.DataFrame(result23)
dat26a = pd.DataFrame(freeCell)
dat26a.columns = ['           ']
result10A = dat26a.join(dat25a)

dat33 = pd.DataFrame(result10A)
dat34 = pd.DataFrame(newCCIGraph)
dat34.columns = ['CCI Region']
result17 = dat33.join(dat34)

dat35 = pd.DataFrame(result17)
dat36 = pd.DataFrame(dotcate)
dat36.columns = ['Dot Pattern']
result18 = dat35.join(dat36)

# dat47 = pd.DataFrame(result21)
# dat48 = pd.DataFrame(maxminPattern)
# dat48.columns = ['Min Max']
# result24 = dat47.join(dat48)


# dat49 = pd.DataFrame(result24)
# dat50 = pd.DataFrame(datamovers)
# dat50.columns = ['DATA MOVERS']
# result25 = dat49.join(dat50)


dat49 = pd.DataFrame(result18)
dat50 = pd.DataFrame(changeSlot)
dat50.columns = ['DATA MOVERS']
result25 = dat49.join(dat50)

dat51 = pd.DataFrame(result25)
dat52 = pd.DataFrame(changeMinMax)
dat52.columns = ['Change Min Max']
result26 = dat51.join(dat52)

# dat1 = pd.DataFrame(data2)
# dat2 = pd.DataFrame(newCCI)
# dat2.columns = ['CCI']
# result1 = dat1.join(dat2)


# dat3 = pd.DataFrame(result1)
# dat4 = pd.DataFrame(newSI)
# dat4.columns = ['K']
# result2 = dat3.join(dat4)


# dat5 = pd.DataFrame(result2)
# dat6 = pd.DataFrame(newDSI)
# dat6.columns = ['D']
# result3 = dat5.join(dat6)









dat41 = pd.DataFrame(result26)
dat42 = pd.DataFrame(dumbDataPattern)
dat42.columns = ['Data pattern']
result21 = dat41.join(dat42)


dat88 = pd.DataFrame(result21)
dat89 = pd.DataFrame(lumsum)
dat89.columns = ['Lumsum']
result88 = dat88.join(dat89)


df1 = pd.DataFrame(result88)
writer = pd.ExcelWriter('resultFinal.xlsx', engine='xlsxwriter')
df1.to_excel(writer, sheet_name='Sheet1')
worksheet = writer.sheets['Sheet1']
worksheet.set_column('B:B', 12)
worksheet.set_column('C:C', 10)
worksheet.set_column('D:D', 10)
worksheet.set_column('E:E', 10)
worksheet.set_column('F:F', 10)
worksheet.set_column('G:G', 10)
worksheet.set_column('H:H', 10)
worksheet.set_column('I:I', 10)
worksheet.set_column('J:J', 10)
worksheet.set_column('K:K', 10)
worksheet.set_column('L:L', 10)
worksheet.set_column('M:M', 10)
worksheet.set_column('N:N', 10)
worksheet.set_column('O:O', 10)
worksheet.set_column('P:P', 10)
worksheet.set_column('Q:Q', 10)
worksheet.set_column('R:R', 10)
worksheet.set_column('S:S', 10)
worksheet.set_column('T:T', 10)
worksheet.set_column('U:U', 10)
worksheet.set_column('V:V', 12)
worksheet.set_column('W:W', 12)
worksheet.set_column('X:X', 12)
writer.save()
