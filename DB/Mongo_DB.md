# Mongo DB

1. MongoDB의 개요
2. MongoDB 데이터 처리
3. MongoDB 인덱스와 관리
4. MongoDB 튜닝과 백업/복구
5. MongoDB 설계와 데이터 모델링

---

### NoSQL

* HDFS (hadoop file system) 특징 - 리눅스 베이스



* NoSQL끼리 API로 연결가능
  * ex) mongo로는 지도데이터처리 힘들어서 Graph Database인 reis나 nodes를 설치해 서로 연동 가능

* MapReduce = 알고리즘 : 클러스터 환경에서 **대용량의 데이터**를 병렬처리 하기 위해 개발되었다.

| Map 함수                                         | Reduce 함수                    |
| ------------------------------------------------ | ------------------------------ |
| 여러 개의 작은 Split-Peace로 분산 입력           | 중복 데이터 제거               |
| 큰 용량 => 잘라 => 그룹화 => 각 그룹끼리 처리 => | => 통합      :    검색 속도 up |

---



| RDBMS(mariaDB)        | NoSQL(mongoDB)                                             |
| --------------------- | ---------------------------------------------------------- |
| create table 테이블명 | db.createCollection 컬렉션 명                              |
| column                | field                                                      |
| row                   | document                                                   |
| primary key           | _ID Field                                                  |
| insert into           | save() - 변수를 받아 저장,                                 |
|                       | insert(값) - 키 밸류를 작성해서 저장                       |
|                       |                                                            |
|                       | db.emp.find({},(enpno:1,ename:1))  - 여기서1은 True라는 뜻 |
|                       |                                                            |
|                       |                                                            |



capped collection <--> non capped collection





















