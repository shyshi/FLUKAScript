#!/bin/python
__author__ = 'Shy'
import os, sys, re

def execute():
    times=raw_input("Please input the time you want to cycle:")
    runcommand="rfluka -N0 -M"+str(i)+" input.inp"
    os.system(runcommand)

def checkandrunusrbin():
    f1=open("input.inp","r")
    num=0
    for s in f1.readlines():
        if s.startswith("USRBIN"):
		num+=1
    if (num != 0):
        FileList = []
        rootdir=os.getcwd();
        for root, subFolders, files in os.walk(rootdir):
            for f in files:
                if f.find('.50') != -1:
                    FileList.append(f)
        myfile=open('EOF1',"w");
        myfile.close();
        os.system("chmod u+x EOF1")
        myfile=open("EOF1","r+")
        myfile.write("#!/bin/bash\n")
        myfile.write("\n")
        myfile.write("$FLUPRO/flutil/usbsuw <<EOF\n")
        for item in FileList:
            myfile.writelines(item+'\n');
        neu=name+".rea";
        myfile.write("\n");
        myfile.write(neu+"\n");
        myfile.write("EOF")
        myfile.close();
        myfile=open("EOF2","w")
        myfile.write("#!/bin/bash\n")
        myfile.write("\n")
        myfile.write("$FLUPRO/flutil/usbrea <<EOF\n")
        myfile.write(neu+"\n")
        myfile.write(name+".usrbin\n")
        myfile.write("EOF")
        myfile.close();
        os.system("chmod u+x EOF2")
        os.system("./EOF1")
        os.system("./EOF2")

def afterrun():
    myfile=open('./count.txt','r');
    c=myfile.readline();
    myfile.close();
    c.strip('\n');
    i=int(c);
    i=i+1;
    c=str(i);
    myfile=open('./count.txt','w');
    myfile.write(c+'\n');
    myfile.close();
    mk='mkdir '+c;
    os.system(mk);
    c=c+'/';
    os.system('mv *.50 *.out *.log *.rea *.usrbin '+c);
    os.system('cp input.inp '+c);
    os.system('rm -rf ran*');
    os.system('rm -rf *.err');
    os.system('rm -rf '+name+'*');

name=raw_input("Please input the file name you want:");
execute();
checkandrunusrbin();
afterrun();

