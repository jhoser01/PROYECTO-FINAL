
import pandas as pd
from pytube import YouTube
import os
import pyttsx3
from moviepy.editor import *



#cambiar a la ubicacion donde esta el csv
df1 = pd.read_csv(r"H:\Mi unidad\Universidad\CICLO III\PROGRAMACION I\SEMESTRE\PROYECTO FINAL\dialogos.csv",delimiter=";")



#respuestas basicas
def basico():
    respuesta=0
    for j in range(len(llamado)):
        
        
        if respuesta!=0:
            break
        
        for i in range(10):
            list_pregunta=df1.iloc[i,0].split(" ")
            if llamado[j] in list_pregunta:
                respuesta=df1.iloc[i,1]
                
                engine = pyttsx3.init()
                engine.setProperty('rate', 170)
                
                print(respuesta)

                engine.say(respuesta)
                engine.runAndWait()

                
                    
                break
        
            i+=1        
         
        j+=1  
        
        
            
#preguta infinita
while True:

    orden=input("Esperando ordenes: ")
    
    llamado=orden.split(" ")
    
    
    
   
    if orden=="salir":
        break
    elif "descargar" in llamado:   #descarga audios o videos
        
        if "video" in llamado: #modo video
            engine = pyttsx3.init()
            engine.setProperty('rate', 170)
            engine.say("Introduce la URL")
            
            engine.runAndWait()
            url = input("Introduce la URL: ")
            
            
            yt = YouTube(url)
            engine = pyttsx3.init()
            engine.setProperty('rate', 170)
            engine.say(f"El título del video es {yt.title}")
            print(yt.title)
            
            engine.say(f"Del canal de {yt.author}")
            print(yt.author)
            
            engine.runAndWait()
            
            lstst=yt.streams.filter(mime_type="video/mp4",adaptive=True,file_extension=("mp4")).all()
            engine = pyttsx3.init()
            engine.setProperty('rate', 170)

            engine.say("Elige la resolución de tu video")
                
            print("⭐MIRA AQUI ABAJO⭐")
            engine.runAndWait()
            for st in lstst:   
                print(f"{st.resolution}==>{st.itag}")
                
                        
            quality = input("Elige el numero que esta a la derecha de la calidad de video que desees==> ")
            videoclip=yt.streams.get_by_itag(quality).download(r"E:\Youtube_videos")
            videoclip2=VideoFileClip(videoclip)

            audioclip=yt.streams.get_audio_only().download(r"E:\audio")
            audioclip1=AudioFileClip(audioclip)

            videoclip2=videoclip2.set_audio(audioclip1)
            videoclip2.write_videofile(videoclip2.filename.replace(" ", "_"))

            os.remove(audioclip1.filename)
            os.remove(videoclip2.filename)
            
            #codigo trasnformador 
            engine = pyttsx3.init()
            engine.setProperty('rate', 170)

            engine.say("Descargado con éxito")
                
            print("⭐VIDEO DESCARGADO⭐")
            engine.runAndWait()
            
            
        elif "audio" in llamado:   #Modo audio
            engine = pyttsx3.init()
            engine.setProperty('rate', 170)
            engine.say("Introduce la URL")
            
            engine.runAndWait()
            url = input("Introduce la URL: ")
            yt = YouTube(url)
            engine = pyttsx3.init()
            engine.setProperty('rate', 170)
            engine.say(f"El título del video es {yt.title}")
            print(yt.title)
            
            engine.say(f"Del canal de {yt.author}")
            print(yt.author)
            
            engine.runAndWait()
            ruta_fin = yt.streams.get_audio_only().download('/Youtube_audios')
            audioclip = AudioFileClip(ruta_fin)
            audioclip.write_audiofile(audioclip.filename.replace('.mp4', '.mp3'))

            os.remove(audioclip.filename)
            engine = pyttsx3.init()
            engine.setProperty('rate', 170)

            engine.say("Descargado con éxito")
                
            print("⭐AUDIO DESCARGADO⭐")
            engine.runAndWait()
            
            
     
        

    else:
        basico()



        

