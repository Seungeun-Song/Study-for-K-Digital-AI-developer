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
> * **INSERT INTO 테이블명 VALUES( , , )** 
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
> * **UPDATE  테이블명  SET  수정값  WHERE  조건**
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
>   -- PRIMARY KEY 삭제
>   ALTER TABLE 테이블명
>   	DROP PRIMARY KEY,
>   	CHANGE id id_no INT NOT NULL; -- AUTO_INCREMENT 삭제 = 컬럼명과 형태 변경, 
>
>   -- Foreign key 삭제
>   ALTER TABLE 테이블명
>   	DROP CONSTRAINT 외래키명;
>   ```
>
> * **외래키명 확인하기**
>
>   ```mariadb
>   SELECT * FROM information_schema.TABLE_CONSTRAINTS 
>   	WHERE TABLE_NAME = 'comment_board';
>   ```
>
>   
>
> * **인덱스 생성**
>
>
>   ```mariadb
>   ```mariadb
>   CREATE INDEX idx_addr ON stdtbl(addr);
> 
>   EXPLAIN SELECT * FROM stdtbl WHERE stdName='조용필';
>   -- key = 'primary key', type = const
>   EXPLAIN SELECT * FROM stdtbl WHERE addr = '서울';
>    -- 인덱스를 이용해 찾았다는 type ='ref'가 나타난다 key = 'idx_addr'
> 
>   SHOW INDEX FROM stdtbl;
> 
>   -- 인덱스 삭제
>   DROP INDEX 인덱스 이름 ON 테이블 이름;
> 
>   ```

---

> ## **데이터 조회와 활용**
>
> ```mariadb
> SHOW TABLES;
> SHOW TABLE STATUS;
> SHOW INDEX FROM stdtbl;
> 
> EXPLAIN SELECT * FROM stdtbl;
>  
> describe 테이블명;
> ```
>
> 
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
>   ```mariadb
>   SELECT B.userID, U.name, B.prodname, U.addr, CONCAT(mobile1,mobile2) AS '연락처'
>   	FROM buytbl B
>   	INNER JOIN usertbl U 
>   	 ON B.userID = U.userID
>   	 	 ORDER BY B.name ;
>   ```
>
>   
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

---

> ### 인덱스, 뷰, 스토어드 프로시저, 트리거 등의 활용
>
> * **뷰**
>
>   ```mariadb
>   CREATE VIEW userview_membertbl 
>   	AS SELECT membername, memberaddress FROM membertbl;
>   ```
>
> 
>
> * **스토어드 프로시저**
>
>   ```mariadb
>   DELIMITER $$
>   CREATE PROCEDURE userproc2(
>   	IN userbirth INT,     -- 변수값의 개념
>   	IN userheight INT
>   )
>   BEGIN 
>   	SELECT * FROM usertbl
>   		WHERE birthyear>userbirth AND height > userheight;
>   END $$
>   DELIMITER ;
>
>   CALL userproc2(1970,178);
>   ```
>
> * **트리거**
>
>   ```mariadb
>   CREATE TABLE deletednametbl(
>   	NAME CHAR(8),
>   	addr CHAR(20),
>   	tall INT,
>   	deletedDate date
>   );
>   ```
>   
>   ```mariadb
>     DELIMITER//
>     CREATE TRIGGER trg_deletedmembertbl    -- 트리거 이름
>     	AFTER DELETE	
>     	ON stdtbl									-- 트리거를 부착할 테이블
>     	FOR EACH ROW
>     BEGIN
>     	INSERT INTO deletednametbl				-- OLD 테이블의 내용을 백업 테이블에 삽입
>     		VALUES(OLD.stdname, OLD.addr, OLD.tall, CURDATE());
>     END //
>     DELIMITER ;
>   ```
>
> *  **INNER JOIN** - 두 개 이상의 테이블을 서로 묶어서 하나의 결과집합으로 만들어내는 것
>
>
>   ```mariadb
>   select 열 목록
>   from 첫번째 테이블
>   	inner join 두번째 테이블
>   	on 조인될 조건
>   where 검색조건
>   ```
>
>   ```mariadb
>   -- 세 개 이상 테이블 조인
>   SELECT S.stdname, S.addr, C.clubname, C.roomno
>   	FROM stdtbl S
>   		INNER JOIN stdclubtbl SC
>   			ON S.stdName = SC.stdName
>   	 	-- WHERE S.stdname = '공유';
>   		INNER JOIN clubtbl C
>   			ON SC.clubname = C.clubname
>   	ORDER BY S.stdname;
>   ```
>
> 
>
> * **캐스케이드**





>```mariadb
>-- 기존의 테이블을 새롭게 복사
>CREATE TABLE new (SELECT stdname, height FROM stdtbl);
>```
>
>* **SQL프로그래밍**
>
>  * **CASE** - if구문과 유사
>
>    ```mariadb
>    SELECT NAME, SUM(price*amount),  
>    	case
>    		when (SUM(price*amount) >= 1500) then '최우수고객'
>    	    when (SUM(price*amount) >= 1000) then '우수고객'
>    	    when (SUM(price*amount) >= 1) then '일반고객'
>    	    ELSE '유령고객'
>    	END AS '고객등급'     -- case 구문을 추가
>    	  
>    	FROM buytbl
>    		RIGHT OUTER JOIN usertbl
>    			ON buytbl.userID = usertbl.userID
>    	GROUP BY name
>    	ORDER BY SUM(price*amount) DESC;
>    ```
>
>  * **IF ... ELSE**
>
>    ```mariadb
>    DELIMITER  $$
>    CREATE PROCEDURE ifProc2()
>    BEGIN
>    	DECLARE hiredate DATE;  -- 입사일
>    	DECLARE CURDATE DATE;   -- 오늘
>    	DECLARE days INT;       -- 근무한 일수	
>    	
>    	SELECT hire_date INTO hiredate  --hire_date열의 결과를 hiredate에 대입
>    		FROM employees.employees
>    		WHERE emp_no = 10001;
>    		
>    	SET CURDATE = CURRENT_DATE(); -- 현재 날짜
>    	SET days = DATEDIFF(CURDATE, hiredate); -- 날짜의 차이, 일 단위
>    	
>    	if (days/365) >= 5 then -- 5년이 지났다면
>    			SELECT CONCAT('입사한지',days,'일이나 지났습니다. 축하합니다!');
>    	else
>    			SELECT '입사한지' + days + '일밖에 안되었네요. 열심히 일하세요';
>    	END if;
>    END $$
>    DELIMITER;
>    CALL ifproc2();
>    
>    ```
>
>    