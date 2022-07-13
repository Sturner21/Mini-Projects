from gtts import gTTS
import os

my_text = '''
Enter your text here
'''

#Sets parameters for speaking
myobj = gTTS(text=my_text, lang='en', slow=False, tld='com.au')

#Saves file into current directory
myobj.save('TTS.mp3')
