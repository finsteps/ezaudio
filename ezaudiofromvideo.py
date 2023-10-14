import moviepy.editor

video=moviepy.editor.VideoFileClip('videotoaudio/video.mp4')

audio=video.audio

audio.write_audiofile('video.mp3')
print("Completed")
