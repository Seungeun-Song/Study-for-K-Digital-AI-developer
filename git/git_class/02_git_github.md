# Github

---

>Git은 **폴더 단위**로 프로젝트/코드를 관리!!!

---



## 1. TIL ?

* TIL은 Today I Learned의 줄임말로 개발자 사이에서 매일 자신이 학습한 내용을 commit(기록)하는 것.

* github, bitbucket, gitlab과 같은 원격 저장소에서 제공하는 1commit-1 grass의 흥미 요소 제공

* Git = **SCM**(Source Code Management) & **VCS**(Version Control System) 

  ​          코드 관리 & 버전관리



## 2. TIL 세팅

### (1) 환경설정 : `git config`

* 설치 후 한 번만
* ```git config --global [user.name] "사용자이름("John")"```
* ```git config --global [user.email] "사용자 이메일("John@gmail.com")"```
* 이름이나 이메일을 잘못 적었을 경우, 다시 ``git config --global [user.name] "Josh"`` 또는 `git config --global [user.email] "Josh@gmail.com"` 하여 덮어씀



### (2) git과의 소통 : `git status`

**가장 중요한 명령어**

* git의 상태를 출력

  ```sh
  $ git status
  ```

  ```
  On branch master
  
  No commits yet
  
  nothing to commit (create/copy files and use "git add" to track)
  ```

  * No commits yet : 아직 commit은 없다 (버전 == 스냅샷 == 특정상태 == 저장)
  * nothing to commit : commit 할 게 없다



### (3) Git으로 프로젝트 관리 시작 : `git init`

* 자신이 앞으로 학습한 내용을 기록할 `TIL`폴더를 하나 생성(`git mkdir [폴더명]`)한다. 이때 해당 폴더는 최상단에 생성한다.

* `git bash`에서 `TIL`폴더로 이동한 이후에 아래의 명령어로 `git`관리를 시작한다.

     "`.git`"폴더를 생성한다는 뜻 = "`master`"브랜치가 생성된다는 뜻

```sh
$ git init
```

```shell
$ touch a.txt
```

```sh
$ git status
```

```
On branch master

No commits yet

Untracked files:
(use "git add <file>..." to include in what will be committed)
      a.txt
      
nothing added to commit but untracked files present (use "git add" to track)
```

	* untracked files : 추적되지 않은 파일이 있다. (어떤 파일)
	* nothing added to commit but untracked files present : 커밋을 위해 staging area에 add된 파일은 없고, 추적되지 않은 파일은 있다.

```shell
* git 삭제
rm -r .git 
```

### (4) Commit을 위한 Staging : `git add [파일명]`

* 현재 코드 상태의 스냅샷을 찍기 위한 파일 선택 ( ==Staging Area에 파일 추가)

```sh
$ git add a.txt  # 파일명이 "." 은 모든 변경 사항을 staging area로 올리는 명령어($ git add .)
```

```
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file: a.txt
```

* Changes to be committed : commit될 준비가 된 파일이 있음



### (5) 버전 관리를 위한 스냅샷 저장 : `git commit -m [커밋 메시지]`

* 현재 상태에 대한 스냅샷으로 `commit`하여, 버전 관리를 진행한다.

* commit은 체크포인트를 만드는 것과 같은 행위

  * `-m` : message의 줄임말

  1. 언제 찍었는지
  2. 누가 찍었는지 ($ git config)
  3.  메시지



```shell
$ git commit -m 'Add a.txt'
```

```
On branch master
nothing to commit, working tree clean
```

* nothing to commit : commit 할 게 없음
* working tree(directory) clean : 작업 폴더가 깔끔



### (6) 버전 관리 이력을 조회 : `git log`

* git으로 지금까지 저장된 커밋들의 로그(아이디)를 출력
* `git log --oneline` : 한 줄로 커밋을 출력
* `git --log --[숫자] : 입력된 숫자만큼 역순으로 출력

```
commit 0912bb3256b7d885ce61966dfe17f886a8cb6055
Author: Seongeun Song <lilybad88@gmail.com>
Date:   Sat Jan 9 17:34:52 2021 +0900

    Add c.txt

commit 3e92d9f76be3007850bffdeceabcc7a13ccbada4
Author: Seongeun Song <lilybad88@gmail.com>
Date:   Sat Jan 9 17:34:33 2021 +0900

    Add b.txt

:
```

​		* `:`은 log의 목록이 한 화면에 출력하지 못할 만큼 많다는 뜻. 방향키를 통해 아래위로 이동가능

​		* 이 상태에서 exit 키는 - `Q`



### (7) git restore --staged [파일명]

staging area에 추가된 파일을 복원시키는 것



---

# 협업 도구로써의 git



### (8) 원격 저장소 정보 추가 : `git remote [원격 저장소의 이름(=origin)] [원격 저장소의 주소]

```sh
$ git remote	#git에 remote된 주소가 있는지 확인
```

```sh
$ git remote -v   #주소까지 상세 정보를 출력 (v = verbose mode, 말 수가 많은)
```

* Github 원격(remote) 저장소(repository)를 생성하고 `TIL`폴더와 연결한다
* 새로운 원격 저장소가 추가될 때만 입력한다.

```sh
$ git remote add origin https://github.com/github유저네임/저장소의이름  #해당 원격 저장소 정보 추가
```

```sh
$ git remote remove [원격저장소의 이름(=origin)]    #해당 원격 저장소 정보를 삭제
```

 

### (9) 원격 저장소로 업로드 : `git push [원격 저장소의 이름] [브랜치의 이름]`

* 최종적으로 Github 원격 저장소에 코드를 push(업로드, 밀어넣기)한다.

```sh
$ git push origin master
```

```shell
$ git push -u origin master   #업스트림(upstream)설정
```

* 로컬에서 원격으로 push할 경우 commit한 전부가 올라감. 선택적으로 push할 수 없어.



### (10) 원격 저장소에서 다운로드 : `git pull [원격저장소의 이름][브랜치의 이름]`

```sh
$ git pull origin master
```



### (11) 원격 저장소 복제하기 : `git clone [원격저장소의 주소]`

```sh
$ git clone ['https://github.com/John/new']
```

```
Cloning into 'new'...
remote : Counting objects: 70630, done.
remote : Compressing objects: 100% (20470/20470), done.
```





---

### (12) branch == 평형 세계

 1. branch 목록 조회 : `git branch`

    ​	현재 생성되어 있는 branch들의 목록을 출력

    ```sh
    $ git branch
    ```

    

2. branch 생성 : `git branch [브랜치 이름]`

   ```sh
   $ git branch [new]
   ```



3. branch 사이를 이동 : `git checkout [브랜치 이름]`

   ```sh
   $ git checkout new    #master branch -> new branch로 이동
   ```



4. branch 병합 : `git merge [브랜치 이름]`

   현재 속한 브랜치에서 인자로 주어진 브랜치를 합병

   ```sh
   $ git merge new   #master branch의 위치에서 [브랜치 이름]에 적힌 new branch를 병합 
   ```

   **(현재 브랜치가 master인지 확실히 확인!!!)**

   ```sh
   Hyuna@DESKTOP-69MIK67 MINGW64 ~/empty (master)
   $ git merge new
   Updating 4b7abe2..03dd7a0
   Fast-forward
    b.txt | 0
    1 file changed, 0 insertions(+), 0 deletions(-)
    create mode 100644 b.txt
   ```

   

5. 브랜치 삭제 : `git branch -d [브랜치 이름]`

   >(거의 모든, 주요 branch를 제외한) branch는 **일회용**이다. 병함ㅁ된 브랜치는 항상 삭제한다.

   * `-d` : 삭제 (delete)
   * `git branch -d new ` : new라는 브랜치를 삭제

   ```sh
   Hyuna@DESKTOP-69MIK67 MINGW64 ~/송승은 (master)
   $ git branch -d new
   Deleted branch new (was 42bc21d).
   ```

   

---

