import pygame
from pygame.locals import *

class Person:
    def __init__(self, screen_load):
        self.screenon = screen_load
        self.person = pygame.image.load("man.png")
        self.x = 40
        self.y = 300
        self.x_change = 0
        self.y_change = 0
        self.jump_avlue = 15
        self.jump_avai = False

    def show_person(self, x, y):
        self.x = x
        self.y = y
        self.screenon.blit(self.person, (self.x, self.y))

    def move_right(self):
        self.x_change = 0.2
    def move_left(self):
        self.x_change = -0.2
    
    def jump(self):
        if self.jump_avai == True:
            if self.jump_avlue >= -15:
                neg = 1 
                if self.jump_avlue < 0:
                    neg = -1
                self.y -= (self.jump_avlue ** 2) * 0.01 * neg
                self.jump_avlue -= 0.05
            else:
                self.jump_avai = False
                self.jump_avlue = 15

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("box")
        

        self.screen = pygame.display.set_mode((1000, 500))
        self.screen.fill((0, 128, 128)) 
        

        self.doan = Person(self.screen)

    def run(self):
        
        running = True

        left_action = False
        right_action = False

        while running:
            self.screen.fill((0, 128, 128))
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == KEYDOWN:
                    if event.key == K_SPACE: 
                        self.doan.jump_avai = True
                    if event.key == K_RIGHT:
                        right_action = True
                        left_action = False
                    if event.key == K_LEFT:
                        left_action = True
                        right_action = False
                if event.type == KEYUP:
                    if event.key == K_SPACE: 
                        self.doan.jump_avai = True
                    if event.key == K_RIGHT:
                       right_action = False
                    if event.key == K_LEFT:
                        left_action = False

                print(self.doan.x)
                print(self.doan.y)
                    
            

                if event.type == KEYUP:
                    self.doan.x_change = 0
            

            if left_action is True :
                self.doan.move_left()
            if right_action is True:
                self.doan.move_right()

            self.doan.jump()
            
            
            self.doan.x += self.doan.x_change
            self.doan.show_person(self.doan.x, self.doan.y)
            pygame.draw.rect(self.screen, (0, 0, 0), [300, 300, 40, 60])
            pygame.display.update()



if __name__ == "__main__":
    game = Game()
    game.run()