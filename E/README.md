# E조 프로젝트

데잇걸즈 과정 중 M3~M4 마일스톤에서 진행된 조별 프로젝트이다. **E조**는 *강민경([@ddongule](https://github.com/ddonggule)), 강채원([@chaewonkang](https://github.com/chaewonkang)), 송서영([@seoyeongsong](https://github.com/seoyeongsong)), 정지혜([@jyeeee95](https://github.com/jyeeee95)), 홍다영([@DayoungHong](https://github.com/DayoungHong))*로 이루어져 있다.



### 주제

1. 의약품 소비량과 병원/약국 데이터 분석
2. 홍대의 Boundary 변화 데이터 분석 (키워드 : '홍대 카페')





## 지역별 의약품 소비량

지역별(데이터 수집의 용이를 위해 서울시로 한정)의 [ATC 코드](https://github.com/dataitgirls2/m3/blob/master/E/medicine/ATC_Code.md)에 따른 의약품 소비량을 분석해본다. ATC 코드 1단계 기준으로 의약품의 소비량과 판매 금액을 구별로 구분하여 수집한다.



#### 데이터 수집

- [보건의료빅데이터개방시스템](http://opendata.hira.or.kr/op/opc/olapAtc3Info.do) : ATC 코드 3단계 기준으로 의약품의 소비량과 판매 금액
- [Seoul Maps](https://github.com/southkorea/seoul-maps) : 서울시 행정구역에 따른 지도 데이터(json file)
- [서울시 인구밀도 통계](https://opengov.seoul.go.kr/data/14382965) : 서울시 인구밀도에 대한 공공 데이터



#### 프로젝트 진행 방향

1. ATC 코드 3단계 기준으로 받은 데이터를 1단계 기준으로 취합
2. 각 구별 인구 등*(진행 중)*에 대해 의약품 소비량 분석
3. 11월 12월 결측치 데이터 다른 페이지를 통해 찾아 채워넣기
4. 의약품을 통해 전할 수 있는 메세지 + 상권 분석
  - 서울시 구별 건강지표 데이터
  - 서울시 구별 병의원 분포 데이터
  - 서울시 의약품 제조 및 판매업 현황





## 어디까지가 홍대일까?

사람들이 '홍대에서 보자'라고 말을 할 때에, 홍익대학교 정문에서 보자고 하는것일까 아니면 연남동, 상수 등등까지 싸잡아서 홍대라고 하는것일까?
우리는 그 말속에 담긴 시크릿한 내용들을 파헤쳐 보기로 했다.
아! 이 얼마나 멋진 일인가!



#### 데이터 수집

- 네이버 블로그 포스팅 크롤링 (기간별 크롤링)


#### 프로젝트 진행 방향

1. 네이버 블로그를 활용한 크롤링 작업
2. 기타 데이터를 활용한 홍대 분석
3. 웹 
