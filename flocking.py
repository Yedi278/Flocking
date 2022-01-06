import pygame
import pygame_widgets
from pygame_widgets.slider import Slider
import sys
import math


size= [500,500]
pygame.init()
window = pygame.display.set_mode(size)
slider = Slider(window, 100, 20, 100, 10, min=0, max=2*math.pi, step=0.2)
class triangle():
    def __init__(self,angle, v_i):
        self.angle  =   angle
        self.v_i    =   v_i
        

    def draw_triangle(self,pos,tetha):
        r = 15
        vertex_1 = ((pos[0]+r*math.sin(tetha)),(pos[1]-math.cos(tetha)*r))
        vertex_2 = ((pos[0]+r*math.sin(tetha + (math.pi*5/6))),(pos[1]-math.cos(tetha + (math.pi*5/6))*r))
        vertex_3 = ((pos[0]+r*math.sin(tetha - (math.pi*5/6))),(pos[1]-math.cos(tetha - (math.pi*5/6))*r))
        #pygame.draw.circle(window,(255,255,255),vertex_1,5,2)
        points = (vertex_1,vertex_2,vertex_3)
        pygame.draw.polygon(window,(255,255,255),points)
        
        
        



def main():
    
    tri = triangle(0,0)
    posx = 200
    posy = 200
    

    run = True
    while(run):
        event = pygame.event.get()
        window.fill((0,1,0))
        center = [250,250]
        tetha = slider.getValue()
        tri.draw_triangle(center,tetha)



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
             run = False
        pygame_widgets.update(event)
        pygame.display.update()
    

main()
