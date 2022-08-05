#-- Used for transcribing voice data

# Dependencies
import speech_recognition as sr

# Proof of life
print('speech_recognition_main.py script is running')

def Speach_to_Text():
    r = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    response = {
        "success": True,
        "error": None,
        "transcription": None}

    try:
        response["transcription"] = r.recognize_google(audio)
    except sr.RequestError:
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        response["success"] = False
        response["error"] = "Unable to recognize speech."

    return response

while True:
    get_text = Speach_to_Text()
    print(get_text["transcription"])
