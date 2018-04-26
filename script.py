import os
import random

def findfile():  # List and Let user choose the input file to run
        rootdir=os.getcwd()
        fileLists=[]
        for root, subFolders, files in os.walk(rootdir):
                for f in files:
                        if f.endswith("inp"):
                                fileLists.append(f)
        fileCount=len(fileLists)
        if (fileCount==0):
                print("No Input File Found!")
        else:
                for f in fileLists:
                        findex=fileLists.index(f)+1
                        print(str(findex)+" "+f)
                selectFile=raw_input("Please input the number of the input file you with to execute\n")
                selectFile=int(selectFile)-1
                fileName=fileLists[selectFile]
        return fileName

def changerandom(index,inputfile):
        workFile=open(inputfile)
        contents=workFile.readlines()
        workFile.close()
        for content in contents:
                if content.startswith("RANDOMIZ"):
                        lineindex=contents.index(content)
                        randomnumber=int(random.random()*1E6)
                        newcontent="RANDOMIZ          1.   "+str(randomnumber)+".\n"
                        contents[lineindex]=newcontent
        fileMainName=inputfile.rstrip("inp")
        fileMainName=fileMainName.rstrip(".")
        newFileName=fileMainName+str(index)+".inp"
        inputfileLists.append(newFileName)
        workFile=open(newFileName,"w")
        for content in contents:
                workFile.write(content)
        workFile.close()

def generateFiles(inputfile):
        subProcessNumber=raw_input("Please input the number of subprocesses you want to run\n")
        for i in range(0,int(subProcessNumber)):
                changerandom(i+1,inputfile)

def execute():
        rootdir=os.getcwd()
        userroutingFileLists=[]
        for root, subFolders, files in os.walk(rootdir):
                for f in files:
                        if f.endswith("inp"):
                                continue
                        else:
                                userroutingFileLists.append(f)
        fileCount=len(userroutingFileLists)
        if (fileCount==0):
                print("No File Found!")
        else:
                for f in userroutingFileLists:
                        findex=userroutingFileLists.index(f)+1
                        print(str(findex)+" "+f)
                selectFile=raw_input("Please input the index of the user routing file you with to execute, 0 for\n")    
        if (selectFile=="0"):
                runcommandpreifx="$FLUPRO/flutil/rfluka -N0 -M5 "
        else:
                selectFile=int(selectFile)-1
                fileName=userroutingFileLists[selectFile]
                runcommandpreifx="$FLUPRO/flutil/rfluka -e "+fileName+"-N0 -M5 "
        for everyfile in inputfileLists:
                runcommand=runcommandpreifx+everyfile+"&"
                os.system(runcommand)

def checkflukafolder():
    subfoloderList=[]
    rootdir=os.getcwd()
    for root, subFolders, files in os.walk(rootdir):
        for subFolder in subFolders:
            if subFolder.startswith("fluka"):
                subfoloderList.append(subFolder)
    foldernumber=len(subfoloderList)
    return foldernumber

def makeusrfiles(usrcard,cardtype,inputfile):
        f1=open(inputfile)
        count_of_lines=0
        usrcards=["a"]
        detectornames=["a"]
        index_of_usrcards=["a"]
        for lines in f1.readlines():
                if lines.startswith(usrcard):
                        usrcards.append(lines)
                        count_of_lines+=1
        print(count_of_lines)
        if (count_of_lines!=0):
                count_of_cards=1
                while (count_of_cards<count_of_lines):
                        temp=usrcards[count_of_cards]
                        detectorname_in_cards=temp[70:80]
                        print(detectorname_in_cards)
                        print(temp)
                        count_of_cards+=2
                        temp_split=detectorname_in_cards[0:len(detectorname_in_cards)-1]
                        print(temp_split)
                        detectornames.append(temp_split)
                        usrcardsindexline=temp.split()
                        index=usrcardsindexline[3][1:len(usrcardsindexline[3])-1]
                        index_of_usrcards.append("."+index)
                print(detectornames)
                detectornames.remove("a")
                print(index_of_usrcards)
                index_of_usrcards.remove("a")
                print(index_of_usrcards)
                number_of_cards=len(detectornames)
                print(count_of_cards)
                rootdir=os.getcwd()
                count_of_cards=0
                while (count_of_cards<number_of_cards):
                        FileList=[]
                        for root, subFolders, files in os.walk(rootdir):
                                for f in files:
                                        if (f.find(index_of_usrcards[count_of_cards])!=-1):
                                                FileList.append(f)
                        print(FileList)
                        ScriptsName=usrcard+"Script"+str(count_of_cards)
                        tempfile=open(ScriptsName,"w")
                        tempfile.close()
                        tempfile=open(ScriptsName,"r+")
                        tempfile.write("#!/bin/bash\n")
                        tempfile.write("\n")
                        tempfile.write("$FLUPRO/flutil/us"+cardtype+"suw <<EOF\n")
                        for item in FileList:
                                tempfile.writelines(item+'\n')
                        detectorname=name+detectornames[count_of_cards]+index_of_usrcards[count_of_cards][1:3]
                        tempfile.write("\n")
                        tempfile.write(detectorname+"\n")
                        tempfile.write("EOF")
                        tempfile.close()
                        os.system("chmod u+x "+ScriptsName)
                        os.system("./"+ScriptsName)
                        if (cardtype=="b"):
                                ScriptsName="USBREAScript"+str(count_of_cards)
                                tempfile=open(ScriptsName,"w")
                                tempfile.write("#!/bin/bash\n")
                                tempfile.write("\n")
                                tempfile.write("$FLUPRO/flutil/usbrea <<EOF\n")
                                tempfile.write(detectorname+"\n")
                                tempfile.write(detectorname+".usrbin\n")
                                tempfile.write("EOF")
                                tempfile.close()
                                os.system("chmod u+x "+ScriptsName)
                                os.system("./"+ScriptsName)
                        count_of_cards+=1

def afterrun(inputfile):
        for everyfile in inputfileLists:
                os.system("rm -rf "+everyfile)
        os.system("rm -rf US*")
        os.system("rm -rf ran*")
        os.system("mv "+inputfile+" input.inp")
        prefix=inputfile.rstrip(".inp")
        os.system("rm -rf "+prefix+"*")
        os.system("mv input.inp "+inputfile)
        finishcommand="echo \""+name+" is Finished.\" | mail -s \"Mission Complete\" shihy@ihep.ac.cn"
        os.system(finishcommand)

inputfile=findfile()
name=raw_input("Please input the name you want:\n")
print(inputfile)
inputfileLists=[]
generateFiles(inputfile)
execute()
os.system("sleep 10")
checked=checkflukafolder()
while (checked!=0):
    os.system("sleep 5")
    checked=checkflukafolder()
makeusrfiles("USRTRACK","t",inputfile)
makeusrfiles("USRBIN","b",inputfile)
makeusrfiles("USRBDX","x",inputfile)
afterrun(inputfile)
