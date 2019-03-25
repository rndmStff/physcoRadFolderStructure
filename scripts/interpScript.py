"""
Interpolate existing PhysCoResults to smaller timesteps.
"""
import os
import csv


def interpPhysCo(fileName, outputFileName=None,timeInterInMin=1,startWithZeroRow=True):

    """
    Take an existing SolarLoad calc and interpolate to smaller time steps.
    :param fileName: File path of the existing file.
    :param outputFileName: Path to which the interpolated results should be written to.
        Will be assigned automatically if not provided.
    :param timeInterInMin: Time interval. Can be any value from 1,2,3,4,5,6,10,12,15,30
    :param startWithZeroRow: If set to True, then the first row will start with zero
        radiation values.
    :return:
    """

    if not outputFileName:
        nameOnly,extn=os.path.splitext(fileName)
        outputFileName=nameOnly+"Interp%02d"%timeInterInMin+extn

    intervals=(1,2,3,4,5,6,10,12,15,30)
    assert timeInterInMin in intervals,\
        "The time interval should be one of the following: %s"%",".join(list(map(str,intervals)))

    previousLine=[]

    tsteps=int(60/timeInterInMin)

    with open(fileName) as fileData,open(outputFileName,"w") as csvStream:

        csvWrite=csv.writer(csvStream)

        for idx,lines in enumerate(fileData):
            lineSplit = lines.strip().split(",")
            try:

                nums=list(map(float,lineSplit))
                if previousLine or startWithZeroRow:
                    if not previousLine:
                        previousLine = [nums[0] - 1] + [0] * (len(nums) - 1)
                    for idx2,val2 in enumerate(range(int(60/timeInterInMin))):
                        newList=["%.3f"%(previousLine[indx]+idx2*(nums[indx]-previousLine[indx])/tsteps) for indx,lval in enumerate(nums)]
                        csvWrite.writerow(newList)
                    previousLine=nums
                else:
                    previousLine=nums
            except ValueError:
                csvWrite.writerow(lineSplit)
        csvWrite.writerow(lineSplit)
if __name__ == "__main__":

    interpPhysCo("/mnt/E610176D10174449/scripts/physcoRadFolderStructure/withNoGeo/resultsPhysco3Ph/withNoGeo-Bolzano_Clear-Mnknfzl.csv",
             timeInterInMin=1)