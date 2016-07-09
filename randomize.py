import os
import subprocess as sp

def check(runtime):
    topresult=sp.getoutput("top -b -n 1 | grep flukahp")
    string="\n"
    current=topresult.count(string)
    current=current+1
    capacity=16-current
    if (capacity>=runtime):
        cores=runtime
        randomize(cores)
    else:
        cores=capacity
        randomize(cores)
        nexttime=runtime-capacity
        check(nexttime)

def randomize(cores):
    current=1
    while (current <= cores):
        finput=open("input.inp")
        if (current >= 10):
            seed = str(current) + str(current) + str(current)
        else:
            seed = str(current) + str(current) + str(current) + str(current) + str(current) + str(current)
        lines=finput.readlines()
        randomline="RANDOMIZ         1.0   "+seed+".\n"
        for line in lines:
            if line.startswith("RANDOMIZ"):
                number=lines.index(line)
                lines[number]=randomline
                print(lines[number])
        randominputfile="input"+str(current)+".inp"
        frandominput=open(randominputfile,"w")
        for line in lines:
            frandominput.write(line)
        current=current+1
        finput.close()
        frandominput.close()

check(12)
#
# finput=open("input.inp")
# current=1
# cores = 5
# while (current <= cores):
#     if (current >= 10):
#         seed = str(current) + str(current) + str(current)
#     else:
#         seed = str(current) + str(current) + str(current) + str(current) + str(current) + str(current)
#     lines=finput.readlines()
#     randomline="RANDOMIZ         1.0   "+seed+".\\n"
#     for line in lines:
#         if line.startswith("RANDOMIZE"):
#             number=lines.index(line)
#             lines[number]=randomline
#     randominputfile="input"+str(current)+".inp"
#     frandominput=open(randominputfile,"w")
#     for line in lines:
#         frandominput.write(line)
#     current=current+1