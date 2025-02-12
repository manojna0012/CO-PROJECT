register = {
  "zero": "00000",
  "ra": "00001",
  "sp": "00010",
  "gp": "00011",
  "tp": "00100",
  "t0": "00101",
  "t1": "00110",
  "t2": "00111",
  "s0": "01000",
  "fp": "01000",
  "s1": "01001",
  "a0": "01010",
  "a1": "01011",
  "a2": "01100",
  "a3": "01101",
  "a4": "01110",
  "a5": "01111",
  "a6": "10000",
  "a7": "10001",
  "s2": "10010",
  "s3": "10011",
  "s4": "10100",
  "s5": "10101",
  "s6": "10110",
  "s7": "10111",
  "s8": "11000",
  "s9": "11001",
  "s10": "11010",
  "s11": "11011",
  "t3": "11100",
  "t4": "11101",
  "t5": "11110",
  "t6": "11111"
}


r_type_instructions = {
    "add": {"opcode": "0110011", "rd": "", "funct3": "000", "rs1": "", "rs2": "", "funct7": "0000000"},
    "sub": {"opcode": "0110011", "rd": "", "funct3": "000", "rs1": "", "rs2": "", "funct7": "0100000"},
    "sll": {"opcode": "0110011", "rd": "", "funct3": "001", "rs1": "", "rs2": "", "funct7": "0000000"},
    "slt": {"opcode": "0110011", "rd": "", "funct3": "010", "rs1": "", "rs2": "", "funct7": "0000000"},
    "sltu": {"opcode": "0110011", "rd": "", "funct3": "011", "rs1": "", "rs2": "", "funct7": "0000000"},
    "xor": {"opcode": "0110011", "rd": "", "funct3": "100", "rs1": "", "rs2": "", "funct7": "0000000"},
    "srl": {"opcode": "0110011", "rd": "", "funct3": "101", "rs1": "", "rs2": "", "funct7": "0000000"},
    "or": {"opcode": "0110011", "rd": "", "funct3": "110", "rs1": "", "rs2": "", "funct7": "0000000"},
    "and": {"opcode": "0110011", "rd": "", "funct3": "111", "rs1": "", "rs2": "", "funct7": "0000000"}
}

i_type_instructions = {
    "lw": {"opcode": "0000011","rd": "", "funct3": "010", "rs1": "",  "imm": ""},
    "addi": {"opcode": "0010011","rd": "", "funct3": "000", "rs1": "",  "imm": ""},
    "sltiu": {"opcode": "0010011","rd": "", "funct3": "011", "rs1": "", "imm": ""},
    "jalr": {"opcode": "1100111","rd": "", "funct3": "000", "rs1": "",  "imm": ""}
}

s_type_instructions = {
    "sw": {"opcode": "0100011","imm":"", "funct3": "010","rs1":"","rs2":""},
}

b_type_instructions = {
    "beq": {"opcode": "1100011", "imm1": "", "funct3": "000", "rs1": "", "rs2": "", "imm2": ""},
    "bne": {"opcode": "1100011", "imm1": "", "funct3": "001", "rs1": "", "rs2": "", "imm2": ""},
    "blt": {"opcode": "1100011", "imm1": "", "funct3": "100", "rs1": "", "rs2": "", "imm2": ""},
    "bge": {"opcode": "1100011", "imm1": "", "funct3": "101", "rs1": "", "rs2": "", "imm2": ""},
    "bltu": {"opcode": "1100011", "imm1": "", "funct3": "110", "rs1": "", "rs2": "", "imm2": ""},
    "bgeu": {"opcode": "1100011", "imm1": "", "funct3": "111", "rs1": "", "rs2": "", "imm2": ""}
}

u_type_instructions = {
    "lui": {"opcode": "0110111","rd":"","imm":""},
    "auipc": {"opcode": "0010111","rd":"","imm":""},
}

j_type_instructions = {
    "jal": {"opcode": "1101111","rd":"","imm":""},
}

instruction_types=[r_type_instructions,i_type_instructions,s_type_instructions,b_type_instructions,u_type_instructions,j_type_instructions]
