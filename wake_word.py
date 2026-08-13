from audio.recorder import record_audio
from audio.transcriber import speech_to_text

WAKE_WORDS = [
    "hey jarvis",
    "jarvis",
    "hello jarvis"
]


def wait_for_wake_word():

    print("=" * 50)
    print("🎤 Waiting For Wake Word...")
    print("=" * 50)

    while True:

        audio_file = record_audio(
            filename="recordings/wake.wav",
            duration=3
        )

        text = speech_to_text(audio_file).lower()

        print("Heard :", text)

        if any(word in text for word in WAKE_WORDS):
            print("\n✅ Wake Word Detected")
            return