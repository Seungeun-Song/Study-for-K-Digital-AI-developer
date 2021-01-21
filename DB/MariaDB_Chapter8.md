# Chapter 8. 테이블과 뷰

---

### 8-1. 테이블

### 8-1-2. 제약조건(primary, foreign, unique, check, default)

```mariadb
-- key가 어떻게 되어있는지
SHOW KEYS FROM usertbl;
```

```mariadb
SHOW INDEX FROM buytbl;
```

---

* **기본 키(PRIMARY KEY)**

  * 테이블에 존재하는 많은 행 데이터 구분 가능한 식별자
  * 자동으로 클러스트형 인덱스 생성(358p 참고)
  * `PRIMARY KEY` 

  ```mariadb
  DROP TABLE if EXISTS buyTBL, userTBL;
  CREATE TABLE userTBL
  (userID CHAR(8) NOT NULL PRIMARY KEY,
   NAME   VARCHAR(10) NOT NULL,
   birthYear  INT NOT null
   ); 
  ```

  ```mariadb
  DROP TABLE if EXISTS userTBL;
  CREATE TABLE userTBL
  (userID CHAR(8) NOT NULL,
   NAME   VARCHAR(10) NOT NULL,
   birthYear INT NOT NULL,
   CONSTRAINT PRIMARY KEY PK_userTBL_userID (userID)
   );
  ```

  * **ALTER TABLE** 

    ```mariadb
    ALTER TABLE usertbl
    	ADD PRIMARY KEY (userID); 
    ```

  * **PK** -  '제품코드 + 제품일련번호'

    ```mariadb
    DROP TABLE if EXISTS prodTbl;
    CREATE TABLE prodTbl
    (prodCode CHAR(3) NOT NULL,
     prodID CHAR(4) NOT NULL,
     prodDate DATETIME NOT NULL,
     prodCur CHAR(10) null
     );
     ALTER TABLE prodTbl
     	ADD CONSTRAINT PK_PRODTbl_proCode_prodID
     	PRIMARY KEY (prodCode,prodID);
    ```

    ```mariadb
    DROP TABLE if EXISTS prodTbl;
    CREATE TABLE prodTbl
    (prodCode CHAR(3) NOT NULL,
     prodID CHAR(4) NOT NULL,
     prodDate DATETIME NOT NULL,
     prodCur CHAR(10) null,
     CONSTRAINT PK_PRODTbl_proCode_prodID
     PRIMARY KEY (prodCode,prodID)
     );
    ```

  * **SHOW**

    ```mariadb
    SHOW INDEX FROM prodtbl;
    ```

---



* **외래 키** 테이블이 참조하는 기준 테이블의 열

  * 반드시 Primary Key or Unique 제약 조건이 설정되어 있어야 

  * **FOREIGN KEY**

    * 설정 - `FOREIGN KEY(열 이름) REFERENCES 열이 참조하는 기준 테이블 명(열 이름)` or 

     	 -- 이름지어주기 : FK는 하나의 테이블에 여러 개가 생성될 수 있으니까 이름을 지정해서 관리하는 것이 		편하다`CONSTRAINT 외래키의 이름 FOREINGN KEY(열 이름) REFERENCES 테이블명(열이름)`

    ```mariadb
    CREATE table buytbl
    (num INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
     userID CHAR(8) NOT NULL,
     prodName CHAR(6) NOT NULL,
     FOREIGN KEY(userID) REFERENCES usertbl(userID)
     );
    ```

    ```mariadb
    CREATE table buytbl
    (num INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
     userID CHAR(8) NOT NULL,
     prodName CHAR(6) NOT NULL,
     CONSTRAINT FK_usertbl_buytbl FOREIGN KEY(userID) REFERENCES usertbl(userID)
     );
    ```

    * **ALTER**

      ```mariadb
      ALTER TABLE prodtbl
      	ADD CONSTRAINT FK_usertbl_buytbl
      	FOREIGN KEY (userID)
      	REFERENCES usertbl(userID);
      ```

    * **DROP FOREIGN KEY**

      ```mariadb
      ALTER TABLE buytbl
      	DROP FOREIGN KEY KF_userTbl_buyTbl;
      ```

  * **ON UPDATE CASCADE/  ON DELETE CASCADE** 

    ```mariadb
    ALTER TABLE buytbl
    	ADD CONSTRAINT FK_userTbl_buyTbl
    	FOREIGN KEY (userID)
    	REFERENCES usertbl(userID)
    	ON UPDATE CASCADE;
    ```

    * **ON UPDATE NO ACTION / ON DELETE NO ACTION**- 별도로 지정하지 않으면 이것을 지정한 것과 동일. 회원 테이블의 회원 아이디가 변경되어도 아무런 일이 일어나지 않는다.

  

* **UNIQUE** - 중복되지 않는 유일한 값

  * PRIMARY KEY와 거의 비슷 <--> 차이점 : UNIQUE는 NULL값을 허용

  ```mariadb
  CREATE TABLE usertbl
  (userID CHAR(8) NOT NULL PRIMARY KEY,
   NAME VARCHAR(10) NOT NULL,
   birthYear INT NOT NULL,
   email CHAR(30) NULL unique
   );
  ```

  ```mariadb
   CREATE TABLE usertbl
   (userID CHAR(8) NOT NULL PRIMARY KEY,
   NAME VARCHAR(10) NOT NULL,
   birthYear INT NOT NULL,
   email CHAR(30) NULL,
   CONSTRAINT AK_email UNIQUE(email)   -- Unique는 주로 AK사용. (=Alternate Key)
   );
  ```

---



* **CHECK 제약조건** - 입력되는 데이터를 점검하는 기능

* * check 제약 조건 설정 후, 위배되는 값은 입력불가
  * ex)  키height에 마이너스 값이 들어올 수 없게 or 출생년도가 1900년 이후 등

  ```mariadb
  -- 출생연도가 1900년 이후, 2020년 이전, 이름은 반드시!!
  CREATE TABLE usertble
  (userID CHAR(8) NOT NULL PRIMARY KEY,
   NAME VARCHAR(10),
   birthYEar INT CHECK (birthYear >= 1900 AND birthYear<= 2000),
   mobile1 CHAR(3) NULL,
   CONSTRAINT CK_name CHECK (NAME IS NOT NULL)
   );
  ```

  * **ALTER**

    ```mariadb
    ALTER TABLE usertble
    	ADD CONSTRAINT CK_mobile1
    	CHECK (mobile1 IN ('010','011','016','017','018','019'));
    ```

---



* **DEFAULT 정의** - *값을 입력하지 않았을 때,* 자동으로 입력되는 기본값

  ```mariadb
  -- 출생연도를 입력하지 않으면 -1로 입력되고, 주소를 입력하지 않았다면 '서울'이 입력되며, 키를 입력하지 않으면 170이라고 입력되도록
  CREATE TABLE usertbl
  (userID CHAR(8) NOT NULL PRIMARY KEY,
  NAME VARCHAR(10) NOT NULL,
  birthYear INT NOT NULL DEFAULT -1,
  addr CHAR(2) NOT NULL DEFAULT '서울',
  mibile1 CHAR(3) NULL CHECK (mobile1 = '010'),
  mobile2 CHAR(8) NULL,
  height SMALLINT NULL DEFAULT 170,
  mdate DATE NULL
  );
  ```

  **ALTER COLUMN** 
  
  ```mariadb
  CREATE TABLE userTbl
  (userID CHAR(8) NOT NULL PRIMARY KEY,
   NAME VARCHAR(10) NOT NULL,
   birthYear INT NOT NULL,
   addr CHAR(2) NOT NULL,
   mobile1 CHAR(3) NULL CHECK (mobile1 ='010'),
   mobile2 CHAR(8) NULL,
   height SMALLINT NULL,
   mdate DATE null
   );
   
   
   ALTER TABLE usertbl
  	ALTER COLUMN birthYear SET DEFAULT -1;
  ALTER TABLE usertbl
  	ALTER COLUMN addr SET DEFAULT '서울';
  ALTER TABLE usertbl
  	ALTER COLUMN height SET DEFAULT 170;
  ```
  
  ```mariadb
  -- default 문은 DEFAULT로 설정된 값을 자동 입력한다.
  INSERT INTO userTBL VALUES ('LHL', '이혜리', default, default, '011', '1234567', default, '2022.12.12');
  
  -- 열이름이 명시되지 않으면 DEFAULT로 설정된 값을 자동 입력한다
  INSERT INTO userTBL(userID, name) VALUES('KAY', '김아영');
  
  -- 값이 직접 명기되면 DEFAULT로 설정된 값은 무시된다.
  INSERT INTO userTBL VALUES ('WB', '원빈', 1982, '대전', '019', '9876543', 176, '2023.5.5');
  SELECT * FROM userTBL;
  ```
  
  

---

### 8-1-6. 테이블 수정

* **열의 추가**

  ```mariadb
  ALTER TABLE usertbl
  	ADD homepage VARCHAR(30)
  		DEFAULT 'http://www.hanbit.co.kr'
  		null;
  ```

* **열의 삭제**

  ```mariadb
  ALTER TABLE usertbl
  	DROP COLUMN mobile1;
  ```

* **열의 이름 및 데이터 형식 변경**

  ```mariadb
  ALTER TABLE usertbl
  	CHANGE COLUMN NAME uname VARCHAR(20) NULL;
  ```

* **열의 제약 조건 추가 및 삭제** - PRIMARY KEY 삭제

  ```mariadb
  ALTER TABLE usertbl
  DROP PRIMARY KEY;
  ```



---

### 8-2.  뷰

* **뷰의 장점**

  * 보안

  * 복잡한 쿼리를 단순화

    ```mariadb
    SELECT U.uerid, U.name, B.prodName, U.addr, CONCAT(U.mobile1, U.mobile2) AS '연락처'
    FROM usertbl U
    	INNER JOIN buytbl B
    		ON U.userid = B.userID;
    ```

    --> 만약 이 쿼리를 자주 사용해야 한다면, 이 뷰를 생성해 놓고 사용자들은 해당 뷰만 접근 가능

    ```mariadb
    CREATE TABLE v_userbuyTbl
    AS 
    SELECT U.uerid, U.name, B.prodName, U.addr, CONCAT(U.mobile1, U.mobile2) AS '연락처'
    FROM usertbl U
    	INNER JOIN buytbl B
    		ON U.userid = B.userID;
    ```

    ```mariadb
    -- where절 사용가능
    SELECT * FROM v_userbuytbl WHERE NAME = N'김범수'
    ```

    

