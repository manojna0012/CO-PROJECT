def file_read(file_name):
    with open (file_name,"r") as f:
        data=f.readlines()
    for i in range(len(data)):
        data[i]=data[i].strip("\n")
    return data
def twos_comp(n):
    s=str(n)
    snew=""
    for i in s:
        if i=="0":
            snew+="1"
        else: 
            snew+="0"
    sint=int(snew)
    sint+=1
    return sint
def dec_to_bin(n):
    s=""
    if n==0:
        return "0"
    while n!=0:
        s+=str(n%2)
        n//=2
    return s[::-1]
def bin_to_dec(s):
    n=0
    x=0
    s=s[::-1]
    for i in s:
        n+=int(i)*((2)**x)
        x+=1
    return n
registers = { "00000" : 0,
              "00001" : 0,
              "00010" : 0,
              "00011" : 0, 
              "00100" : 0,
              "00101" : 0,
              "00110" : 0,
              "00111" : 0,
              "01000" : 0,  
              "01001" : 0,
              "01010" : 0, 
              "01011" : 0, 
              "01100" : 0, 
              "01101" : 0, 
              "01110" : 0,
              "01111" : 0, 
              "10000" : 0, 
              "10001" : 0, 
              "10010" : 0, 
              "10011" : 0, 
              "10100" : 0, 
              "10101" : 0, 
              "10110" : 0, 
              "10111" : 0, 
              "11000" : 0, 
              "11001" : 0, 
              "11010" : 0, 
              "11011" : 0, 
              "11100" : 0, 
              "11101" : 0, 
              "11110" : 0, 
              "11111" : 0}
memory = {"0x00010000" : 0,
          "0x00010004" : 0,
          "0x00010008" : 0, 
          "0x0001000c" : 0,
          "0x00010010" : 0,
          "0x00010014" : 0,
          "0x00010018" : 0, 
          "0x0001001c" : 0,
          "0x00010020" : 0,
          "0x00010024" : 0,
          "0x00010028" : 0, 
          "0x0001002c" : 0,
          "0x00010030" : 0,
          "0x00010034" : 0,
          "0x00010038" : 0, 
          "0x0001003c" : 0,
          "0x00010040" : 0,
          "0x00010044" : 0,
          "0x00010048" : 0, 
          "0x0001004c" : 0,
          "0x00010050" : 0,
          "0x00010054" : 0,
          "0x00010058" : 0, 
          "0x0001005c" : 0,
          "0x00010060" : 0,
          "0x00010064" : 0,
          "0x00010068" : 0, 
          "0x0001006c" : 0,
          "0x00010070" : 0,
          "0x00010074" : 0,
          "0x00010078" : 0, 
          "0x0001007c" : 0 }

def r_type(line):
    rd = line[20:25]
    rs1 = line[12:17]
    rs2 = line[7:12]
    func7 = line[0:7]
    func3 = line[17:20]
    #sub
    if func7=='0100000':
        registers[rd]=registers[rs1]-registers[rs2]
    #add
    elif func3=="000":
        registers[rd]=registers[rs1]+registers[rs2]
    #slt
    elif func3=="010":
        if registers[rs1]<registers[rs2]:
            registers[rd]=1
        else:
            registers[rd]=0
    #srl
    elif func3=="101":
        x=bin_to_dec(str(int(dec_to_bin(registers[rs2]))%100000))
        registers[rd]=registers[rs1]*(2**x)
    #or
    elif func3=="110":
        bin1=dec_to_bin(registers[rs1])
        bin2=dec_to_bin(registers[rs2])
        if len(bin1)>len(bin2):
            bin2=("0"*(len(bin1)-len(bin2)))+bin2
        else:
            bin1=("0"*(len(bin2)-len(bin1)))+bin1
        ans=""
        for i in range(len(bin1)):
            if bin1[i]=="1" or bin2[i]=="1":
                ans+="1"
            else:
                ans+="0"
        registers[rd]=bin_to_dec(ans)
    #and
    elif func3=="111":
        bin1=dec_to_bin(registers[rs1])
        bin2=dec_to_bin(registers[rs2])
        if len(bin1)>len(bin2):
            bin2=("0"*(len(bin1)-len(bin2)))+bin2
        else:
            bin1=("0"*(len(bin2)-len(bin1)))+bin1
        ans=""
        for i in range(len(bin1)):
            if bin1[i]=="1" and bin2[i]=="1":
                ans+="1"
            else:
                ans+="0"
        registers[rd]=bin_to_dec(ans)
def j_type(line,PC):
    rd=line[20:25]
    imm=bin_to_dec(line[0]+line[12:20]+line[11]+line[1:11]+"0")
    temp=PC+1
    for i in memory:
        if temp==0:
            break
        temp-=1
    registers[rd]=i#it is in hex!!!!!!!!!!!!!!!!!!!!!
    PC+=imm/4
    # for i in memory:
    #     if PC==0:
    #         break
    #     PC-=1
    return PC
def main():
    input_file="input.txt"
    lines=file_read(input_file)
    PC=0
    flag=0
    update=PC
    for line in lines:
        if line!="00000000000000000000000001100011" and flag==0:
            PC+=1
            update+=1
            if line[25:]=="0110011":
                r_type(line)
            if line[25:]=="1101111":
                update=j_type(line,PC)
                flag=1
        elif line!="00000000000000000000000001100011" and flag==1:
            PC+=1
        else:
            break
        if update==PC:
            flag=0
main()
