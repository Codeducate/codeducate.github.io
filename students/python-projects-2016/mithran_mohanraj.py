import pygame
import sys
from pygame.locals import*
img = pygame.image.load('calculator.bmp')

#Welcome to the calculator's code! Press the play button!
number_one = int(input("What is your first number? (Please make real number):"))
operation = input("Choose an operation, +, -, *, /, or ^ for an exponent:")
number_two = int(input("What is your second number? (Please make real number):"))

if operation == "+":
    solution = number_one + number_two
elif operation == "-":
    solution = number_one - number_two
elif operation == "*":
    solution = number_one * number_two
elif operation == "/":
    solution = number_one / number_two
elif operation == "^":
    solution = number_one ** number_two
else:
    print("IT LOOKS LIKE YOU DIDN'T INPUT +, -, *, /, or ^!!!")
    sys.exit()

solution = str(solution)
print("THE SOLUTION IS HERE:" + solution)
copy_paste = "Look at the 'Python Shell' to copy and paste the answer!"

pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

size = (1279, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Red Calculator")

# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here... but there is no game...

    # --- Drawing code should go here...
    screen.fill(WHITE)
    screen.blit(img,(0,0))
    font = pygame.font.SysFont('Comic Sans MS', 72, True, False)
    text = font.render((solution), True, WHITE)
    screen.blit(text, [180, 70])
    font2 = pygame.font.SysFont('Comic Sans MS', 36, True, False)
    text2 = font2.render((copy_paste), True, WHITE)
    screen.blit(text2, [130, 210])
    # --- Flip the screen
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
pygame.quit()