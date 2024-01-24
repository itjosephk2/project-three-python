import os
import random
import time

# Tutorial system variables
is_game_loop = True
is_player_turn = True


class Fighter:
    """
    Class for fighter
    """
    energy_blast_counter = 0

    def __init__(
            self, name: str, hp: int,
            attack: int, defense: int, special: int, speed: int
    ):
        self.name = name
        self.hp = hp
        self.hp_remaining = hp
        self.attack = attack
        self.defense = defense
        self.special = special
        self.speed = speed


def clear():
    """
    Clears the screen
    :return:
    """
    os.system("clear")


def floss_dance_animation():
    """
    Fun winning animation that looks like loading screen
    :return:
    """
    frames = [
        "   O     ",
        "   /|\\    ",
        "   / \\    ",
        "          ",
        "   O     ",
        "  /|\\    ",
        "  / \\    ",
        "          ",
        "   O     ",
        "  /|\\    ",
        "  / \\    ",
        "          ",
        "   O     ",
        "   /|\\    ",
        "   / \\    ",
        "          ",
        "   O     ",
        "  /|\\    ",
        "  / \\    ",
        "          ",
    ]
    # Iterate through 4 lines of the array to represent a full human
    for i in range(0, len(frames), 4):
        clear()
        for j in range(4):
            print(frames[i + j])
        time.sleep(0.2)


def draw_line():
    """
    Prints a border for the screen width
    :return:
    """
    print(
        "Xx-------------------------------------"
        "--------------------------------------xX"
    )

def main():
    """
    Main method that prints the main menu
    :return:
    """
    clear()
    draw_line()
    print("  Dragon Ball Z Fighters")
    print("  This is a dragon ball z fighting game.")
    draw_line()
    input("> Continue")
    clear()
    draw_line()
    print("1: Story Mode")
    print("2: Free Battle")
    print("3: Tutorial")
    print("0: Quit")
    draw_line()
    main_menu_choice = input("> ")
    game_loop(main_menu_choice)


def draw_goku():
    """
    Draws Goku to the screen
    :return:
    """
    clear()
    draw_line()
    print("             ___     -._")
    print("            `-. \"\"\"--._ `-.")
    print("               `.      \"\"\"-. `.")
    print(" _____           `.       `.\ ")
    print("`-.   \"\"\"---.._    \\        `.\\ ")
    print("   `-.         \"-.  \\         `\\")
    print("      `.          `-.\\         "
          " \\_.-\"\"\"\"\"\"\"\"\"--._")
    print("        `.           `                          \"-.")
    print("          `.                    "
          "                   `.    __....-------...")
    print("--..._      \\                       "
          "                `--\"\"\"\"\"\"---...")
    print("__...._\"_-.. \\                      "
          " _,                             _..-\"\"")
    print("`-.      \"\"\"--`           /      "
          " ,-'/|     ,                   _.-\"")
    print("   `-.                 , /|  "
          "   ,'  / |   ,'|    ,|        _..-\"")
    print("      `.              /|| |    /   / |  ,"
          "'  |  ,' /        ----\"\"\"\"\"\"_`-")
    print("        `.            ( \\  \\      | "
          " | /   | ,'  //                 _.-\"")
    print("          `.        .'-\\/\"\"\\ |  ' "
          " | /  .-/'\"`\\' //            _.-\"")
    print("    /'`.____`-.  ,'\"\\  ''''?-V`.  "
          " |/ .'..-P''''  /\"`.     _.-\"")
    print("   '(   `.-._\"\"  ||(?|    /'   >.\\ "
          " ' /.<   `\\    |P)||_..-\"___.....---")
    print("     `.   `. \"-._ \\ ('   |     `8 "
          "     8'     |   `) /\"\"\"\"_\".\"")
    print("       `.   `.   `.`.b|   `.__    "
          "        __.'   |d.'  __...--\"\"")
    print("         `.   `.   \".`-  .---      "
          ",-.     ---.  -'.-\"")
    print("           `.   `.   \"\"|      -._ "
          "     _.-      |\"")
    print("             `.  .-\"`.  `.      "
          " `\"\"\"'       ,'")
    print("               `/     `.. \"\"--."
          ".__    __..--\"\"")
    print("                `.      /7.--|   "
          " \"\"\"\"    |--.__")
    print("                  ..--\"| (  /'  "
          "          `\\  ` \"\"--..")
    print("               .-\"      \\\\  |\"\""
          "--.    .--\"|          \"-.")
    print("              <.         \\\\  `.   "
          " -.    ,'       ,'     >")
    print("             (P'`.        `%,  `.     "
          " ,'        /,' .-\"?)")
    print("             P    `. \\      `%,  `.  "
          ",'         /' .'     \\")
    print("            | --\"  _\\||       `%,  `"
          "'          /.-'   .    )")
    print("            |       `-\"\"--..   `%..--"
          "\"\"\"\\\"--.'       \"-  |")
    print("            \\          `.  .--\"\"  \""
          "\\.\\.\\ \\\\.'       )     |")
    print("                  You play as Goku in the main Story Line")
    draw_line()
    input("> Continue")

def goku_meets_yamcha():
    clear()
    draw_line()
    print("  Goku and krillin are travelling through the dessert.")
    print("  Krillin: Goku where are we going?")
    print("  Goku: I'm hungry!!")
    print("  Krillin: Me too, But seriously where are we going?")
    print("  Goku: I'm not sure krillin.")
    print("  Master-Roshi just sent us out to"
          " get him something from the ox king.")
    print("  Krillin: Look over there !!")
    print("  An oasis there might be food near the water.")
    print("  Narrator: Goku and Krillin "
          "stumble across a juicy leg of meat.")
    print("  It almost looks too god to be true!!")
    print("  Have they stumbled upon a life saving meal.")
    print("  or have they come across "
          "some trap left out by evil poachers.")
    draw_line()
    input('> Continue')
    clear()
    draw_line()
    print("  Goku runs Towards the food.")
    print("  Just as he goes to pick u"
          "p the food a man jumps out.")
    print("  Anonymous: Hey! WHat are "
          "you doing! My name is Yamcha.")
    print("  Yamcha: This is my trap "
          "for catching sojme larger food!")
    print("  Goku: I..")
    print("  Yamcha Interupts Goku.")
    print("  Yamcha: Don't you dare steal my food kid.")
    print("  Yamcha: Let's fight to s"
          "ettle this.")
    print("  Krillin: Don't do this Go"
          "ku it could be very dangerous.")
    print("  Goku: Let's go Yamcha, I n"
          "ever back down from a challenge.")
    draw_line()
    input('> Continue')

if __name__ == "__main__":
    clear()
    draw_line()
    print("   __")
    print("  |  \"\"--.--.._                 "
          "                            __..    ,--.")
    print("  |       `.   \"-.\"\\_...-----"
          "..._   ,--. .--..-----.._.\"\"|   |   /   /")
    print("  |_   _    \\__   ).  \\       "
          "    _/_ |   \\|  ||  ..    >  `.  |  /   /")
    print("    | | `.   ._)  /|\\  \\ .-\"\"\":-\" "
          "  \"-.   `  ||  |.'  ,'`. |  |_/_  /")
    print("    | |_.'   |   / \"\"`  \\  ===/  "
          "..|..  \\     ||      < \"\"  `.  \"  |/__")
    print("    `.      .    \\ ,--   \\-..-\\  "
          " /\"\\   /     ||  |>   )--   |    /    |")
    print("     |__..-'__||__\\   |___\\ __.:-."
          "._..-'_|\\___||____..-/  |__|--\"____/")
    print("                           ______"
          "_________________")
    print("                          /      "
          "                ,'")
    print("                         /     "
          " ___            ,'")
    print("                        /   "
          "_.-'  ,'        ,-'   /")
    print("                       / ,-'"
          " ,--."
          "'        ,'   .'/")
    print("                      /.'     `. "
          "        '.  ,' /")
    print("                     /      ,-' "
          "      ,\"--','  /")
    print("                          ,'    "
          "    ,'  ,'    /")
    print("                         ,-'   "
          "   ,' .-'     /")
    print("                      ,-'      "
          "             /")
    print("                    ,:_______"
          "______________/")
    draw_line()
    time.sleep(1.5)
    main()
