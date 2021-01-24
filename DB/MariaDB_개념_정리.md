# MariaDB 개념 정리

1. 업무 파악
2. 데이터베이스 모델링 + 생성
3. 테이블 생성
4. 데이터 입력
5. 데이터 조회와 활용
6. 인덱스, 뷰, 스토어드 프로시저, 트리거 등의 활용

---

## 참고 - 271p 실습 6.



> ## **데이터베이스 생성**
>
> ```mariadb
> DROP DATABASE if EXISTS club;
> 
> CREATE DATABASE club;
> ```

---

> ## **테이블 생성**
>
> ```mariadb
> DROP TABLE if EXISTS stdtbl;
> 
> CREATE TABLE stdtbl(
> stdName VARCHAR(10) NOT NULL PRIMARY KEY,
> addr CHAR(4) NOT NULL
> );
> 
> DROP TABLE if EXISTS clubtbl;
> 
> CREATE TABLE clubtbl(
> clubname VARCHAR(10) NOT NULL PRIMARY KEY,
> roomNo CHAR(4) NOT NULL
> );
> 
> 
> DROP TABLE if EXISTS stdclubtbl;
> 
> create TABLE stdclubtbl(
> num INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
> stdName VARCHAR(10) NOT NULL,
> clubname VARCHAR(10) NOT NULL
> );
> 
> SHOW TABLES;
> SHOW TABLE STATUS;
> ```

---

> ## **데이터 생성**
>
> * **INSERT INTO       VALUES** 
>
> ```mariadb
> INSERT INTO clubtbl VALUES('수영','101호');
> INSERT INTO clubtbl VALUES('바둑','102호');
> INSERT INTO clubtbl VALUES('축구','103호');
> INSERT INTO clubtbl VALUES('봉사','104호');
> 
> INSERT INTO stdclubtbl VALUES(NULL, '김범수','바둑');
> INSERT INTO stdclubtbl VALUES(NULL, '김범수','축구');
> INSERT INTO stdclubtbl VALUES(NULL, '조용필','축구');
> INSERT INTO stdclubtbl VALUES(NULL, '은지원','축구');
> INSERT INTO stdclubtbl VALUES(NULL, '은지원','봉사');
> INSERT INTO stdclubtbl VALUES(NULL, '바비킴','봉사');
> 
> INSERT INTO stdtbl VALUES('김범수','경남');
> INSERT INTO stdtbl VALUES('성시경','서울');
> INSERT INTO stdtbl VALUES('조용필','경기');
> INSERT INTO stdtbl VALUES('은지원','경북');
> INSERT INTO stdtbl VALUES('바비킴','서울');
> ```
> * **UPDATE SET            WHERE**
>
> ```mariadb
> UPDATE stdtbl
> 	SET height = 170
> 	WHERE stdname = '김범수';
> ```
>
> * **DELETE  FROM**  - 행 단위로 데이터 삭제
>
> ```mariadb
> DELETE FROM stdtbl WHERE stdname = '조용필';
> ```
>
> * **DROP COLUMN** - 열 삭제
>
>   ```mariadb
>   ALTER TABLE stdtbl
>   	DROP COLUMN height;
>   ```
>
>   
>
> * **ALTER**
>
>   ```mariadb
>   -- 열 삽입
>   ALTER TABLE	stdtbl
>   	ADD height INT NOT NULL;
>   	
>   -- 열 이름 및 데이터 형식 변경
>   ALTER TABLE stdtbl
>   	CHANGE COLUMN height tall INT NULL;
>   ```
>
>   
>
>   
>
> * **제약조건 만들기**
>
>   ```mariadb
>   ALTER TABLE stdclubtbl
>   	ADD CONSTRAINT FK_name 
>   		FOREIGN KEY stdclubtbl(stdName) REFERENCES stdtbl(stdName);
>   		
>   ALTER TABLE stdclubtbl
>   	ADD CONSTRAINT FK_clubName
>   		FOREIGN KEY stdclubtbl(clubname) REFERENCES clubtbl(clubname);
>   
>   
>   ```
>
> * **인덱스 생성**
>
>   ```mariadb
>   CREATE INDEX idx_addr ON stdtbl(addr);
>   
>   EXPLAIN SELECT * FROM stdtbl WHERE stdName='조용필';
>   -- key = 'primary key', type = const
>   EXPLAIN SELECT * FROM stdtbl WHERE addr = '서울';
>    -- 인덱스를 이용해 찾았다는 type ='ref'가 나타난다 key = 'idx_addr'
>    
>   SHOW INDEX FROM stdtbl;
>   ```

---

> ## **데이터 조회와 활용**
>
> * **WHERE**
>
>   ```mariadb
>   -- AND
>   SELECT * FROM stdtbl WHERE height > 170 AND height < 180;
>   -- BETWEEN
>   SELECT * FROM stdtbl WHERE height BETWEEN 170 AND 180;  --(170<=height<=180)
>   -- IN
>   SELECT * FROM stdtbl WHERE addr IN ('서울','경북');
>   -- LIKE
>   SELECT * FROM stdtbl WHERE stdname LIKE '%지%';
>   -- ANY
>   select * FROM stdtbl WHERE height <= ANY (SELECT height FROM stdtbl WHERE addr = '서울');
>   ```
>
>   
>
> * **ORDER BY**
>
>   ```mariadb
>   SELECT * FROM stdtbl ORDER BY height asc;
>   SELECT * FROM clubtbl ORDER BY roomno DESC;
>   ```
>
> * **DISTINCT**
>
>   ```mariadb
>   SELECT DISTINCT(clubname) FROM stdclubtbl;
>   ```
>
> * **LIMIT**
>
>   ```mariadb
>   SELECT * FROM stdtbl ORDER BY height DESC	LIMIT 3;
>   ```
>
>   
>
> * **연산자**
>
>   ```mariadb
>   SELECT * FROM stdtbl 
>   	WHERE height > (SELECT height FROM stdtbl WHERE stdNAME = '은지원');
>   	
>   SELECT * FROM stdtbl 
>   	WHERE height > (SELECT height FROM stdtbl WHERE addr = '경기');
>   ```
>
>   
>
> * **GROUP BY**
>
>   ```mariadb
>   SELECT * FROM stdclubtbl GROUP BY clubname;
>   
>   SELECT userID, SUM(amount) FROM buyTbl GROUP BY userID;
>   ```
>
> * **AS**
>
>   ```mariadb
>   SELECT userID AS '사용자 아이디', SUM(amount) AS '총 구매개수' FROM buytbl GROUP BY userID;
>   ```
>
> * **집계 함수** - AVG(), MIN(), MAX(), COUNT(), COUNT(DISTINCT)
>
>   ```mariadb
>   -- MAX, MIN
>   SELECT stdNAME, height FROM stdtbl 
>   	WHERE height = (SELECT MAX(height) FROM stdtbl) 
>   		OR height = (SELECT MIN(height) FROM stdtbl);
>   		
>   -- COUNT
>   SELECT COUNT(*) FROM stdtbl;
>   ```
>
>   
>
> * **HAVING** -  집계함수에서의 조건절 (집계함수와 where는 함께 할 수 X)
>
>   ```mariadb
>   SELECT stdname, height FROM stdtbl HAVING height > 170;
>   ```
>
> * **CHECK**
>
>   



> * **뷰**
> * **스토어드 프로시저**
> * **캐스케이드**

>```mariadb
>-- 기존의 테이블을 새롭게 복사
>CREATE TABLE new (SELECT stdname, height FROM stdtbl);
>```
>
>