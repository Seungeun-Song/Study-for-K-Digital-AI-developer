# Chapter 3. MariaDB 전체 운영 실습

---

```
1. 데이터베이스 관련 필수 용어 파악 / * 업무파악
```

​                      V

```
2. 데이터베이스 생성
```

​                     V

```
3. 테이블 생성
```

​                     V 

```
4. 데이터 입력
```

​                     V

```
5. 데이터 조회/검색과 활용(어떻게 조회하느냐에 따라 다르니까)
```

​                     V

```
6. 인덱스, 뷰, 스토어드 프로시저, 트리거 등의 활용

인덱스 -  속도를 빠르게 하기 위해
뷰 - 가상 환경 생성. 제한된 열람,활용을 주기 위해
스토어드 프로시저 - 함수와 유사. 
트리거 - 어떤 액션이 실행될 때 찾아서 적당한 액션을 취하는 것  (ex, insert, update, delete)
커서 - 
```

​                     V   

```
7. 데이터 백업과 복원
```

​                      V

```
8. 응용프로그램과 MariaDB의 연동
```

---

### 1. 설계 및 모델링

1. ) 정보시스템 구축 절차 (5단계)

   분석 -> 설계(**전체 공정의 50%차지**) -> 구현 -> 시험 -> 유지보수

   ​	*절대 바로 코딩부터 시작X, 분석,설계를 충분히*

2. ) 모델링 

   * 현실세계의 데이터  -->  DB에 어떻게 옮겨 놓을지 고민
   * **데이터 체계**
     - Data(=raw data) --가공--> Information --사용--> Knowledge --> wisdom

   * 생성 과정 = 개념모델링 -> 논리 모델링 -> 물리적 모델링

3. ) 데이터베이스 모델링 관련 용어

   * 데이터베이스(DB) - 테이블이 저장되는 저장소
   * DBMS - 데이터베이스를 관리하는 시스템 또는 소프트 웨어



###  2. 테이블 생성

Q. 수강신청 업무파악 -> 테이블 생성

**수강신청**

* 학생정보
* 수강과목정보 
* 수강과목코드
* 수강신청

**학생 table**

| 학번(INT)-primary | 이름(문자열) | 이름의 길이               | 주소 | 핸번 |
| ----------------- | ------------ | ------------------------- | ---- | ---- |
| 127               | 홍길동       | ex김 수한무바둑이와너구리 | 서울 |      |
| 153               | 홍길순       |                           |      |      |
| 219               | 홍길동       |                           | 부산 |      |

**수강신청 table**

| 학생코드-primary | 수강과목 코드 | 신청날짜 | 상태 |
| ---------------- | ------------- | -------- | ---- |
|                  |               |          |      |

**수강과목 table**

| 코드명-primary | 과목명 | 담당 교수명 |
| -------------- | ------ | ----------- |
| 1001           | 국어   |             |
| 1002           | 수학   |             |
| 1003           | 영어   |             |

테이블을 만들어야 데이터를 이력할 수 있다



### 3. 데이터 입력

* **SELECT**문 :

  * SELECT 열 이름 FROM 테이블 이름 WHERE 조건; 
  * IntelliSense 기능 - Ctrl + Space키를 누르면 관련 글자 표시

* **CREATE**문 :

  * CREATE TABLE 테이블 이름 (열이름 데이터유형) 

    ```mariadb
    CREATE TABLE `my testTBL` (id INT);
    ```

* **DROP** 문: (삭제)

  ```mariadb
  DROP TABLE `my TestTBL` ;	-- ``백틱 사용!
  
  ```

* **주석처리**:

  * `--` + `space` 

* **인덱스(INDEX) **:

  * 대용량 데이터의 경우 필요
  * 데이터베이스 기능을 향상시키는 튜닝에서 중요한 요소 - 쿼리 문에 대한 응답 속도 향상
  * 데이터의 열 단위에서 생성

* ```mariadb
  -- employees 테이블에서 데이터를 500개 가져와 indexTBL이라는 테이블을 만든다
  CREATE TABLE indexTBL (first_name varchar(14), last_name varchar(16), hire_date date);
  INSERT INTO indexTBL
  	SELECT first_name, last_name, hire_date
  	FROM employees.employees
  	LIMIT 500;
  SELECT * FROM indexTBL;    
  ```

  * ```mariadb
    -- 먼저 인덱스가 없는 상태에서 쿼리
    SELECT * FROM indexTBL WHERE first_name = 'Mary';
    ```

  * ```mariadb
    -- 같은 쿼리에 EXPLAIN 문을 붙여서 다시 실행
    EXPLAIN SELECT * FROM indexTBL WHERE first_name = 'Mary';
    ```

    -- EXPLAIN 문 : 쿼리문이 실행될 때 어떤 상식으로 실행되는지 **실행계획**의 내용을 보여준다

    ​    (ex, 인덱스 생성 전의 실행 계획 : type - all /전체 테이블 검색)

  * ```mariadb
    -- 인덱스 생성
    CREATE INDEX idx_indexTBL_firstname ON indexTBL(first_name);
    ```

  * ```mariadb
    -- EXPLAIN문 실행
    EXPLAIN SELECT * FROM indexTBL WHERE first_name = 'Mary';
    ```

    --  인덱스 생성 후 실행 계획 : type - ref/ 인덱스를 사용해서 결과를 찾았다는 의미

* **뷰(View)** :

  * 가상의 테이블- 진짜 테이블에 링크Link된 개념

  * 실제 행 데이터를 가지고 있지 않으나 사용자의 입장에서는 테이블과 동일하게 보임

  * 개인정보 보호와 같은 데이터 보호/보안에 사용

  * ```mariadb
    CREATE VIEW uv_memberTBL
    AS
    	SELECT memberName, memberAddress FROM memberTBL;
    ```

    * 뷰의 실체는 SELECT문이다. 뷰(uv_memberTBL)에 접근하게 되면 뷰 생성 시에 입력한 SELECT문이 그때 작동하는 것. 

  * ```mariadb
    SELECT * FROM uv_memberTBL;
    ```

    --  이제는 안심하고 아르바이트생에게 출력된 테이블에 주소변경 작업을 맡기면 된다 

* **스토어드 프로시저(Stored Procedure)**:

  * MariaDB에서 제공해주는 프로그래밍.

  * 즉, SQL문을 하나로 묶어서 편리하게 사용하는 기능.

  * 실무에서는 SQL문(주로 SELECT)을 매번 하나하나 수행하기보다는 스토어드 프로시저로 만들어 놓은 후 스토어드 프로시저를 호출하는 방식을 많이 사용.

  * ```;
    SELECT * FROM memberTBL WHERE memberName = '당탕이';
    SELECT * FROM productTBL WHERE productName = '냉장고';
    ```

* **트리거(Trigger)**:

  * 테이블에 부착되어 테이블에 INSERT(회원가입)나 UPDATE, DELETE 작업이 발생되면 실행되는 코드

    ex) 회원이 탈퇴할 경우 탈퇴자 테이블에 데이터를 일부 옮겨놓고 지우는 작업

  * 삭제 작업이 일어날 경우 백업 테이블에 지워진 데이터를 기록하는 트리거 생성

  * ```mariadb
    DELIMITER//
    CREATE TRIGGER trg_deletedMemberTBL -- 트리거 이름
    	AFTER DELETE -- 삭제 후에 작동하게 지정
    	ON memberTBL -- 트리거를 부착할 테이블
    	FOR EACH ROW -- 각 행마다 적용시킴
    BEGIN
    	-- OLD 테이블의 내용을 백업 테이블에 삽입
    	INSERT INTO deletedMemberTBL
    		VALUES (OLD.memberID, OLD.memberName, OLD.memberAddress, CURDATE());
    END//
    DELIMITER;
    ```

  * 



















