```
        ██████╗ ██╗   ██╗██████╗  █████╗ ████████╗██╗ ██████╗ ███╗   ██╗      
        ██╔══██╗██║   ██║██╔══██╗██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║      
        ██║  ██║██║   ██║██████╔╝███████║   ██║   ██║██║   ██║██╔██╗ ██║      
        ██║  ██║██║   ██║██╔══██╗██╔══██║   ██║   ██║██║   ██║██║╚██╗██║      
        ██████╔╝╚██████╔╝██║  ██║██║  ██║   ██║   ██║╚██████╔╝██║ ╚████║      
        ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝      
                                                                              
        ██████╗ ███████╗████████╗███████╗ ██████╗████████╗██╗██╗   ██╗███████╗
        ██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝██║██║   ██║██╔════╝
        ██║  ██║█████╗     ██║   █████╗  ██║        ██║   ██║██║   ██║█████╗  
        ██║  ██║██╔══╝     ██║   ██╔══╝  ██║        ██║   ██║╚██╗ ██╔╝██╔══╝  
        ██████╔╝███████╗   ██║   ███████╗╚██████╗   ██║   ██║ ╚████╔╝ ███████╗
        ╚═════╝ ╚══════╝   ╚═╝   ╚══════╝ ╚═════╝   ╚═╝   ╚═╝  ╚═══╝  ╚══════╝
```


<h1 align="center">  </h1>
<div align= "center">
  <h4>A tree-like tool to check the media duration in your folders/subfolders.</h4>
</div>

## 🚀&nbsp; Installation

### Create a virtual environment (if needed)
```
$ python3 -m venv <your_env>
source <your_env>/bin/activate
```

#### Install via pip
```
pip install duration-detective
```

#### Run it
```
$ DurationDetective --path "/path/to/your/folder"

Scanning Folder :
/path/to/your/folder ...
├──22mins 02secs ⏲️  Batman Hush (2019) (1080p BluRay x265 SAMPA).mkv
├──16mins 39secs ⏲️  Batman.The.Killing.Joke.2016.1080p.6CH.ShAaNiG-[Bi-3-Seda.Ir].mkv
├──27mins 07secs ⏲️  Batman.VsTeenage.Mutant.Ninja.Turtles.2019.720p.WEBRip.x264-[YTS.AM].mp4
├──14mins 16secs ⏲️  Batman.and.Harley.Quinn.2017.WEB-DL.720p.MkvCage.mkv
├──12mins 07secs ⏲️  Batman.vs.Two.Face.2017.DVDRip.MkvCage.mkv
├──45mins 55secs ⏲️  Dark.Web.Cicada.3301.2021.720p.BRRip.Tamil.Dub.Dual-Audio.x264-1XBET.mkv
├──Good Will Hunting (1997) [1080p]/
│   ├──06mins 33secs ⏲️  Good.Will.Hunting.1997.1080p.BrRip.x264.YIFY.mp4
│   └──06mins 33secs ⏲️ : Good Will Hunting (1997) [1080p]/
├──Ship Of Theseus (2012)/
│   ├──24mins 42secs ⏲️  Ship.Of.Theseus.2012.720p.BluRay.x264.[YTS.AG].mp4
│   └──24mins 42secs ⏲️ : Ship Of Theseus (2012)/
├──The.Batman.2022.1080p.WEBRip.x265-RARBG/
│   ├──Subs/
│   │   └──00mins 00secs ⏲️ : Subs/
│   ├──56mins 12secs ⏲️  The.Batman.2022.1080p.WEBRip.x265-RARBG.mp4
│   └──56mins 12secs ⏲️ : The.Batman.2022.1080p.WEBRip.x265-RARBG/

✅ Total Duration: 3hr 39min 33secs ⏲️ 

```
## Use case
I have been using it personally for planning hours before diving into any Course videos or before Planning to binge watch any Television Series. Gives me a rough estimate of How much time consuming it can be.

### Contribution
```
$ git clone https://github.com/3l-d1abl0/DurationDetective.git
```

### Raise Issues
``` https://github.com/3l-d1abl0/DurationDetective/issues ```