import os
from pydub import AudioSegment  
from pydub.playback import play  
from OSS_Library.proc import volumeAdjustment, addReverb, StereoToMono, Panning
# OSS_Library에서 오디오 효과 관련 함수들 임포트

# 입력 및 출력 디렉토리 설정
INPUT_DIR = "input"  
OUTPUT_DIR = "output"  
INPUT_FILE = os.path.join(INPUT_DIR, "sample_audio.wav") 

def process_audio(input_file, output_dir):
    
    #오디오 파일에 다양한 효과를 적용하고 결과를 저장하는 함수
    
    os.makedirs(output_dir, exist_ok=True)  # 출력 디렉토리가 없으면 생성

    if not os.path.exists(input_file):
        # 입력 파일이 존재하지 않을 경우 사용자에게 알림
        print(f"입력 파일이 존재하지 않습니다: {input_file}")
        return

    try:
        # 오디오 파일 로드
        audio = AudioSegment.from_file(input_file)
    except Exception as e:
        # 파일 로드 중 오류가 발생하면 사용자에게 알림
        print(f"오디오 파일 로드 중 오류 발생: {e}")
        return

    # 적용할 효과와 결과 파일 이름 목록
    effects = [
        ("volume_adjusted.wav", lambda: volumeAdjustment(audio, volume_persent=120)),  # 볼륨 조절
        ("reverb_audio.wav", lambda: addReverb(audio, gapsecond=0.3, reverb_count=5, decreace_volume_persent=30)),  # 리버브 추가
        ("mono_audio.wav", lambda: StereoToMono(audio)),  # 스테레오 -> 모노 변환
        ("panned_audio.wav", lambda: Panning(audio, pan_percent=-50)),  # 팬닝 적용 (왼쪽 50%)
    ]

    for file_name, effect_func in effects:
        try:
            # 효과 적용
            processed_audio = effect_func()

            # 결과 파일 저장 경로
            output_path = os.path.join(output_dir, file_name)
            # 처리된 오디오 파일을 저장
            processed_audio.export(output_path, format="wav")
            print(f"처리 완료: {file_name} -> {output_path}")

        except Exception as e:
            # 효과 적용 중 오류가 발생하면 사용자에게 알림
            print(f"효과 적용 중 오류 발생: {file_name} -> {str(e)}")

def main():
    # 메인 함수
    print("오디오 처리 작업 시작...")  # 작업 시작 알림
    process_audio(INPUT_FILE, OUTPUT_DIR)  # 오디오 처리 함수 호출
    print("모든 작업이 완료되었습니다. 결과는 'output' 디렉토리에 저장됩니다.")  # 작업 완료 알림

if __name__ == "__main__":
    # main() 호출
    main()
