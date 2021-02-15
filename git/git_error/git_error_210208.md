```
SONG@DESKTOP-K52EVCT MINGW64 ~/teamproject/Project_WebPage (main)
$ git pull origin main
From https://github.com/Kwang-wan/Project_WebPage
 * branch            main       -> FETCH_HEAD
error: Your local changes to the following files would be overwritten by merge:
        개발/a. 통합/roof/page/__pycache__/models.cpython-38.pyc
        개발/a. 통합/roof/page/models.py
        개발/a. 통합/roof/roof/__pycache__/views.cpython-38.pyc
        개발/a. 통합/roof/templates/base.html
Please commit your changes or stash them before you merge.
Aborting
Updating 5aaec0e..c05c20b

```



## 에러메세지

```
Please commit your changes or stash them before you merge.
```



---

### 해결책

1. **git stash** : 현재 Staging 영역에 있는 파일의 변경사항을 스택에 넣기

```


SONG@DESKTOP-K52EVCT MINGW64 ~/teamproject/Project_WebPage (main)
$ git stash
Saved working directory and index state WIP on main: 5aaec0e 20210208 mod4

```

2.  **git pull origin main**  : main에서 pull하거나, git checkout 등 원격 저장소에서 내 로컬 브랜치로 변경사항을 적용한다.

   출처: https://goddaehee.tistory.com/253 [갓대희의 작은공간]

```
SONG@DESKTOP-K52EVCT MINGW64 ~/teamproject/Project_WebPage (main)
$ git pull origin main
From https://github.com/Kwang-wan/Project_WebPage
 * branch            main       -> FETCH_HEAD
Updating 5aaec0e..c05c20b
Fast-forward
 KakaoTalk_20210208_140725922.jpg                   | Bin 0 -> 162464 bytes
 .../roof/page/__pycache__/models.cpython-38.pyc"   | Bin 3318 -> 3307 bytes
 .../page/migrations/0006_auto_20210208_1428.py"    |  18 +++
 .../page/migrations/0007_auto_20210208_1431.py"    |  18 +++
 .../0006_auto_20210208_1428.cpython-38.pyc"        | Bin 0 -> 646 bytes
 .../0007_auto_20210208_1431.cpython-38.pyc"        | Bin 0 -> 628 bytes
 .../roof/page/models.py"                           |   2 +-
 .../roof/page/templates/page/member_list.html"     |  13 ++
 .../roof/roof/__pycache__/views.cpython-38.pyc"    | Bin 888 -> 678 bytes
 .../roof/roof/views.py"                            |   5 +-
 .../roof/templates/base.html"                      |   8 +-
 .../roof/templates/home.html"                      |   9 +-
 .../\352\264\221\354\231\204/roof/.gitignore"      |   5 +
 .../\352\264\221\354\231\204/roof/manage.py"       |  22 ++++
 .../roof/page/__init__.py"                         |   0
 .../roof/page/__pycache__/__init__.cpython-38.pyc" | Bin 0 -> 168 bytes
 .../roof/page/__pycache__/admin.cpython-38.pyc"    | Bin 0 -> 2371 bytes
 .../roof/page/__pycache__/apps.cpython-38.pyc"     | Bin 0 -> 384 bytes
 .../roof/page/__pycache__/models.cpython-38.pyc"   | Bin 0 -> 3307 bytes
 .../roof/page/__pycache__/urls.cpython-38.pyc"     | Bin 0 -> 834 bytes
 .../roof/page/__pycache__/views.cpython-38.pyc"    | Bin 0 -> 2819 bytes
 .../\352\264\221\354\231\204/roof/page/admin.py"   |  34 ++++++
 .../\352\264\221\354\231\204/roof/page/apps.py"    |   5 +
 .../roof/page/migrations/0001_initial.py"          |  22 ++++
 .../page/migrations/0002_auto_20210204_1519.py"    |  57 +++++++++
 .../page/migrations/0003_auto_20210204_1606.py"    |  31 +++++
 .../page/migrations/0004_auto_20210205_1347.py"    |  34 ++++++
 .../page/migrations/0005_auto_20210208_1055.py"    |  48 ++++++++
 .../page/migrations/0006_auto_20210208_1428.py"    |  18 +++
 .../page/migrations/0007_auto_20210208_1431.py"    |  18 +++
 .../roof/page/migrations/__init__.py"              |   0
 .../__pycache__/0001_initial.cpython-38.pyc"       | Bin 0 -> 727 bytes
 .../0002_auto_20210204_1519.cpython-38.pyc"        | Bin 0 -> 1578 bytes
 .../0003_auto_20210204_1606.cpython-38.pyc"        | Bin 0 -> 733 bytes
 .../0004_auto_20210205_1347.cpython-38.pyc"        | Bin 0 -> 1018 bytes
 .../0005_auto_20210208_1055.cpython-38.pyc"        | Bin 0 -> 1041 bytes
 .../0006_auto_20210208_1428.cpython-38.pyc"        | Bin 0 -> 646 bytes
 .../0007_auto_20210208_1431.cpython-38.pyc"        | Bin 0 -> 628 bytes
 .../__pycache__/__init__.cpython-38.pyc"           | Bin 0 -> 179 bytes
 .../\352\264\221\354\231\204/roof/page/models.py"  |  62 ++++++++++
 .../page/templates/category/category_list.html"    |   0
 .../page/templates/page/member_category_list.html" |   0
 .../roof/page/templates/page/member_list.html"     |  13 ++
 .../page/templates/page/member_photo_detail.html"  |   0
 .../page/templates/page/member_post_detail.html"   |   0
 .../roof/page/templates/tag/tag_list.html"         |   0
 .../\352\264\221\354\231\204/roof/page/tests.py"   |   3 +
 .../\352\264\221\354\231\204/roof/page/urls.py"    |  28 +++++
 .../\352\264\221\354\231\204/roof/page/views.py"   |  67 ++++++++++
 .../roof/roof/__init__.py"                         |   0
 .../roof/roof/__pycache__/__init__.cpython-38.pyc" | Bin 0 -> 168 bytes
 .../roof/roof/__pycache__/settings.cpython-38.pyc" | Bin 0 -> 2476 bytes
 .../roof/roof/__pycache__/urls.cpython-38.pyc"     | Bin 0 -> 1078 bytes
 .../roof/roof/__pycache__/views.cpython-38.pyc"    | Bin 0 -> 678 bytes
 .../roof/roof/__pycache__/wsgi.cpython-38.pyc"     | Bin 0 -> 565 bytes
 .../\352\264\221\354\231\204/roof/roof/asgi.py"    |  16 +++
 .../roof/roof/settings.py"                         | 136 +++++++++++++++++++++
 .../\352\264\221\354\231\204/roof/roof/urls.py"    |  25 ++++
 .../\352\264\221\354\231\204/roof/roof/views.py"   |  11 ++
 .../\352\264\221\354\231\204/roof/roof/wsgi.py"    |  16 +++
 .../roof/static/img/roof.png"                      | Bin 0 -> 53748 bytes
 .../roof/templates/base.html"                      | 130 ++++++++++++++++++++
 .../roof/templates/home.html"                      |  13 ++
 .../\354\212\271\354\235\200/roof/.gitignore"      |   5 +
 .../\354\212\271\354\235\200/roof/manage.py"       |  22 ++++
 .../roof/page/__init__.py"                         |   0
 .../roof/page/__pycache__/__init__.cpython-38.pyc" | Bin 0 -> 168 bytes
 .../roof/page/__pycache__/admin.cpython-38.pyc"    | Bin 0 -> 2371 bytes
 .../roof/page/__pycache__/apps.cpython-38.pyc"     | Bin 0 -> 384 bytes
 .../roof/page/__pycache__/models.cpython-38.pyc"   | Bin 0 -> 3307 bytes
 .../roof/page/__pycache__/urls.cpython-38.pyc"     | Bin 0 -> 834 bytes
 .../roof/page/__pycache__/views.cpython-38.pyc"    | Bin 0 -> 2819 bytes
 .../\354\212\271\354\235\200/roof/page/admin.py"   |  34 ++++++
 .../\354\212\271\354\235\200/roof/page/apps.py"    |   5 +
 .../roof/page/migrations/0001_initial.py"          |  22 ++++
 .../page/migrations/0002_auto_20210204_1519.py"    |  57 +++++++++
 .../page/migrations/0003_auto_20210204_1606.py"    |  31 +++++
 .../page/migrations/0004_auto_20210205_1347.py"    |  34 ++++++
 .../page/migrations/0005_auto_20210208_1055.py"    |  48 ++++++++
 .../page/migrations/0006_auto_20210208_1428.py"    |  18 +++
 .../page/migrations/0007_auto_20210208_1431.py"    |  18 +++
 .../roof/page/migrations/__init__.py"              |   0
 .../__pycache__/0001_initial.cpython-38.pyc"       | Bin 0 -> 727 bytes
 .../0002_auto_20210204_1519.cpython-38.pyc"        | Bin 0 -> 1578 bytes
 .../0003_auto_20210204_1606.cpython-38.pyc"        | Bin 0 -> 733 bytes
 .../0004_auto_20210205_1347.cpython-38.pyc"        | Bin 0 -> 1018 bytes
 .../0005_auto_20210208_1055.cpython-38.pyc"        | Bin 0 -> 1041 bytes
 .../0006_auto_20210208_1428.cpython-38.pyc"        | Bin 0 -> 646 bytes
 .../0007_auto_20210208_1431.cpython-38.pyc"        | Bin 0 -> 628 bytes
 .../__pycache__/__init__.cpython-38.pyc"           | Bin 0 -> 179 bytes
 .../\354\212\271\354\235\200/roof/page/models.py"  |  62 ++++++++++
 .../page/templates/category/category_list.html"    |   0
 .../page/templates/page/member_category_list.html" |   0
 .../roof/page/templates/page/member_list.html"     |  13 ++
 .../page/templates/page/member_photo_detail.html"  |   0
 .../page/templates/page/member_post_detail.html"   |   0
 .../roof/page/templates/tag/tag_list.html"         |   0
 .../\354\212\271\354\235\200/roof/page/tests.py"   |   3 +
 .../\354\212\271\354\235\200/roof/page/urls.py"    |  28 +++++
 .../\354\212\271\354\235\200/roof/page/views.py"   |  67 ++++++++++
 .../roof/roof/__init__.py"                         |   0
 .../roof/roof/__pycache__/__init__.cpython-38.pyc" | Bin 0 -> 168 bytes
 .../roof/roof/__pycache__/settings.cpython-38.pyc" | Bin 0 -> 2476 bytes
 .../roof/roof/__pycache__/urls.cpython-38.pyc"     | Bin 0 -> 1078 bytes
 .../roof/roof/__pycache__/views.cpython-38.pyc"    | Bin 0 -> 678 bytes
 .../roof/roof/__pycache__/wsgi.cpython-38.pyc"     | Bin 0 -> 565 bytes
 .../\354\212\271\354\235\200/roof/roof/asgi.py"    |  16 +++
 .../roof/roof/settings.py"                         | 136 +++++++++++++++++++++
 .../\354\212\271\354\235\200/roof/roof/urls.py"    |  25 ++++
 .../\354\212\271\354\235\200/roof/roof/views.py"   |  11 ++
 .../\354\212\271\354\235\200/roof/roof/wsgi.py"    |  16 +++
 .../roof/static/img/roof.png"                      | Bin 0 -> 53748 bytes
 .../roof/templates/base.html"                      | 130 ++++++++++++++++++++
 .../roof/templates/home.html"                      |  13 ++
 .../\354\232\251\355\230\204/roof/.gitignore"      |   5 +
 .../\354\232\251\355\230\204/roof/manage.py"       |  22 ++++
 .../roof/page/__init__.py"                         |   0
 .../roof/page/__pycache__/__init__.cpython-38.pyc" | Bin 0 -> 168 bytes
 .../roof/page/__pycache__/admin.cpython-38.pyc"    | Bin 0 -> 2371 bytes
 .../roof/page/__pycache__/apps.cpython-38.pyc"     | Bin 0 -> 384 bytes
 .../roof/page/__pycache__/models.cpython-38.pyc"   | Bin 0 -> 3307 bytes
 .../roof/page/__pycache__/urls.cpython-38.pyc"     | Bin 0 -> 834 bytes
 .../roof/page/__pycache__/views.cpython-38.pyc"    | Bin 0 -> 2819 bytes
 .../\354\232\251\355\230\204/roof/page/admin.py"   |  34 ++++++
 .../\354\232\251\355\230\204/roof/page/apps.py"    |   5 +
 .../roof/page/migrations/0001_initial.py"          |  22 ++++
 .../page/migrations/0002_auto_20210204_1519.py"    |  57 +++++++++
 .../page/migrations/0003_auto_20210204_1606.py"    |  31 +++++
 .../page/migrations/0004_auto_20210205_1347.py"    |  34 ++++++
 .../page/migrations/0005_auto_20210208_1055.py"    |  48 ++++++++
 .../page/migrations/0006_auto_20210208_1428.py"    |  18 +++
 .../page/migrations/0007_auto_20210208_1431.py"    |  18 +++
 .../roof/page/migrations/__init__.py"              |   0
 .../__pycache__/0001_initial.cpython-38.pyc"       | Bin 0 -> 727 bytes
 .../0002_auto_20210204_1519.cpython-38.pyc"        | Bin 0 -> 1578 bytes
 .../0003_auto_20210204_1606.cpython-38.pyc"        | Bin 0 -> 733 bytes
 .../0004_auto_20210205_1347.cpython-38.pyc"        | Bin 0 -> 1018 bytes
 .../0005_auto_20210208_1055.cpython-38.pyc"        | Bin 0 -> 1041 bytes
 .../0006_auto_20210208_1428.cpython-38.pyc"        | Bin 0 -> 646 bytes
 .../0007_auto_20210208_1431.cpython-38.pyc"        | Bin 0 -> 628 bytes
 .../__pycache__/__init__.cpython-38.pyc"           | Bin 0 -> 179 bytes
 .../\354\232\251\355\230\204/roof/page/models.py"  |  62 ++++++++++
 .../page/templates/category/category_list.html"    |   0
 .../page/templates/page/member_category_list.html" |   0
 .../roof/page/templates/page/member_list.html"     |  13 ++
 .../page/templates/page/member_photo_detail.html"  |   0
 .../page/templates/page/member_post_detail.html"   |   0
 .../roof/page/templates/tag/tag_list.html"         |   0
 .../\354\232\251\355\230\204/roof/page/tests.py"   |   3 +
 .../\354\232\251\355\230\204/roof/page/urls.py"    |  28 +++++
 .../\354\232\251\355\230\204/roof/page/views.py"   |  67 ++++++++++
 .../roof/roof/__init__.py"                         |   0
 .../roof/roof/__pycache__/__init__.cpython-38.pyc" | Bin 0 -> 168 bytes
 .../roof/roof/__pycache__/settings.cpython-38.pyc" | Bin 0 -> 2476 bytes
 .../roof/roof/__pycache__/urls.cpython-38.pyc"     | Bin 0 -> 1078 bytes
 .../roof/roof/__pycache__/views.cpython-38.pyc"    | Bin 0 -> 678 bytes
 .../roof/roof/__pycache__/wsgi.cpython-38.pyc"     | Bin 0 -> 565 bytes
 .../\354\232\251\355\230\204/roof/roof/asgi.py"    |  16 +++
 .../roof/roof/settings.py"                         | 136 +++++++++++++++++++++
 .../\354\232\251\355\230\204/roof/roof/urls.py"    |  25 ++++
 .../\354\232\251\355\230\204/roof/roof/views.py"   |  11 ++
 .../\354\232\251\355\230\204/roof/roof/wsgi.py"    |  16 +++
 .../roof/static/img/roof.png"                      | Bin 0 -> 53748 bytes
 .../roof/templates/base.html"                      | 130 ++++++++++++++++++++
 .../roof/templates/home.html"                      |  13 ++
 .../\355\230\234\353\271\210/roof/.gitignore"      |   5 +
 .../\355\230\234\353\271\210/roof/manage.py"       |  22 ++++
 .../roof/page/__init__.py"                         |   0
 .../roof/page/__pycache__/__init__.cpython-38.pyc" | Bin 0 -> 168 bytes
 .../roof/page/__pycache__/admin.cpython-38.pyc"    | Bin 0 -> 2371 bytes
 .../roof/page/__pycache__/apps.cpython-38.pyc"     | Bin 0 -> 384 bytes
 .../roof/page/__pycache__/models.cpython-38.pyc"   | Bin 0 -> 3307 bytes
 .../roof/page/__pycache__/urls.cpython-38.pyc"     | Bin 0 -> 834 bytes
 .../roof/page/__pycache__/views.cpython-38.pyc"    | Bin 0 -> 2819 bytes
 .../\355\230\234\353\271\210/roof/page/admin.py"   |  34 ++++++
 .../\355\230\234\353\271\210/roof/page/apps.py"    |   5 +
 .../roof/page/migrations/0001_initial.py"          |  22 ++++
 .../page/migrations/0002_auto_20210204_1519.py"    |  57 +++++++++
 .../page/migrations/0003_auto_20210204_1606.py"    |  31 +++++
 .../page/migrations/0004_auto_20210205_1347.py"    |  34 ++++++
 .../page/migrations/0005_auto_20210208_1055.py"    |  48 ++++++++
 .../page/migrations/0006_auto_20210208_1428.py"    |  18 +++
 .../page/migrations/0007_auto_20210208_1431.py"    |  18 +++
 .../roof/page/migrations/__init__.py"              |   0
 .../__pycache__/0001_initial.cpython-38.pyc"       | Bin 0 -> 727 bytes
 .../0002_auto_20210204_1519.cpython-38.pyc"        | Bin 0 -> 1578 bytes
 .../0003_auto_20210204_1606.cpython-38.pyc"        | Bin 0 -> 733 bytes
 .../0004_auto_20210205_1347.cpython-38.pyc"        | Bin 0 -> 1018 bytes
 .../0005_auto_20210208_1055.cpython-38.pyc"        | Bin 0 -> 1041 bytes
 .../0006_auto_20210208_1428.cpython-38.pyc"        | Bin 0 -> 646 bytes
 .../0007_auto_20210208_1431.cpython-38.pyc"        | Bin 0 -> 628 bytes
 .../__pycache__/__init__.cpython-38.pyc"           | Bin 0 -> 179 bytes
 .../\355\230\234\353\271\210/roof/page/models.py"  |  62 ++++++++++
 .../page/templates/category/category_list.html"    |   0
 .../page/templates/page/member_category_list.html" |   0
 .../roof/page/templates/page/member_list.html"     |  13 ++
 .../page/templates/page/member_photo_detail.html"  |   0
 .../page/templates/page/member_post_detail.html"   |   0
 .../roof/page/templates/tag/tag_list.html"         |   0
 .../\355\230\234\353\271\210/roof/page/tests.py"   |   3 +
 .../\355\230\234\353\271\210/roof/page/urls.py"    |  28 +++++
 .../\355\230\234\353\271\210/roof/page/views.py"   |  67 ++++++++++
 .../roof/roof/__init__.py"                         |   0
 .../roof/roof/__pycache__/__init__.cpython-38.pyc" | Bin 0 -> 168 bytes
 .../roof/roof/__pycache__/settings.cpython-38.pyc" | Bin 0 -> 2476 bytes
 .../roof/roof/__pycache__/urls.cpython-38.pyc"     | Bin 0 -> 1078 bytes
 .../roof/roof/__pycache__/views.cpython-38.pyc"    | Bin 0 -> 678 bytes
 .../roof/roof/__pycache__/wsgi.cpython-38.pyc"     | Bin 0 -> 565 bytes
 .../\355\230\234\353\271\210/roof/roof/asgi.py"    |  16 +++
 .../roof/roof/settings.py"                         | 136 +++++++++++++++++++++
 .../\355\230\234\353\271\210/roof/roof/urls.py"    |  25 ++++
 .../\355\230\234\353\271\210/roof/roof/views.py"   |  11 ++
 .../\355\230\234\353\271\210/roof/roof/wsgi.py"    |  16 +++
 .../roof/static/img/roof.png"                      | Bin 0 -> 53748 bytes
 .../roof/templates/base.html"                      | 130 ++++++++++++++++++++
 .../roof/templates/home.html"                      |  13 ++
 216 files changed, 3317 insertions(+), 12 deletions(-)
 create mode 100644 KakaoTalk_20210208_140725922.jpg
 create mode 100644 "\352\260\234\353\260\234/a. \355\206\265\355\225\251/roof/page/migrations/0006_auto_20210208_1428.py"
 create mode 100644 "\352\260\234\353\260\234/a. \355\206\265\355\225\251/roof/page/migrations/0007_auto_20210208_1431.py"
```

3. **git stash pop** : 변경 사항을 적용하고, 스택에서 제거 한다.

```
SONG@DESKTOP-K52EVCT MINGW64 ~/teamproject/Project_WebPage (main)
$ git stash pop

```

```

```

