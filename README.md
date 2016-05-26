HOW TO PYGAME

- 초반부 꼭 해야할 것들

import pygame
from pygame.locals import *
임포트할 것들은 이러하다.

pygame.init()
pygame에서 내부적으로 동작하는 모든 것들을 이니셜라이즈 해준다.
screen = pygame.display.set_mode((1000,500))
위 코드의 pygame.display.set_mode 함수가 윈도우를 생성한다. 첫 번째 인자로 길이가 2인 튜플을 주면 사이즈를 맞춰준다. 반환값은 스크린에 대한 핸들러 오브젝트이다(-> screen)
Clock = pygame.time.Clock()
시간과 관련된 것들을 처리해주는 오브젝트를 반환해준다. 주로 pygame.time.Clock.tick()함수 외에는 쓰지 않는다. pygame.time.Clock.tick(int) 함수는 첫번째 인자로 원하는 프레임 레이트를 받아서. 프로그램이 너무 빠르게 돌면 중간중간 적절히 sleep을 해준다. 반환값은 Frame Delta Time(현재 처리하는 프레임과 전 프레임과의 시간 간격)이다.

- 프레임 처리

어떤 방식으로든 Clock.tick(framerate) 명령을 각 프레임에 한번씩 들어가도록 해주면 인터프리터가 끝나기 전까지는 윈도우도 꺼지지 않는다. pygame.org/docs 의 tutorial 항목들을 보면 Clock.tick(framerate)가 보통 프레임 처리의 첫 부분이 된다. 
While True :
	// TODO : Frame
위와 같은 식으로 하거나
isContinue = True
while isContinue :
	// TODO : Frame
이런 식으로 boolean변수를 선언해서 isContinue변수를 이용해서 프로그램 종료를 제어할 수 있도록 할 수도 있다. While True를 사용하는 경우 sys모듈을 임포트해서(import sys) sys.exit(0)함수를 호출해서 프로그램 종료할 수도 있다.

- 영상 처리

Pygame에서 왠만한 모든 이미지 관련 객체들은 pygame.Surface이거나 혹은 그 하위 객체들이다.
pygame.display.set_mode()함수가 반환하는 핸들러의 경우도 pygame.Surface이고. 이 Surface에 그림을 그릴 경우 윈도우에도 그대로 출력되게 된다.
Surface위에 그림을 그리는 방법은 surface.blit(image, position)을 사용하면 된다.
Image는 그릴 Surface이고. Position은 말 그대로 그리기 시작할 위치이다.
만약 어떤 1000x1000짜리 background라는 Surface가 있고. 100x100짜리 image라는 Surface가 있으며, 사용자는 background의 (400,400)위치에 image를 그리고 싶다면
background.blit(image, (400,400))을 호출하면 된다.

pygame.image.load(filepath)함수를 사용하면 filepath에 있는 이미지 파일을 불러와서 이미지 파일크기의 Surface를 생성해서 그 그림을 Surface에 그린 후에 반환해 준다.
만약. 어떤 pygame소스코드의 절대 경로가 C:\source\pygame.py 이고. 어떤 이미지 파일이 C:\source\Data\image.bmp 라면. 
img = pygame.image.load(‘Data/image.bmp’) 를 통해 그 이미지를 가지는 Surface를 불러와서 img라는 변수에 넣어줄 수 있다.
그리고 이것을 출력해 주고 싶다면 pygame.display.set_mode(window_size)를 통해 얻은 Surface의 blit함수를 호출해서 출력할 수 있다.(screen.blit(img, position))

- 입력 받는 방법

pygame.event.get() 함수를 호출하면 이벤트들이 들어있는 리스트를 반환해준다. pygame.org/docs 의 tutorial들에서는 주로.
for event in pygame.event.get() :
이러한 for문으로 event들을 처리하는 것을 볼 수 있다.
각 event들은 type값을 가지고 있어서. KEYDOWN, MOUSEBUTTONDOWN등의 값을 가지고 있다.
그래서 if event.type == KEYDOWN : 을 통해서 키 입력에 관한 곳과. If event.type==pygame.MOUSEBUTTONDOWN을 통해서 마우스 입력과 관련된 것들을 구분할 수 있다.
event.type 이 KEYDOWN일 경우 event는 key값을 가지고 있다. 이 키 값은
K_a, K_b, K_c …. K_z 나 K_ESCAPE(Esc키), K_SPACE, K_RETURN(Enter키), K_LALT(Left Alt키), K_RALT, K_LCTRL, K_RCTRL, K_LSHIFT, K_RSHIFT
http://www.pygame.org/docs/ref/key.html
등의 값을 가진다.
event.type이 MOUSEBUTTONDOWN일 경우, event.button 값이 왼쪽 버튼일 경우 1, 오른쪽 버튼일 경우 3이 들어간다. 또, event.pos에 마우스 커서의 위치가 들어간다.
그래서 만약 ESC키를 입력하거나 (0,0),(100,100)사이를 마우스왼쪽버튼 클릭할 경우 프로그램이 종료되도록 하고 싶다면 아래의 코드를 프레임 부분에 추가하면 된다.
```python
for event in pygame.event.get() :
	if event.type==KEYDOWN :
		if event.key == K_ESCAPE :
			sys.exit(0)
	if event.type == MOUSEBUTTONDOWN :
		if event.button == 1:
			if 0 <= event.pos[0] and event.pos[0[] <= 100 and \
				0 <= event.pos[1] and event.pos[1] <= 100 :
				sys.exit(0)
```

