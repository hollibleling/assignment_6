# assignment_6
원티드x위코드 백엔드 프리온보딩 과제6
- 과제 출제 기업 정보
  - 기업명 : 카닥

## Members

|이름   |Github                   |Blog|
|-------|-------------------------|--------------------|
|김정수 |[hollibleling](https://github.com/hollibleling) | https://velog.io/@hollibleling  |

## 과제 내용

카닥에서 실제로 사용하는 프레임워크를 토대로 타이어 API를 설계 및 구현합니다.
  - 사용자 생성 API
  - 사용자가 소유한 타이어 정보를 저장하는 API
  - 사용자가 소유한 타이어 정보 조회 API

### [주요 고려 사항]
- 로그인 성공시 인증 토큰을 발급하고 이후의 API는 인증된 사용자만 호출이 가능하다.
- 자동차 차종ID(trimID)를 이용하여 사용자 소유의 자동차 정보를 저장한다.
- 한 번에 최대 5명까지의 사용자에 대한 요청을 받을 수 있도록 해야한다.
- 사용자 ID를 통해서 저장한 타이어 정보를 조회할 수 있어야 한다.

✔️ **API 상세설명**
---

- 사용자 생성 API
    - 이메일 형태의 ID로 회원가입 가능
    - 이메일 중복 불가
    - 비밀번호 Validation 확인(8자 이상, 숫자, 영문, 특수문자 포함 필수)
- 로그인 API
    - 로그인 성공시 토큰 발급(테스트 편의를 위해 360분으로 설정)
- 데이터 입력 API
    - 로그인 성공한 (토큰을 갖고 있는 유저)만 데이터 입력 가능
    - 최대 5개의 정보까지 한 번에 입력 가능
    - 타이어의 정보 형태가 225/60R16가 아닐 경우 에러 반환
- 데이터 조회 API
    - 타이어가 저장된 ID 값으로 호출 가능 ex) /tire/1
    - 유저의 name 컬럼으로 유저의 타이어 정보 호출 가능 ex) tire?name=위코더2
    - 전체 목록 조회 가능 /tire
    
## 기술 스택

- Back-End : python, django-rest-framework, sqlite3
- Tool     : Git, Github, slack, postman

## API

### ENDPOINT

| Method | endpoint | Request Header | Request Body | Remark |
|:------:|-------------|-----|------|--------|
|POST|/user||email, password, name|회원가입 기능|
|POST|api/token/||email, password|로그인 기능|
|POST|/tire|access_token|name, trimId|타이어 정보 입력 기능|
|GET|/tire/\<int\>|access_token||타이어 Id 값으로 정보 조회 기능|
|GET|/tire?name="유저이름"|access_token||유저 이름으로 정보 조회 기능|

## API 명세(request/response)
  
  [Postman link](https://documenter.getpostman.com/view/17228945/UVJckGgy)

## 폴더 구조
```
├── car
│   ├── __init__.py
│   ├── migrations           
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── user
│   ├── __init__.py
│   ├── migrations           
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── db.sqlite3
├── manage.py
├── requirements.txt
├── README.md
└── cardoc
    ├── __init__.py
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py

```

# Reference
이 프로젝트는 원티드x위코드 백엔드 프리온보딩 과제 일환으로 원티드랩에서 출제한 과제를 기반으로 만들었습니다.
