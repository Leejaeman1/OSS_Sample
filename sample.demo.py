
import os
from pydub import AudioSegment
from pydub.playback import play
from OSS_Library.proc import volumeAdjustment, addReverb, StereoToMono, Panning

# 입력 및 출력 경로
INPUT_FILE = "input/sample_audio.wav"  # 오디오 파일 경로

def process_audio(input_file, output_dir="output"):
    """
    입력 오디오에 다양한 효과를 적용한 후 결과를 저장합니다.

    input_file : 처리할 오디오 파일 경로
    output_dir : 효과가 적용된 오디오 파일을 저장할 경로
    """
    # 디렉터리 생성 (존재하지 않을 경우에만 생성)
    os.makedirs(output_dir, exist_ok=True)

    # 원본 오디오 로드
    audio = AudioSegment.from_file(input_file)

    # 효과 적용 및 저장
    effects = [
        ("panned_audio.wav", lambda: Panning(audio, pan_percent=-50)),  # 팬 효과 (왼쪽 50%)
        ("reverb_audio.wav", lambda: addReverb(audio, gapsecond=0.3, reverb_count=5, decreace_volume_persent=30)),  # 리버브 효과
        ("volume_adjusted_audio.wav", lambda: volumeAdjustment(audio, volume_persent=120)),  # 볼륨 조절 (120%)
        ("mono_audio.wav", lambda: StereoToMono(audio)),  # 스테레오 -> 모노 변환
    ]

    for file_name, effect_function in effects:
        print(f"Applying {file_name.split('_')[0]} effect...")  # 현재 적용 중인 효과 표시
        processed_audio = effect_function()  # 효과 적용
        output_path = os.path.join(output_dir, file_name)  # 파일 저장 경로 설정
        processed_audio.export(output_path, format="wav")  # 결과 오디오를 WAV 형식으로 저장
        print(f"Saved {file_name} at '{output_path}'")  # 저장 완료 메시지 출력

    print(f"Processed audio files saved to the '{output_dir}' directory.")  # 전체 완료 메시지

def play_audio(file_path):
    """
    주어진 오디오 파일을 재생합니다.
    file_path : 재생할 오디오 파일의 경로
    """
    # 파일 존재 여부 확인
    if not os.path.exists(file_path):
        print(f"Audio file '{file_path}' not found!")  # 파일이 없을 경우 오류 메시지 출력
        return
    print(f"Playing '{file_path}'...")  # 재생 중인 파일 표시
    audio = AudioSegment.from_file(file_path)  # 파일 로드
    play(audio)  # 오디오 재생

# 메인 함수
def main():
    # 입력 파일이 존재하지 않을 경우 실행 중단
    if not os.path.exists(INPUT_FILE):
        print(f"Input file '{INPUT_FILE}' not found. Please ensure it exists.")
        return

    # 입력 오디오에 다양한 효과를 적용
    process_audio(INPUT_FILE)

    # panned_audio.wav 파일 재생
    play_audio(os.path.join("output", "panned_audio.wav"))

# 메인 함수 호출
if __name__ == "__main__":
    main()

