import openai
import sounddevice as sd
import speech_recognition as sr
import pyttsx3

openai.api_key = ''  #Use your own OpenAI key

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        text = r.recognize_google(audio)
        print("You said:", text)
        return text

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def chat_with_gpt(prompt):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=50,
        temperature=0.7
    )
    return response.choices[0].text.strip()

def main():
    while True:
        text_input = get_audio()
        if text_input.lower() == 'exit':
            break
        response = chat_with_gpt(text_input)
        speak(response)

if __name__ == '__main__':
    main()