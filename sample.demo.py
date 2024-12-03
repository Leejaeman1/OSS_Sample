

import os
from pydub import AudioSegment
from pydub.playback import play
from OSS_Library.proc import normalize_volume, adjust_pitch, add_reverb, apply_pan_effect

# 입력 및 출력 경로
INPUT_FILE = "input/sample_audio.wav"

def process_audio(input_file, output_dir="output"):
    """
    입력 오디오에 다양한 효과 적용 후 결과 저장했음
    """
    os.makedirs(output_dir, exist_ok=True)

    effects = [
        ("panned_audio.wav", apply_pan_effect, {"pan_value": -0.8}),
        ("reverb_audio.wav", add_reverb, {"reverb_level": 0.5}),
        ("pitched_audio.wav", adjust_pitch, {"pitch_factor": 1.2}),
        ("normalized_audio.wav", normalize_volume, {"target_db": -10}),
    ]

    for file_name, effect_function, params in effects:
        print(f"Applying {file_name.split('_')[0]} effect...")
        processed_audio = effect_function(input_file, **params)
        output_path = os.path.join(output_dir, file_name)
        processed_audio.export(output_path, format="wav")
        print(f"Saved {file_name} at '{output_path}'")

    print(f"Processed audio files saved to the '{output_dir}' directory.")

def play_audio(file_path):
    """
    주어진 오디오 파일을 재생.
    """
    if not os.path.exists(file_path):
        print(f"Audio file '{file_path}' not found!")
        return
    print(f"Playing '{file_path}'...")
    audio = AudioSegment.from_file(file_path)
    play(audio)

def main():
    if not os.path.exists(INPUT_FILE):
        print(f"Input file '{INPUT_FILE}' not found. Please ensure it exists.")
        return

    process_audio(INPUT_FILE)

    # panned_audio.wav 재생을 한다 
    play_audio(os.path.join("output", "panned_audio.wav"))

if __name__ == "__main__":
    main()
