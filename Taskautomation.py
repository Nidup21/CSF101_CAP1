import pyttsx3

def japanese_hello():
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')  # Get the current speaking rate
    engine.setProperty('rate', rate - 50)  # Reduce the speaking rate (adjust as needed)
    
    engine.say("Hello ")  # You can modify this text for a different greeting
    engine.runAndWait()

if __name__ == "__main__":
    japanese_hello()