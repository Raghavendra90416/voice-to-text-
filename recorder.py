import os
import sounddevice as sd
import soundfile as sf

MIC_DEVICE = 9


def record_audio(filename, duration=3):

    os.makedirs(os.path.dirname(filename), exist_ok=True)

    device_info = sd.query_devices(MIC_DEVICE, "input")
    sample_rate = int(device_info["default_samplerate"])

    print("\n🎤 Speak...")

    audio = sd.rec(
        int(duration * sample_rate),
        samplerate=sample_rate,
        channels=1,
        dtype="float32",
        device=MIC_DEVICE
    )

    sd.wait()

    sf.write(filename, audio, sample_rate)

    print("✅ Recording Completed")

    return filename