import sys
input_file=sys.argv[1]
output_file=sys.argv[2]
def file_read(file_name):
    with open (file_name,"r") as f:
        data=f.readlines()
    for i in range(len(data)):
        data[i]=data[i].strip("\n")
    return data

def hex_to_dec(s):
    n=0
    x=0
    s=s[2:]
    s=s[::-1]
    for i in s:
        n+=int(i)((16)*x)
        x+=1
    return n

def sign_extend_to_32(binary):
    """Extends an n-bit binary number to 32 bits using sign extension."""
    n=len(binary)
    if n>=32:
        return binary
    sign_bit=binary[0]  
    extension=sign_bit*(32-n) 
    ans=extension+binary 
    return ans

def bin_to_dec_unsigned(binary):
    return int(binary, 2) 

def bin_to_dec(binary):
    n=len(binary)
    if binary[0]=='1': 
        decimal=int(binary, 2)-(1<<n) 
    else:
        decimal=int(binary, 2)
    return decimal

def dec_to_bin(decimal, bits=32):
    """Converts a decimal number to an n-bit binary string with two's complement for negatives."""
    if decimal<0:  
        decimal=(1<<bits)+decimal  
    return format(decimal, f'0{bits}b') 

registers = { "00000" : 0,
              "00001" : 0,
              "00010" : 380,
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
          "0x0001000C" : 0,
          "0x00010010" : 0,
          "0x00010014" : 0,
          "0x00010018" : 0, 
          "0x0001001C" : 0,
          "0x00010020" : 0,
          "0x00010024" : 0,
          "0x00010028" : 0, 
          "0x0001002C" : 0,
          "0x00010030" : 0,
          "0x00010034" : 0,
          "0x00010038" : 0, 
          "0x0001003C" : 0,
          "0x00010040" : 0,
          "0x00010044" : 0,
          "0x00010048" : 0, 
          "0x0001004C" : 0,
          "0x00010050" : 0,
          "0x00010054" : 0,
          "0x00010058" : 0, 
          "0x0001005C" : 0,
          "0x00010060" : 0,
          "0x00010064" : 0,
          "0x00010068" : 0, 
          "0x0001006C" : 0,
          "0x00010070" : 0,
          "0x00010074" : 0,
          "0x00010078" : 0, 
          "0x0001007C" : 0 }

def r_type(line,PC,output_file):
    rd = line[20:25]
    rs1 = line[12:17]
    rs2 = line[7:12]
    func7 = line[0:7]
    func3 = line[17:20]
    #sub
    if func7=='0100000':
        registers[rd]=bin_to_dec_unsigned(dec_to_bin(registers[rs1]-registers[rs2]))
    #add
    elif func3=="000":
        registers[rd]=bin_to_dec_unsigned(dec_to_bin(registers[rs1]+registers[rs2]))
    #slt
    elif func3=="010":
        if registers[rs1]<registers[rs2]:
            registers[rd]=1
        else:
            registers[rd]=0
    #srl
    elif func3=="101":
        x=dec_to_bin(registers[rs1])
        registers[rd]=bin_to_dec_unsigned(("0"*registers[rs2])+x[:(-registers[rs2]-1)])
    #or
    elif func3=="110":
        registers[rd]=bin_to_dec_unsigned(dec_to_bin(registers[rs1] | registers[rs2]))
    #and
    elif func3=="111":
        registers[rd]=bin_to_dec_unsigned(dec_to_bin(registers[rs1] & registers[rs2]))
    PC += 4
    return PC

def j_type(line,PC):
    #jal
    rd=line[20:25]
    imm=bin_to_dec(line[0]+line[12:20]+line[11]+line[1:11]+"0")
    registers[rd]=PC+4
    PC+=imm
    return PC

def i_type(line,PC,output_file):
    opcode=line[25:32]
    rd=line[20:25] # Bits (11:7)
    func3=line[17:20] # Bits (14:12)
    rs1=line[12:17]       # Bits (19:15)
    imm=line[0:12]
    imm=sign_extend_to_32(imm)
    decimm=bin_to_dec(imm)
    #addi
    if func3=="000" and opcode=="0010011":
        #PC=PC+4
        ans=registers[rs1]+decimm
        ans=dec_to_bin(ans)
        registers[rd]=bin_to_dec_unsigned(ans)
        PC += 4
    #lw
    elif func3=="010" and opcode=="0000011":
        #PC=PC+4
        ans=registers[rs1]+decimm
        ans= format(ans, '#010x').lower()
        registers[rd]=memory.get(ans, 0)
        PC += 4
    #jalr
    elif opcode=="1100111":
        rd=line[20:25]
        if rd!="00000":registers[rd]=PC+4
        PC=registers[rs1]+decimm
    return PC

def s_type(line,PC,output_file):
    rs1 = line[12:17]
    rs2 = line[7:12]
    imm = line[0:7] + line[20:25]
    imm = sign_extend_to_32(imm)
    decimm = bin_to_dec(imm)
    #sw
    address_dec= registers[rs1] + decimm
    final_address= f"0x{(address_dec):08x}"
    # if final_address in memory:
    memory[final_address] = registers[rs2]
    PC += 4
    return PC
    # else:
    #     print(final_address)
    #     print("invalid memory location")
    #     return -1

def b_type(line,PC,output_file):
    func=line[17:20]
    rs1=line[12:17]
    rs2=line[7:12]
    imm=bin_to_dec(line[0]+line[24]+line[1:7]+line[20:24]+"0")
    #beq
    if func=="000" and registers[rs1]==registers[rs2]:
        PC+=imm
    #bne
    elif func=="001" and registers[rs1]!=registers[rs2]:
        PC+=imm
    else:
        PC+=4
    
    return PC

def writepc(PC,output_file):
    with open(output_file,"a") as f:
        f.write(str(PC))
        f.write(" ")
    return

def writepcbin(PC,output_file):
    with open(output_file,"a") as f:
        f.write("0b")
        f.write(sign_extend_to_32(dec_to_bin((PC))))
        f.write(" ")
    return

def displaybin(PC,registers,output_file):
    with open(output_file,"a") as f:
        writepcbin(PC,output_file)
        for key in registers:
            f.write("0b")
            f.write(str(sign_extend_to_32(dec_to_bin(registers[key]))))
            f.write(" ")
        f.write("\n")

def main():
    input_file=sys.argv[1]
    output_file=sys.argv[2]
    lines=file_read(input_file)
    PC=0
    # flag=0
    with open(output_file,"w") as f:
        f.write("")
    with open(output_file,"a") as f:
        while(lines[(PC//4)]!="00000000000000000000000001100011"):
            line=lines[(PC//4)]
            if line[25:]=="0110011":
                PC = r_type(line,PC,output_file)
            if line[25:]=="1101111":
                PC=j_type(line,PC)
            if line[25:]=="0010011" or line[25:]=="1100111" or line[25:]=="0000011":
                PC = i_type(line,PC,output_file)
            if line[25:]=="0100011":
                PC = s_type(line,PC,output_file)
                if PC==-1:
                    break
            if line[25:]=="1100011":
                PC=b_type(line,PC,output_file)
            displaybin(PC,registers,output_file)
        displaybin(PC,registers,output_file)
        for i in memory:
            if int(i,16) >= 65536 :
                f.write(i)
                f.write(":")
                f.write("0b")
                f.write(sign_extend_to_32(dec_to_bin(memory[i])))
                f.write("\n")
main()
