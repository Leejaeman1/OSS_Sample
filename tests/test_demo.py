import os
from OSS_Library.proc import normalize_volume, adjust_pitch, add_reverb, apply_pan_effect

def test_apply_pan_effect():
    """팬닝 효과 테스트"""
    input_file = "input/sample_audio.wav"
    output_file = "output/panned_audio.wav"

    audio = apply_pan_effect(input_file, pan_value=-0.8)
    audio.export(output_file, format="wav")

    assert os.path.exists(output_file), "팬닝 적용 결과 파일이 없습니다."

def test_add_reverb():
    """리버브 효과 테스트"""
    input_file = "input/sample_audio.wav"
    output_file = "output/reverb_audio.wav"

    audio = add_reverb(input_file, reverb_level=0.5)
    audio.export(output_file, format="wav")

    assert os.path.exists(output_file), "리버브 적용 결과 파일이 없습니다."

def test_adjust_pitch():
    """피치 조정 테스트"""
    input_file = "input/sample_audio.wav"
    output_file = "output/pitched_audio.wav"

    audio = adjust_pitch(input_file, pitch_factor=1.2)
    audio.export(output_file, format="wav")

    assert os.path.exists(output_file), "피치 조정 결과 파일이 없습니다."

def test_normalize_volume():
    """볼륨 정규화 테스트"""
    input_file = "input/sample_audio.wav"
    output_file = "output/normalized_audio.wav"

    audio = normalize_volume(input_file, target_db=-10)
    audio.export(output_file, format="wav")

    assert os.path.exists(output_file), "볼륨 정규화 결과 파일이 없습니다."
