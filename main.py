from pytube import YouTube
import os
import librosa
import argparse
import warnings
from pydub import AudioSegment
import time
import sys
from colorama import Style, Fore

def loading_animation():
    for _ in range(3):
        sys.stdout.write("\r\033[K")
        sys.stdout.write("Loading.")
        sys.stdout.flush()
        time.sleep(0.5)

        sys.stdout.write("\r\033[K")  # Move cursor back and clear the line
        sys.stdout.write("Loading..")
        sys.stdout.flush()
        time.sleep(0.5)

        sys.stdout.write("\r\033[K")  # Move cursor back and clear the line
        sys.stdout.write("Loading...")
        sys.stdout.flush()
        time.sleep(0.5)



parser = argparse.ArgumentParser(description='Turnes a youtube video into a mappable audio file + BPM finder' )
parser.add_argument('YtVideoLink', type=str, help="Youtube video to take the audio from")
parser.add_argument('SilenceLength', type=int, help="The amount of time there will be silence")

args = parser.parse_args()
videoLink = args.YtVideoLink
silenceLeng = args.SilenceLength * 1000

textContent = None
# test url --> url = 'https://www.youtube.com/watch?v=iZErWEzbcAw'
video = YouTube(videoLink)
warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.simplefilter(action='ignore', category=UserWarning)
outPath = video.streams.filter(only_audio=True).first().download()
new_name = os.path.splitext(outPath)
os.rename(outPath, new_name[0]+'.wav')













AudioSegment.from_file(new_name[0]+'.wav').export('song2.ogg', format='ogg')
three_second_silence = AudioSegment.silent(duration=silenceLeng)
original_audio = AudioSegment.from_file("song2.ogg")
new_audio = three_second_silence + original_audio
new_audio.export('song.ogg', format='ogg')

print('Output file created')
loading_animation()
sys.stdout.write("\r\033[K")
audio_file = librosa.load('song2.ogg')
y, sr = audio_file
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
print(Fore.GREEN + 'ESTIMATED: {:.2f} beats per minute'.format(tempo))
print(Fore.BLUE+ 'Output sample rate --> ' + str(librosa.get_samplerate('song.ogg')))
print(Fore.CYAN + 'Silence of ' + str(silenceLeng) + ' seconds have been added')







