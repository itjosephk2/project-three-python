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
