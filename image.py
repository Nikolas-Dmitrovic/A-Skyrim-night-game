import os
import sys
import pygame

pygame.init()
WIN = pygame.display.set_mode((400, 400))


def import_image(image, image_location = None, alpha = None, alpha_color = (0,0,0)):
    if image_location == None:
        if alpha != None:
            try:
                image = pygame.image.load(image).convert()
                image.set_alpha(alpha)
                return image


            except FileNotFoundError:
                print("hello")
        
            # raise pygame.error("Unsupported image format")
            except pygame.error:
                if pygame.get_error() == "Unsupported image format":
                    print("hi")
            
        if alpha_color != (0,0,0):

        else:

            try:
                return pygame.image.load(image).convert()


            except FileNotFoundError:
                print("hello")
        
            # raise pygame.error("Unsupported image format")
            except pygame.error:
                if pygame.get_error() == "Unsupported image format":
                    print("hi")




image = import_image("select_image.png")
print(image.get_alpha())