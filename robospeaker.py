import pyttsx3

def speak(text):
      # Initialize the text-to-speech engine
  engine=pyttsx3.init()
  
     # Set the speech rate (optional)
  rate=engine.getProperty('rate')
  engine.setProperty('rate',rate-75)
  
  # Set the voice (optional, default is usually English)
  voices = engine.getProperty('voices')
  engine.setProperty('voice', voices[1].id) 
  
  # Speak the text
  engine.say(text)
  engine.runAndWait()

if __name__ == '__main__':
  print("Welcome to RoboSpeaker 1.1. Created by Akarshan")
  
  while True:
    x=input("Enter what you want me to speak: ")
    
    if x=="Q":
      break
    
    speak(x)
  
  