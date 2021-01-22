```
>mongod --version

>mkdir c:\mongodb\test   -- mkdir 디렉토리 만들기 --mongodb 폴더 안에 test 만들기

>mongod --dbpath c:\mongodb\test  -- test 디렉토리 안에 서비스가 시작됨 = 인스턴스
                                 -- 인스턴스를 여러개 만들 수 있다.(분산, 복제)
```

```
-- 여러개 인스턴트 만들기

>mkdir c:\mongodb\test2
>mkdir c:\mongodb\test3

c:\> mongod --dbpath c:\mongodb\test  (server)

c:\> mongod --dbpath c:\mongodb\test1  (server1)

c:\> mongod --dbpath c:\mongodb\test2  (server2)

c:\> mongod --dbpath c:\mongodb\test3  (server3)
```



```shell
--> 다른 cmd 띄우기
>mongo localhost:27017  -- 접근하기
```

```
>db.help()   -db. = db에서의 명령어 시작
```

```
>use test -- 데이터베이스를 쓰겠다

>db.stats()
```

```
>db.stats()
---------------------------------------------------------------------------
 {
        "db" : "test",          <-DB명
        "collections" : 0,      <-컬렉션 수
        "views" : 0,            <-뷰어의 수
        "objects" : 0,          <-오브젝트 수
        "avgObjSize" : 0,       <-오브젝트의 평균 크기
        "dataSize" : 0,         <-데이터 크기
        "storageSize" : 0,      <-저장공간의 크기
        "numExtents" : 0,       <- 총 익스턴트 수
        "indexes" : 0,          <- 인덱스 수
        "indexSize" : 0,        <- 인덱스 크기
        "fsUsedSize" : 0,       <- 사용된 파일 크기
        "fsTotalSize" : 0,      <- 총 파일 크기
        "ok" : 1                <- 문장의 실행 상태(정상:1,  실패:0) 
}

```

```
>db.hostInfo()          <- 대소문자 구분O

----------------------------------------------
uncaught exception: TypeError: db.hostinfo is not a function :
@(shell):1:1
> db.hostInfo()
{
        "system" : {
                "currentTime" : ISODate("2021-01-22T04:21:41.288Z"),
                "hostname" : "DESKTOP-K52EVCT",
                "cpuAddrSize" : 64,
                "memSizeMB" : NumberLong(15790),
                "memLimitMB" : NumberLong(15790),
                "numCores" : 16,
                "cpuArch" : "x86_64",
                "numaEnabled" : false
        },
        "os" : {
                "type" : "Windows",
                "name" : "Microsoft Windows 10",
                "version" : "10.0 (build 19042)"
        },
        "extra" : {
                "pageSize" : NumberLong(4096),
                "physicalCores" : 8
        },
        "ok" : 1
}
```

```shell
>use admin
switched to db admin
>db.shutdownServer()   <-- 인스턴스(서버)를 shutdown하는 것 - 서버/인스턴트가 끊겨
server should be down...
>exit
bye
>db.logout()       <-- 인스턴스랑 연결이 끊김/ 다른 cmd에서는 인스턴트랑 연결 가능
{'ok':1}               연결만 끊고 mongo 프로그램에는 아직 존재
>exit              <-- mongo 프로그램에서 나가는 것
```

```
>use SALES
switched to db SALES       -- 데이터베이스가 없어도 내부적으로 임시 생성/ 스스로 적당히 판단

>db.createCollection ("employees" , {capped: true, size: 100000 })
{ "ok" : 1 }
>show collections
employees
>db.employees.stats()
{
        "ns" : "SALES.employees",
        "size" : 0,
        "count" : 0,
        "storageSize" : 4096,
        "freeStorageSize" : 0,
        "capped" : true,
        "max" : -1,
        "maxSize" : 100096,
        "sleepCount" : 0,
        "sleepMS" : 0,
        "wiredTiger" : {
                "metadata" : {
                        "formatVersion" : 1
                }, 
                
>db.emloyees.renameCollection("emp") -- 이름바꾸기
{ "ok" : 1 }
> show collections
emp
> db.emp.drop()  --삭제
true
> show collections
>               -- 내용 표시X = 삭제완료



>db.employees.insert({key:value})
>db.employees.find()
```



```
-- save()

> use test
switched to db test
> m={ename:"smith"}
{ "ename" : "smith" }
> n={empno:1101}
{ "empno" : 1101 }
> db.things.save(m)
WriteResult({ "nInserted" : 1 })
> db.things.save(n)
WriteResult({ "nInserted" : 1 })
> db.things.find()                      -- 저장된 데이터 검색 -> object ID 출력
{ "_id" : ObjectId("600a6d35de6141b859c2b137"), "ename" : "smith" }
{ "_id" : ObjectId("600a6d5cde6141b859c2b138"), "empno" : 1101 }
> show collections
things                      -- create 컬렉션 한적 없지만 만들어졌어!! 이런 방식으로도 생성가능

> db.things.stats()
{
        "ns" : "test.things",
        "size" : 76,
        "count" : 2,
        "avgObjSize" : 38,
        "storageSize" : 20480,
        "freeStorageSize" : 0,
        "capped" : false,
        "wiredTiger" : {
                "metadata" : {
                        "formatVersion" : 1
                },
```

```
--insert()

> db.things.insert({ empno : 1102, ename : "king"})
WriteResult({ "nInserted" : 1 })
> db.things.find()
{ "_id" : ObjectId("600a6d35de6141b859c2b137"), "ename" : "smith" }
{ "_id" : ObjectId("600a6d5cde6141b859c2b138"), "empno" : 1101 }
{ "_id" : ObjectId("600a6ff2de6141b859c2b139"), "empno" : 1102, "ename" : "king" }
> db.things.insert({empno:1101,job:"student"})
WriteResult({ "nInserted" : 1 })
> db.things.find()
{ "_id" : ObjectId("600a6d35de6141b859c2b137"), "ename" : "smith" }
{ "_id" : ObjectId("600a6d5cde6141b859c2b138"), "empno" : 1101 }
{ "_id" : ObjectId("600a6ff2de6141b859c2b139"), "empno" : 1102, "ename" : "king" }
{ "_id" : ObjectId("600a70aede6141b859c2b13a"), "empno" : 1101, "job" : "student" }
  -- 두번째 1101과 네번째 1101은 전혀 다른 것. ID주소자체가 달라.
>db.things.update({n:1103},{$set: {ename:"stanford",dept:"research" }}) 
  -- 이렇게 해야됨. RDBMS와는 다름!!
  
```

```
> for (var n = 1103; n <= 1120; n++) db.things.save({n : n , m : "test"})
       --var = 변수 선언/ n=1103 시작/ n<=1120 끝/ n++ 하나씩 증가/ n(키) :n(변수선언의 n- 넘버 증가), m(키):"test"(밸류)

> db.things.find()    <- FOR 반복문을 통해 증가된 값을 n 필드에 적용하여 데이터를 저장


> it      <- 출력된 결과가 20개를 초과하면 it 명령어로 다음 화면으로 이동
```

```
>  for (var n = 1103; n <= 1120; n++) db.things.save({n : n , m : "test"})
WriteResult({ "nInserted" : 1 })
> db.things.find()
{ "_id" : ObjectId("600a6d35de6141b859c2b137"), "ename" : "smith" }
{ "_id" : ObjectId("600a6d5cde6141b859c2b138"), "empno" : 1101 }
{ "_id" : ObjectId("600a6ff2de6141b859c2b139"), "empno" : 1102, "ename" : "king" }
{ "_id" : ObjectId("600a70aede6141b859c2b13a"), "empno" : 1101, "job" : "student" }
{ "_id" : ObjectId("600a72d5de6141b859c2b13b"), "n" : 1103, "m" : "test" }
{ "_id" : ObjectId("600a72d5de6141b859c2b13c"), "n" : 1104, "m" : "test" }
{ "_id" : ObjectId("600a72d5de6141b859c2b13d"), "n" : 1105, "m" : "test" }
{ "_id" : ObjectId("600a72d5de6141b859c2b13e"), "n" : 1106, "m" : "test" }
{ "_id" : ObjectId("600a72d5de6141b859c2b13f"), "n" : 1107, "m" : "test" }
{ "_id" : ObjectId("600a72d5de6141b859c2b140"), "n" : 1108, "m" : "test" }
{ "_id" : ObjectId("600a72d5de6141b859c2b141"), "n" : 1109, "m" : "test" }
{ "_id" : ObjectId("600a72d5de6141b859c2b142"), "n" : 1110, "m" : "test" }
{ "_id" : ObjectId("600a72d5de6141b859c2b143"), "n" : 1111, "m" : "test" }
{ "_id" : ObjectId("600a72d5de6141b859c2b144"), "n" : 1112, "m" : "test" }
{ "_id" : ObjectId("600a72d5de6141b859c2b145"), "n" : 1113, "m" : "test" }
{ "_id" : ObjectId("600a72d5de6141b859c2b146"), "n" : 1114, "m" : "test" }
{ "_id" : ObjectId("600a72d5de6141b859c2b147"), "n" : 1115, "m" : "test" }
{ "_id" : ObjectId("600a72d5de6141b859c2b148"), "n" : 1116, "m" : "test" }
{ "_id" : ObjectId("600a72d5de6141b859c2b149"), "n" : 1117, "m" : "test" }
{ "_id" : ObjectId("600a72d5de6141b859c2b14a"), "n" : 1118, "m" : "test" }
Type "it" for more
> it
{ "_id" : ObjectId("600a72d5de6141b859c2b14b"), "n" : 1119, "m" : "test" }
{ "_id" : ObjectId("600a72d5de6141b859c2b14c"), "n" : 1120, "m" : "test" }
```

```
-데이터 수정
> db.things.update({n:1103}, { $set: {ename : "standford", dept : "research"}})
WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })
> db.things.find()
{ "_id" : ObjectId("600a6d35de6141b859c2b137"), "ename" : "smith" }
{ "_id" : ObjectId("600a6d5cde6141b859c2b138"), "empno" : 1101 }
{ "_id" : ObjectId("600a6ff2de6141b859c2b139"), "empno" : 1102, "ename" : "king" }
{ "_id" : ObjectId("600a70aede6141b859c2b13a"), "empno" : 1101, "job" : "student" }
{ "_id" : ObjectId("600a72d5de6141b859c2b13b"), "n" : 1103, "m" : "test", "dept" : "research", "ename" : "standford" }
{ "_id" : ObjectId("600a72d5de6141b859c2b13c"), "n" : 1104, "m" : "test" }
{ "_id" : ObjectId("600a72d5de6141b859c2b13d"), "n" : 1105, "m" : "test" }
{ "_id" : ObjectId("600a72d5de6141b859c2b13e"), "n" : 1106, "m" : "test" }
{ "_id" : ObjectId("600a72d5de6141b859c2b13f"), "n" : 1107, "m" : "test" }
{ "_id" : ObjectId("600a72d5de6141b859c2b140"), "n" : 1108, "m" : "test" }
{ "_id" : ObjectId("600a72d5de6141b859c2b141"), "n" : 1109, "m" : "test" }
{ "_id" : ObjectId("600a72d5de6141b859c2b142"), "n" : 1110, "m" : "test" }
{ "_id" : ObjectId("600a72d5de6141b859c2b143"), "n" : 1111, "m" : "test" }
{ "_id" : ObjectId("600a72d5de6141b859c2b144"), "n" : 1112, "m" : "test" }
{ "_id" : ObjectId("600a72d5de6141b859c2b145"), "n" : 1113, "m" : "test" }
{ "_id" : ObjectId("600a72d5de6141b859c2b146"), "n" : 1114, "m" : "test" }
{ "_id" : ObjectId("600a72d5de6141b859c2b147"), "n" : 1115, "m" : "test" }
{ "_id" : ObjectId("600a72d5de6141b859c2b148"), "n" : 1116, "m" : "test" }
{ "_id" : ObjectId("600a72d5de6141b859c2b149"), "n" : 1117, "m" : "test" }
{ "_id" : ObjectId("600a72d5de6141b859c2b14a"), "n" : 1118, "m" : "test" }
Type "it" for more



> db.things.update({n:1104}, { $set: {ename : "John", dept : "inventory"}})
WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })
> db.things.update({n:1105}, { $set: {ename : "Jeo", dept : "accounting"}})
WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })
>  db.things.update({n:1106}, { $set: {ename : "king", dept : "research"}})
WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })
> db.things.update({n:1107}, { $set: {ename : "adams", dept : "personel"}})
WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })
>  db.things.update({n:1108}, { $set: {ename : "blake", dept : "inventory"}})
WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })
> db.things.update({n:1109}, { $set: {ename : "smith", dept : "accounting"}})
WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })
> db.things.update({n:1110}, { $set: {ename : "allen", dept : "research"}})
WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })
> db.things.update({n:1119}, { $set: {ename : "clief", dept : "human resource"}})
WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })
>  db.things.update({n:1120}, { $set: {ename : "miller", dept : "personel"}})
WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })
> db.things.find()
{ "_id" : ObjectId("600a6d35de6141b859c2b137"), "ename" : "smith" }
{ "_id" : ObjectId("600a6d5cde6141b859c2b138"), "empno" : 1101 }
{ "_id" : ObjectId("600a6ff2de6141b859c2b139"), "empno" : 1102, "ename" : "king" }
{ "_id" : ObjectId("600a70aede6141b859c2b13a"), "empno" : 1101, "job" : "student" }
{ "_id" : ObjectId("600a72d5de6141b859c2b13b"), "n" : 1103, "m" : "test", "dept" : "research", "ename" : "standford" }
{ "_id" : ObjectId("600a72d5de6141b859c2b13c"), "n" : 1104, "m" : "test", "dept" : "inventory", "ename" : "John" }
{ "_id" : ObjectId("600a72d5de6141b859c2b13d"), "n" : 1105, "m" : "test", "dept" : "accounting", "ename" : "Jeo" }
{ "_id" : ObjectId("600a72d5de6141b859c2b13e"), "n" : 1106, "m" : "test", "dept" : "research", "ename" : "king" }
{ "_id" : ObjectId("600a72d5de6141b859c2b13f"), "n" : 1107, "m" : "test", "dept" : "personel", "ename" : "adams" }
{ "_id" : ObjectId("600a72d5de6141b859c2b140"), "n" : 1108, "m" : "test", "dept" : "inventory", "ename" : "blake" }
{ "_id" : ObjectId("600a72d5de6141b859c2b141"), "n" : 1109, "m" : "test", "dept" : "accounting", "ename" : "smith" }
{ "_id" : ObjectId("600a72d5de6141b859c2b142"), "n" : 1110, "m" : "test", "dept" : "research", "ename" : "allen" }
{ "_id" : ObjectId("600a72d5de6141b859c2b143"), "n" : 1111, "m" : "test" }
{ "_id" : ObjectId("600a72d5de6141b859c2b144"), "n" : 1112, "m" : "test" }
{ "_id" : ObjectId("600a72d5de6141b859c2b145"), "n" : 1113, "m" : "test" }
{ "_id" : ObjectId("600a72d5de6141b859c2b146"), "n" : 1114, "m" : "test" }
{ "_id" : ObjectId("600a72d5de6141b859c2b147"), "n" : 1115, "m" : "test" }
{ "_id" : ObjectId("600a72d5de6141b859c2b148"), "n" : 1116, "m" : "test" }
{ "_id" : ObjectId("600a72d5de6141b859c2b149"), "n" : 1117, "m" : "test" }
{ "_id" : ObjectId("600a72d5de6141b859c2b14a"), "n" : 1118, "m" : "test" }
Type "it" for more
> it
{ "_id" : ObjectId("600a72d5de6141b859c2b14b"), "n" : 1119, "m" : "test", "dept" : "human resource", "ename" : "clief" }
{ "_id" : ObjectId("600a72d5de6141b859c2b14c"), "n" : 1120, "m" : "test", "dept" : "personel", "ename" : "miller" }
```

```
-- save

 db.things.save({empno : 1101, ename : "Blake", dept : "account"})
WriteResult({ "nInserted" : 1 })
> db.things.find()
{ "_id" : ObjectId("600a6d35de6141b859c2b137"), "ename" : "smith" }
{ "_id" : ObjectId("600a6d5cde6141b859c2b138"), "empno" : 1101 }
{ "_id" : ObjectId("600a6ff2de6141b859c2b139"), "empno" : 1102, "ename" : "king" }
{ "_id" : ObjectId("600a70aede6141b859c2b13a"), "empno" : 1101, "job" : "student" }
{ "_id" : ObjectId("600a72d5de6141b859c2b13b"), "n" : 1103, "m" : "test", "dept" : "research", "ename" : "standford" }
{ "_id" : ObjectId("600a72d5de6141b859c2b13c"), "n" : 1104, "m" : "test", "dept" : "inventory", "ename" : "John" }
{ "_id" : ObjectId("600a72d5de6141b859c2b13d"), "n" : 1105, "m" : "test", "dept" : "accounting", "ename" : "Jeo" }
{ "_id" : ObjectId("600a72d5de6141b859c2b13e"), "n" : 1106, "m" : "test", "dept" : "research", "ename" : "king" }
{ "_id" : ObjectId("600a72d5de6141b859c2b13f"), "n" : 1107, "m" : "test", "dept" : "personel", "ename" : "adams" }
{ "_id" : ObjectId("600a72d5de6141b859c2b140"), "n" : 1108, "m" : "test", "dept" : "inventory", "ename" : "blake" }
{ "_id" : ObjectId("600a72d5de6141b859c2b141"), "n" : 1109, "m" : "test", "dept" : "accounting", "ename" : "smith" }
{ "_id" : ObjectId("600a72d5de6141b859c2b142"), "n" : 1110, "m" : "test", "dept" : "research", "ename" : "allen" }
{ "_id" : ObjectId("600a72d5de6141b859c2b143"), "n" : 1111, "m" : "test" }
{ "_id" : ObjectId("600a72d5de6141b859c2b144"), "n" : 1112, "m" : "test" }
{ "_id" : ObjectId("600a72d5de6141b859c2b145"), "n" : 1113, "m" : "test" }
{ "_id" : ObjectId("600a72d5de6141b859c2b146"), "n" : 1114, "m" : "test" }
{ "_id" : ObjectId("600a72d5de6141b859c2b147"), "n" : 1115, "m" : "test" }
{ "_id" : ObjectId("600a72d5de6141b859c2b148"), "n" : 1116, "m" : "test" }
{ "_id" : ObjectId("600a72d5de6141b859c2b149"), "n" : 1117, "m" : "test" }
{ "_id" : ObjectId("600a72d5de6141b859c2b14a"), "n" : 1118, "m" : "test" }
Type "it" for more
> it
{ "_id" : ObjectId("600a72d5de6141b859c2b14b"), "n" : 1119, "m" : "test", "dept" : "human resource", "ename" : "clief" }
{ "_id" : ObjectId("600a72d5de6141b859c2b14c"), "n" : 1120, "m" : "test", "dept" : "personel", "ename" : "miller" }
{ "_id" : ObjectId("600a74cfde6141b859c2b14e"), "empno" : 1101, "ename" : "Blake", "dept" : "account" }
```

```
-- 데이터 제거하기 remove

> db.things.remove({m:"test"})
WriteResult({ "nRemoved" : 18 })
> db.things.find()
{ "_id" : ObjectId("600a6d35de6141b859c2b137"), "ename" : "smith" }
{ "_id" : ObjectId("600a6d5cde6141b859c2b138"), "empno" : 1101 }
{ "_id" : ObjectId("600a6ff2de6141b859c2b139"), "empno" : 1102, "ename" : "king" }
{ "_id" : ObjectId("600a70aede6141b859c2b13a"), "empno" : 1101, "job" : "student" }
{ "_id" : ObjectId("600a74cfde6141b859c2b14e"), "empno" : 1101, "ename" : "Blake", "dept" : "account" }

> db.things.remove({})   -- 모조리 삭제
WriteResult({ "nRemoved" : 5 })
> db.things.find()
>  --삭제 완료
> show collections
things  -- 데이터만 지워지고 컬렉션은 남아
> db.things.drop()  -컬렉션 삭제
true
> show collections 
>          -- 컬렉션 아무것도 없어
>show dbs  -- 처음에도 보이지 않았어. 직접 저장한게 X 따라서 메모리에만 가상으로 생성

```









