HOW TO PYGAME

- �ʹݺ� �� �ؾ��� �͵�

import pygame
from pygame.locals import *
����Ʈ�� �͵��� �̷��ϴ�.

pygame.init()
pygame���� ���������� �����ϴ� ��� �͵��� �̴ϼȶ����� ���ش�.
screen = pygame.display.set_mode((1000,500))
�� �ڵ��� pygame.display.set_mode �Լ��� �����츦 �����Ѵ�. ù ��° ���ڷ� ���̰� 2�� Ʃ���� �ָ� ����� �����ش�. ��ȯ���� ��ũ���� ���� �ڵ鷯 ������Ʈ�̴�(-> screen)
Clock = pygame.time.Clock()
�ð��� ���õ� �͵��� ó�����ִ� ������Ʈ�� ��ȯ���ش�. �ַ� pygame.time.Clock.tick()�Լ� �ܿ��� ���� �ʴ´�. pygame.time.Clock.tick(int) �Լ��� ù��° ���ڷ� ���ϴ� ������ ����Ʈ�� �޾Ƽ�. ���α׷��� �ʹ� ������ ���� �߰��߰� ������ sleep�� ���ش�. ��ȯ���� Frame Delta Time(���� ó���ϴ� �����Ӱ� �� �����Ӱ��� �ð� ����)�̴�.

- ������ ó��

� ������ε� Clock.tick(framerate) ����� �� �����ӿ� �ѹ��� ������ ���ָ� ���������Ͱ� ������ �������� �����쵵 ������ �ʴ´�. pygame.org/docs �� tutorial �׸���� ���� Clock.tick(framerate)�� ���� ������ ó���� ù �κ��� �ȴ�. 
While True :
	// TODO : Frame
���� ���� ������ �ϰų�
isContinue = True
while isContinue :
	// TODO : Frame
�̷� ������ boolean������ �����ؼ� isContinue������ �̿��ؼ� ���α׷� ���Ḧ ������ �� �ֵ��� �� ���� �ִ�. While True�� ����ϴ� ��� sys����� ����Ʈ�ؼ�(import sys) sys.exit(0)�Լ��� ȣ���ؼ� ���α׷� ������ ���� �ִ�.

- ���� ó��

Pygame���� �ظ��� ��� �̹��� ���� ��ü���� pygame.Surface�̰ų� Ȥ�� �� ���� ��ü���̴�.
pygame.display.set_mode()�Լ��� ��ȯ�ϴ� �ڵ鷯�� ��쵵 pygame.Surface�̰�. �� Surface�� �׸��� �׸� ��� �����쿡�� �״�� ��µǰ� �ȴ�.
Surface���� �׸��� �׸��� ����� surface.blit(image, position)�� ����ϸ� �ȴ�.
Image�� �׸� Surface�̰�. Position�� �� �״�� �׸��� ������ ��ġ�̴�.
���� � 1000x1000¥�� background��� Surface�� �ְ�. 100x100¥�� image��� Surface�� ������, ����ڴ� background�� (400,400)��ġ�� image�� �׸��� �ʹٸ�
background.blit(image, (400,400))�� ȣ���ϸ� �ȴ�.

pygame.image.load(filepath)�Լ��� ����ϸ� filepath�� �ִ� �̹��� ������ �ҷ��ͼ� �̹��� ����ũ���� Surface�� �����ؼ� �� �׸��� Surface�� �׸� �Ŀ� ��ȯ�� �ش�.
����. � pygame�ҽ��ڵ��� ���� ��ΰ� C:\source\pygame.py �̰�. � �̹��� ������ C:\source\Data\image.bmp ���. 
img = pygame.image.load(��Data/image.bmp��) �� ���� �� �̹����� ������ Surface�� �ҷ��ͼ� img��� ������ �־��� �� �ִ�.
�׸��� �̰��� ����� �ְ� �ʹٸ� pygame.display.set_mode(window_size)�� ���� ���� Surface�� blit�Լ��� ȣ���ؼ� ����� �� �ִ�.(screen.blit(img, position))

- �Է� �޴� ���

pygame.event.get() �Լ��� ȣ���ϸ� �̺�Ʈ���� ����ִ� ����Ʈ�� ��ȯ���ش�. pygame.org/docs �� tutorial�鿡���� �ַ�.
for event in pygame.event.get() :
�̷��� for������ event���� ó���ϴ� ���� �� �� �ִ�.
�� event���� type���� ������ �־. KEYDOWN, MOUSEBUTTONDOWN���� ���� ������ �ִ�.
�׷��� if event.type == KEYDOWN : �� ���ؼ� Ű �Է¿� ���� ����. If event.type==pygame.MOUSEBUTTONDOWN�� ���ؼ� ���콺 �Է°� ���õ� �͵��� ������ �� �ִ�.
event.type �� KEYDOWN�� ��� event�� key���� ������ �ִ�. �� Ű ����
K_a, K_b, K_c ��. K_z �� K_ESCAPE(EscŰ), K_SPACE, K_RETURN(EnterŰ), K_LALT(Left AltŰ), K_RALT, K_LCTRL, K_RCTRL, K_LSHIFT, K_RSHIFT
http://www.pygame.org/docs/ref/key.html
���� ���� ������.
event.type�� MOUSEBUTTONDOWN�� ���, event.button ���� ���� ��ư�� ��� 1, ������ ��ư�� ��� 3�� ����. ��, event.pos�� ���콺 Ŀ���� ��ġ�� ����.
�׷��� ���� ESCŰ�� �Է��ϰų� (0,0),(100,100)���̸� ���콺���ʹ�ư Ŭ���� ��� ���α׷��� ����ǵ��� �ϰ� �ʹٸ� �Ʒ��� �ڵ带 ������ �κп� �߰��ϸ� �ȴ�.

for event in pygame.event.get() :
	if event.type==KEYDOWN :
		if event.key == K_ESCAPE :
			sys.exit(0)
	if event.type == MOUSEBUTTONDOWN :
		if event.button == 1:
			if 0 <= event.pos[0] and event.pos[0[] <= 100 and \
				0 <= event.pos[1] and event.pos[1] <= 100 :
				sys.exit(0)

