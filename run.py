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

def goku_meets_ox_king():
    clear()
    draw_line()
    print("  Goku: Wow that was a great Fight.")
    print("  Yamcha: You are a tough kid Goku.")
    print("  Goku: thank you Master Roshi trained me and Krillen.")
    print("  We are heading back there soon to continue our training.")
    print("  Would you would like to join us?")
    print("  Yamcha: Ya I would love to join"
          " ye, I want to train under this Master Roshi")
    print("  Goku: but first we must meet the"
          " ox king to get something for Master Roshi")
    draw_line()
    input('> Continue')
    clear()
    draw_line()
    print("  Goku, Krillin and yamcha walk through the dessert.")
    print("  They find their way to the ox kings village.")
    print("  The OX King appears")
    print("  OX King: Who dares come onto my land")
    print("  Goku: Hi, I am Goku,")
    print("  Master Roshi Sent us to collect a package")
    print("  OX King: Master Roshi You say, Prove it!")
    print("  He is the best trainer in all the planet.")
    print("  Beat me in a fight and I will know you are telling the truth")
    print("  Goku: Let's Fight!")
    draw_line()
    input('> Continue')
    clear()

def goku_trains_with_roshi(character: Fighter):
    clear()
    draw_line()
    print("  Goku, Krillin, and Yamcha return to Master Roshi's island.")
    print("  Master Roshi: Welcome back, my students.")
    print("  I see you've gained some experience.")
    print("  Goku: Yes, Master Roshi. ")
    print("  We had some adventures and even made a new friend, Yamcha.")
    print("  Master Roshi: Good to meet you, Yamcha.")
    print(" Now, Goku, it's time for some training.")
    print("  Goku: I'm ready, Master.")
    draw_line()
    input('> Continue')
    clear()
    draw_line()
    print("  Master Roshi trains Goku intensely, ")
    print("  focusing on enhancing his strength, speed, and techniques.")
    print("  After weeks of training, "
          "Goku's stats have improved significantly.")
    print(f"  {character.name}'s Stats After Training:")
    print(f"  HP: {character.hp + 20}")
    print(f"  Attack: {character.attack + 5}")
    print(f"  Defense: {character.defense + 3}")
    print(f"  Special: {character.special + 5}")
    print(f"  Speed: {character.speed + 3}")
    draw_line()
    input('> Continue')
    clear()
    draw_line()
    print("  Master Roshi: Well done, Goku. ")
    print("  Now, let's see how much you've improved.")
    print("  Goku and Master Roshi engage in a friendly spar.")
    draw_line()
    input('> Continue')


def goku_vs_piccolo():
    clear()
    draw_line()
    print("  The tranquil Master Roshi's island "
          "is disrupted by an ominous presence.")
    print("  Dark clouds gather, "
          "a sinister figure descends: Piccolo, the evil Namekian.")
    print("  Goku, Krillin, Yamcha, and Roshi"
          " stand united, ready to defend their home.")
    print("  Goku: Piccolo, what are you doing here?")
    print("  Piccolo: I've come to claim this island,")
    print(" and show you the true extent of my power.")
    draw_line()
    input('> Continue')

    clear()
    draw_line()
    print("  Goku: Piccolo, you won't get away with threatening our home!")
    print("  Goku unleashes his true power "
          "and transforms into a Super Saiyan!")
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
