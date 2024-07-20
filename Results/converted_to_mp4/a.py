from moviepy.editor import *

# Load the audio file and set its relative address
addr = "..\input.wav"
audio = AudioFileClip(addr)

# Create a blank video clip with the same duration as the audio
video = ColorClip(size=(640, 480), color=(0, 0, 0), duration=audio.duration)

# Set the audio of the video clip
video = video.set_audio(audio)

# Write the result to a file
video.write_videofile("output.mp4", codec="libx264", fps=24)

