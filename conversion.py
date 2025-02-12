def bin_to_dec(bin):
    bin=bin[::-1]
    dec=0
    j=0
    for i in bin:
        dec+=int(i)*((2)**j)
        j+=1
    return dec

def dec_to_bin(dec):
    bin=""
    while dec!=0:
        bin+=str(dec%2)
        dec//=2
    return bin[::-1]
