import pygame
from sys import exit
import random

pygame.init()
clock = pygame.time.Clock()

# Window
screen_height = 720
screen_width = 551
screen = pygame.display.set_mode((screen_width, screen_height))

# Images
bird_sprites = [pygame.image.load("assets/bird_down.png"),
                pygame.image.load("assets/bird_mid.png"),
                pygame.image.load("assets/bird_up.png")]
background_image = pygame.image.load("assets/background.png")
ground_image = pygame.image.load("assets/ground.png")
top_pipe_image = pygame.image.load("assets/pipe_top.png")
bottom_pipe_image = pygame.image.load("assets/pipe_bottom.png")
game_over_image = pygame.image.load("assets/game_over.png")
start_image = pygame.image.load("assets/start.png")

# Game
scroll_speed = 1
bird_start_position = (100, 250)
score = 0
font = pygame.font.SysFont('Segoe', 26)
game_active = True


class Bird(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = bird_sprites[0]
        self.rect = self.image.get_rect()
        self.rect.center = bird_start_position
        self.image_index = 0
        self.velocity = 0
        self.flap = False
        self.alive = True

    def update(self, user_input):
        # Animate Bird
        if self.alive:
            self.image_index += 1
        if self.image_index >= 30:
            self.image_index = 0
        self.image = bird_sprites[self.image_index // 10]

        # Gravity and Flap
        self.velocity += 0.5
        if self.velocity > 7:
            self.velocity = 7
        if self.rect.y < 500:
            self.rect.y += int(self.velocity)
        if self.velocity == 0:
            self.flap = False

        # Rotate Bird
        self.image = pygame.transform.rotate(self.image, self.velocity * -7)

        # User Input
        if user_input[pygame.K_SPACE] and not self.flap and self.rect.y > 0 and self.alive:
            self.flap = True
            self.velocity = -7


class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, image, pipe_type):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.enter, self.exit, self.passed = False, False, False
        self.pipe_type = pipe_type

    def update(self):
        # Move Pipe
        self.rect.x -= scroll_speed
        if self.rect.x <= -screen_width:
            self.kill()

        # Score
        global score
        if self.pipe_type == 'bottom':
            if bird_start_position[0] > self.rect.topleft[0] and not self.passed:
                self.enter = True
            if bird_start_position[0] > self.rect.topright[0] and not self.passed:
                self.exit = True
            if self.enter and self.exit and not self.passed:
                self.passed = True
                score += 1


class Ground(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = ground_image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def update(self):
        # Move Ground
        self.rect.x -= scroll_speed
        if self.rect.x <= -screen_width:
            self.kill()


def quit_game():
    # Exit Game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


# Game Main Method
def main():
    global score

    # Instantiate Bird
    bird_group = pygame.sprite.GroupSingle()
    bird_group.add(Bird())

    # Setup Pipes
    pipe_timer = 0
    pipe_group = pygame.sprite.Group()

    # Instantiate Initial Ground
    ground_x, ground_y = 0, 520
    ground_group = pygame.sprite.Group()
    ground_group.add(Ground(ground_x, ground_y))

    run_game = True
    while run_game:
        # Quit
        quit_game()

        # Reset Frame
        screen.fill((0, 0, 0))

        # User Input
        user_input = pygame.key.get_pressed()

        # Draw Background
        screen.blit(background_image, (0, 0))

        # Spawn Ground
        if len(ground_group) <= 2:
            ground_group.add(Ground(screen_width, ground_y))

        # Draw - Pipes, Ground and Bird
        pipe_group.draw(screen)
        ground_group.draw(screen)
        bird_group.draw(screen)

        # Show Score
        score_text = font.render('Score: ' + str(score), True, pygame.Color(255, 255, 255))
        screen.blit(score_text, (20, 20))

        # Update - Pipes, Ground and Bird
        if bird_group.sprite.alive:
            pipe_group.update()
            ground_group.update()
        bird_group.update(user_input)

        # Collision Detection
        collision_pipes = pygame.sprite.spritecollide(bird_group.sprites()[0], pipe_group, False)
        collision_ground = pygame.sprite.spritecollide(bird_group.sprites()[0], ground_group, False)
        if collision_pipes or collision_ground:
            bird_group.sprite.alive = False
            if collision_ground:
                screen.blit(game_over_image, (screen_width // 2 - game_over_image.get_width() // 2,
                                              screen_height // 2 - game_over_image.get_height() // 2))
                if user_input[pygame.K_r]:
                    score = 0
                    break

        # Spawn Pipes
        if pipe_timer <= 0 and bird_group.sprite.alive:
            top_pipe_x, bottom_pipe_x = 550, 550
            top_pipe_y = random.randint(-600, -480)
            bottom_pipe_y = top_pipe_y + random.randint(90, 130) + bottom_pipe_image.get_height()
            pipe_group.add(Pipe(top_pipe_x, top_pipe_y, top_pipe_image, 'top'))
            pipe_group.add(Pipe(bottom_pipe_x, bottom_pipe_y, bottom_pipe_image, 'bottom'))
            pipe_timer = random.randint(180, 250)
        pipe_timer -= 1

        clock.tick(60)
        pygame.display.update()


# Menu
def menu():
    global game_active

    while game_active:
        quit_game()

        # Draw Menu
        screen.fill((0, 0, 0))
        screen.blit(background_image, (0, 0))
        screen.blit(ground_image, Ground(0, 520))
        screen.blit(bird_sprites[0], (100, 250))
        screen.blit(start_image, (screen_width // 2 - start_image.get_width() // 2,
                                  screen_height // 2 - start_image.get_height() // 2))

        # User Input
        user_input = pygame.key.get_pressed()
        if user_input[pygame.K_SPACE]:
            main()

        pygame.display.update()


menu()
