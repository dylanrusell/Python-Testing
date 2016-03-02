import sys
import re

regs = {'r0':  0,
        'r1':  0,
        'r2':  0,
        'r3':  0,
        'r4':  0,
        'r5':  0,
        'r6':  0,
        'r7':  0,
        'r8':  0,
        'r9':  0,
        'r10': 0,
        'r11': 0,
        'r12': 0,
        'r13': 0,
        'r14': 0,
        'r15': 0
}

def regDisp():
   for i in range(0,16):
       string = 'r' + str(i)
       output = regs[string]
       print(str(string) + " " + str(output))

def readFile(lines):
    progMem = {}
    lineCount = 0

    for line in lines:
        progMem[lineCount] = line
        lineCount += 1
    return progMem

def fetch(progCounter):
    return progCounter + 1

def scanner(progMem):
    progMem = re.split("[" + re.escape("(, \t\n)") + "]", progMem)
    return [x for x in progMem if(x != '')]

def execute(instr):
    if(instr[0].lower() == 'add'):
        regs[instr[1]] = regs[instr[1]] + regs[instr[2]]
        return 1
    elif(instr[0].lower() == 'or'):
        regs[instr[1]] = regs[instr[1]] | regs[instr[2]]
        return 1
    elif(instr[0].lower() == 'ldi'):
        regs[instr[1]] = int(instr[2])
        return 1
    else:
        print("fail")
        return -1



def main():
    readText = open(sys.argv[1], "r")
    lines = readText.readlines()
    readText.close()

    progMem = readFile(lines)
    progCounter = 0

    while(progCounter < len(progMem)):
        instr = scanner(progMem[progCounter])
        print(instr)
        status = execute(instr)
        progCounter = fetch(progCounter)
    regDisp()

main()
