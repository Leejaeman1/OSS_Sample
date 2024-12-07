import os
from pydub import AudioSegment
from pydub.playback import play
from OSS_Library.proc import volumeAdjustment, addReverb, StereoToMono, Panning

# 입력 및 출력 디렉토리 설정
INPUT_DIR = "input"
OUTPUT_DIR = "output"
INPUT_FILE = os.path.join(INPUT_DIR, "sample_audio.wav")

def process_audio(input_file, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    if not os.path.exists(input_file):
        print(f"입력 파일이 존재하지 않습니다: {input_file}")
        return

    try:
        audio = AudioSegment.from_file(input_file)
    except Exception as e:
        print(f"오디오 파일 로드 중 오류 발생: {e}")
        return

    effects = [
        ("volume_adjusted.wav", lambda: volumeAdjustment(audio, volume_persent=120)),  # 볼륨 조절
        ("reverb_audio.wav", lambda: addReverb(audio, gapsecond=0.3, reverb_count=5, decreace_volume_persent=30)),  # 리버브 추가
        ("mono_audio.wav", lambda: StereoToMono(audio)),  # 스테레오 -> 모노 변환
        ("panned_audio.wav", lambda: Panning(audio, pan_percent=-50)),  # 팬닝 적용 (왼쪽 50%)
    ]

    for file_name, effect_func in effects:
        try:
            processed_audio = effect_func()

            output_path = os.path.join(output_dir, file_name)
            processed_audio.export(output_path, format="wav")
            print(f"처리 완료: {file_name} -> {output_path}")

        except Exception as e:
            print(f"효과 적용 중 오류 발생: {file_name} -> {str(e)}")

def main():
    print("오디오 처리 작업 시작...")
    process_audio(INPUT_FILE, OUTPUT_DIR)
    print("모든 작업이 완료되었습니다. 결과는 'output' 디렉토리에 저장됩니다.")

if __name__ == "__main__":
    main()

