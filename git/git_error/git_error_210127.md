```shell
SONG@DESKTOP-K52EVCT MINGW64 ~/multi_campus/Web/HTML_CSS_JS (master|MERGING)
$ git checkout master
error: you need to resolve your current index first
Web/HTML_CSS_JS/01.HTML_기본문법.md: needs merge
Web/HTML_CSS_JS/JavaScript.html: needs merge
Web/HTML_CSS_JS/style.css: needs merge


```



```shell
SONG@DESKTOP-K52EVCT MINGW64 ~/multi_campus/Web/HTML_CSS_JS (master|MERGING)
$ git push origin master
To https://github.com/Seungeun-Song/Study-for-K-Digital-AI-developer.git
 ! [rejected]        master -> master (non-fast-forward)
error: failed to push some refs to 'https://github.com/Seungeun-Song/Study-for-K-Digital-AI-developer.git'
hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. Integrate the remote changes (e.g.
hint: 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.


```

```
SONG@DESKTOP-K52EVCT MINGW64 ~/multi_campus/Web/HTML_CSS_JS (master|MERGING)
$ git pull origin master
error: Pulling is not possible because you have unmerged files.
hint: Fix them up in the work tree, and then use 'git add/rm <file>'
hint: as appropriate to mark resolution and make a commit.
fatal: Exiting because of an unresolved conflict.

```

### $ git reset --merge

```shell
SONG@DESKTOP-K52EVCT MINGW64 ~/multi_campus/Web/HTML_CSS_JS (master|MERGING)
$ git reset --merge

SONG@DESKTOP-K52EVCT MINGW64 ~/multi_campus/Web/HTML_CSS_JS (master)


```

```shell
SONG@DESKTOP-K52EVCT MINGW64 ~/multi_campus/Web/HTML_CSS_JS (master)
$ git pull origin master
From https://github.com/Seungeun-Song/Study-for-K-Digital-AI-developer
 * branch            master     -> FETCH_HEAD
CONFLICT (rename/add): Rename Web/style.css->Web/HTML_CSS_JS/style.css in 5fc5016ef6a3725cde053773c05605e5c1ccbc49.  Added Web/HTML_CSS_JS/style.css in HEAD
Auto-merging Web/HTML_CSS_JS/style.css
CONFLICT (rename/add): Rename Web/JavaScript.html->Web/HTML_CSS_JS/JavaScript.html in 5fc5016ef6a3725cde053773c05605e5c1ccbc49.  Added Web/HTML_CSS_JS/JavaScript.html in HEAD
Auto-merging Web/HTML_CSS_JS/JavaScript.html
CONFLICT (rename/add): Rename Web/01.HTML_기본문법.md->Web/HTML_CSS_JS/01.HTML_기본문법.md in 5fc5016ef6a3725cde053773c05605e5c1ccbc49.  Added Web/HTML_CSS_JS/01.HTML_기본문법.md in HEAD
Auto-merging Web/HTML_CSS_JS/01.HTML_기본문법.md
Automatic merge failed; fix conflicts and then commit the result.

SONG@DESKTOP-K52EVCT MINGW64 ~/multi_campus/Web/HTML_CSS_JS (master|MERGING)

```

```shell
SONG@DESKTOP-K52EVCT MINGW64 ~/multi_campus/Web/HTML_CSS_JS (master|MERGING)
$ git reset --merge

SONG@DESKTOP-K52EVCT MINGW64 ~/multi_campus/Web/HTML_CSS_JS (master)
$ git push origin master
To https://github.com/Seungeun-Song/Study-for-K-Digital-AI-developer.git
 ! [rejected]        master -> master (non-fast-forward)
error: failed to push some refs to 'https://github.com/Seungeun-Song/Study-for-K-Digital-AI-developer.git'
hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. Integrate the remote changes (e.g.
hint: 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.

```

```shell
SONG@DESKTOP-K52EVCT MINGW64 ~/multi_campus/Web/HTML_CSS_JS (master|MERGING)
$ git merge FETCH
error: Merging is not possible because you have unmerged files.
hint: Fix them up in the work tree, and then use 'git add/rm <file>'
hint: as appropriate to mark resolution and make a commit.
fatal: Exiting because of an unresolved conflict.

```

```shell
SONG@DESKTOP-K52EVCT MINGW64 ~/multi_campus/Web/HTML_CSS_JS (master)
$ git push origin master
To https://github.com/Seungeun-Song/Study-for-K-Digital-AI-developer.git
 ! [rejected]        master -> master (non-fast-forward)
error: failed to push some refs to 'https://github.com/Seungeun-Song/Study-for-K-Digital-AI-developer.git'
hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. Integrate the remote changes (e.g.
hint: 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.


```

```shell
$ git pull origin master --allow-unrelated-histories
From https://github.com/Seungeun-Song/Study-for-K-Digital-AI-developer
 * branch            master     -> FETCH_HEAD
CONFLICT (rename/add): Rename Web/style.css->Web/HTML_CSS_JS/style.css in 5fc5016ef6a3725cde053773c05605e5c1ccbc49.  Added Web/HTML_CSS_JS/style.css in HEAD
Auto-merging Web/HTML_CSS_JS/style.css
CONFLICT (rename/add): Rename Web/JavaScript.html->Web/HTML_CSS_JS/JavaScript.html in 5fc5016ef6a3725cde053773c05605e5c1ccbc49.  Added Web/HTML_CSS_JS/JavaScript.html in HEAD
Auto-merging Web/HTML_CSS_JS/JavaScript.html
CONFLICT (rename/add): Rename Web/01.HTML_기본문법.md->Web/HTML_CSS_JS/01.HTML_기본문법.md in 5fc5016ef6a3725cde053773c05605e5c1ccbc49.  Added Web/HTML_CSS_JS/01.HTML_기본문법.md in HEAD
Auto-merging Web/HTML_CSS_JS/01.HTML_기본문법.md
Automatic merge failed; fix conflicts and then commit the result.

SONG@DESKTOP-K52EVCT MINGW64 ~/multi_campus/Web/HTML_CSS_JS (master|MERGING)

```

```shell
SONG@DESKTOP-K52EVCT MINGW64 ~/multi_campus/Practice (master)
$ git log
commit 3bf246b6b51dee07fd7b6f13fa8f9af8f7892505 (HEAD -> master, origin/master)
Author: Seungeun_Song <lilybad88@gmail.com>
Date:   Wed Jan 27 23:44:22 2021 +0900

```

```shell
SONG@DESKTOP-K52EVCT MINGW64 ~/multi_campus/Practice (master)
$ git push origin master
To https://github.com/Seungeun-Song/Study-for-K-Digital-AI-developer.git
 ! [rejected]        master -> master (fetch first)
error: failed to push some refs to 'https://github.com/Seungeun-Song/Study-for-K-Digital-AI-developer.git'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.

```



### git 해결 

```shell
$git fetch origin
```

