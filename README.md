## OSS_Sample

### 개요

OSS_Sample은 OSS_Library의 기능을 활용하여 오디오 처리 작업을 시연하는 샘플 프로젝트입니다. 

OSS_Library의 주요 오디오 처리 기능을 실행하고 결과를 확인할 수 있습니다.

--

### 설치 방법

#### 1. Python 버전

이 프로젝트는 Python 3.12 에서 동작합니다.

#### 2. FFmpeg 설치

FFmpeg가 시스템에 설치되어 있어야 합니다:
- Ubuntu/Debian: `sudo apt install ffmpeg`
- Windows: [FFmpeg 설치 가이드](https://ffmpeg.org/download.html)

### 테스트 

 - 개발 중간 Library_Initial_Package 브랜치에서 패키지화된 라이브러리를 로컬에 다운받아 테스트.

 - python setup.py sdist

 - OSS_Sample에 들어가서
 - pip install dist/OSS_Library-0.0.1.tar.gz

### 디렉토리 구조

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

### 입력 파일:

   - 입력 파일은 WAV 형식이며, `OSS_Sample/input/sample_audio.wav` 경로에 위치해야 합니다.

### 결과 확인

   - 처리된 파일은 `OSS_Sample/output/` 디렉토리에 저장됩니다.

#### 출력 파일 설명

| 파일 이름              | 효과 적용                      | 설명                            
|-----------------------|------------------------------|----------------------------------
| `volume_adjusted.wav` | 볼륨 조절                    | 볼륨이 조정된 오디오 파일.          
| `reverb_audio.wav`    | 리버브 추가                  | 울림 효과가 추가된 오디오 파일.      
| `mono_audio.wav`      | 스테레오 → 모노 변환         | 모노로 변환된 오디오 파일.           
| `panned_audio.wav`    | 팬닝 효과 적용               | 좌/우 팬닝 효과가 적용된 오디오 파일.

--------------------------------------------------------------------
### 개발할 때

### 디렉토리는 재량껏 수정

#### 1. branch 규칙

 - main : 최종 릴리스 브랜치. 나중에 제출할 때 사용
 - dev : default 브랜치로 모든 개인 작업은 dev로 병합
 - indiv : 개별 작업 브랜치

#### 2. 작업할 때 흐름

 - git clone 레포지토리 URL
 - cd 레포지토리

모든 개인 작업은 개별 작업 브랜치에서 하고 병합은 dev로만

 - git checkout dev   # 브랜치 변경
 - git pull origin dev   # dev 브랜치 내용 가져오기
 - git checkout -b indiv   # 개별 브랜치 생성

개별 브랜치에서 작업을 끝내면

 - git add . 
 - git commit -m "작업 내용"   # commit할 때 작업 내용 꼭 쓰기
 - git push origin indiv

그 후 GitHub에서 Pull Request 생성하고 dev에 병합

