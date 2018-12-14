"""
Importing the os to get directory and
searching a file

Importing base64 to save the score on another file
with base64 encoding

Importing the pygame to make the window and all the
mechanic functions

Importing sys to break the mainloop if the
GUI is closed

Importing random to get the obstacle randomly

Importing the Class of Character and Obstacle
from another files
"""
import os, base64, pygame, sys, random
from pygame.locals import *
from assets.character import Character
from assets.obstacle import Obstacle

"""
Make the class of Game
"""
class Game:

    """
    Initiating all the unit of the game
    """
    def __init__(self):
        pygame.init()

        # Searching the file of font to get the absolute path
        self.font = self.search("FFFFORWA.TTF") + "/" + "FFFFORWA.TTF"

        # Defining a variable for the width and height of game window
        self.screen_width = 800
        self.screen_height = 600

        # Save the display in the variable
        self.screen = pygame.display.set_mode((self.screen_width,
                        self.screen_height))

        # Setting the caption for the GUI
        pygame.display.set_caption('Block Dash by Muhammad Ariq Basyar')

        # Default bes score is 0
        self.best_score_val = 0

        # searching a file and read to get the save file of best score
        file_log = self.search("LOG.txt") + "/" + "LOG.txt"
        file = open(file_log, "r")
        isi_file = file.read().split()
        file.close()

        # Checking the file if the file is real to minimize expliotation
        try:
            self.isi_log = isi_file[0]
            decoded_isinya = str(base64.b64decode(self.isi_log))[2:-1]
            if decoded_isinya[:13] == "best score = " :
                self.best_score_val = float(decoded_isinya[13:])
        except:
            self.best_score_val = 0



    """
    Define a function to make a text
    with font and size also the color
    """
    def make_text(self, message, textFont, textSize, textColor):
        newFont = pygame.font.Font(textFont, textSize)
        newText = newFont.render(message, 0, textColor)
        return newText

    """
    Defining a function to save the
    best score to another file with
    base64 encoding
    """
    def save_the_score(self):

        # Search the file with my function and open it
        file_output = self.search("LOG.txt") + "/" + "LOG.txt"
        file = open(file_output, "w")

        # Write a base64 encoding for the best score
        file.write(str(base64.b64encode(f'best score = {self.best_score_val:.1f}'.encode()))[2:-1])
        file.close()

    """
    Defining a menu session for
    the menu of the game
    """
    def menu(self):
        # The mainloop (while loop) of the menu to make better game
        while True:

            # Filling the screen with blue color
            self.screen.fill((70, 20, 200))

            # Make the header text on the menu
            self.header = self.make_text("Block Dash",
                            self.font, 60, (255, 255, 0))
            self.best_score = self.make_text(f"Best Score: {self.best_score_val}",
                            self.font, 25, (140, 128, 120))
            self.start = self.make_text("Start", self.font, 30,
                            (100, 255, 150))
            self.help = self.make_text("Help", self.font, 30, (100, 255, 150))
            self.about = self.make_text("About", self.font, 30,
                            (100, 255, 150))
            self.exit = self.make_text("Exit", self.font, 30, (100, 255, 150))
            self.reset = self.make_text("Reset", self.font, 25, (0, 0, 0))

            # Place all the text to the screen of game menu
            self.screen.blit(self.header,
                (self.screen_width/2 - (self.header.get_rect()[2]/2), 100))
            self.screen.blit(self.best_score,
                (self.screen_width/2 - (self.best_score.get_rect()[2]/2),
                    230))
            self.screen.blit(self.start,
                (self.screen_width/2 - (self.start.get_rect()[2]/2), 300))
            self.screen.blit(self.help,
                (self.screen_width/2 - (self.help.get_rect()[2]/2), 350))
            self.screen.blit(self.about,
                (self.screen_width/2 - (self.about.get_rect()[2]/2), 400))
            self.screen.blit(self.exit,
                (self.screen_width/2 - (self.exit.get_rect()[2]/2), 450))
            self.screen.blit(self.reset,
                (self.screen_width - (self.reset.get_rect()[2]) - 15, 555))


            # Make a rectangle for the button
            self.start_rect = Rect(347, 300, 106, 47)
            self.help_rect = Rect(347, 350, 106, 47)
            self.about_rect = Rect(347, 400, 106, 47)
            self.exit_rect = Rect(347, 450, 106, 47)
            self.reset_rect = Rect(690, 555, 95, 36)


            # Don't forget to update the display
            pygame.display.update()

            # Looking for the every event clicked on the game
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    mouse_pos = event.pos  # gets mouse position
                    # checks if mouse position is over the button
                    if self.start_rect.collidepoint(mouse_pos):
                        self.main()
                    elif self.help_rect.collidepoint(mouse_pos):
                        self.help_session()
                    elif self.about_rect.collidepoint(mouse_pos):
                        self.about_session()
                    elif self.reset_rect.collidepoint(mouse_pos):

                        # Make all the assets of the reset choices
                        reset_image = Obstacle((0, 0, 0), 225, 200, 350, 200)
                        reset_image.set_alpha(190)
                        list_of_reset = pygame.sprite.Group()
                        list_of_reset.add(reset_image)
                        list_of_reset.draw(self.screen)

                        # The mainloop of the reset
                        while True:

                            # Make the text to place on the screen
                            self.reset_sure = self.make_text("Are you sure?",
                                        self.font, 35, (100, 255, 150))
                            self.reset_yes = self.make_text("Yes",
                                        self.font, 30, (100, 255, 150))
                            self.reset_no = self.make_text("No",
                                        self.font, 30, (100, 255, 150))

                            # Placing all the text on the screen
                            self.screen.blit(self.reset_sure,
                                        (self.screen_width/2 - (self.reset_sure.get_rect()[2]/2) + 3,
                                        230))
                            self.screen.blit(self.reset_yes,
                                        (290,
                                        320))
                            self.screen.blit(self.reset_no,
                                        (460,
                                        320))

                            # Make the rectangle of button
                            self.reset_yes = Rect(290, 320, 106, 47)
                            self.reset_no = Rect(460, 320, 106, 47)

                            # Don't forget to update the display
                            pygame.display.update()

                            # Checks all event in the game
                            for event in pygame.event.get():
                                if event.type == MOUSEBUTTONDOWN:
                                    mouse_pos = event.pos  # Gets mouse position
                                    # Checks if mouse position is over the button
                                    if self.reset_no.collidepoint(mouse_pos):
                                        self.menu()
                                    if self.reset_yes.collidepoint(mouse_pos):
                                        self.best_score_val = 0
                                        self.menu()

                                # Checks if the user is want to quit game
                                if event.type == QUIT:
                                    self.save_the_score()
                                    pygame.quit()
                                    sys.exit()

                    # If the user is clicked at the button of exit
                    elif self.exit_rect.collidepoint(mouse_pos):
                        self.save_the_score()
                        pygame.quit()
                        sys.exit()

                # Make the boolean if user want to exit
                if event.type == QUIT:

                    # Don't forget to save the file
                    self.save_the_score()

                    # Quiting the GUI with pygame.quit and
                    # destroy the mainloop with sys.exit()
                    pygame.quit()
                    sys.exit()

    """
    Make a function to search a file
    on your folder
    """
    def search(self, folder):
        for dir_name, dirs, files in os.walk(os.getcwd()):
            if folder in files:
                # All we need is just the directory name
                return dir_name

    """
    Defining a function to reset
    all the data (the best score)
    """
    def reset_data(self):
        self.best_score_val = 0
        self.menu()

    """
    Defining a function to move to
    about session
    """
    def about_session(self):

        # Searching the file of about me and open it
        # Also write it on the screen of Game
        file_about = self.search("ABOUT ME.txt") + "/" + "ABOUT ME.txt"
        file = open(file_about, "r")
        isi = list(map(lambda s: s.strip(), file.readlines()))
        file.close()
        x = 20

        # The mainloop of the about session
        while True:

            # Filling the screen with aqua color
            self.screen.fill((0, 255, 255))

            # For loop to print all the text on my file about me
            y = 50
            for i in isi:
                self.isi_help_session = self.make_text(i,
                                self.font, 16, (128, 0, 128))
                self.isi_rect = self.isi_help_session.get_rect()
                self.screen.blit(self.isi_help_session, (x, y))
                y += 25


            # Make the text for the button to back to the menu
            self.back = self.make_text("Back to Menu",
                            self.font, 16, (255, 0, 0))
            self.back_rect = self.back.get_rect()
            self.screen.blit(self.back,
                (self.screen_width/2 - (self.back_rect[2]/2),
                    self.screen_height/2 - 20))

            # Don't forget to update the display on mainloop
            pygame.display.update()

            # Make a rectangle for the button to back to the menu
            self.back_rect = Rect(329, 280, 142, 23)
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    mouse_pos = event.pos  # Gets mouse position
                    # Checks if mouse position is over the button
                    if self.back_rect.collidepoint(mouse_pos):
                        self.menu()
                if event.type == QUIT:
                    self.save_the_score()
                    pygame.quit()
                    sys.exit()

    """
    Define a func to get to the
    help session
    """
    def help_session(self):
        file_help = self.search("help.txt") + "/" + "help.txt"
        file = open(file_help, "r")
        isi = list(map(lambda s: s.strip(), file.readlines()))
        file.close()

        # Mainloop of the help session
        while True:
            self.screen.fill((0, 255, 255))
            y = self.screen_height/2 - 100
            for i in isi:
                self.isi_help_session = self.make_text(i,
                        self.font, 16, (128, 128, 128))
                self.isi_rect = self.isi_help_session.get_rect()
                self.screen.blit(self.isi_help_session,
                        (self.screen_width/2 - (self.isi_rect[2]/2), y))
                y += 25

            #  Make the text to back to the menu
            self.back = self.make_text("Back to Menu",
                    self.font, 16, (255, 0, 0))
            self.back_rect = self.back.get_rect()

            # Placing the te=xt on the center
            self.screen.blit(self.back,
                    (self.screen_width/2 - (self.back_rect[2]/2),
                            self.screen_height/2 + 30))

            # Updating the
            pygame.display.update()

            # Make a rectangle for the button
            self.back_rect = Rect(329, 330, 142, 23)
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    mouse_pos = event.pos  # gets mouse position
                    # checks if mouse position is over the button
                    if self.back_rect.collidepoint(mouse_pos):
                        self.menu()
                if event.type == QUIT:
                    self.save_the_score()
                    pygame.quit()
                    sys.exit()

    """
    Defining the main function of the Game
    to make the game screen
    """
    def main(self):

        # Make all the obstacle randomly
        self.obstacle_1 = Obstacle((random.randint(0, 255),
                                    random.randint(0, 255),
                                    random.randint(0, 255)),
                                    800, 470, 40, 40)

        self.obstacle_2 = Obstacle((random.randint(0, 255),
                                    random.randint(0, 255),
                                    random.randint(0, 255)),
                                    1067, 470, 40, 40)

        self.obstacle_3 = Obstacle((random.randint(0, 255),
                                    random.randint(0, 255),
                                    random.randint(0, 255)),
                                    1334, 470, 40, 40)

        self.land = Obstacle((0, 128, 128), 0, 510, 800, 90)
        self.char = Character((0, 200, 75), 90, 470, 40, 40)

        # Grouping the obstacle to make them move together
        self.all_sprites_list = pygame.sprite.Group()
        self.all_block_list = pygame.sprite.Group()
        self.all_sprites_list.add(self.obstacle_1,
                                self.obstacle_2,
                                self.obstacle_3,
                                self.land)

        self.all_block_list.add(self.obstacle_1,
                                self.obstacle_2,
                                self.obstacle_3)

        # Frame rate per secon for the smoothness of screen
        fps = 60
        clock = pygame.time.Clock()

        # Counter for the score
        self.current_score = 0

        # All units for jumping
        self.naik  = False
        self.turun = False
        self.velocity_index = 0
        self.platform_y = 470


        # Counter for the countdown
        count = 3


        # The mainloop of the screen game
        while True:

            # check if current score is greater than best score
            if self.current_score >= self.best_score_val:
                self.best_score_val = self.current_score

            # Make the while loop for the countdown
            while count > 0 :
                self.screen.fill((0, 255, 255))

                self.the_score = self.make_text(f"score: {self.current_score:.1f}",
                        self.font, 14, (250, 100, 0))
                self.screen.blit(self.the_score,
                        (self.screen_width - (self.the_score.get_rect()[2]) - 10,
                                10))

                self.the_best_score = self.make_text(f"Best score: {self.best_score_val:.1f}",
                        self.font, 14, (250, 100, 0))
                self.screen.blit(self.the_best_score,
                        (self.screen_width - (self.the_best_score.get_rect()[2]) - 10,
                                30))

                self.all_sprites_list.draw(self.screen)

                pygame.draw.rect(self.screen,
                                self.char.color,
                                (self.char.rect.x,
                                self.char.rect.y,
                                self.char.rect.width,
                                self.char.rect.height))

                self.counter = self.make_text(str(count),
                                self.font, 120, (0, 0, 0))

                self.screen.blit(self.counter, (200, 200))
                pygame.display.update()
                pygame.time.delay(1000)
                count -= 1
                for event in pygame.event.get():
                    if event.type == QUIT:
                        self.save_the_score()
                        pygame.quit()
                        sys.exit()

            # Filling the screen with aqua
            self.screen.fill((0, 255, 255))

            # Make the text of the score and best score on the right top
            self.the_score = self.make_text(f"Score: {self.current_score:.1f}",
                    self.font, 14, (250, 100, 0))
            self.screen.blit(self.the_score,
                    (self.screen_width - (self.the_score.get_rect()[2]) - 10,
                            10))
            self.the_best_score = self.make_text(f"Best score: {self.best_score_val:.1f}",
                    self.font, 14, (250, 100, 0))
            self.screen.blit(self.the_best_score,
                (self.screen_width - (self.the_best_score.get_rect()[2]) - 10,
                    30))

            # Draw all sprites
            self.all_sprites_list.draw(self.screen)
            pygame.draw.rect(self.screen,
                            self.char.color,
                            (self.char.rect.x,
                            self.char.rect.y,
                            self.char.rect.width,
                            self.char.rect.height))




            # Don't forget to update the list of sprites and display
            self.all_block_list.update()
            pygame.display.update()
            for i in self.all_block_list:

                # Detect if the player collides with obstacle
                if pygame.sprite.collide_rect(self.char, i):
                    # print(self.char.rect.y)
                    # If collide on the left side of obstacle
                    if  i.rect.y - 32 < self.char.rect.y < i.rect.y + 35:

                        # Make the screen of game over
                        end_image_1 = Obstacle((0, 0, 0), 0, 0, 800, 600)
                        end_image_1.set_alpha(120)
                        end_image_2 = Obstacle((0, 0, 0), 200, 50, 400, 500)
                        end_image_2.set_alpha(65)

                        # Make a group of sprites
                        list_of_end = pygame.sprite.Group()
                        list_of_end.add(end_image_1)
                        list_of_end.add(end_image_2)
                        list_of_end.draw(self.screen)

                        # Save the score before make decision on game over menu
                        self.save_the_score()

                        # Mainloop for the game over's screen
                        while True:

                            # The title is Game Over
                            self.pause_text = self.make_text("Game Over",
                                            self.font, 49, (0, 255, 255))
                            self.screen.blit(self.pause_text, (245, 100))

                            # The player's score
                            self.current_score_text = self.make_text(f"Your score is: {self.current_score:.1f}",
                                    self.font, 25, (0, 200, 255))
                            self.screen.blit(self.current_score_text,
                                    (self.screen_width/2 - (self.current_score_text.get_rect()[2]/2),
                                            180))

                            # The best score
                            self.best_score_text = self.make_text(f"Best score is: {self.best_score_val:.1f}",
                                    self.font, 25, (0, 200, 255))
                            self.screen.blit(self.best_score_text,
                                    (self.screen_width/2 - (self.best_score_text.get_rect()[2]/2), 230))

                            # Make a text to restart the screen of game
                            self.restart_text = self.make_text("Restart",
                                    self.font, 40, (0, 255, 255))
                            self.screen.blit(self.restart_text, (305, 290))

                            # Make the text to go to the menu
                            self.menu_text = self.make_text("Menu",
                                    self.font, 40, (0, 255, 255))
                            self.screen.blit(self.menu_text, (330, 370))

                            # Text for exiting the program
                            self.exit_text = self.make_text("Exit",
                                    self.font, 40, (0, 255, 255))
                            self.screen.blit(self.exit_text, (355, 450))

                            # Make the rectangle for the buttons of
                            # restart, menu and exit
                            self.restart_text = Rect(305, 290, 200, 56)
                            self.menu_text = Rect(330, 370, 145, 56)
                            self.exit_text = Rect(355, 450, 100, 56)

                            # Don't forget to update the screen
                            pygame.display.update()
                            event = pygame.event.wait()

                            # Checks if playes is pressing something
                            if pygame.key.get_pressed()[K_ESCAPE] :
                                break

                            # Quit the program
                            if event.type == QUIT:
                                self.save_the_score()
                                pygame.quit()
                                sys.exit()

                            # Checks when playes is clicking something
                            if event.type == MOUSEBUTTONDOWN:
                                mouse_pos = event.pos # Gets mouse position
                                # Checks if mouse position is over the button
                                if self.restart_text.collidepoint(mouse_pos):
                                    self.main()
                                if self.menu_text.collidepoint(mouse_pos):
                                    self.menu()
                                if self.exit_text.collidepoint(mouse_pos):
                                    self.save_the_score()
                                    pygame.quit()
                                    sys.exit()

                    # If collide on the bottom of obstacle
                    elif self.char.rect.y > i.rect.y + i.rect.height - 15:
                        self.char.rect.y = i.rect.y + i.rect.height
                        self.velocity_index = 0
                        self.turun = True
                        self.naik = False

                    # If collide on top side of obstacle
                    else:
                        self.char.rect.y = i.rect.y - i.rect.height
                        self.turun = False
                        self.velocity_index = 0
                        if (pygame.key.get_pressed()[K_UP] or pygame.key.get_pressed()[K_SPACE]):
                            self.naik = True

                # Make the gravity and the character is always going to down
                # the character's oordinate is below 469 and the character
                # is not down
                elif self.char.rect.y < 469 and not self.naik:
                    self.turun = True

            # Make the list of velocity to up and down
            self.vel_naik = [i/3 for i in range (-40, 1, 2)]
            self.vel_turun = [i/3 for i in range (0, 41, 2)]

            # Make the up algorithm
            if self.naik:
                self.char.rect.y += self.vel_naik[self.velocity_index]
                self.velocity_index += 1

                # The character is going to down if the velocity index is
                # greater than the length of list of velocity
                if self.velocity_index >= len(self.vel_naik) - 1:

                    # Make the index is back to zero and self.turun is True
                    self.velocity_index = 0
                    self.naik = False
                    self.turun = True

            # Also the down algorithm
            if self.turun:
                self.char.rect.y += self.vel_turun[self.velocity_index]
                self.velocity_index += 1
                if self.velocity_index >= len(self.vel_turun) - 1:
                    self.velocity_index -= 1

                # If the character's oordinate is above 470, the character's
                # orrdinate is 470 so the character doesn't go to the below
                # of the land
                if self.char.rect.y >= 470:
                    self.char.rect.y = 470
                    self.velocity_index = 0
                    self.turun = False


            # Set the speed of frame on your computer
            clock.tick(fps)

            # Counter for the score
            self.current_score += 0.2

            # Make the game is faster every loop
            fps += 0.02

            # Checks all event on the game
            for event in pygame.event.get():

                # Checks if the player is want to exit
                if event.type == QUIT:
                    self.save_the_score()
                    pygame.quit()
                    sys.exit()


                # Check if the player is want to jump
                if (pygame.key.get_pressed()[K_UP] or pygame.key.get_pressed()[K_SPACE]) and not (self.naik or self.turun):
                    self.naik = True


                # Check if player want to pause the game
                if pygame.key.get_pressed()[K_ESCAPE] :

                    # Make the transparant black blocks for the pause menu
                    pause_image_1 = Obstacle((0, 0, 0), 250, 100, 300, 400)
                    pause_image_1.set_alpha(90)
                    pause_image_2 = Obstacle((0, 0, 0), 0, 0, 800, 600)
                    pause_image_2.set_alpha(120)

                    # Grouping the sprites of pause menu
                    list_of_pause = pygame.sprite.Group()

                    # Add all the transparant black blocks to the
                    # sprites group
                    list_of_pause.add(pause_image_1, pause_image_2)

                    # Draw all the list of sprites to the main screen
                    list_of_pause.draw(self.screen)

                    # Pause screen's mainloop
                    while True:

                        # Make all the text of pause menu
                        # The title "Paused"
                        self.pause_text = self.make_text("Paused",
                                self.font, 59, (100, 255, 255))
                        self.screen.blit(self.pause_text, (265, 125))

                        # The text "Resume"
                        self.resume_text = self.make_text("Resume",
                                self.font, 40, (0, 255, 255))
                        self.screen.blit(self.resume_text, (302, 230))

                        # The text "Restart"
                        self.restart_text = self.make_text("Restart",
                                self.font, 40, (0, 255, 255))
                        self.screen.blit(self.restart_text, (305, 300))

                        # The text "Menu"
                        self.menu_text = self.make_text("Menu",
                                self.font, 40, (0, 255, 255))
                        self.screen.blit(self.menu_text, (330, 370))

                        # The text "exit"
                        self.exit_text = self.make_text("Exit",
                                self.font, 40, (0, 255, 255))
                        self.screen.blit(self.exit_text, (350, 440))

                        # Makes the buttons of pause menu with rectangle
                        # The button "Resume"
                        self.resume_rect = Rect(302, 230, 200, 56)

                        # The button "Restart"
                        self.restart_rect = Rect(305, 300, 272, 82)

                        # The button "Menu"
                        self.menu_rect = Rect(330, 370, 200, 56)

                        # The button "exit"
                        self.exit_rect = Rect(350, 440, 145, 56)

                        # Don't forget to always update the screen
                        pygame.display.update()

                        # The event is wait and waiting for the next event
                        event = pygame.event.wait()

                        # Checks if the player is pressing something
                        if pygame.key.get_pressed()[K_ESCAPE] :
                            break
                        if event.type == QUIT:
                            self.save_the_score()
                            pygame.quit()
                            sys.exit()

                        # Checks if the playes is clicking something
                        if event.type == MOUSEBUTTONDOWN:

                            # Gets the mouse position
                            mouse_pos = event.pos

                            # Checks if the mouse position if above the button
                            if self.resume_rect.collidepoint(mouse_pos):
                                break

                            if self.restart_rect.collidepoint(mouse_pos):

                                # Go to the main program if the mouse hit the
                                # "Restart" button
                                self.main()

                            if self.menu_rect.collidepoint(mouse_pos):

                                # Go back to the menu if the mouse hit the
                                # "Menu" button
                                self.menu()

                            if self.exit_rect.collidepoint(mouse_pos):
                                self.save_the_score()
                                pygame.quit()
                                sys.exit()
