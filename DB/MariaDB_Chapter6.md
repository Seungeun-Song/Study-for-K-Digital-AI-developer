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
SELECT 열이름
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

