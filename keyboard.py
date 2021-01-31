
from pygame.locals import *
import pygame
 
pygame.init()
 
 
while True:
    for event in pygame.event.get():

        if event.type==KEYDOWN:
            if event.key==K_LEFT:
                print('key: left')
            elif event.key==K_RIGHT:
                print('key: right') 
            elif event.key==K_UP:
                print('key: up')
            elif event.key==K_DOWN:
                print('key: down')
        if event.type==KEYUP:
            if event.key==K_LEFT:
                print('key: left')
            if event.key==K_RIGHT:
                print('key: right')
            elif event.key==K_UP:
                print('key: up')
            elif event.key==K_DOWN:
                print('key: down ')