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
        string name = "";
        int CheckStart(string cardName)//检查以cardName开头的行数并记录
        {
            int count = 0;
            string line;
            FileStream inputFile = new FileStream("input.inp", FileMode.Open);
            StreamReader sr = new StreamReader(inputFile);
            line = sr.ReadLine();
            while (line !=null)
            {
                if (line.StartsWith(cardName))
                    count += 1;
                line = sr.ReadLine();
            }
            sr.Close();
            return count;
        }

        void CreateTempInputFiles(int i)
        {
            FileStream inputFile = new FileStream("input.inp", FileMode.Open);
            StreamReader srinputFile = new StreamReader(inputFile);
            string tempInputFileName = name + i.ToString() + ".inp";
            FileStream tempInputFile = new FileStream(tempInputFileName, FileMode.Create);
            StreamWriter srtempInputFile = new StreamWriter(tempInputFileName);
            string inputFileLine = srinputFile.ReadLine();
            string number="";
            number=i.ToString()+i.ToString()+i.ToString()+i.ToString()+i.ToString()+i.ToString();
            while (inputFileLine !=null)
            {
                inputFileLine = inputFileLine.Replace("111111", number);
                srtempInputFile.WriteLine(inputFileLine);
                inputFileLine = srinputFile.ReadLine();
            }
            srinputFile.Close();
            srtempInputFile.Close();
        }
        static void Main(string[] args)
        {
            Console.WriteLine("Hello, World!");
        }
    }
}
