from gtts import gTTS
import os
text1= "sbbs sbbs sbbs University"
language="en"
obj = gTTS(text=text1,lang=language,slow=True)
obj.save("audio.mp3")
os.system("audio.mp3")