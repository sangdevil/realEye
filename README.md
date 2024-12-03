
# Django API Project

## 프로젝트 개요
이 프로젝트는 Django와 딥러닝 모델을 이용해 `.png` 파일을 업로드받고, 
업로드된 이미지의 AI-Generated 여부를 판단하는 api를 제공하는 서버입니다. 

---

## 1. 가상환경 생성 및 활성화

### 가상환경 생성
1. 프로젝트 디렉토리를 생성하고 해당 디렉토리로 이동합니다:
   ```bash
   mkdir my_django_project
   cd my_django_project
   ```

2. Python 가상환경을 생성합니다:
   ```bash
   python -m venv venv
   ```

### 가상환경 활성화
- **Windows**:
  ```bash
  venv\Scripts\activate
  ```

- **macOS/Linux**:
  ```bash
  source venv/bin/activate
  ```

---

## 2. 필요 모듈 설치

1. 가상환경이 활성화된 상태에서 다음 명령어를 실행합니다:
   ```bash
   pip install -r requirements.txt
   ```

---

## 3. 서버 실행
1. Django 개발 서버를 실행합니다:
   ```bash
   python manage.py runserver
   ```

2. 브라우저에서 `http://127.0.0.1:8000/api/image/`로 접속하여 서버가 실행 중인지 확인합니다.

---

## 4. API 테스트 방법

### Postman 설치
1. [Postman 다운로드](https://www.postman.com/downloads/) 페이지에서 설치 파일을 다운로드하고 설치합니다.

### API 테스트
1. Postman을 열고 새 요청(Request)을 생성합니다.
2. **Method**를 `POST`로 설정합니다.
3. **URL**에 `http://127.0.0.1:8000/api/image/`를 입력합니다.
4. Body 탭에서 `form-data`를 선택합니다:
   - Key: `multipartFile`
   - Type: `File`
   - Value: `.png` 파일을 선택합니다.
5. `Send` 버튼을 눌러 요청을 전송합니다.

### 응답 예시
#### 성공 시:
```json
{
    "suspiciousness": 0.9,
}
```

#### 실패 시:
1. 파일이 없을 경우:
   ```json
   {
       "error": "No file provided."
   }
   ```

2. 파일 형식이 `.png`가 아닐 경우:
   ```json
   {
       "error": "Only .png files are supported."
   }
   ```

---
