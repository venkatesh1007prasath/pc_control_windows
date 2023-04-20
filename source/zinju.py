import speech_recognition as sr
import pyttsx3

# Initialize the speech recognition and text-to-speech engines
r = sr.Recognizer()
engine = pyttsx3.init()
response = ""

# Define the Zinju chatbot function
def zinju():
    # Get input from the user's microphone
    with sr.Microphone() as source:
        print("Speak something!")
        audio = r.listen(source)

    # Use the Google Speech Recognition API to convert the user's speech to text
    try:
        user_input = r.recognize_google(audio)
        print(f"You said: {user_input}")

        # Define Zinju's responses based on the user's input
        if "hello" in user_input:
            response = "Hello, how can I help you?"
        elif "what's the weather like" in user_input:
            response = "I'm sorry, I don't have that information."
        elif "what time is it" in user_input:
            response = "It's currently 3:00pm."

        # Have Zinju speak her response to the user
        engine.say(response)
        engine.runAndWait()

    # If Zinju can't recognize the user's speech, ask them to repeat themselves
    except sr.UnknownValueError:
        print("I didn't understand what you said. Please try again.")

# Call the zinju() function to start the chatbot
zinju()
