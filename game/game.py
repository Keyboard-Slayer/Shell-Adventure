#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import pygame

from pygame.locals import *
from game.mechanics.term.Term import Term
from game.mechanics.quest.Quest import Quest
from game.mechanics.rpg.Rpg import Rpg
from game.lang.Interpreter import Interpreter
from game.lang.ide import Ide

GAMEFILES = os.getcwd()

def launchGame(liveMode=False):
    pygame.init()
    clock = pygame.time.Clock()
    clock.tick(60)
    mono = pygame.font.Font("font/monospace.ttf", 22)
    display = pygame.display.set_mode((1920, 1080))
    pygame.display.set_caption("Shell Adventure")

    term = Term("test-user", "localhost", (500, 540), font=mono)
    quest = Quest((500, 540), font=mono)
    rpg = Rpg((1420, 1080))

    lang = Interpreter(GAMEFILES, term, quest, rpg)
    # os.chdir(term.getenv()["HOME"])
    
    if not liveMode:
        lang.execute("Intro/base.adv")
    else:
        ide = Ide()
        ide.mainloop()
    
    
    while True:
        termPos, questPos, rpgPos = lang.mainloop()
        term_rect = display.blit(term.get_surface(), termPos)
        display.blit(quest.get_surface(), questPos)
        rpg_rect = display.blit(rpg.get_surface(), rpgPos)
        pygame.display.flip()
        rect = pygame.Rect(pygame.mouse.get_pos(), pygame.mouse.get_cursor()[0])
        term.set_mouse_collide(rect.colliderect(term_rect))
        rpg.set_mouse_collide(rect.colliderect(rpg_rect))

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                term.keydown(event.key)
                rpg.keydown(event.key)
