import os

def execute():
        times=raw_input("Please input the time you want to cycle:")
        runcommand="$FLUPRO/flutil/rfluka -N0 -M"+str(times)+" input.inp"
        os.system(runcommand)

def makeusrfiles(usrcard,cardtype):
        f1=open("input.inp")
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

def afterrun():
        os.system("rm -rf US*")
        os.system("rm -rf ran*")
        finishcommand="echo \""+name+" is Finished.\" | mail -s \"Mission Complete\" shihy@ihep.ac.cn"
        os.system(finishcommand)

name=raw_input("Please make sure that you run the fluka script in screen shell.\n Please input the file name you want:")
execute()
makeusrfiles("USRTRACK","t")
makeusrfiles("USRBIN","b")
makeusrfiles("USRBDX","x")
afterrun()
