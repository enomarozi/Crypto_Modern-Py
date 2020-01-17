import deslibPy

def encrypt():
    text = "01 23 45 67 89 ab cd ef".split(" ")
    key = "13 34 57 79 9B BC DF F1".split(" ")
    #binary_text = "".join([format(ord(i),"b").rjust(8,"0") for i in text]) #for text = ascii
    binary_text = "".join([bin(int(i,16))[2:].rjust(8,"0") for i in text]) #for text = hexa
    binary_key = "".join([bin(int(i,16))[2:].rjust(8,"0") for i in key])
    IPx = "".join(binary_text[i-1] for i in deslibPy.IP)
    L0R0 = [IPx[:i][-32:] for i in range(32,len(IPx)+32,32)]
    PC1 = "".join(binary_key[i-1] for i in deslibPy.PC1)
    C0D0 = [PC1[:i][-28:] for i in range(28,len(PC1)+28,28)]
    Cx0x = []
    for i in C0D0:
        Cx0x.append([[i[-len(i)+j:]+i[:j]][:28] for j in deslibPy.Shift])
    c1d1 = []
    for i in range(16):
        proses = "".join(Cx0x[0][:28][i])+"".join(Cx0x[1][:28][i])
        c1d1.append("".join(proses[j-1] for j in deslibPy.PC2))
        
    R0 = [L0R0[1]]
    ExpansR1 = "".join([R0[0][i-1] for i in deslibPy.Expans])
    A1 = "".join(str(int(c1d1[0][i])^int(ExpansR1[i])) for i in range(48))
    resultA1 = [A1[:i][-6:] for i in range(6,len(A1)+6,6)]
    prosesA1 = []
    for i in range(len(resultA1)):
        prosesA1.append(str(i+1)+resultA1[i])
    sboxA1 = ""
    for i in prosesA1:
        sboxA1 += "".join([bin(int(deslibPy.Sbox[j]))[2:].rjust(4,"0") for j in deslibPy.Sbox.keys() if i == j])
    pboxA1 = "".join(sboxA1[i-1] for i in deslibPy.Pbox)
    R1 = "".join(str(int(L0R0[0][i])^int(pboxA1[i])) for i in range(32))
    R0.append(R1)
    
    for ex in range(15):
        ExpansR = "".join([R0[1+ex][i-1] for i in deslibPy.Expans])
        A = "".join(str(int(c1d1[1+ex][i])^int(ExpansR[i])) for i in range(48))
        resultA = [A[:i][-6:] for i in range(6,len(A)+6,6)]
        prosesA = []
        for i in range(len(resultA)):
            prosesA.append(str(i+1)+resultA[i])
        sboxA = ""
        for i in prosesA:
            sboxA += "".join([bin(int(deslibPy.Sbox[j]))[2:].rjust(4,"0") for j in deslibPy.Sbox.keys() if i == j])
        pboxA = "".join(sboxA[i-1] for i in deslibPy.Pbox)
        All_R = "".join(str(int(R0[0+ex][i])^int(pboxA[i])) for i in range(32))
        R0.append(All_R)
    R16L16 = R0[16]+R0[15]
    proses_enc = "".join([R16L16[i-1] for i in deslibPy.InitP])
    print("Encryption :")
    print("Binary --> "+" ".join(proses_enc[:j][-8:] for j in range(8,len(proses_enc)+8,8)))
    print("Hex    --> "+" ".join(hex(int(proses_enc[:j][-8:],2))[2:].rjust(2,"0") for j in range(8,len(proses_enc)+8,8)))
    print("Binary --> "+" ".join(chr(int(proses_enc[:j][-8:],2)) for j in range(8,len(proses_enc)+8,8)))

encrypt()
