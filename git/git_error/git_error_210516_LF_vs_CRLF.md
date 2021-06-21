```
SONG@DESKTOP-K52EVCT MINGW64 ~/workspace/skin_assistant/skin_assistant (master)
$ git add --all
warning: LF will be replaced by CRLF in app.py.
The file will have its original line endings in your working directory
warning: LF will be replaced by CRLF in templates/index.html.
The file will have its original line endings in your working directory
warning: LF will be replaced by CRLF in templates/jquery.js.
The file will have its original line endings in your working directory
warning: LF will be replaced by CRLF in templates/nicepage.js.
The file will have its original line endings in your working directory



```

유닉스 시스템에서는 한 줄의 끝이 **LF(Line Feed)**로 이루어지는 반면, 윈도우에서는 줄 하나가 **CR(Carriage Return)**와 **LF(Line Feed)**, 즉 **CRLF**로 이루어지기 때문이다. 따라서 어느 한 쪽을 선택할지 Git에게 혼란이 온 것이다.