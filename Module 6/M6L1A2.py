import pygame
pygame.init()
screen_width=500
screen_height=500
display_surface=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Welcome")
background_img=pygame.transform.scale(pygame.image.load('images.jpg').convert(), (screen_width,screen_height))
display_img=pygame.transform.scale(pygame.image.load('images.jpg').convert_alpha(), (100,100))
penguin_rect=display_img.get_rect(center=(0.5*screen_width, 0.5*screen_height))
text=pygame.font.Font(None,36).render("Hello World", True, pygame.Color("black"))
text_rect=display_img.get_rect(center=(0.5*screen_width, 0.5*screen_height-100))
def game_loop():
    clock=pygame.time.Clock()
    running=True
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
        display_surface.blit(background_img,(0,0))
        display_surface.blit(display_img,penguin_rect)
        display_surface.blit(text,text_rect)
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()
game_loop()