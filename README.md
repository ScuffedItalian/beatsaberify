# BeatSaberify 📁
BeatSaberify is a CLI (Command Line Interface) program that allows you to take a song from Youtube and convert it into a a .ogg able to be used in mapping software such as [Chromapper](https://cm.topc.at/dl)

# Download Instructions
You can follow [this](https://youtu.be/Lhj7SLzjYFk) video to learn how to install it!

# Command example / parameters 
### Example
`python main.py https://www.youtube.com/watch?v=iZErWEzbcAw 5`
### Parameters
`python main.py <YT-Link> <Silence>`
* `<YT_Link>` - Link to the audio file you'd like to download
* `<Silence>` - Amount of time you'd like for silence to begin (in seconds, 3 is the recommened amount)

# To-dos
* Add song offset adjuser
* Add BPM adjuster


# Notes
3 files will be created, you can delete 2 of them but the file labeled `song.ogg` is the final song file.


