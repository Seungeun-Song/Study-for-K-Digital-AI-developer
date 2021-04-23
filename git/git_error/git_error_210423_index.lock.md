```
SONG@DESKTOP-K52EVCT MINGW64 ~/multi_campus/Practice (master)
$ git add 21_04_20_Cosine_Similarity.ipynb
fatal: Unable to create 'C:/Users/SONG/multi_campus/.git/index.lock': File exists.

Another git process seems to be running in this repository, e.g.
an editor opened by 'git commit'. Please make sure all processes
are terminated then try again. If it still fails, a git process
may have crashed in this repository earlier:
remove the file manually to continue.

```



```
SONG@DESKTOP-K52EVCT MINGW64 ~/multi_campus/Practice (master)
$ rm -rf./.git/index.lock
rm: unknown option -- .
Try 'rm --help' for more information.

```



```
SONG@DESKTOP-K52EVCT MINGW64 ~/multi_campus/Practice (master)
$ rm .git/index.lock
rm: cannot remove '.git/index.lock': No such file or directory

```





```
SONG@DESKTOP-K52EVCT MINGW64 ~/multi_campus/Practice (master)
$ rm -f ./.git/index.lock   
---이 코드는 도움이 되는 것처럼 에러 메세지가 뜨지는 않았지만 다시 add했을 때 결과는 똑같아

SONG@DESKTOP-K52EVCT MINGW64 ~/multi_campus/Practice (master)
$ git add 21_04_20_Cosine_Similarity.ipynb
fatal: Unable to create 'C:/Users/SONG/multi_campus/.git/index.lock': File exists.

Another git process seems to be running in this repository, e.g.
an editor opened by 'git commit'. Please make sure all processes
are terminated then try again. If it still fails, a git process
may have crashed in this repository earlier:
remove the file manually to continue.


```



>
>
