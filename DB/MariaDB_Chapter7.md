# 7. SQL 고급

---

## 7-1. 데이터 형식

* 변수 사용 - 스토어드 프로시저나 함수 안에서 변수를 사용하려면 DECLARE 문 필요

```mariadb
-- 변수의 선언과 값의 대입 형식

SET @변수이름 = 변수의 값;    -- 변수의 선언 및 값 대입
SELECT @변수이름;            -- 변수의 값 출력
```

```mariadb
USE sqlDB;
SET @myVar1 = 5 ;
SET @myVar2 = 3 ;
SET @myVar3 = 4.25 ;
SET @myVar4 = '가수 이름==> ' ;

SELECT @myVar1 ;

SELECT @myVar2 + @myVar3 ;

SELECT @myVar4 , Name FROM userTBL WHERE height > 180 ;
```

* **PREPARE 쿼리이름 FROM 쿼리문** --> **EXECUTE  쿼리이름  USING @변수**

```mariadb
SET @myVar1 = 3 ;
PREPARE myQuery 
    FROM 'SELECT Name, height FROM userTBL ORDER BY height LIMIT ?';
    -- = 'SELECT Name, height FROM userTBL ORDER BY height LIMIT 3'
EXECUTE myQuery USING @myVar1 ;
```



* 데이터 형식과 형 변환
  * CAST() , CONVERT(),  CONCAT(), CONCAT_WS

```mariadb
SELECT CAST(AVG(amount) AS SIGNED INTEGER) AS '평균 구매 개수'  FROM buyTBL ;
-- 또는
SELECT CONVERT(AVG(amount) , SIGNED INTEGER) AS '평균 구매 개수'  FROM buyTBL ;

```

```mariadb
SELECT CAST('2022$12$12' AS DATE);
SELECT CAST('2022/12/12' AS DATE);
SELECT CAST('2022%12%12' AS DATE);
SELECT CAST('2022@12@12' AS DATE);
```

```mariadb
-- CONCAT : 문자열을 연결하는
SELECT num, CONCAT(CAST(price AS CHAR(10)), 'X', CAST(amount AS CHAR(4)) ,'=' )  AS '단가X수량',
	price*amount AS '구매액' 
  FROM buyTBL ;

```



###  7-2. 내장함수와 윈도 함수

* IF(수식, 참, 거짓)

* IFNULL(수식1, 수식2) - NULL인지 아닌지 판단하기 위함. 

* NULLIF(수식1, 수식2) -수식1과2가 같은지

* CASE ~ WHEN ~ ELSE ~ END

  ```mariadb
  SELCET CASE 10    -- CASE 뒤의 값이 10
  	WHEN 1 THEN '일'
  	WHEN 5 THEN '오'
  	WHEN 10 THEN '십'
  	ELSE '모름'
  END;
  ```

* FORMAT

  ```mariadb
  SELECT FORMAT(123456.123456, 4);
  ```

* INSERT
* LEFT(문자열, 길이), RIGHT(문자열, 길이)
* UPPER, LOWER
* SYSADATE(), NOW(), CURDATE(), CURTIME()   - 날짜, 시간 함수



### 7-3 조인

#### 7-3-1. INNER JOIN - 내부조인 (교집합X --> 링크되어 있는 부분)

```mariadb
SELECT 열 목록 
FROM 첫번째 테이블                   -- 테이블의 순서에 따라 속도가 달라질 수도.
	INNER JOIN 두번째 테이블         -- 첫번째 테이블 값을 전부 읽고 두번째 테이블을 읽게 되는
	ON 조인될 조건
WHERE 검색조건
```

```mariadb
-- 구매 내역이 있는(양쪽 테이블에 데이터가 있는) 데이터만 출력되는 것
SELECT *
	FROM buytbl
		INNER JOIN usertbl
			ON buytbl.userID = usertbl.userID
	WHERE buytbl.userID ='JYP';
```

```mariadb
SELECT *
	FROM usertbl
		INNER JOIN buytbl
			ON usertbl.userID = buytbl.userID
	WHERE usertbl.userID='JYP';			
```

```mariadb
-- 출력 열 선택
SELECT buytbl.userID, NAME,prodName, CONCAT(mobile1, mobile2)-- userID가 불확실하다는 오류
	FROM buytbl 								  -- 어느테이블의 .userID
		INNER JOIN usertbl
			ON buytbl.userID = usertbl.userID
```

```mariadb
-- AS 별칭사용
SELECT B.userid, U.name, B.prodname, U.addr, CONCAT(U.mobile1, U.mobile2) AS '연락처'
	FROM buytbl B
		INNER join usertbl U
			ON B.userID = U.userID;
	WHERE U.userID='JYP';	
```



**DISTINCT** 

```mariadb
-- 한 번이라도 구매한 기록이 있는 회원에게 감사 안내문을 발송하기 위해 주소록 뽑기
SELECT DISTINCT u.userid, u.name, u.addr
	FROM usertbl u
		INNER JOIN buytbl b
			ON u.userid = b.userID
		ORDER BY NAME;
```

**EXIST**

```mariadb
SELECT u.userid, u.name, u.addr
	FROM usertbl u
		WHERE EXISTS(
			SELECT *
			FROM buytbl b
			WHERE u.userID = b.userid);
```

**세 개 테이블 조인**

```mariadb
-- 학생 기준으로 학생 이름 / 지역/ 가입 동아리/ 동아리방을 출력
ALTER TABLE stdclubtbl
	ADD CONSTRAINT FK_clubname FOREIGN KEY (clubname) REFERENCES clubtbl(clubname);
```



#### 7-3-2. OUTER JOIN(차집합X --> 링크되지 않은 부분도 전부)

**LEFT/ RIGHT OUTERJOIN에 따라 차집합의 값이 달라짐**

```mariadb
USE sqlDB;
SELECT U.userID, U.name, B.prodName, U.addr, CONCAT(U.mobile1, U.mobile2)  AS '연락처'
   FROM userTBL U
      LEFT OUTER JOIN buyTBL B
         ON U.userID = B.userID 
   ORDER BY U.userID;

SELECT U.userID, U.name, B.prodName, U.addr, CONCAT(U.mobile1, U.mobile2)  AS '연락처'
   FROM buyTBL B 
      RIGHT OUTER JOIN userTBL U
         ON U.userID = B.userID 
   ORDER BY U.userID;

```

* **UNION으로 FULL JOIN**

  * SELECT 필드명이 UNION의 SELECT 필드명과 같지 않으면 에러

  ```mariadb
  SELECT S.stdName, S.addr, C.clubName, C.roomNo
     FROM stdTBL S 
        LEFT OUTER JOIN stdclubTBL SC
            ON S.stdName = SC.stdName
        LEFT OUTER JOIN clubTBL C
            ON SC.clubName = C.clubName
  UNION 
  SELECT S.stdName, S.addr, C.clubName, C.roomNo
     FROM  stdTBL S
        LEFT OUTER JOIN stdclubTBL SC
            ON SC.stdName = S.stdName
        RIGHT OUTER JOIN clubTBL C
            ON SC.clubName = C.clubName;
  
  ```



#### 7-3-4. SELF JOIN

```mariadb
SELECT A.emp AS '부하직원' , B.emp AS '직속상관', B.empTel AS '직속상관연락처'
   FROM empTbl A
      INNER JOIN empTbl B
         ON A.manager = B.emp
   WHERE A.emp = '우대리';

```



#### 7-3-5 UNION/ UNION ALL/ NOT IN/ IN

```mariadb
-- NOT IN
SELECT name, CONCAT(mobile1, mobile2) AS '전화번호' FROM userTBL
   WHERE name NOT IN ( SELECT name FROM userTBL WHERE mobile1 IS NULL) ;

-- IN
SELECT name, CONCAT(mobile1, mobile2) AS '전화번호' FROM userTBL
   WHERE name IN ( SELECT name FROM userTBL WHERE mobile1 IS NULL) ;

```



---

### 7-4. SQL 프로그래밍

**스토어드 프로시저 만드는 법**

```
DELIMITER $$
CREATE PROCEDURE 스토어드 프로시저이름()
BEGIN
  이 부분에 SQL 프로그래밍 코딩
END $$
DELIMITER;
CALL 스토어드 프로시저이름();
```

* IF ~ ELSE

```mariadb
DROP PROCEDURE IF EXISTS ifProc; -- 기존에 만든적이 있다면 삭제
DELIMITER $$
CREATE PROCEDURE ifProc()
BEGIN
  DECLARE var1 INT;  -- var1 변수선언
  SET var1 = 100;  -- 변수에 값 대입

  IF var1 = 100 THEN  -- 만약 @var1이 100이라면,
	SELECT '100입니다.';
  ELSE
    SELECT '100이 아닙니다.';
  END IF;
END $$
DELIMITER ;
CALL ifProc();

```

```mariadb
DROP PROCEDURE IF EXISTS ifProc3; 
DELIMITER $$
CREATE PROCEDURE ifProc3()
BEGIN
    DECLARE point INT ;
    DECLARE credit CHAR(1);
    SET point = 77 ;
    
    IF point >= 90 THEN
		SET credit = 'A';
    ELSEIF point >= 80 THEN
		SET credit = 'B';
    ELSEIF point >= 70 THEN
		SET credit = 'C';
    ELSEIF point >= 60 THEN
		SET credit = 'D';
    ELSE
		SET credit = 'F';
    END IF;
    SELECT CONCAT('취득점수==>', point), CONCAT('학점==>', credit);
END $$
DELIMITER ;
CALL ifProc3();

```

```mariadb
-- CASE 사용

DROP PROCEDURE IF EXISTS caseProc; 
DELIMITER $$
CREATE PROCEDURE caseProc()
BEGIN
    DECLARE point INT ;
    DECLARE credit CHAR(1);
    SET point = 77 ;
    
    CASE 
		WHEN point >= 90 THEN
			SET credit = 'A';
		WHEN point >= 80 THEN
			SET credit = 'B';
		WHEN point >= 70 THEN
			SET credit = 'C';
		WHEN point >= 60 THEN
			SET credit = 'D';
		ELSE
			SET credit = 'F';
    END CASE;
    SELECT CONCAT('취득점수==>', point), CONCAT('학점==>', credit);
END $$
DELIMITER ;
CALL caseProc();

```



#### 7-4-4 오류처리

```mariadb
USE sqlDB;
DROP TABLE IF EXISTS myTable;
CREATE TABLE myTable (id INT AUTO_INCREMENT PRIMARY KEY, mDate DATETIME);

SET @curDATE = CURRENT_TIMESTAMP(); -- 현재 날짜와 시간

PREPARE myQuery FROM 'INSERT INTO myTable VALUES(NULL, ?)';
EXECUTE myQuery USING @curDATE;
DEALLOCATE PREPARE myQuery;

SELECT * FROM myTable;

```



