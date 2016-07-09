import os
import commands

def check(runtime):
    topresult=commands.getoutput("top -b -n 1 | grep flukahp")
    string="\n"
    current=topresult.count(string)
    current=current+1
    capacity=16-current
    if (capacity>=runtime):
        cores=runtime
        randomize(cores)
    else:
        cores=capacity;
        randomize(cores)
        runtime=runtime-capacity
        check(runtime)

def randomize(cores):
    finput=open("input.inp")
    current=1
    while (current <= cores):
        if (current >= 10):
            seed = str(current) + str(current) + str(current)
        else:
            seed = str(current) + str(current) + str(current) + str(current) + str(current) + str(current)
        lines=finput.readlines();
        randomline="RANDOMIZ         1.0   "+seed+"."
        for line in lines():
            if line.startswith("RANDOMIZE"):
                number=lines.index(line)
                lines[number]=randomline
        randominputfile="input"+str(current)+".inp"
        frandominput=open(randominputfile,"w")
        for line in lines():
            frandominput.write(line)
        current=current+1