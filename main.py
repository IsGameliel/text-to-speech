import gtts
from playsound import playsound

# Read text from a file
with open("input.txt", "r") as file:
    text = file.read()

# Make request to Google to get synthesis
tts = gtts.gTTS(text)

# Save the audio file
tts.save("output.mp3")

# Play the audio file
playsound("output.mp3")

# In Spanish
with open("input_spanish.txt", "r") as file:
    text_spanish = file.read()

tts_spanish = gtts.gTTS(text_spanish, lang="es")
tts_spanish.save("output_spanish.mp3")
playsound("output_spanish.mp3")

# Print all available languages along with their IETF tag
print(gtts.lang.tts_langs())
