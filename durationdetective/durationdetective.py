import os
import emoji
import ffmpeg
import mimetypes
from pathlib import Path

class DurationDetective:

    def __init__(self, path_to_folder: str):
        self.ROOT_DIR = path_to_folder

    @classmethod
    def checkUserInput(cls, path_to_folder):
        
        if not os.path.isdir(path_to_folder):
            print("** Please enter a valid Folder Path ** , you entered= ", path_to_folder)
            exit(1)
        elif os.path.exists(os.path.dirname(path_to_folder))==False:
            print("** This folder path does not exist ** , you entered= ", path_to_folder)
            exit(1)

        return cls(path_to_folder)

    @staticmethod
    def durationFormat(duration, full=True):
        TOTAL_MIN=0
        TOTAL_SEC=0
        TOTAL_SEC += int(duration%60)
        TOTAL_MIN += int(duration/60) + int(TOTAL_SEC/60)
        TOTAL_SEC = int(TOTAL_SEC%60)
        

        if full==True:
            return "{}hr {:02}min {:02}secs {}".format(int(TOTAL_MIN/60), TOTAL_MIN%60, TOTAL_SEC, emoji.emojize(":timer_clock:"))
        else:
            return "{:02}mins {:02}secs {}".format(TOTAL_MIN , TOTAL_SEC, emoji.emojize(":timer_clock:"))

    @staticmethod
    def getSortedDirectoryEntry(directoryContent: list[Path]) -> list[Path]:
        return sorted( directoryContent, key=lambda entry: str(entry) )

    def checkMimeType(self, file_path: str) -> bool:

        mimestart = mimetypes.guess_type(file_path)[0]
        if mimestart != None:
            return True if mimestart.split('/')[0]=='audio' or mimestart.split('/')[0]=='video' else False
        else:
            return False

    def getFileDuration(self, filename:Path) -> float:

        try:
            data = ffmpeg.probe(filename)
            #print(data.keys())
            return data['format']['duration']
        except Exception as e:
            #Todo
            print('Error:: ', e)
            return 0.0

    def folderDuration(self, folderPath:Path, folderLevel: int) -> float:

        folderDurationSum = 0.0

        entries = self.getSortedDirectoryEntry( list( Path(folderPath).iterdir() ))
        #print(entries)
        lastIndex = len(entries)-1

        
        for index, path in enumerate(entries):
            
            symbol = "└──" if index == lastIndex else "├──"
            if os.path.isdir(str(path)):

                print("{}{}{}/".format("│   "*folderLevel, symbol, path.name))

                folderDuration = float(self.folderDuration(path, folderLevel+1))
                
                print("{}{}{} : {}/ {}".format( "│   "*(folderLevel+1), "└──", self.durationFormat(folderDuration), path.name, emoji.emojize(":check_mark_button:") ))
                
                folderDurationSum += folderDuration

            elif self.checkMimeType(str(path)):
                
                #Individual File Duration
                currentFileDuration = float(self.getFileDuration(path))
                
                folderDurationSum += currentFileDuration
                
                print("{}{}{}  {}".format("│   "*folderLevel, symbol, self.durationFormat(currentFileDuration), path.name) )
                
        return folderDurationSum



    def run(self):
        mimetypes.init()
        print("\nScanning Folder :\n{} ...".format(self.ROOT_DIR))
        
        #Folder path , current hierarchy Level
        total_duration = self.folderDuration(self.ROOT_DIR, 0)
        
        #print("{} minutes".format(int(duration/60)))
        print( "\n{} Total Duration: {} \n".format(emoji.emojize(":check_mark_button:"), self.durationFormat(total_duration, True))) 
        