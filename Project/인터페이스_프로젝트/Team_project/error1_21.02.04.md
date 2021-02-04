조장 컴퓨터로 DB, VIEW, URL, TEMPLATE 만들고 공유

-runserver로 돌렸을 때 에러.

1. 공유파일을 github에 올린 error - secret key 때문

   > Django로 startproject -> setting.py 에 있는 secret key를 github에서 보안처리.
   >
   > 따라서 secret key를 ignore파일로 JSON처리 하던지 or 압축하는 방식(과거로 타입슬랩ㅠㅠㅠ)

2. 파일을 조장한테 따로 받아 

3. python manage.py migrate - DB통합하기

4. python manage.py createsuperuser 생성