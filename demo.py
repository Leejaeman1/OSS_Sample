from OSS_Library.proc import normalize_volume, adjust_pitch, add_reverb, apply_pan_effect

input_file = "input/sample_audio.wav"

# 1. 팬닝 효과
panned_audio = apply_pan_effect(input_file, pan_value=-0.8)  # 왼쪽으로 팬닝
panned_audio.export("output/panned_audio.wav", format="wav")

# 2. 리버브 효과
reverb_audio = add_reverb(input_file, reverb_level=0.5)  # 리버브 50%
reverb_audio.export("output/reverb_audio.wav", format="wav")

# 3. 피치 조정
pitched_audio = adjust_pitch(input_file, pitch_factor=1.2)  # 피치 상승
pitched_audio.export("output/pitched_audio.wav", format="wav")

# 4. 볼륨 정규화
normalized_audio = normalize_volume(input_file, target_db=-10)  # 볼륨 -10dB로 정규화
normalized_audio.export("output/normalized_audio.wav", format="wav")

print("Processed audio files saved to the output directory.")
