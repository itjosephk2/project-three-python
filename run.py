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
