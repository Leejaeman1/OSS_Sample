.. OSS_Sample documentation master file, created by
   sphinx-quickstart on Mon Dec  9 21:28:58 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

OSS_Sample documentation
========================

---

설치 방법
---------

**Python 버전**

   이 프로젝트는 Python 3.12에서 동작합니다.

**FFmpeg 설치**

   FFmpeg가 시스템에 설치되어 있어야 합니다:
   - Ubuntu/Debian:

        sudo apt install ffmpeg

   - Windows:
     `FFmpeg 설치 가이드 <https://ffmpeg.org/download.html>`_

---

 테스트 
---------

 - 개발 중간 Library_Initial_Package 브랜치에서 패키지화된 라이브러리를 로컬에 다운받아 테스트.

 - python setup.py sdist

 - OSS_Library에 들어가서
 - pip install dist/OSS_Library-0.0.1.tar.gz 하고 sample 코드 테스트

**실행 방법** 
 - OSS_Sample에 들어가서
 - oss-sample

---
OSS_Sample 주요 함수 
---------------------

 - process_audio(input_file, output_dir="output"): 입력된 오디오 파일에 다양한 음향 효과(팬, 리버브, 볼륨 조정, 모노 변환)를 적용한 뒤, 
결과를 지정된 디렉터리에 저장

 - play_audio(file_path): 지정된 경로의 오디오 파일을 재생, 파일이 존재하지 않을 경우 오류 메시지를 출력

 - main(): 입력 파일이 존재하는지 확인한 후, process_audio를 호출하여 오디오 효과를 적용

---

디렉토리 구조
--------------

OSS_Sample/

├── OSS_Sample/          # 샘플 코드

│   ├── __init__.py

│   └── demo.py          # 샘플 코드

├── input/               # 입력 파일

│   └── sample_audio.wav

├── output/

├── .gitignore           #  # 빌드 파일 (dist/) 등을 불필요한 파일이 git 저장소에서 제외되도록 함

├── setup.py             # 패키지 설정 파일

├── README.md            # 샘플 코드 설명 파일

└── MANIFEST.in          # 추가 파일 포함 설정

---

입력 파일:
---------

   - 입력 파일은 WAV 형식이며, `OSS_Sample/input/sample_audio.wav` 경로에 위치해야 합니다.

---
 결과 확인
----------

   - 처리된 파일은 `OSS_Sample/output/` 디렉토리에 저장됩니다.

---

개발 가이드라인
----------------

1. 브랜치 규칙
   - **main**: 최종 릴리스 브랜치. 제출용으로 사용.
   - **dev**: 기본 브랜치로, 모든 개인 작업은 dev로 병합.
   - **indiv**: 개별 작업 브랜치.

2. 작업 흐름
   1. 레포지토리 클론:

         git clone <레포지토리 URL>
         cd OSS_Library

   2. 브랜치 작업:

         git checkout dev           # dev 브랜치로 이동
         git pull origin dev        # dev 브랜치 최신화
         git checkout -b <indiv>    # 개별 작업 브랜치 생성

   3. 작업 완료 후:

         git add .
         git commit -m "작업 내용"
         git push origin <indiv>    # 개별 작업 브랜치 푸시

   4. Pull Request 생성:
      - GitHub에서 Pull Request를 만들어 dev에 병합.

---

이슈 작성 규칙
--------------

1. **제목**: 간단하고 명확하게 작성.
2. **설명**: 문제 상황, 발생한 오류, 해결 방법 등을 구체적으로 작성.
3. **상태 변경**: 해결 완료된 이슈는 **Closed**로 상태 변경.

---
