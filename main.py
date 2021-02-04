from tkinter.messagebox import *
from pygame.locals import *
from random import *
import tkinter as tk
import pygame
base = tk.Tk()
base.geometry('0x0')
base.resizable(False,False)
pygame.init()
def show2048(surf,vals):
    font = pygame.font.Font('songti SC.TTF',100)
    for i in range(len(vals)):
        for j in range(len(vals[i])):
            if (vals[i][j] == None):
                t = font.render(' ', True, (0,0,0), (255,255,255))
            else:
                t = font.render(str(vals[i][j]), True, (0,0,0),(255,255,255))
                t = pygame.transform.scale(t, (100,100))
                surf.blit(t,(100 * i,100 * j))
def gen_val(vals):
    x = randint(0, 3)
    y = randint(0, 3)
    while(vals[x][y] != None):
        x = randint(0,3)
        y = randint(0,3)
    vals[x][y] = choice((2,4))
def c2r(vals):
    return [[vals[j][i] for j in range(len(vals[i]))] for i in range(len(vals))]
def main():
    scr = pygame.display.set_mode((400,400))
    vals = [[None for j in range(4)] for i in range(4)]
    gen_val(vals)
    while(1):
        pygame.display.update()
        scr.fill((255,255,255))
        show2048(scr,vals)
        if(2048 in [vals[i // 4][i % 4] for i in range(16)]):
            return True
        if(None not in [vals[i // 4][i % 4] for i in range(16)]):
            pygame.display.update()
            return False
        for ev in pygame.event.get():
            if(ev.type == QUIT):
                exit()
            elif(ev.type == KEYDOWN):
                if(ev.key == K_DOWN):
                    for i in range(len(vals)):
                        while(None in vals[i]):
                            vals[i].remove(None)
                        for j in range(len(vals[i])):
                            if(j + 1 >= len(vals[i])):
                                break
                            if(vals[i][j + 1] == vals[i][j]):
                                vals[i][j + 1] *= 2
                                vals[i].pop(j)
                        while(len(vals[i]) < 4):
                            vals[i] = [None] + vals[i]
                    gen_val(vals)
                elif(ev.key == K_UP):
                    for i in range(len(vals)):
                        while (None in vals[i]):
                            vals[i].remove(None)
                        for j in range(1,len(vals[i])):
                            if (j >= len(vals[i])):
                                break
                            if (vals[i][j - 1] == vals[i][j]):
                                vals[i][j - 1] *= 2
                                vals[i].pop(j)
                        while (len(vals[i]) < 4):
                            vals[i] = vals[i] + [None]
                    gen_val(vals)
                elif(ev.key == K_LEFT):
                    a = c2r(vals)
                    for i in range(len(a)):
                        while (None in a[i]):
                            a[i].remove(None)
                        for j in range(1, len(a[i])):
                            if (j >= len(a[i])):
                                break
                            if (a[i][j - 1] == a[i][j]):
                                a[i][j - 1] *= 2
                                a[i].pop(j)
                        while (len(a[i]) < 4):
                            a[i] = a[i] + [None]
                    vals = c2r(a)
                    gen_val(vals)
                elif(ev.key == K_RIGHT):
                    a = c2r(vals)
                    for i in range(len(a)):
                        while (None in a[i]):
                            a[i].remove(None)
                        for j in range(len(a[i])):
                            if (j + 1 >= len(a[i])):
                                break
                            if (a[i][j + 1] == a[i][j]):
                                a[i][j + 1] *= 2
                                a[i].pop(j)
                        while (len(a[i]) < 4):
                            a[i] = [None] + a[i]
                    vals = c2r(a)
                    gen_val(vals)
if(__name__ == '__main__'):
    if(main()):
        showinfo('Congratulations!', 'Congratulations!You\'done it!')
    else:
        showinfo('Failed...', 'You are failed')