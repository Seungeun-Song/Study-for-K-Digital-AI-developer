조장 컴퓨터로 DB, VIEW, URL, TEMPLATE 만들고 공유

-runserver로 돌렸을 때 에러.

1. 공유파일을 github에 올린 error - secret key 때문

   > Django로 startproject -> setting.py 에 있는 secret key를 github에서 보안처리.
   >
   > 따라서 secret key를 ignore파일로 JSON처리 하던지 or 압축하는 방식(과거로 타입슬랩ㅠㅠㅠ)

2. 파일을 조장한테 따로 받아 

3. python manage.py migrate - DB통합하기

4. python manage.py createsuperuser 생성



---

anaconda prompt에서 `mysql -u root -p` 실행문이 적용되지 않았다. 

```shell
(base) C:\Users\SONG>mysql -u root -p
'mysql'은(는) 내부 또는 외부 명령, 실행할 수 있는 프로그램, 또는
배치 파일이 아닙니다.
```

mariadb prompt창에서 가능. 

```
C:\Windows\System32>mysql -u root -p
Enter password: 1234
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 152
Server version: 10.5.8-MariaDB mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> create database db utf8;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 'utf8' at line 1
MariaDB [(none)]> create database db character set utf8;
Query OK, 1 row affected (0.003 sec)

MariaDB [(none)]> show databases;
```

 