from pathlib import Path
import argparse
import os
import sys
import mimetypes
mimetypes.init()
import emoji
import ffmpeg

def durationFormat(duration, full=False):
    TOTAL_MIN=0
    TOTAL_SEC=0
    TOTAL_SEC += int(duration%60)
    TOTAL_MIN += int(duration/60) + int(TOTAL_SEC/60)
    TOTAL_SEC = int(TOTAL_SEC%60)

    if full==True:
        return "{}hr {:02}min {:02}secs {}".format(int(TOTAL_MIN/60), TOTAL_MIN%60, TOTAL_SEC, emoji.emojize(":timer_clock:"))
    else:
        return "{:02}mins {:02}secs {}".format(TOTAL_MIN%60, TOTAL_SEC, emoji.emojize(":timer_clock:"))
    #print("Total Duration: {}hr {}min {}secs ".format(TOTAL_MIN/60, TOTAL_MIN%60, TOTAL_SEC))

def getDuration(filename:Path) -> float:

    try:
        data = ffmpeg.probe(filename)
        #print(data.keys())
        #print(data['format'].keys())
        #print(data['format']['duration'])
        return data['format']['duration']
    except Exception as e:
        #Todo
        #print('Error:: ', e)
        return 0.0

def checkMimeType(file_path: str) -> bool:

    mimestart = mimetypes.guess_type(file_path)[0]
    if mimestart != None:
        return True if mimestart.split('/')[0]=='audio' or mimestart.split('/')[0]=='video' else False
    else:
        return False

def getSortedDirectoryEntry(directoryContent: list[Path]) -> list[Path]:
    return sorted( directoryContent, key=lambda entry: str(entry) )


def folderDuration(folderPath:Path, folderLevel: int) -> float:

    duration =0.0

    entries = getSortedDirectoryEntry( list( Path(folderPath).iterdir() ))
    #print(entries)
    lastIndex = len(entries)-1

    
    for index, path in enumerate(entries):
        
        symbol = "└──" if index == lastIndex else "├──"
        if os.path.isdir(str(path)):

            print("{}{}{}/".format("│   "*folderLevel, symbol, path.name))
            curr_scope = float(folderDuration(path, folderLevel+1))
            duration += curr_scope
            print("{}{}({} )".format( "│   "*folderLevel, "└──", durationFormat(curr_scope)) )

        elif checkMimeType(str(path)):
            curr_scope = float(getDuration(path))
            duration += curr_scope
            #Individual File
            print("{}{}{}  {}".format("│   "*folderLevel, symbol, durationFormat(curr_scope), path.name) )

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

    TOTAL_MIN=0
    TOTAL_SEC=0

    #Folder path , current hierarchy Level
    duration = folderDuration(FOLDER_PATH, 0)
    #print("{} minutes".format(int(duration/60)))

    print( "\n{} Total Duration: {} \n".format(emoji.emojize(":check_mark_button:"), durationFormat(duration, True))) 
