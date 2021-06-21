## couldn't find remote ref master



1, after 'git remote add ~', this error came up.



```
$ git pull origin master
fatal: couldn't find remote ref master

```

```
SONG@DESKTOP-K52EVCT MINGW64 ~/workspace/review_with_book (master)
$ git push origin master
error: src refspec master does not match any
error: failed to push some refs to 'https://github.com/Seungeun-Song/Review_with_book.git'

```

```
SONG@DESKTOP-K52EVCT MINGW64 ~/workspace/review_with_book (master)
$ git branch

SONG@DESKTOP-K52EVCT MINGW64 ~/workspace/review_with_book (master)
```

---

This problem is

because branch name is different with github branch. So go the repository of github and check up branch name at code page if it is master or main...



If the name is not master and I want change the name to master, at code click branch and at overview click the icon of pencil and change the name. 

That's all