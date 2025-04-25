import moviepy.editor as mp
import whisper

video_path = "videoPath"

video = mp.VideoFileClip(video_path)
audio_path = "audio.mp3"
video.audio.write_audiofile(audio_path)

model = whisper.load_model("medium")  

'''
Pode ser: tiny, base, small, medium, large. 

Dependendo de qual usar, se tem uma precisão mais alta, mas o tempo para realizar a transcrição aumenta. 
'''

result = model.transcribe(audio_path,verbose=True)

with open("transcricao.txt", "w", encoding="utf-8") as f:
    f.write(result["text"])

print("Transcrição salva.")
