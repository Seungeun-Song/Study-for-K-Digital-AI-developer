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

*  **기본 문법**

  **show, stats(), find()**

> mongod --dbpath c:\mongodb\test  															-----데몬 시작
>
> mongo localhost:27017 																						-----서버접속
>
> use test 																													-----test 데이터베이스 사용
>
> db.createCollection ("employees" , {capped: true, size: 100000 })     		   ----- collection 생성
>
> ​															----- capped collection <--> non capped collection
>
> ​																	(capped = 저장공간 재사용) <->(non capped)
>
> show dbs																												  ---- DB 리스트
>
> show collections  																									---- collection  리스트
>
> db.stats()  																												-----DB 상태, 정보
>
> db.employees.stats()  																					 ----- employees 컬렉션 상태, 정보
>
> db.emloyees.renameCollection("emp")     														 -- 이름바꾸기

---



​	**INSERT - collection에 하나의 Document를 최초 저장할 때 일반적으로 사용되는 메서드**

​	**UPDATE - 하나의 Document에서 특정 필드만을 수정하는 경우**

​	**SAVE - 하나의 Document에서 특정 필드만 변경하더라도 Document 단위로 데이터를 변경**

​		- Document 단위로 데이터를 변경하는 경우 효율적. 필드 단위로 변경하는 경우 UPDATE문이 더 효율적

>m={ename:"smith"}                  																	       ----- JSON형태로 데이터 표현
>
> n={empno:1101}
>
>db.things.save(m)                     																			       ----- 데이터 저장
>
>db.things.save(n)
>
>db.employees.find()                        															  -------- (컬렉션에 저장된) 데이터 검색

---

>db.employees.insert({key:value})                                                                           	  ----- insert
>
>db.things.update({n:1103},{$set: {ename:"stanford",dept:"research" }})          	----- update 

---

> for (var n = 1103; n <= 1120; n++) db.things.save({n : n , m : "test"})   					 ----- for 구문

---

>db.emp.remove({eno : 1101})
>
>db.emp.remove({})  																								 -----  emp 데이터 전체 삭제
>
>db.emp.drop()      																									  -----emp 컬렉션 삭제
>
>db.logout()
>
>db.shutdownServer()
>
>exit



---

* 비교 연산자

  | 연산자 | 설명                                     |
  | ------ | ---------------------------------------- |
  | $eq    | (equals)  =                              |
  | $ne    | (not equals) !=                          |
  | $gt    | (greater than) >                         |
  | $gte   | (greater than or equals) >=              |
  | $lt    | (less than) <                            |
  | $lte   | (less thatn or equeals) <=               |
  | $in    | 주어진 배열 안에 속하는 값               |
  | $ nin  | (not in) 주어진 배열 안에 속하지 않는 값 |

---

* 논리 연산자

  | 연산자 | 설명                                  |
  | ------ | ------------------------------------- |
  | $not   | 주어진 조건을 만족하지 않는           |
  | $or    | 주어진 조건 중 하나라도 만족하는      |
  | $and   | 모든 조건을 만족하는                  |
  | $nor   | 주어진 조건 중 하나라도 만족하지 않는 |

* 산술 연산자

  | 연산자    | 설명                          |
  | --------- | ----------------------------- |
  | $add      | 두 개의 값을 합한 결과를 리턴 |
  | $devide   | 두 개의 값을 나눈 결과를 리턴 |
  | $multiply | 두 개의 값을 곱한 결과를 리턴 |
  | $subtract | 두 개의 값을 뺀 결과를 리턴   |

---

### sharding(partition)

​	sharding의 가장 큰 목적은 파티셔닝을 통한 데이터 분산 처리와 성능 향상을 위한 Load Balancing



