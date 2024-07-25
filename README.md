# 동의보감

## 이 애플리케이션으로 수집한 데이터를 함부로 배포하면 저작권 침해입니다!!!

[![동의보감 AI를 만들어보았다](https://img.youtube.com/vi/PZmT1vRjqNU/0.jpg)](https://youtu.be/PZmT1vRjqNU)

## 기능
* 동의보감에서 찾을 내용을 검색창에 입력하면 가장 유사한 결과 5개를 화면에 출력하는 앱입니다.
* [다음] 버튼을 눌러 그 다음으로 유사한 결과 5개를 확인할 수 있습니다.
* 결과를 클릭하면 [한의학고전DB 사이트](https://mediclassics.kr/)로 이동합니다.

## 실행 방법
1. python으로 scrape.py를 실행합니다. 2~3시간 뒤에 dongui-bogam.txt 파일이 생성됩니다.

linux
```
$ python scrape.py
```
windows
```
PS C:\dongui-bogam> python scrape.py
```
2. python으로 generate_json.py를 실행합니다. 1~2시간 뒤에 dongui-bogam.json 파일이 생성됩니다.

linux
```
$ python genrate_json.py
```
windows
```
PS C:\dongui-bogam> python generate_json.py
```
3. python으로 web_site.py를 실행합니다. 그리고 [http://localhost:5000](http://localhost:5000)에 접속합니다.

linux
```
$ python web_site.py
```
windows
```
PS C:\dongui-bogam> python web_site.py
```
