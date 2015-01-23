using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Diagnostics;
using System.IO;
using System.Text.RegularExpressions;

namespace FLUKAScript
{
    class Program
    {
        static int CheckStart(string cardName)//检查以cardName开头的行数并记录
        {
            int count = 0;
            string line;
            FileStream inputFile = new FileStream("input.inp", FileMode.Open);
            StreamReader sr = new StreamReader(inputFile);
            line = sr.ReadLine();
            while (line != null)
            {
                if (line.StartsWith(cardName))
                    count += 1;
                line = sr.ReadLine();
            }
            sr.Close();
            return count;
        }

        static string CreateTempInputFiles(string name, int i)//创建临时输入文件以供多次运行
        {
            FileStream inputFile = new FileStream("input.inp", FileMode.Open);
            StreamReader srinputFile = new StreamReader(inputFile);
            string tempInputFileName = name + i.ToString() + ".inp";
            FileStream tempInputFile = new FileStream(tempInputFileName, FileMode.OpenOrCreate);
            StreamWriter srtempInputFile = new StreamWriter(tempInputFile);
            string inputFileLine = srinputFile.ReadLine();
            string number = "";
            number = i.ToString() + i.ToString() + i.ToString() + i.ToString() + i.ToString() + i.ToString();
            while (inputFileLine != null)
            {
                inputFileLine = inputFileLine.Replace("111111", number);
                srtempInputFile.WriteLine(inputFileLine);
                inputFileLine = srinputFile.ReadLine();
            }
            srinputFile.Close();
            srtempInputFile.Close();
            return tempInputFileName;
        }

        static void CreateRunScript(string name)//创建运行脚本
        {
            FileStream runScript = new FileStream("run.sh", FileMode.Create);
            StreamWriter srrunScript = new StreamWriter(runScript);
            string line = "#!/bin/bash";
            srrunScript.WriteLine(line);
            srrunScript.WriteLine();
            string tempInputFileName = "";
            int timesOfRun = 1;
            Console.Write("Please input the time you want to run your input files(1-10):");
            timesOfRun = Convert.ToInt16(Console.ReadLine());
            int source = CheckStart("SOURCE");
            string sourceName = "";
            if (source > 0)
            {
                Console.Write("Please input the source file name:");
                sourceName = Console.ReadLine();
                sourceName = "-e " + sourceName + " ";
            }
            for (int i = 0; i < timesOfRun; i++)
            {
                tempInputFileName = CreateTempInputFiles(name, i);
                srrunScript.WriteLine("$FLUPRO/flutil/rfluka " + sourceName + "-N0 -M5 " + tempInputFileName + " >> run" + i.ToString()+".log");
            }
            srrunScript.Close();
        }

        static void execute(string scriptName)
        {
            //System.Diagnostics.Process.Start("chmod u+x "+scriptName);
            //System.Diagnostics.Process.Start("./"+scriptName);
            Console.WriteLine("Succeed!");
        }

        //static string GetNumbers(string card)//获得数据卡片对应的编号信息
        //{
        //    int count = 0;
        //    string numbers = "Lal";
        //    int i = 0;
        //    FileStream inputFile = new FileStream("input.inp", FileMode.Open);
        //    StreamReader sr = new StreamReader(inputFile);
        //    string line;
        //    string sPattern = @"USR";
        //    Regex newRegex = new Regex(sPattern);
        //    string[] cardLines = new string[20];
        //    line = sr.ReadLine();
        //    while (line != null)
        //    {
        //        if (line.StartsWith(card))
        //        {
        //            cardLines[i] = line;
        //            line = sr.ReadLine();
        //            count += 1;
        //        }
        //    }
        //    for (i = 0; i < count;i=i+2)
        //    {
        //        if (newRegex.IsMatch(cardLines[i]))
        //        {
        //            //numbers += cardLines[i].Substring(m.Index, 2);
        //            Console.WriteLine("Success");
        //        }
        //    }    
        //    sr.Close();
        //    return numbers;
        //}

        static void WriteFileNames(StreamWriter srexecuteFile,string number)//遍历目录，找出对应卡片的数据文件并写入处理脚本
        {
            string dirName = System.Environment.CurrentDirectory;
            DirectoryInfo DIR = new DirectoryInfo(dirName);
            string[] fileNames = new string[20];
            int count = 0;
            foreach (FileInfo files in DIR.GetFiles("*." + number))
            {
                fileNames[count] = files.Name;
                count++;
            }
            for (int i = 0; i < count; i++)
            {
                srexecuteFile.WriteLine(fileNames[i]);
            }
        }

        static void DealWithUSRCards(string name,string cardsName,string number)//对USR*卡进行数据处理，参数为工程的用户命名、USR卡的名称和USR*卡1的WHAT(3)-计算输出文件的后缀
        {
            string[] usrcardsName=new string[2];
            string[] usrcardsTempFileName = new string[2];
            switch (cardsName)
            {
                case "USRBIN":
                    usrcardsName[0] = "usbsuw";
                    usrcardsName[1] = "usbrea";
                    usrcardsTempFileName[0] = name + number + "temp";
                    usrcardsTempFileName[1] = name + number + ".usrbin";
                    break;
                case "USRTRACK":
                    usrcardsName[0] = "ustsuw";
                    usrcardsName[1] = "";
                    usrcardsTempFileName[0] = name + "FL" + number;
                    usrcardsTempFileName[1] = "";
                    break;
            }
            FileStream executeFile=new FileStream("execute"+usrcardsName[0],FileMode.Create);
            StreamWriter srexecuteFile = new StreamWriter(executeFile);
            srexecuteFile.WriteLine("#!/bin/bash");
            srexecuteFile.WriteLine();
            srexecuteFile.WriteLine("$FLUPRO/flutil/"+usrcardsName[0]+" <<EOF");
            WriteFileNames(srexecuteFile, number);
            srexecuteFile.WriteLine();
            srexecuteFile.WriteLine(usrcardsTempFileName[0]);
            srexecuteFile.WriteLine("EOF");
            srexecuteFile.Close();
            execute(executeFile.Name);
            if (usrcardsName[1]!="")
            {
                FileStream executeFile2 = new FileStream("execute" + usrcardsName[1], FileMode.Create);
                StreamWriter srexecuteFile2 = new StreamWriter(executeFile2);
                srexecuteFile2.WriteLine("#!/bin/bash");
                srexecuteFile2.WriteLine();
                srexecuteFile2.WriteLine("$FLUPRO/flutil/" + usrcardsName[1] + " <<EOF");
                srexecuteFile2.WriteLine(usrcardsTempFileName[0]);
                srexecuteFile2.WriteLine(usrcardsTempFileName[1]);
                srexecuteFile2.WriteLine("EOF");
                srexecuteFile2.Close();
                execute(executeFile2.Name);
            }
        }
        
        static bool CheckFinish(string name)
        {
            string dirName = System.Environment.CurrentDirectory;
            DirectoryInfo DIR = new DirectoryInfo(dirName);
            bool Finished = false;
            string line = "";
            FileStream logFile;
            StreamReader srlogFile;
            foreach (FileInfo files in DIR.GetFiles(name+"*.log"))
            {
                logFile = new FileStream(files.Name, FileMode.Open);
                srlogFile = new StreamReader(logFile);
                line = srlogFile.ReadLine();
                while (line!=null)
                {
                    if (line.StartsWith("End of FLUKA run"))
                    {
                        Finished=true;
                    }
                }
            }
            return Finished;
        }

        static void Main(string[] args)
        {
            string name = "";
            Console.WriteLine("Hello, World!");
            Console.Write("Please input the project name:");
            name = Console.ReadLine();
            //CreateRunScript(name);
            //Console.WriteLine(GetNumbers("USRBIN"));
            //Console.ReadKey();         
            if (CheckFinish(name))
            { 
                DealWithUSRCards(name, "USRBIN", "50"); 
            }
            else
            {
                Console.WriteLine("Run Finished abnormal, Please Check the log and run again.");
            }
        }
    }
}
