import unittest
import os
from OSS_Sample.demo import process_audio

class TestSampleCode(unittest.TestCase):
    def setUp(self):
        # 테스트용 입력 및 출력 디렉토리 설정
        self.input_dir = "test_input"
        self.output_dir = "test_output"
        os.makedirs(self.input_dir, exist_ok=True)
        os.makedirs(self.output_dir, exist_ok=True)
        self.input_file = os.path.join(self.input_dir, "sample_audio.wav")

        # 테스트용 WAV 파일 생성
        with open(self.input_file, "wb") as f:
            f.write(b"\x00" * 1024)  # 빈 내용의 샘플 파일

    def tearDown(self):
        # 테스트가 끝난 후 디렉토리 및 파일 제거
        for folder in [self.input_dir, self.output_dir]:
            for file in os.listdir(folder):
                os.remove(os.path.join(folder, file))
            os.rmdir(folder)

    def test_process_audio(self):
        # 샘플 코드 실행
        process_audio(self.input_file, self.output_dir)

        # 출력 파일 확인
        output_files = os.listdir(self.output_dir)
        self.assertEqual(len(output_files), 4)  # 출력 파일 수 확인
        expected_files = [
            "volume_adjusted.wav",
            "reverb_audio.wav",
            "mono_audio.wav",
            "panned_audio.wav",
        ]
        for file in expected_files:
            self.assertIn(file, output_files, f"{file} not found in output directory.")

if __name__ == "__main__":
    unittest.main()
