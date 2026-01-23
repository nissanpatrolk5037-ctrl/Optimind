import time
import sounddevice as sd
import numpy as np

RATE = 44100
BLOCK = 256

SOUND_FLOOR = 0.425   # ANY sound
DOUBLE_WINDOW = 0.8
DEBOUNCE = 0.05

_triggered = False


def wait_for_double_sound():
    global _triggered

    last_sound = 0.0
    sound_times = []

    def callback(indata, frames, time_info, status):
        nonlocal last_sound, sound_times
        global _triggered

        if _triggered:
            raise sd.CallbackStop()

        audio = indata[:, 0].astype(np.float32)
        energy = np.max(np.abs(audio))
        now = time.time()

        if energy > SOUND_FLOOR and (now - last_sound) > DEBOUNCE:
            last_sound = now
            sound_times.append(now)
            print("🔊 sound")

        sound_times[:] = [t for t in sound_times if now - t < 2.0]

        if len(sound_times) >= 2:
            if sound_times[-1] - sound_times[-2] <= DOUBLE_WINDOW:
                print("💥💥 DOUBLE SOUND DETECTED")
                _triggered = True
                raise sd.CallbackStop()

    print("🕒 Waiting for double sound to start...")
    with sd.InputStream(
        channels=1,
        samplerate=RATE,
        blocksize=BLOCK,
        callback=callback
    ):
        while not _triggered:
            time.sleep(0.05)
