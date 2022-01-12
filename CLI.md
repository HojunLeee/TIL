# CLI

## GUI vs CLI

1. GUI (그래픽 유저 인터페이스)
   1. 그래픽을 통해서 사용자와 컴퓨터가 상호 작용하는 방식
2. CLI (커맨드 라인 인터페이스)
   1. 터미널을 통해 사용자와 컴퓨터가 상호 작용하는 방식

## CLI 사용 이유

new 라는 폴더를 만들고자 한다면

1. GUI에서는? : 우클릭 -> 새로만들기 -> 폴더 -> new
2.  CLI에서는?

## 작업 위치 (경로)

### 루트 디렉토리 (`/`)

- windows의 경우 일반적으로 c드라이브를 의미

### 홈 디렉토리 (`~`)

#### 상대 경로

- `./` : 현재 작업하고 있는 폴더를 의미
- `../` : 현재 작업하고 있는 폴더의 상위 폴더

TIP. `ctrl + l` : 화면 정리



## 명령어

`cd` `폴더명` 

- 현재 작업중인 디렉토리를 변경하는 명령어
- change directory

```bash
$ cd
-> 홈 디렉토리로 이동
$ cd folder # tab 으로 자동완성

$ cd ..
-> 상위 폴더로 이동
```



`ls`

- list segments
- 현재 작업중인 디렉토리의 폴더 / 파일 명을 보여주는 명령어

```bash
# 기본 사용
$ ls

# all
$ ls -a

#long
$ ls -l

$ ls -a -l
```

`mkdir`

- make diretory
- 폴더를 생성하는 명령어
- 폴더 이름 사이에 공백을 넣고 싶다면 따옴표로 묶어서 입력한다.

```bash
$ mkdir folder folder1
-> 띄어쓰기로 동시에 여러개 생성가능

$ mkdir "2022년 1월 12일"

```

`touch`

- 파일을 생성하는 명령어
- 폴더 생성과 방법이 동일
- 숨김 파일 :  `.`을 파일명 앞에 붙입니다.

```bash
$ touch test.txt
```

`start`

- 폴더 / 파일을 여는 명령어
- mac 에서는 `open`

`rm`

- remove
- 파일을 삭제하는 명령어
- GUI는 휴지통으로 보낸다.
- CLI는 `완전 삭제`
- `-r` : recursive 옵션

```bash
$ rm test.txt
$ rm -r folder/
```

`mv`

- move
- 위치 이동
- 위치 이동할 폴더가 없다면 파일명 변경으로 작동

```bash
$ mv {이동시킬 파일/폴더} {이동할 폴더}
$ mv {변경시킬 파일/폴더} {변경할 이름}
```
