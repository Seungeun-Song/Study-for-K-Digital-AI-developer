* command prompt 창에서 접근 명령어 

    ```
    mysql -u(user) root -p => use sqldb
    ```

    

* <NoSQL 운영 경험이 있는 분 = 분산 서버(DB)를 운영해본 경험이 있는지O, NoSQL의 개념을 아는지X>

    -> 요구하는 경험이 없더라도 회사에서 요구하는 자격사항, 우대사항을 분석 후 그것에 대해 서술해보기!!

   --> 공부만 하지 말고!! 경험까지!!



* DB생성 

  ```MariaDB 
  create database '데이터베이스명' utf8; 
  
  MariaDB [(none)]> create database roofdb utf8; 
  ```

* DB보기 

  ```
  MariaDB [(none)]> show databases;
  ```

* DB삭제

  ```
  DROP DATABASE "삭제 할 데이터베이스 명";
  ```