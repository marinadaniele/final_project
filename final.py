import pygame
import random
import sys

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

def roll_dice():
    return random.randint(1, 6)

def initial_decision():
    player_name = input("Please enter your name: ")
    while player_name == "":
        print("You did not enter your name")
        player_name = input("Please enter your name: ")
    print(
        f"\n{player_name}, you've been trapped in the Alcazar by Vampire Bogdan for not submitting your final project on time. He's holding you captive in a cage and wants you to complete your project by the morning.")
    decision = input("Do you attempt to finish your project by morning or plan your escape? (finish/escape) ").lower()

    if decision == "finish":
        print("You fail to complete the project. You did not follow in class. You're dead.")
        sys.exit()
    elif decision == "escape":
        print("You decide to plan your escape. Let's move on to the next decision.")

def second_decision():
    decision = input("You notice there is a metal bar in your cage. Bogdan gets distracted by an infinite loop. Do you try to steal his keys from his back pocket (steal) or knock him out with the metal bar? (knockout) ").lower()

    if decision == "steal":
        print("He catches you trying to steal his keys and kills you. The game is over.")
        sys.exit()
    elif decision == "knockout":
        print("You knock him out (sorry professor), get his keys, and manage to escape the cage. You move to the dining hall.")
    else:
        print("Invalid action.")
        second_decision()

def roll_dice():
    return random.randint(1, 6)

def roll_for_escape():
    print("In order to move to the next room, you have to roll a 6 on a normal dice.")

    input("Press Enter to roll the dice...")
    dice_roll = roll_dice()
    print(f"You rolled a {dice_roll}.")

    while dice_roll != 6:
        print("You didn't roll a 6, try again.")
        input("Press Enter to roll the dice...")
        dice_roll = roll_dice()
        print(f"You rolled a {dice_roll}.")

    print("You can now enter the kitchen. You hear noises, Bogdan has woken up and is looking for you!! You have to hurry!!!")
    print("You see a knife, garlic, and a bug. You can only take one. Choose wisely.")

def select_weapon():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Select your weapon")

    # Load images
    knife_img = pygame.image.load("knife.png")
    garlic_img = pygame.image.load("garlic.png")
    bug_img = pygame.image.load("bug.png")

    # Define rects for images
    knife_rect = knife_img.get_rect(topleft=(100, 200))
    garlic_rect = garlic_img.get_rect(topleft=(200, 200))
    bug_rect = bug_img.get_rect(topleft=(400, 200))

    running = True
    weapon = ""
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if knife_rect.collidepoint(event.pos):
                    running = False
                    weapon = "knife"
                elif garlic_rect.collidepoint(event.pos):
                    running = False
                    weapon = "garlic"
                elif bug_rect.collidepoint(event.pos):
                    running = False
                    weapon = "bug"

        screen.fill(WHITE)
        screen.blit(knife_img, knife_rect)
        screen.blit(garlic_img, garlic_rect)
        screen.blit(bug_img, bug_rect)
        pygame.display.flip()

    return weapon

def main():
    initial_decision()
    second_decision()
    roll_for_escape()
    weapon = select_weapon()

    if weapon == "knife":
        print("Bogdan kills you. The game ends.")
        sys.exit()
    elif weapon in ["garlic"]:
        print(f"You selected garlic. You gain time as Bogdan gets scared and runs away.")
        print("You manage to escape the Alcázar.")
        final_decision()
    elif weapon in ["bug"]:
        print(f"You selected bug. You gain time as Bogdan stops to debug.")
        print("You manage to escape the Alcázar.")
        final_decision()

def final_decision():
    decision = input("Do you run to Madrid or to the ethics department? (madrid/ethics) ").lower()
    if decision == "madrid":
        print("Bogdan rats you out for not submitting your work on time. You get expelled. Your parents kill you. Game over.")
    elif decision == "ethics":
        print("You win the game! The ethics department cures Bogdan, and he returns to being a human. Segovia is finally free. You still have to submit your work though 😃")

if __name__ == "__main__":
    main()
