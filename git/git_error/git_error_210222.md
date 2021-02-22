### Git 명령을 사용하지 않고 단순히 워킹 디렉터리에서 파일을 삭제하고 `git status` 명령으로 상태를 확인하면 Git은 현재 “Changes not staged for commit” (즉, *Unstaged* 상태)라고 표시



**git pull origin master**

```
SONG@DESKTOP-K52EVCT MINGW64 ~/utilization/webscraping_basic (master)
$ git pull origin master
From https://github.com/Seungeun-Song/utilization
 * branch            master     -> FETCH_HEAD
Already up to date.
```



**git push**

```
SONG@DESKTOP-K52EVCT MINGW64 ~/utilization/webscraping_basic (master)
$ git push
fatal: The current branch master has no upstream branch.
To push the current branch and set the remote as upstream, use

    git push --set-upstream origin master
```







**git push --set-upstream origin master**

```
SONG@DESKTOP-K52EVCT MINGW64 ~/utilization/webscraping_basic (master)
$ git push --set-upstream origin master
Everything up-to-date
Branch 'master' set up to track remote branch 'master' from 'origin'.
```







**git push origin master**

```
SONG@DESKTOP-K52EVCT MINGW64 ~/utilization/webscraping_basic (master)
$ git push origin master
Everything up-to-date
```





**git status**

```
SONG@DESKTOP-K52EVCT MINGW64 ~/utilization/webscraping_basic/gui_basic (master)
$ git status
On branch master
Your branch is up to date with 'origin/master'.

Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        deleted:    ../10_bs4_coupang_pages.py
        deleted:    ../11_daum_movies.py
        deleted:    ../12_csv_stock.py
        deleted:    ../13_selenium.py
        deleted:    ../14_selenium_naver_login.py
        deleted:    ../15_selenium_flight.py
        deleted:    ../15_selenium_movie.py
        deleted:    ../16_selenium_movies_scroll.py
        deleted:    ../17_headless_chrome.py
        deleted:    ../18_headless_chrome_useragent.py
        deleted:    ../19_ quiz.py
        deleted:    ../19_quiz_with_teacher.py
        deleted:    ../1_html.html
        deleted:    ../20_my_secretary.py
        deleted:    ../20_my_secretary_practice.py
        deleted:    ../20_my_secretary_question.py
        deleted:    ../20_my_secretary_with_teacher.py
        deleted:    ../2_xpath.txt
        deleted:    ../3_requests.py
        deleted:    ../4_re.py
        deleted:    ../5_user_agent.py
        deleted:    ../6_bs4.py
        deleted:    ../7_bs4_webtoons.py
        deleted:    ../8_bs4_gauss.py
        deleted:    ../9_bs4_coupang.py
        deleted:    ../mygoogle.html
        deleted:    ../nadocoding.html

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        ../../chromedriver.exe
        ../../google_movie.png
        ../../movie.html
        ../../quiz.html
        ./
        ../rpa_basic/

no changes added to commit (use "git add" and/or "git commit -a")
```





**git rm   <filename>**

```
SONG@DESKTOP-K52EVCT MINGW64 ~/utilization/webscraping_basic (master)
$ git rm 1_html.html  2_xpath.txt 3_requests.py 4_re.py 5_user_agent.py 6_bs4.py 7_bs4_webtoons.py 8_bs4_gauss.py 9_bs4_coupang.py 10_bs4_coupang_pages.py 11_daum_movies.py 12_csv_stock.py 13_selenium.py 14_selenium_naver_login.py
rm 'webscraping_basic/10_bs4_coupang_pages.py'
rm 'webscraping_basic/11_daum_movies.py'
rm 'webscraping_basic/12_csv_stock.py'
rm 'webscraping_basic/13_selenium.py'
rm 'webscraping_basic/14_selenium_naver_login.py'
rm 'webscraping_basic/1_html.html'
rm 'webscraping_basic/2_xpath.txt'
rm 'webscraping_basic/3_requests.py'
rm 'webscraping_basic/4_re.py'
rm 'webscraping_basic/5_user_agent.py'
rm 'webscraping_basic/6_bs4.py'
rm 'webscraping_basic/7_bs4_webtoons.py'
rm 'webscraping_basic/8_bs4_gauss.py'
rm 'webscraping_basic/9_bs4_coupang.py'


```



**git status**

```
SONG@DESKTOP-K52EVCT MINGW64 ~/utilization/webscraping_basic/gui_basic (master)
$ git status
On branch master
Your branch is up to date with 'origin/master'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        deleted:    10_bs4_coupang_pages.py
        deleted:    11_daum_movies.py
        deleted:    12_csv_stock.py
        deleted:    13_selenium.py
        deleted:    14_selenium_naver_login.py
        deleted:    1_html.html
        deleted:    2_xpath.txt
        deleted:    3_requests.py
        deleted:    4_re.py
        deleted:    5_user_agent.py
        deleted:    6_bs4.py
        deleted:    7_bs4_webtoons.py
        deleted:    8_bs4_gauss.py
        deleted:    9_bs4_coupang.py

Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        deleted:    15_selenium_flight.py
        deleted:    15_selenium_movie.py
        deleted:    16_selenium_movies_scroll.py
        deleted:    17_headless_chrome.py
        deleted:    18_headless_chrome_useragent.py

```





**git add ***

```
SONG@DESKTOP-K52EVCT MINGW64 ~/utilization/webscraping_basic (master)
$ git add *
```





**git commit -m "All"**

```
SONG@DESKTOP-K52EVCT MINGW64 ~/utilization/webscraping_basic (master)
$ git commit -m "All"
[master a89371c] All
 29 files changed, 1671 insertions(+)
 rename webscraping_basic/{ => gui_basic}/10_bs4_coupang_pages.py (100%)
 rename webscraping_basic/{ => gui_basic}/11_daum_movies.py (100%)
 rename webscraping_basic/{ => gui_basic}/12_csv_stock.py (100%)
 rename webscraping_basic/{ => gui_basic}/13_selenium.py (100%)
 rename webscraping_basic/{ => gui_basic}/14_selenium_naver_login.py (100%)
 create mode 100644 webscraping_basic/gui_basic/15_selenium_flight.py
 create mode 100644 webscraping_basic/gui_basic/15_selenium_movie.py
 create mode 100644 webscraping_basic/gui_basic/16_selenium_movies_scroll.py
 create mode 100644 webscraping_basic/gui_basic/17_headless_chrome.py
 create mode 100644 webscraping_basic/gui_basic/18_headless_chrome_useragent.py
 create mode 100644 webscraping_basic/gui_basic/19_ quiz.py
 create mode 100644 webscraping_basic/gui_basic/19_quiz_with_teacher.py
 rename webscraping_basic/{ => gui_basic}/1_html.html (100%)
 create mode 100644 webscraping_basic/gui_basic/20_my_secretary.py
 create mode 100644 webscraping_basic/gui_basic/20_my_secretary_practice.py
 create mode 100644 webscraping_basic/gui_basic/20_my_secretary_question.py
 create mode 100644 webscraping_basic/gui_basic/20_my_secretary_with_teacher.py
 rename webscraping_basic/{ => gui_basic}/2_xpath.txt (100%)
 rename webscraping_basic/{ => gui_basic}/3_requests.py (100%)
 rename webscraping_basic/{ => gui_basic}/4_re.py (100%)
 rename webscraping_basic/{ => gui_basic}/5_user_agent.py (100%)
 rename webscraping_basic/{ => gui_basic}/6_bs4.py (100%)
 rename webscraping_basic/{ => gui_basic}/7_bs4_webtoons.py (100%)
 rename webscraping_basic/{ => gui_basic}/8_bs4_gauss.py (100%)
 rename webscraping_basic/{ => gui_basic}/9_bs4_coupang.py (100%)
 create mode 100644 webscraping_basic/gui_basic/mygoogle.html
 create mode 100644 webscraping_basic/gui_basic/nadocoding.html
 create mode 100644 "webscraping_basic/gui_basic/\354\213\234\352\260\200\354\264\235\354\225\2411-200.csv"
 create mode 100644 webscraping_basic/rpa_basic/3.web/1)html.html
```





**git push origin master**

```
SONG@DESKTOP-K52EVCT MINGW64 ~/utilization/webscraping_basic (master)
$ git push origin master
Enumerating objects: 10, done.
Counting objects: 100% (10/10), done.
Delta compression using up to 16 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (8/8), 9.74 KiB | 1.22 MiB/s, done.
Total 8 (delta 1), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/Seungeun-Song/utilization.git
   fc2b2d9..a89371c  master -> master
```

