## ! [remote rejected]   master -> master (pre-receive hook declined)

```
SONG@DESKTOP-K52EVCT MINGW64 ~/Desktop/SEOUL_AI/20210724 (master)
$ git push origin master
Enumerating objects: 31208, done.
Counting objects: 100% (31208/31208), done.
Delta compression using up to 16 threads
Compressing objects: 100% (27769/27769), done.
Writing objects: 100% (31204/31204), 823.59 MiB | 9.42 MiB/s, done.
Total 31204 (delta 2805), reused 31086 (delta 2696), pack-reused 0
remote: Resolving deltas: 100% (2805/2805), completed with 2 local objects.
remote: error: Trace: 757ed47000d2698f197131b1d012c5b198458c3bfef64854f9f4a4fea784c8cb
remote: error: See http://git.io/iEPt8g for more information.
remote: error: File 20210725/venv_20210725/Lib/site-packages/en_core_web_trf/en_core_web_trf-3.1.0/transformer/model/pytorch_model.bin is 475.56 MB; this exceeds GitHub's file size limit of 100.00 MB
remote: error: File 20210725/venv_20210725/Lib/site-packages/torch/lib/torch_cpu.dll is 202.16 MB; this exceeds GitHub's file size limit of 100.00 MB
remote: error: File 20210725/venv_20210725/Lib/site-packages/torch/lib/dnnl.lib is 404.41 MB; this exceeds GitHub's file size limit of 100.00 MB
remote: error: GH001: Large files detected. You may want to try Git Large File Storage - https://git-lfs.github.com.
To https://github.com/Seungeun-Song/advanced-language-courses.git
 ! [remote rejected]   master -> master (pre-receive hook declined)
error: failed to push some refs to 'https://github.com/Seungeun-Song/advanced-language-courses.git'



```

---

**원인**

1, 로컬에서 폴더 삭제 -> github에 그대로 add,commit, push

2, Head에 먼저 반영. & **파일 용량 초과(this exceeds GitHub's file size limit of 100.00 MB)**

```
Author: Seungeun_Song <lilybad88@gmail.com>
commit 8b066c2f923000518061d5cd95ad8aecfc9fa449 (HEAD -> master)
Author: Seungeun_Song <lilybad88@gmail.com>
Date:   Thu Aug 12 21:25:32 2021 +0900

    Changed

commit 918b19c95d8a2fe783b1dc0a609a45a53581f773 (origin/master)
Author: Seungeun_Song <lilybad88@gmail.com>
Date:   Wed Aug 11 12:30:04 2021 +0900

    Add

commit 6220013136c93743e0917ea283aba3e377aeb7f9
Author: Seungeun_Song <lilybad88@gmail.com>
Date:   Wed Aug 11 12:29:47 2021 +0900

    Add

commit b61ae475070f62bf84b73676a84da113084bb281
Author: Seungeun_Song <lilybad88@gmail.com>
Date:   Tue Aug 10 17:10:08 2021 +0900

```







따라서 commit 취소

```
SONG@DESKTOP-K52EVCT MINGW64 ~/Desktop/SEOUL_AI/20210724 (master)
$git reset HEAD^
```

```
SONG@DESKTOP-K52EVCT MINGW64 ~/Desktop/SEOUL_AI/20210724 (master)
$ git log
commit 918b19c95d8a2fe783b1dc0a609a45a53581f773 (HEAD -> master, origin/master)
Author: Seungeun_Song <lilybad88@gmail.com>
Date:   Wed Aug 11 12:30:04 2021 +0900

    Add

commit 6220013136c93743e0917ea283aba3e377aeb7f9
Author: Seungeun_Song <lilybad88@gmail.com>
Date:   Wed Aug 11 12:29:47 2021 +0900

    Add

```



```
SONG@DESKTOP-K52EVCT MINGW64 ~/Desktop/SEOUL_AI/20210724 (master)
$git push --set-upstream origin master
```

git rm -rf <파일명>

```
SONG@DESKTOP-K52EVCT MINGW64 ~/Desktop/SEOUL_AI/20210724 (master)
$git rm -rf venv_20210724
```

git commit

```
SONG@DESKTOP-K52EVCT MINGW64 ~/Desktop/SEOUL_AI/20210724 (master)
$git commit -m "Changed"
```

git push 

```
SONG@DESKTOP-K52EVCT MINGW64 ~/Desktop/SEOUL_AI/20210724 (master)
$git push origin master
```

```
Author: Seungeun_Song <lilybad88@gmail.com>
commit 8b066c2f923000518061d5cd95ad8aecfc9fa449 (HEAD -> master)
Author: Seungeun_Song <lilybad88@gmail.com>
Date:   Thu Aug 12 21:25:32 2021 +0900

    Changed

commit 918b19c95d8a2fe783b1dc0a609a45a53581f773 (origin/master)
Author: Seungeun_Song <lilybad88@gmail.com>
Date:   Wed Aug 11 12:30:04 2021 +0900

    Add

commit 6220013136c93743e0917ea283aba3e377aeb7f9
Author: Seungeun_Song <lilybad88@gmail.com>
Date:   Wed Aug 11 12:29:47 2021 +0900

    Add

commit b61ae475070f62bf84b73676a84da113084bb281
Author: Seungeun_Song <lilybad88@gmail.com>
Date:   Tue Aug 10 17:10:08 2021 +0900

```