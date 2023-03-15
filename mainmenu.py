from announcement import Announcement
from subscribe import Subscribe


def MainMenu():
    print("Main Menu")
    selectmenu = input(str("""
mm - Main Menu
an - Announcement
sb - Subscribe More
"""))
    if selectmenu == "mm":
        MainMenu()
    elif selectmenu == "an":
        Announcement()
        MainMenu()
    else:
        Subscribe()
        MainMenu()


