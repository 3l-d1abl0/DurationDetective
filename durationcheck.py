from pathlib import Path
import argparse
import subprocess32 as subprocess
import math
import os
import sys

def format_time(seconds):
    TOTAL_MIN=0
    TOTAL_SEC=0
    
    TOTAL_SEC += int(seconds%60)
    TOTAL_MIN += int(seconds/60) + int(TOTAL_SEC/60)
    TOTAL_SEC = int(TOTAL_SEC%60)

    return "{:.1f}hr {}min {}secs ".format(math.floor(TOTAL_MIN/60), TOTAL_MIN%60, TOTAL_SEC)


def getDuration(filename):

    command = [
        'ffprobe',
        '-v',
        'error',
        '-show_entries',
        'format=duration',
        '-of',
        'default=noprint_wrappers=1:nokey=1',
        filename
      ]

    try:
        filename =str(filename)
        output = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                             "format=duration", "-of",
                             "default=noprint_wrappers=1:nokey=1", filename],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)

    except subprocess.CalledProcessError as e:
        output = float(output.stdout)
        
    if output.stdout.decode("utf-8") =="N/A":
        return '0.0'
    else:
        return output.stdout.decode("utf-8") 


def folderDuration(folderPath):

    duration =0.0

    for path in Path(folderPath).iterdir():
        info = path.stat()
        if os.path.isdir(str(path)):
            curr_scope = float(folderDuration(path)) 
            duration += curr_scope
            
            print("{}/ --> {}".format( str(path).replace(str(folderPath),''), format_time(curr_scope)) )
        elif str(path).endswith('.mp4') or str(path).endswith('.avi') or str(path).endswith('.ts'):
            curr_scope = float(getDuration(path)) 
            duration += curr_scope
            #print("{} --> {}".format( path, curr_scope) )
        
    return duration


if __name__=="__main__":
    
    ap = argparse.ArgumentParser()
    ap.add_argument("-f", "--path", required=True, help=" \"path\" to target folder")
    args = vars(ap.parse_args())
    
    FOLDER_PATH = str(args["path"])
    
    print("\nScanning Folder :\n{} ... \n".format(FOLDER_PATH))
    
    if not os.path.isdir(FOLDER_PATH):
        print("** Please enter a valid Folder Path **")
        exit()
        
    elif os.path.exists(os.path.dirname(FOLDER_PATH))==False:
        print("** This folder path does not exist **")
        exit()
    
    duration = folderDuration(FOLDER_PATH)
    print(duration,' sec')

    print("Total Duration: {}  ".format(format_time(duration)))
