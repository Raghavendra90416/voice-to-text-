from faster_whisper import WhisperModel

print("Loading Whisper Model...")

model = WhisperModel(
    "small",
    device="cpu",
    compute_type="int8"
)


def speech_to_text(audio_file):

    segments, info = model.transcribe(
        audio_file,
        language="en",
        vad_filter=True
    )

    text = ""

    for segment in segments:
        text += segment.text + " "

    return text.strip()