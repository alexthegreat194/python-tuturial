import pygame
from objects import Apple, Player, Strawberry, Bomb


pygame.init()
screen = pygame.display.set_mode([500, 500])
clock = pygame.time.Clock()

apple = Apple()
player = Player()
strawberry = Strawberry()
bomb = Bomb()

# Make a group
all_sprites = pygame.sprite.Group()
# Add sprites to group
all_sprites.add(player)
all_sprites.add(apple)
all_sprites.add(strawberry)
all_sprites.add(bomb)

# make a fruits Group
fruit_sprites = pygame.sprite.Group()
fruit_sprites.add(apple)
fruit_sprites.add(strawberry)

running = True
while running:
    # Looks at events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Check for event type KEYBOARD
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_LEFT:
                player.left()
            elif event.key == pygame.K_RIGHT:
                player.right()
            elif event.key == pygame.K_UP:
                player.up()
            elif event.key == pygame.K_DOWN:
                player.down()
    
    # Clear screen
    screen.fill((255, 255, 255))

    for entity in all_sprites:
        entity.move()
        entity.render(screen)

    # Check Colisions
    fruit = pygame.sprite.spritecollideany(player, fruit_sprites)
    if fruit:
        fruit.reset()

    # Check collision player and bomb
    if pygame.sprite.collide_rect(player, bomb):
        running = False

    # Update the window
    pygame.display.flip()
    clock.tick(60)
    #print(f"{bomb.x}:{bomb.y}")

