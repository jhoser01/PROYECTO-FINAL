import pandas as pd
from pytube import YouTube
import os
import pyttsx3
from moviepy.editor import *

url = input("Introduce la URL: ")
yt = YouTube(url)
audioclip=yt.streams.get_audio_only().download(r"E:\audio")