import pyttsx3

# Initialize the pyttsx3 engine
engine = pyttsx3.init()

# Set the speech rate (optional)
engine.setProperty('rate', 150)

# Set the voice (optional)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) # Use the second voice in the list

# Get user input
text = input("Enter the text you want to convert to speech: ")

# Convert text to speech
engine.say(text)
engine.runAndWait()
