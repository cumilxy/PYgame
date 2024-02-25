from pygame import *
import pygame_menu
from pygame_menu import *
from ping_pong import *

init()
window = display.set_mode((500,400))
menu = pygame_menu.Menu("main menu",500,400, theme=pygame_menu.themes.THEME_BLUE.copy())
def start():
    starting() 
def end():
    print('closing game...')
    exit()
def help():
    print('opening help window...')
    help_menu = pygame_menu.Menu("Help window", 500,400,theme=pygame_menu.themes.THEME_GREEN.copy())
    help_menu.add.label('Information:')
    help_menu.add.label('To play the game press "Play game"')
    help_menu.add.label('To exit the game press "Exit"')
    
    def exithlpmenu():
        menu.enable()
        help_menu.disable()
        menu.mainloop(window)
    help_menu.add.button('exit help menu', exithlpmenu)
    menu.disable()
    help_menu.mainloop(window)


menu.add.button('Play game', start)
menu.add.button('Exit game', end)
menu.add.button('Help', help)

menu.mainloop(window)
