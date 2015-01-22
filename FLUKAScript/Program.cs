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
        //static int CheckStart(string cardName)//检查以cardName开头的行数并记录
        //{
        //    int count = 0;
        //    string line;
        //    FileStream inputFile = new FileStream("input.inp", FileMode.Open);
        //    StreamReader sr = new StreamReader(inputFile);
        //    line = sr.ReadLine();
        //    while (line !=null)
        //    {
        //        if (line.StartsWith(cardName))
        //            count += 1;
        //        line = sr.ReadLine();
        //    }
        //    sr.Close();
        //    return count;
        //}

        //static string CreateTempInputFiles(string name, int i)//创建临时输入文件以供多次运行
        //{
        //    FileStream inputFile = new FileStream("input.inp", FileMode.Open);
        //    StreamReader srinputFile = new StreamReader(inputFile);
        //    string tempInputFileName = name + i.ToString() + ".inp";
        //    FileStream tempInputFile = new FileStream(tempInputFileName, FileMode.OpenOrCreate);
        //    StreamWriter srtempInputFile = new StreamWriter(tempInputFile);
        //    string inputFileLine = srinputFile.ReadLine();
        //    string number="";
        //    number=i.ToString()+i.ToString()+i.ToString()+i.ToString()+i.ToString()+i.ToString();
        //    while (inputFileLine !=null)
        //    {
        //        inputFileLine = inputFileLine.Replace("111111", number);
        //        srtempInputFile.WriteLine(inputFileLine);
        //        inputFileLine = srinputFile.ReadLine();
        //    }
        //    srinputFile.Close();
        //    srtempInputFile.Close();
        //    return tempInputFileName;
        //}

        //static void CreateRunScript(string name)//创建运行脚本
        //{
        //    FileStream runScript = new FileStream("run.sh", FileMode.Create);
        //    StreamWriter srrunScript = new StreamWriter(runScript);
        //    string line = "#!/bin/bash";
        //    srrunScript.WriteLine(line);
        //    srrunScript.WriteLine();
        //    string tempInputFileName = "";
        //    int timesOfRun = 1;
        //    Console.Write("Please input the time you want to run your input files(1-10):");
        //    timesOfRun=Convert.ToInt16(Console.ReadLine());
        //    int source = CheckStart("SOURCE");
        //    string sourceName = "";
        //    if (source > 0)
        //    {
        //        Console.Write("Please input the source file name:");
        //        sourceName = Console.ReadLine();
        //        sourceName = "-e " + sourceName + " ";
        //    }
        //    for (int i=0;i<timesOfRun;i++)
        //    {
        //        tempInputFileName = CreateTempInputFiles(name, i);
        //        srrunScript.WriteLine("$FLUPRO/flutil/rfluka " + sourceName + "-N0 -M5 " + tempInputFileName);
        //    }
        //    //System.Diagnostics.Process.Start("chmod u+x run.sh");
        //    srrunScript.Close();
        //}

        //static void execute()
        //{
        //    System.Diagnostics.Process.Start("./run.sh");
        //}

        static string GetNumbers(string card)//获得数据卡片对应的编号信息
        {
            int count = 0;
            string numbers = "Lal";
            int i = 0;
            FileStream inputFile = new FileStream("input.inp", FileMode.Open);
            StreamReader sr = new StreamReader(inputFile);
            string line;
            string sPattern = @"USR";
            Regex newRegex = new Regex(sPattern);
            string[] cardLines = new string[20];
            line = sr.ReadLine();
            while (line != null)
            {
                if (line.StartsWith(card))
                {
                    cardLines[i] = line;
                    line = sr.ReadLine();
                    count += 1;
                }
            }
            for (i = 0; i < count;i=i+2)
            {
                if (newRegex.IsMatch(cardLines[i]))
                {
                    //numbers += cardLines[i].Substring(m.Index, 2);
                    Console.WriteLine("Success");
                }
            }    
            sr.Close();
            return numbers;
        }

        static void DealWithUSRBIN()
        {

        }
        
        static void Main(string[] args)
        {
            //string name="";
            Console.WriteLine("Hello, World!");
            //Console.Write("Please input the project name:");
            //name = Console.ReadLine();
            //CreateRunScript(name);
            Console.WriteLine(GetNumbers("USRBIN"));
            //Console.ReadKey();            
        }
    }
}
