# Python Django 프로젝트
- Server Repository: <a href="https://github.com/pshho/aws-django.git">서버 Git 주소</a>
- Web Page 주소: <a href="http://ec2-3-37-74-149.ap-northeast-2.compute.amazonaws.com/">집집 홈페이지</a>

## <img src="https://github.com/pshho/team3_django_project/assets/128444203/7531dc8b-c696-4c42-b39c-902f873e9dd9" style="width: 40px; height: 25px;" alt="Image"> 프로젝트 소개
* 프로젝트 명: 집집
  > “ 각 집. 또는 모든 집. " 을 뜻하는 순 우리말 - 대한민국 모든 집의 정보와 집과 관련된 핵심적인 내용들을 모아 놓은 홈페이지
* 기획 의도
  > 중장년층 뿐만 아니라 청년들까지도 ‘내 집 마련의 꿈’ 에 대한 열기가 뜨거워지는 만큼 부동산에 관심 있는 사람들과 정보들은 늘어나고 있습니다.
  > 각자가 필요로 하는 정보들을 검색 기능을 사용하여 쉽게 찾을 수 있으며 홈페이지 회원들을 위한 정보 교류가 가능하도록 목표를 두었습니다.
  > <br>**Figma**: <a href="https://www.figma.com/file/zffQCT0SZ5TDC3JORNaqUA/Project_Django_Team-3?type=whiteboard&node-id=0-1&t=Q6DA7FvR7HepJfcw-0">집집 설계</a>

### :mantelpiece_clock: 개발 기간
- 2023.06.19 - 2023.07.02

### :wrench: 개발 환경
- `Python 3.11`
- `HTML | CSS | JavaScript`
- **Framework**: Django
- **Database**: Sqlite3
- **개발 Tool**: VS Code, PyCharm, Figma, Git

### :gear: 주요 기능
#### * 로그인/회원가입/마이페이지
- 하나의 페이지에서 로그인과 회원가입(별도 Page Parsing) 구현
- 소셜로그인 기능 구현(구글, 카카오, 네이버)
- 회원가입 시 아이디(영문, 숫자)/사업자 등록증/비밀번호 8자 이상(영, 숫자) 유효성 검사 구현
- 로그인 후 마이페이지를 통해 회원정보 수정, 회원탈퇴, 해당 아이디의 게시판 작성글 확인 기능 구현
<details>
  <summary>마이페이지</summary>
  <p>
    <img src="https://github.com/pshho/team3_django_project/assets/128444203/8b114c60-a997-4ee5-a1bc-926ebb90d887" alt="MyPage">
    <img src="https://github.com/pshho/team3_django_project/assets/128444203/96c0dabd-ddd4-450a-a4b0-7a65a15eb122" alt="MyPage">
  </p>
</details>

<a href="http://ec2-3-37-74-149.ap-northeast-2.compute.amazonaws.com/common/signin/"> > 로그인/회원가입</a>

#### * 청약 달력/점수 계산
- 공공데이터포털 한국부동산원이 제공하는 실제 청약 일정 데이터를 API를 통해 달력에 표시 후 정보 제공
- 청약 가점 계산 공식을 무주택기간/부양가족수/청약통장가입기간을 입력받아 계산 후 점수 제공

<a href="http://ec2-3-37-74-149.ap-northeast-2.compute.amazonaws.com/koreaCalendar/"> > 청약 일정</a><br>
<a href="http://ec2-3-37-74-149.ap-northeast-2.compute.amazonaws.com/calculate/calculate/"> > 청약 점수 조회</a>

#### 지도(검색)
-

#### 정보 제공
-

#### 게시판
-

### :people_holding_hands: 구성 멤버
<details>
  <summary>멤버별 역할</summary>
  <p>
    <img src="https://github.com/pshho/team3_django_project/assets/128444203/fde8351a-6709-4135-9c47-f07718e4d8d4" alt="Member">
  </p>
</details>



