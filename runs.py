#!/bin/python
__author__ = 'Shy'
import os, sys, re

def execute():
    times=raw_input("Please input the time you want to cycle:")
    runcommand="rfluka -N0 -M"+str(times)+" input.inp"
    os.system(runcommand)

def processusrbin():
    f1=open("input.inp","r")
    num=0
    usrbins=["a"]
    usrbindetectorname=['a']
    usrbinindex=['a']
    eof="binEOF"
    for s in f1.readlines():
        if s.startswith("USRBIN"):
            usrbins.append(s)
            num+=1
    if (num!=0):
        count=1
        while (count<num):
            temp=usrbins[count]
            detector=temp[70:80]
            count+=2
            temp_split=detector[0:len(detector)-1]
            usrbindetectorname.append(detector)
            usrbinindexline=temp.split()
            index=usrbinindexline[3][1:len(usrbinindexline[3])-1]
            usrbinindex.append('.'+index)
        FileList = []
        rootdir=os.getcwd();
        count=1
        while (count<num):
            for root, subFolders, files in os.walk(rootdir):
                for f in files:
                    if (f.find(usrbinindex[(count+1)/2]) != -1):
                        FileList.append(f)
            eof="binEOF"+str(count)
            myfile=open(eof,"w");
            myfile.close();
            myfile=open(eof,"r+")
            myfile.write("#!/bin/bash\n")
            myfile.write("\n")
            myfile.write("$FLUPRO/flutil/usbsuw <<binEOF\n")
            for item in FileList:
                myfile.writelines(item+'\n');
            neu=name+usrbindetectorname[(count+1)/2];
            neu=neu[0:len(neu)-1]
            myfile.write("\n");
            myfile.write(neu+".rea\n");
            myfile.write("binEOF")
            myfile.close();
            os.system("chmod u+x "+eof)
            os.system("./"+eof)
            eof="binEOF"+str(count+1)
            myfile=open(eof,"w")
            myfile.write("#!/bin/bash\n")
            myfile.write("\n")
            myfile.write("$FLUPRO/flutil/usbrea <<binEOF\n")
            myfile.write(neu+".rea\n")
            myfile.write(neu+".usrbin\n")
            myfile.write("binEOF")
            myfile.close();
            os.system("chmod u+x "+eof)
            os.system("./"+eof)
            count+=2;
            
def processusrtrack():
    f1=open("input.inp","r")
    num=0
    usrtracks=["a"]
    usrtrackdetectorname=['a']
    usrtrackindex=['a']
    eof="trackEOF"
    for s in f1.readlines():
        if s.startswith("USRTRACK"):
            usrtracks.append(s)
            num+=1
    if (num!=0):
        count=1
        while (count<num):
            temp=usrtracks[count]
            detector=temp[70:80]
            count+=2
            temp_split=detector[0:len(detector)-1]
            usrtrackdetectorname.append(detector)
            usrtrackindexline=temp.split()
            index=usrtrackindexline[3][1:len(usrtrackindexline[3])-1]
            usrtrackindex.append('.'+index)
        FileList = []
        rootdir=os.getcwd();
        count=1
        while (count<num):
            for root, subFolders, files in os.walk(rootdir):
                for f in files:
                    if (f.find(usrtrackindex[(count+1)/2]) != -1):
                        FileList.append(f)
            eof="trackEOF"+str(count)
            myfile=open(eof,"w");
            myfile.close();
            myfile=open(eof,"r+")
            myfile.write("#!/bin/bash\n")
            myfile.write("\n")
            myfile.write("$FLUPRO/flutil/ustsuw <<trackEOF\n")
            for item in FileList:
                myfile.writelines(item+'\n');
            neu=name+usrtrackdetectorname[(count+1)/2];
            neu=neu[0:len(neu)-1]
            myfile.write("\n");
            myfile.write(neu+".track\n");
            myfile.write("trackEOF")
            myfile.close();
            os.system("chmod u+x "+eof)
            os.system("./"+eof)
            count+=2;

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

name=raw_input("Please make sure that you run the fluka script in screen shell.\n Please input the file name you want:");
execute();
processusrbin();
processusrtrack();
#afterrun();

