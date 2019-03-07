""""""
import os

def trimWea(inputWea,outputWea):
    with open(inputWea) as weafile,open(outputWea,"w") as weafileWrite:
        for lines in weafile:
            lineSplit=lines.strip().split()
            try:
                month,date,hour,dirNorm,diffHorz=map(float,lineSplit)
                month,date,dirNorm,diffHorz=map(int,(month,date,dirNorm,diffHorz))
                if (month,date) in ((3,20),(6,21),(9,23),(12,22)) and (hour>8 and hour<18.5):
                    weafileWrite.write(lines)
            except ValueError:
                weafileWrite.write(lines)

if __name__ == "__main__":
    trimWea("assets/Bolzano_Clear_Full.wea","assets/Bolzano_ClearTrim.wea")