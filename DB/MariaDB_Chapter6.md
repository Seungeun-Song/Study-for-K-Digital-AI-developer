# Chapter 6. SQL 기본

---

```
SELECT문의 형식과 사용법
```

​						V

```
책 전체에서 사용할 sqlDB 생성
```

​						V

```
특정 조건을 조회하는 WHERE절
```

​						V

```
ORDER BY절 및 LIMIT절
```

​						V

```
GROUP BY 및 HAVING 그리고 집계함수
```

​						V

```
INSERT/UPDATE/DELETE문의 형식
```

---

### 6-1 SELECT문

* **SELECT 구문 형식**

```mariadb
SELECT select_expr
	[FROM table_references]
	[WHERE where_condition]
	[GROUP BY {col_name|expr|position}]
	[HAVING where_condition]
	[ORDER BY {col_name|expr|position}]
```

```
SELECT 열이름(출력형태-AS, SUM() AS....)
FROM 테이블이름
WHERE 조건
```

```mariadb
SELECT first_name, last_name FROM employees;

-- limit 사용
SELECT * FROM employees LIMIT 20;

-- COUNT 사용
SELECT COUNT(*) FROM employees;
SELECT COUNT(first_name) FROM employees;

-- 세미콜론이 없으면 여러줄을 한줄로 읽는다
SELECT emp_nom birth_date
FROM employees -- 직원정보테이블명이다.
LIMIT 50;
```



* **USE 구문** :  현재 사용하는 데이터베이스를 지정 또는 변경하는 구문

```mariadb
USE 데이터베이스명;
USE employees;

USE 데이터베이스명.테이블명;
SELECT * FROM employees.titles; = SELECT * FROM titles;
```



* **SHOW 구문** - prompt 창에서 유용

```mariadb
SHOW DATABASES;  -- 현재 서버에 어떤 데이터베이스가 있는지 조회
USE employees;  -- 우리가 찾는 데이터베이스 이름을 지정한다
SHOW TABLE STATUS;  -- 현재 데이터베이스에 있는 테이블의 정보를 조회
```

* **DESCRIBE 문**

```mariadb
DESCRIBE employees;  -- employees 테이블의 열이 무엇이 있는지 확인
= DESC employees;
```

* **AS(Alias) - 별칭**

```mariadb
SELECT first_name AS 이름, gender 성별, hire_date '회사 입사일'
FROM employees;
```

* **WHERE - 조건**

```mariadb
SELECT 필드이름 FROM 테이블명 WHERE 조건식;
```

```mariadb
SELECT * FROM usertbl WHERE NAME = '김경호';
```

* * **관계연산자**

  ```mariadb
  -- AND 연산자
  SELECT userid, NAME FROM usertbl WHERE height >=182 and birthyear>= 1970;
  ```

  ```mariadb
  -- OR 연산자
  SELECT userID, NAME FROM usertbl WHERE height >= 182 OR birthyear >= 1970;
  ```

* **BETWEEN .. AND**

```mariadb
SELECT NAME, height FROM usertbl WHERE height BETWEEN 180 AND 183;

SELECT NAME, height FROM usertbl WHERE height >= 180 AND height <= 183;
```

* **IN**

```mariadb
SELECT NAME, addr FROM usertbl WHERE addr IN ('경남','경북','전남');

SELECT NAME, addr FROM usertbl WHERE addr = '전남' OR addr = '경북' OR addr ='경남';
```

* **LIKE**

```mariadb
SELECT NAME, addr FROM usertbl WHERE name LIKE '김%'

SELECT NAME, addr FROM usertbl WHERE name LIKE '_종_'
```

* **ANY/ALL/SOME**

```mariadb
-- 김경호보다 키가 크거나 같은 사람의 이름과 키를 출력
SELECT NAME, height FROM usertbl WHERE height > 
	(SELECT height FROM usertbl WHERE NAME ='김경호')
```

```mariadb
--  경남 사람의 키보다 키가 크거나 같은 사람을 추출
SELECT NAME, addr, height FROM usertbl WHERE height >=
	ANY (SELECT height FROM usertbl WHERE addr ='경남');
-- ANY를 적지 않으면 경남의 키 값이 170, 173 두 개이므로 어떤 값을 말하는 지 몰라
```

```mariadb
SELECT NAME, addr, height FROM usertbl WHERE height >=
	ALL (SELECT height FROM usertbl WHERE addr ='경남');
-- 경남 키에 모두 해당되야 하므로, 결국 173 이상
```

```mariadb
SELECT NAME, addr, height FROM usertbl WHERE height =
	ANY (SELECT height FROM usertbl WHERE addr ='경남');

SELECT NAME, addr, height FROM usertbl WHERE height IN (SELECT height FROM usertbl WHERE addr = '경남');

-- 같은 뜻
```

* **OREDER BY** - 기본: 오름차순(ASC)/ 내림차순(DESC)

```mariadb
-- 가입한 순서로 회원들 출력
SELECT NAME, mdate FROM usertbl ORDER BY mdate;
```

```mariadb
SELECT NAME, mdate FROM usertbl ORDER BY mdate DESC;
```

```mariadb
-- 키가 큰 순서로 정렬하되, 만약  키가 같을 경우에 이름 순으로 정렬
SELECT height, name FROM usertbl ORDER BY height desc, NAME asc ;
```

* **DISTINCT** - 중복된 것은 하나만

```mariadb
-- 회원 테이블에서 회원들의 거주지역이 몇 군데인지 출력
SELECT addr FROM usertbl ORDER BY addr;
```

```mariadb
SELECT distinct addr FROM usertbl;
```

* **LIMIT**

```mariadb
-- hire_date(입사일)열에서 오래된 직원 5명의 emp_no(사원번호)를 알고 싶다면
SELECT hire_date, emp_no, CONCAT(first_name, last_name) FROM employees
	ORDER BY hire_date ASC LIMIT 0, 5;  -- LIMIT 시작, 개수
```

* **CREATE TABLE ~ SELECT**

```mariadb
CREATE TABLE 새로운 테이블 (SELECT 복사할 열 FROM 기존 테이블);
```

```mariadb
-- buytbl을 buytbl2로 복사
-- BUT, PK 또는 FK 지정 따위는 복사가 X
CREATE TABLE buytbl2 (SELECT * FROM buytbl);   -- 일부 열만 복사 가능
SELECT * FROM buytbl2;
```

* **GROUP BY**

```mariadb
-- buytbl에서 사용자가 구매한 물품의 개수
SELECT userid, sum(amount) FROM buytbl GROUP BY userid;
SELECT userid, amount FROM buytbl GROUP BY userid;
```

```mariadb
-- 고객별로 구매액의 총합
SELECT userid, SUM(price*amount) AS '총구매액' FROM buytbl GROUP BY userid;
```

```mariadb
-- 전체 구매자가 구매한 물품 개수의 평균
SELECT AVG(amount) FROM buytbl;
```

```mariadb
-- 가장 큰 키와 가장 작은 키의 회원 이름과 키를 출력
SELECT userID, height FROM usertbl 
	WHERE height = (SELECT MAX(height) FROM usertbL)
		OR height = (SELECT MIN(height) FROM usertbl);

```

```mariadb
-- 휴대폰이 있는 사용자의 수를 카운트
SELECT COUNT(mobile1) AS '휴대폰이 있는 사용자'  FROM usertbl;
```



* **HAVING** - 집계 함수 쓸 때 사용하는 조건식. GROUP BY와 함께!!

```mariadb
SELECT userid, SUM(price*amount) FROM buytbl GROUP BY userid 
	HAVING SUM(price*amount) > 1000
		ORDER BY SUM(price*amount);
```



* **ROLLUP** - 총합 또는 중간 합계가 필요하다면 GROUP BY 절과 함께

```mariadb
SELECT num, groupname, SUM(amount*price) FROM buytbl 
	GROUP BY groupname, num WITH ROLLUP;
```



### 6-2. 데이터 변경을 위한 SQL문

- **INSERT, UPDATE, DELET**

### 6-2-1. INSERT

```mariadb
INSERT [INTO] 테이블(열1,열2) VALUES (값1, 값2)
              -- 순서, 개수, 데이터타입 맞추기!!
```

```mariadb
USE sqldb;
CREATE TABLE testTBL1(id INT, username CHAR(3), age INT);

INSERT INTO testtbl1 VALUES(1,'홍길동',25);
INSERT INTO testtbl1(id, username) VALUES (2, '설현');
INSERT INTO testtbl1(username, age, id) VALUES ('초아',26,3);  -- 열 순서 변경 가능

SELECT * FROM testtbl1;
```

```mariadb
-- 타입 에러
INSERT INTO testtbl1(username, age, id) VALUES(3,'초아',26); 
```

```mariadb
-- 자동으로 증가 AUTO_INCREMENT - 해당 열은 입력X/ AUTO_INCREMENT로 지정할 때는 꼭 PRIMARY KEY 또는 UNIQUE로 지정. 숫자 형태만 가능
CREATE TABLE testtbl2(id INT AUTO_INCREMENT PRIMARY KEY, username CHAR(3), age INT);

INSERT INTO testtbl2 VALUES(NULL,'지민',25);
INSERT INTO testtbl2 VALUES(NULL, '유나',22);
INSERT INTO testtbl2 VALUES(NULL,'유경',21);

SELECT * FROM testtbl2;
```

```mariadb
INSERT INTO testtbl2(username,age) VALUES('태연',31);  -- NULL 생략 가능
```

**ALTER**

```mariadb
-- ALTER TABLE 테이블명 AUTO_INCREMENT = 시작값; -> 증가 시작값 변경
CREATE TABLE testtbl3(id INT AUTO_INCREMENT PRIMARY KEY, username CHAR(3), age INT);

ALTER TABLE testtbl3 AUTO_INCREMENT = 1000;
SET @@auto_increment_increment=3;

INSERT INTO testtbl3 VALUES(NULL,'나연',20);
INSERT INTO testTBL3 VALUES (NULL, '정연', 18);
INSERT INTO testTBL3 VALUES (NULL, '모모', 19);
SELECT * FROM testTBL3;
```

**대량의 샘플 데이터 생성** - INSERT INTO ~ SELECT(VALUE 대신)

```mariadb
CREATE TABLE testTBL4 (id int, Fname varchar(50), Lname varchar(50));

INSERT INTO testTBL4      -- VALUE 대신 SELECT
  SELECT emp_no, first_name, last_name
    FROM employees.employees ;  -- 데이터베이스.테이블
-- primary key 같은 형식은 따라가지 X
```



### 6-2-2. UPDATE

 **WHERE절은 생략이 가능한데, 실무에서는 큰일!! 날 수도 있으니까 WHERE절을 먼저 꼭 적는 습관**

```mariadb
UPDATE 테이블명
	SET 열1=깂1, 열2=값2, 열3=값3
	WHERE 조건;
```

```mariadb
SELECT * FROM testtbl4 WHERE fname='kyoichi';

UPDATE testtbl4
	SET lname = '없음'
	WHERE fname = 'kyoichi';

SELECT * FROM testtbl4 WHERE fname='kyoichi'; 
SELECT * FROM testtbl4 WHERE lname= '없음';
-- 첫번째 select와 두번째 select의 출력값 개수로 변경값의 수를 확인가능
```

```mariadb
SELECT * FROM buytbl2          -- update 하기 전에 어떤 부분이 수정이 될지 미리 예상해보는 습관
UPDATE buytbl2 SET price = price *1.5;
-- Heidi는 where절이 없는데 괜찮냐는 안내문이
```



### 6-2-3 DELETE

**DELETE, DROP, TRUNCATE**

```
DELETE - DML문이라 트래잭션 로그 기록 -> 성능/속도 나쁨
DROP - 테이블 자체 삭제 -> 아예 필요없을 경우
TRUNCATE - 트랜잭션 로그 기록 X -> 성능.속도 보다 빠름, 테이블 구조는 남기고 싶을 때
			(속도가 느려도 실무에서는 잘 X, 로그기록 없기 때문)
```



```mariadb
DELETE FROM 테이블명 WHERE 조건;
-- where 절이 샹략되면 테이블 전체의 데이터 삭제
```

```mariadb
SELECT * FROM testtbl4 WHERE fname = 'Aamer'; -- DELETE 하기 전 확인해볼 것!!

DELETE FROM testtbl4 WHERE fname = 'Aamer';
```



```mariadb
CREATE TABLE bigTBL1 (SELECT * FROM employees.employees);
CREATE TABLE bigTBL2 (SELECT * FROM employees.employees);
CREATE TABLE bigTBL3 (SELECT * FROM employees.employees);

DELETE FROM bigTBL1;   -- 데이터는 없고, 테이블은 있고
DROP TABLE bigTBL2;    -- 오류 메시지. 존재하지 않는다는 
TRUNCATE TABLE bigTBL3;

```



### 6-2-4 조건부 데이터 입력, 변경

* INSERT IGNORE - PK 중복처럼 오류가 생겨도 오류를 발생시키지 않아 오류 이후의 데이터는 입력됨

* ON DUPLICATE UPDATE -

* WITH절 

  * CTE(common table expression) - 표현구문

    ```mariadb
    WITH CTE 테이블이름(열이름)
    
    AS (쿼리문)
    
    SELECT 열이름    FROM  CTE 테이블 이름
    ```

  ```
  각 지역별로 가장 큰키를 뽑고 -> WITH
  ```

  