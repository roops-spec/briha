from brain import process_command
from listener import listen
from speaker import speak

def main():
    speak("BRIHA activated. How can I help you?")
    while True:
        command = listen()
        if command:
            if "exit" in command.lower():
                speak("Goodbye.")
                break
            response = process_command(command)
            speak(response)

if __name__ == "__main__":
    main()
