# -*- coding: utf-8 -*-

import pygame, math, sys, random
from pygame.locals import *

SCREEN_SIZE = (1000,500)
FRAME_RATE = 60
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()
while True :
	clock.tick(FRAME_RATE)
	key = pygame.key.get_pressed() # 키들이 눌려있는지 저장하는 Dictionary

	for event in pygame.event.get() :
		if event.type == KEYDOWN :
			if event.key == K_ESCAPE :
				sys.exit(0)
		elif event.type == MOUSEBUTTONDOWN :
			pos = event.pos # 마우스 커서 위치
			if event.button == 1:
				# TODO : 마우스 왼쪽 버튼 입력시 (pass는 지워도 됨)
				pass
			elif event.button == 3:
				# TODO : 마우스 오른쪽 버튼 입력시
				pass

	screen.fill((0,0,0))
	# TODO : screen.blit등을 이용해서 여기서 렌더링

	pygame.display.flip()