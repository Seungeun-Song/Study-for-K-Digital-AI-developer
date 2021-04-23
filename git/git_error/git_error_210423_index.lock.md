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







>Try deleting `index.lock` file in your `.git` directory.
>
>```
>rm -f .git/index.lock
>```
>
>Such problems generally occur when you execute two `git` commands simultaneously; maybe one from the command prompt and one from an IDE.
>
>
>
>참조: https://stackoverflow.com/questions/38004148/another-git-process-seems-to-be-running-in-this-repository





```
SONG@DESKTOP-K52EVCT MINGW64 ~/multi_campus/Practice (master)
$ git add 21_04_20_Cosine_Similarity.ipynb
warning: LF will be replaced by CRLF in Practice/21_04_20_Cosine_Similarity.ipynb.
The file will have its original line endings in your working directory

SONG@DESKTOP-K52EVCT MINGW64 ~/multi_campus/Practice (master)


---

clear! but 'rm -f .git/index.lock'를 실행한 directory를 현재 디렉토리와 git 상위 디렉토리 두군데서 실행. 어떤 것 때문인지 정확하지는 않음. But 상위 디렉토리에서 수행했기 때문이라 추측. 이전에 했을 때는 여전히 똑같은 에러 메세지를 보냈기 때문
```

