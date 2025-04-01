# KOLON BENIT AI 채팅 시스템

## 프로젝트 개요
이 프로젝트는 KOLON BENIT 브랜딩을 위한 AI 채팅 시스템입니다. Django 기반의 웹 애플리케이션과 Nginx 웹 서버, 그리고 DeepSeek AI 모델을 통합하여 구축되었습니다.

## 시스템 아키텍처

### 1. 웹 서버 (mynginx)
- Nginx를 사용한 프록시 서버
- 정적 파일 서빙 및 SSL/TLS 처리
- Django 애플리케이션으로의 요청 전달
- Kubernetes 배포 설정 포함

### 2. 웹 애플리케이션 (myproject)
- Django 기반의 웹 애플리케이션
- 사용자 인증 및 세션 관리
- 채팅 인터페이스 제공
- 데이터베이스 연동 (MySQL)
- 주요 기능:
  - 사용자 등록/로그인
  - AI 채팅 인터페이스
  - 채팅 기록 관리
  - KOLON BENIT 브랜딩 UI

### 3. AI 서비스 (mysolseek)
- DeepSeek AI 모델 통합
- Kubernetes 기반 배포
- AI 채팅 응답 생성
- 모델 관리 및 스케일링

## 기술 스택

### 백엔드
- Python 3.x
- Django
- MySQL
- DeepSeek AI

### 프론트엔드
- HTML5
- CSS3
- JavaScript
- Bootstrap

### 인프라
- Docker
- Kubernetes
- Nginx
- CI/CD

## 배포 구조
```
[사용자] → [Nginx] → [Django App] → [AI Service]
                    ↓
              [Static Files]
```

## 주요 기능
1. 사용자 관리
   - 회원가입
   - 로그인/로그아웃
   - 프로필 관리

2. AI 채팅
   - 실시간 대화
   - 채팅 기록 저장
   - 컨텍스트 관리

3. 관리자 기능
   - 사용자 관리
   - 시스템 모니터링
   - 로그 확인

## 개발 가이드
각 컴포넌트별 상세 문서는 다음 위치에서 확인할 수 있습니다:
- Nginx 설정: `mynginx/GUIDE.md`
- Django 개발: `myproject/docs/01_basic_concepts.md`
- AI 서비스: `mysolseek/deepseek-deployment.yaml`

## 설치 및 실행
1. 저장소 클론
2. 의존성 설치
3. 환경 변수 설정
4. 데이터베이스 마이그레이션
5. 서비스 실행

## 라이선스
KOLON BENIT 프로젝트 - All rights reserved 
