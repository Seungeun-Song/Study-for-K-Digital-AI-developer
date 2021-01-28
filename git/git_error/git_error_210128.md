```
SONG@DESKTOP-K52EVCT MINGW64 ~/multi_campus/git/git_class (master)
$ git add --all
```





```
SONG@DESKTOP-K52EVCT MINGW64 ~/multi_campus/git/git_class (master)
$ git restore --staged --a
error: unknown option `a'
usage: git restore [<options>] [--source=<branch>] <file>...
```

```
SONG@DESKTOP-K52EVCT MINGW64 ~/multi_campus/git/git_class (master)
$ git restore --staged --all
error: unknown option `all'
usage: git restore [<options>] [--source=<branch>] <file>...

```

```
SONG@DESKTOP-K52EVCT MINGW64 ~/multi_campus/git/git_class (master)
$ git restore --staged *
error: unknown option `*'
usage: git restore [<options>] [--source=<branch>] <file>...
```





```
SONG@DESKTOP-K52EVCT MINGW64 ~/multi_campus/git/git_class (master)
$ git reset head

SONG@DESKTOP-K52EVCT MINGW64 ~/multi_campus/git/git_class (master)
$ git status
On branch master
Untracked files:
  (use "git add <file>..." to include in what will be committed)

```

--------------

----------

--------



#### vi 편집기로 작업하는 동안 비정상적인 종료 등이 발생하면 파일을 임시로 저장해놓는데 그런 파일이 있다는 알림창 

```
E325: ATTENTION
Found a swap file by the name "C:/Users/SONG/multi_campus/.git/.MERGE_MSG.swp"
          owned by: SONG   dated: Thu Jan 28 21:17:06 2021
         file name: ~SONG/multi_campus/.git/MERGE_MSG
          modified: YES
         user name: SONG   host name: DESKTOP-K52EVCT
        process ID: 939
While opening file "C:/Users/SONG/multi_campus/.git/MERGE_MSG"
             dated: Thu Jan 28 22:06:07 2021
      NEWER than swap file!

(1) Another program may be editing the same file.  If this is the case,
    be careful not to end up with two different instances of the same
    file when making changes.  Quit, or continue with caution.
(2) An edit session for this file crashed.
    If this is the case, use ":recover" or "vim -r C:/Users/SONG/multi_campus/.g
it/MERGE_MSG"
    to recover the changes (see ":help recovery").
    If you did this already, delete the swap file "C:/Users/SONG/multi_campus/.g
it/.MERGE_MSG.swp"
    to avoid this message.

Swap file "C:/Users/SONG/multi_campus/.git/.MERGE_MSG.swp" already exists!
[O]pen Read-Only, (E)dit anyway, (R)ecover, (D)elete it, (Q)uit, (A)bort:

```



#### git vi창

```
Merge branch 'master' of https://github.com/Seungeun-Song/Study-for-K-Digital-AI-developer
# Please enter a commit message to explain why this merge is necessary,
# especially if it merges an updated upstream into a topic branch.
#
# Lines starting with '#' will be ignored, and an empty message aborts
# the commit.
~
~
~
~
~
~
----------------------------------------------------------------------
:q
```

