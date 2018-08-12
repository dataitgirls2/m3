# E조 프로젝트

데잇걸즈 과정 중 M3~M4 마일스톤에서 진행된 조별 프로젝트이다. **E조**는 *강민경([@ddongule](https://github.com/ddonggule)), 강채원([@chaewonkang](https://github.com/chaewonkang)), 송서영([@seoyeongsong](https://github.com/seoyeongsong)), 정지혜([@jyeeee95](https://github.com/jyeeee95))*로 이루어져 있다.



### 주제

1. 지역별 의약품 소비량
2. 커플의 연애 기간에 따른 데이트 장소 변화





## 지역별 의약품 소비량

지역별(데이터 수집의 용이를 위해 서울시로 한정)의 [ATC 코드](https://github.com/dataitgirls2/m3/blob/master/E/medicine/ATC_Code.md)에 따른 의약품 소비량을 분석해본다. ATC 코드 1단계 기준으로 의약품의 소비량과 판매 금액을 구별로 구분하여 수집한다.



#### 데이터 수집

- [보건의료빅데이터개방시스템](http://opendata.hira.or.kr/op/opc/olapAtc3Info.do) : ATC 코드 3단계 기준으로 의약품의 소비량과 판매 금액
- [Seoul Maps](https://github.com/southkorea/seoul-maps) : 서울시 행정구역에 따른 지도 데이터(json file)
- [서울시 인구밀도 통계](https://opengov.seoul.go.kr/data/14382965) : 서울시 인구밀도에 대한 공공 데이터



#### 프로젝트 진행 방향

1. ATC 코드 3단계 기준으로 받은 데이터를 1단계 기준으로 취합
2. 각 구별 인구 등*(진행 중)*에 대해 의약품 소비량 분석





## 커플의 연애 기간에 따른 데이트 장소 변화

커플의 연애 기간에 따른 데이트 장소 변화를 분석해본다. 인스타그램을 통해 커플들이 100일, 200일, 300일, 1주년 등의 기념일에 방문하는 장소를 크롤링 해보고, 기타 데이터를 활용해 이를 분석한다.



#### 데이터 수집

- *진행중*



#### 프로젝트 진행 방향

1. 인스타그램의 해시태그를 활용한 크롤링 작업
2. 기타 데이터를 활용한 데이트 장소 분석
