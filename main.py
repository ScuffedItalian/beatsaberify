from pytube import YouTube
import os
import librosa
import argparse
import warnings

parser = argparse.ArgumentParser(description='Turnes a youtube video into a mappable audio file + BPM finder' )
parser.add_argument('YtVideoLink', type=str, help="Youtube video to take the audio from")
args = parser.parse_args()
videoLink = args.YtVideoLink

# test url --> url = 'https://www.youtube.com/watch?v=iZErWEzbcAw'
video = YouTube(videoLink)
warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.simplefilter(action='ignore', category=UserWarning)
outPath = video.streams.filter(only_audio=True).first().download()
new_name = os.path.splitext(outPath)
os.rename(outPath, new_name[0]+'.ogg')
print('Song File Downloaded')
print('Getting BPM Info...')
audio_file = librosa.load(new_name[0]+'.ogg')
y, sr = audio_file

tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
print('ESTIMATED: {:.2f} beats per minute'.format(tempo))




