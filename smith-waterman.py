import numpy as np
import sys
S1=""
S2=""
def PointFind(word):
    a = "a"
    if (word) in PamScore:
        a = PamScore[word]
    else:
        word = list(word)
        word.reverse()
        word = ''.join(map(str, word))
        a = PamScore[word]
    return a

#screen write
def PrintMatris(matrix, seq1,seq2):
    print("   ", end="")
    for i in seq1:
        print("  ", i, end="", sep="")
    print("\n---","---"*len(seq1), sep="")
    for i in range(0, len(seq2)):
        print(seq2[i],"|", end="")
        for j in range(0, len(seq1)):
            print("{:3}".format(matrix[j][i]), end="", sep="")
        print()

def SeqBack(x,y):
    global S1,S2
    if x == 0 or y == 0:
        print("\n","match is over!")
    if PointMatrisLocation[x][y] == "z":
        print("Tek eşleşen var o da:")
    elif PointMatrisLocation[x][y] == "c":
        S1+=seq1[x]
        S2+=seq2[y]
        x-=1
        y-=1
        SeqBack(x,y)
    elif PointMatrisLocation[x][y] == "u":
        S1+="-"
        S2+=seq2[y]
        y-=1
        SeqBack(x,y)
    elif PointMatrisLocation[x][y] == "l":
        S2+="-"
        S1+=seq1[x]
        x-=1
        SeqBack(x,y)
    return S1,S2

#pam250
PamScore = {'AA': 2, 'RA': -2, 'RR': 6, 'NA': 0, 'NR': 0, 'NN': 2, 'DA': 0, 'DR': -1, 'DN': 2, 'DD': 4, 'CA': -2, 'CR': -4, 'CN': -4, 'CD': -5, 'CC': 12, 'QA': 0, 'QR': 1, 'QN': 1, 'QD': 2, 'QC': -5, 'QQ': 4, 'EA': 0, 'ER': -1, 'EN': 1, 'ED': 3, 'EC': -5, 'EQ': 2, 'EE': 4, 'GA': 1, 'GR': -3, 'GN': 0, 'GD': 1, 'GC': -3, 'GQ': -1, 'GE': 0, 'GG': 5, 'HA': -1, 'HR': 2, 'HN': 2, 'HD': 1, 'HC': -3, 'HQ': 3, 'HE': 1, 'HG': -2, 'HH': 6, 'IA': -1, 'IR': -2, 'IN': -2, 'ID': -2, 'IC': -2, 'IQ': -2, 'IE': -2, 'IG': -3, 'IH': -2, 'II': 5, 'LA': -2, 'LR': -3, 'LN': -3, 'LD': -4, 'LC': -6, 'LQ': -2, 'LE': -3, 'LG': -4, 'LH': -2, 'LI': -2, 'LL': 6, 'KA': -1, 'KR': 3, 'KN': 1, 'KD': 0, 'KC': -5, 'KQ': 1, 'KE': 0, 'KG': -2, 'KH': 0, 'KI': -2, 'KL': -3, 'KK': 5, 'MA': -1, 'MR': 0, 'MN': -2, 'MD': -3, 'MC': -5, 'MQ': -1, 'ME': -2, 'MG': -3, 'MH': -2, 'MI': 2, 'ML': 4, 'MK': 0, 'MM': 6, 'FA': -3, 'FR': -4, 'FN': -3, 'FD': -6, 'FC': -4, 'FQ': -5, 'FE': -5, 'FG': -5, 'FH': -2, 'FI': 1, 'FL': 2, 'FK': -5, 'FM': 0, 'FF': 9, 'PA': 1, 'PR': 0, 'PN': 0, 'PD': -1, 'PC': -3, 'PQ': 0, 'PE': -1, 'PG': 0, 'PH': 0, 'PI': -2, 'PL': -3, 'PK': -1, 'PM': -2, 'PF': -5, 'PP': 6, 'SA': 1, 'SR': 0, 'SN': 1, 'SD': 0, 'SC': 0, 'SQ': -1, 'SE': 0, 'SG': 1, 'SH': -1, 'SI': -1, 'SL': -3, 'SK': 0, 'SM': -2, 'SF': -3, 'SP': 1, 'SS': 2, 'TA': 1, 'TR': -1, 'TN': 0, 'TD': 0, 'TC': -2, 'TQ': -1, 'TE': 0, 'TG': 0, 'TH': -1, 'TI': 0, 'TL': -2, 'TK':
            0, 'TM': -1, 'TF': -3, 'TP': 0, 'TS': 1, 'TT': 3, 'WA': -6, 'WR': 2, 'WN': -4, 'WD': -7, 'WC': -8, 'WQ': -5, 'WE': -7, 'WG': -7, 'WH': -3, 'WI': -5, 'WL': -2, 'WK': -3, 'WM': -4, 'WF': 0, 'WP': -6, 'WS': -2, 'WT': -5, 'WW': 17, 'YA': -3, 'YR': -4, 'YN': -2, 'YD': -4, 'YC': 0, 'YQ': -4, 'YE': -4, 'YG': -5, 'YH': 0, 'YI': -1, 'YL': -1, 'YK': -4, 'YM': -2, 'YF': 7, 'YP': -5, 'YS': -3, 'YT': -3, 'YW': 0, 'YY': 10, 'VA': 0, 'VR': -2, 'VN': -2, 'VD': -2, 'VC': -2, 'VQ': -2, 'VE': -2, 'VG': -1, 'VH': -2, 'VI': 4, 'VL': 2, 'VK': -2, 'VM': 2, 'VF': -1, 'VP': -1, 'VS': -1, 'VT': 0, 'VW': -6, 'VY': -2, 'VV': 4}
#sequence FASTA al
seq1, seq2 = "CCWW", "CWEEW"
Gap = -11

#başlarına 0 ekledim ki ilk satırları 0 ile doldurayım
seq1 = '0' + seq1
seq2 = '0' + seq2
#print(seq1, seq2)

#matrisler tanimlandi birinisi puan ikincisi yon
PointMatris = np.zeros((len(seq1), len(seq2)), int)
PointMatrisLocation = np.zeros((len(seq1), len(seq2)), (str,3))

indel = False

for i in range(1, len(seq1)):
    for j in range(1, len(seq2)):
        word = seq1[i]+seq2[j]
        point = PointFind(word)
        #leftSide
        LeftPoint = PointMatris[i-1][j]+Gap
        #upSide
        UpPoint = PointMatris[i][j-1]+Gap
        #crossSide
        CrossSide = PointMatris[i-1][j-1]+point
        #Point save
        point2 = max(LeftPoint, UpPoint, CrossSide, 0)
        #location save
        if point2 == 0:
            PointMatrisLocation[i][j] = "z"
            PointMatris[i][j] = point2
        elif point2 == CrossSide:
            PointMatrisLocation[i][j] = "c"
            PointMatris[i][j] = point2
            indel = False
        elif point2 == UpPoint:
            if indel == False:
                PointMatris[i][j] = point2
                indel = True
            else:
                PointMatris[i][j] = point2-1-Gap #genisletme cezasi
            PointMatrisLocation[i][j] = "u"
        elif point2 == LeftPoint:
            if indel == False:
                PointMatris[i][j] = point2
                indel = True
            else:
                PointMatris[i][j] = point2-1-Gap #genisletme cezasi
            PointMatrisLocation[i][j] = "l"

MaximumPoint = np.amax(PointMatris) #max değeri bulduk
result = np.where(PointMatris == MaximumPoint)
if type(result[0]) is list:
    maxX = int(result[0][0])
    maxY = int(result[1][0])
else:
    maxX = int(result[0])
    maxY = int(result[1])
#eslesenleri artik aliyoruz

PrintMatris(PointMatris,seq1,seq2)
Ss1,Ss2 = SeqBack(maxX,maxY)

print("\nGen1 Uzunluk:",len(seq1))
print("Gen2 Uzunluk:",len(seq2))
print("\nGen hizalama sonucu:")
print("Gen1:",Ss1 )
print("Gen1:",Ss2 )
match = 0
unmatch = 0
gap = 0
for i in range(0, len(Ss2)):
    if Ss1[i] == Ss2[i]:
        match += 1
    elif Ss1[i] == "-" and Ss2[i] == "-" :
        unmatch += 1
    else:
        gap += 1

print("\nEslesme sayisi:", match)
print("Eslesmeme sayisi:", unmatch)
print("Bosluk sayisi:", gap)

f = open("Output.txt", "a")
f.write("\nGen1 Uzunluk:"+str(len(seq1))+"\n")
f.write("Gen2 Uzunluk:"+str(len(seq2))+"\n")
f.write("\nGen hizalama sonucu:+\n")
f.write("Gen1:"+str(Ss1) +"\n")
f.write("Gen1:"+str(Ss2)+"\n")
f.write("\nEslesme sayisi:"+ str(match)+"\n")
f.write("Eslesmeme sayisi:"+ str(unmatch)+"\n")
f.write("Bosluk sayisi:"+ str(gap)+"\n")
f.close()
