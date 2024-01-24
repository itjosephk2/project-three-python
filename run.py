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


def game_loop(main_menu_choice: str) -> None:
    """
    Controls the flow of the main Menu
    :param main_menu_choice:
    :return:
    """
    if main_menu_choice == "1":
        # Creates character for the main Game
        character_choice = Fighter("Goku", 100, 12, 7, 12, 12)
        draw_goku()

        # Chapter 1 Goku meets Yamcha
        goku_meets_yamcha()
        # create Yamcha character
        enemy_character = Fighter("Yamcha", 80, 10, 6, 3, 8)
        # Check for winner
        is_fight_won = battle_controller(character_choice, enemy_character)
        if not is_fight_won:
            print("  You lost Please try again")
            main()

        # Chapter 2 Goku meets Ox King
        goku_meets_ox_king()
        # Reset gokus health
        character_choice.hp_remaining = character_choice.hp
        # create ox king character
        enemy_character = Fighter("ox King", 120, 9, 20, 5, 5)
        # check for winner
        is_fight_won = battle_controller(character_choice, enemy_character)
        if not is_fight_won:
            print("  You lost Please try again")
            main()

        # Chapter 3 Goku trains with master roshi
        goku_trains_with_roshi(character_choice)
        # reset Gokus hp
        character_choice.hp_remaining = character_choice.hp
        # create Master Roshi character
        enemy_character = Fighter("Master Roshi", 110, 15, 10, 20, 10)
        # CHeck for the winner
        is_fight_won = battle_controller(character_choice, enemy_character)
        draw_line()
        if not is_fight_won:
            print("  Master Roshi: Not bad, Goku,")
            print(" but there's always room for improvement.")
            input('> Continue')
            main()
        else:
            print("  Master Roshi: Excellent! ")
            print("  You've grown stronger, Goku. Keep up the good work.")
        draw_line()
        input('> Continue')



        # Chapter 3 Piccolo vs Goku
        goku_vs_piccolo()

        # Set up the final battle
        enemy_character = Fighter("Piccolo", 150, 20, 18, 20, 16)

        # Goku transforms into Super Saiyan, boosting his stats
        character_choice = Fighter(
            "Super Saiyan Goku", 150, 25, 20, 100, 20)

        # Start the final battle with boosted stats
        is_fight_won = battle_controller(character_choice, enemy_character)

        clear()
        draw_line()
        if not is_fight_won:
            print("  Piccolo: You're stronger than I expected Goku."
                  " But this island is still mine.")
            print("  Piccolo creates a massive energy blast,"
                  " causing destruction around.")
            print("  Goku and his friends are forced to retreat,"
                  " vowing to return even stronger.")
            print("  Master Roshi: Goku, we'll train"
                  " harder and face Piccolo again.")
        else:
            print("  Goku: This is the power of a Super Saiyan!")
            print("  Piccolo, your reign of terror ends now!")
            print("  Piccolo, weakened and surprised by Goku's"
                  " newfound strength, admits defeat.")
            print("  Piccolo: You've surpassed my expectations,"
                  " Goku. But this isn't over.")
            print("  Piccolo retreats, promising to return stronger.")
            print("  Master Roshi: Goku, you've become"
                  " a true protector of this island.")
            print("  I'm proud of you.")
        draw_line()
        input('> Continue')
        main()

    elif main_menu_choice == "2":
        character_choice = choose_player()
        enemy_character = choose_enemy_character()
        print("  Lets fight")
        draw_line()
        input("> Continue")
        battle_controller(character_choice, enemy_character)
        main()
    elif main_menu_choice == "3":
        tutorial()
    elif main_menu_choice == "0":
        clear()
        quit()
    else:
        clear()
        draw_line()
        print("  Please enter a valid option given above")
        draw_line()
        input("> Continue")
        main()

def choose_player():
    """
    Menu for choosing your character
    :return:
    """
    is_choosing_character = True
    while is_choosing_character:
        clear()
        draw_line()
        characters = {
            "1": Fighter("Goku", 100, 12, 7, 12, 12),
            "2": Fighter("Gohan", 90, 14, 6, 14, 11),
            "3": Fighter("Vegeta", 90, 12, 8, 11, 11),
            "4": Fighter("Picolo", 100, 10, 10, 10, 10),
            "5": Fighter("Master Roshi", 80, 11, 8, 13, 7),
            "6": Fighter("ox King", 120, 9, 20, 5, 5),
            "7": Fighter("Yamcha", 80, 10, 6, 3, 8),
            "8": Fighter("Krillin", 90, 9, 11, 6, 11),
            "9": Fighter("King Kai", 130, 9, 7, 10, 8)
        }
        print("1: Goku")
        print("2: Gohan")
        print("3: Vegeta")
        print("4: Picolo")
        print("5: Master Roshi")
        print("6: ox King")
        print("7: Yamcha")
        print("8: Krillin")
        print("9: King Kai")
        print("0: Exit")
        draw_line()
        character_choice = input("> ")
        if str(character_choice) == "0":
            main()
        try:
            character_choice = characters[character_choice]
            is_choosing_character = False
        except KeyError:
            clear()
            draw_line()
            print("  Invalid choice. Please select a valid character.")
            draw_line()
            input("> ")
            is_choosing_character = True

    clear()
    draw_line()
    print("  You chose")
    return character_choice

def choose_enemy_character():
    """
    Randomly chooses character for the enemy
    :return:
    """
    characters = {
        "1": Fighter("Goku", 100, 12, 7, 12, 12),
        "2": Fighter("Gohan", 90, 14, 6, 14, 11),
        "3": Fighter("Vegeta", 90, 12, 8, 11, 11),
        "4": Fighter("Picolo", 100, 10, 10, 10, 10),
        "5": Fighter("Master Roshi", 80, 11, 8, 13, 7),
        "6": Fighter("ox King", 120, 9, 20, 5, 5),
        "7": Fighter("Yamcha", 80, 10, 6, 3, 8),
        "8": Fighter("Krillin", 90, 9, 11, 6, 11),
        "9": Fighter("King Kai", 130, 9, 7, 10, 8)
    }
    input("> Continue")
    clear()
    return characters[str(random.randint(1, 9))]

def battle_controller(player: Fighter, enemy: Fighter):
    """
    Controls the flow and logic of a battle
    :param player:
    :param enemy:
    :return:
    """
    is_battle = True
    while is_battle:
        if player.hp_remaining <= 0:
            is_battle = False
            clear()
            draw_line()
            print("  " + enemy.name + " wins better luck next time")
            draw_line()
            return False
        elif enemy.hp_remaining <= 0:
            is_battle = False
            clear()
            draw_line()
            print("  Well done you won")
            draw_line()
            input("> Continue")
            floss_dance_animation()
            clear()
            return True
        clear()
        draw_line()
        print("  " + player.name + " HP: " + str(player.hp_remaining))
        print("  " + enemy.name + " HP: " + str(enemy.hp_remaining))
        draw_line()
        input("> Continue")
        # Decide who's turn it is
        # based on the speed stat
        # and previous move choice
        # then take it in turns to move
        if player.speed == enemy.speed:
            if random.randint(0, 1) == 0:
                is_player_turn = True
            else:
                is_player_turn = False
        elif player.speed > enemy.speed:
            is_player_turn = True
        else:
            is_player_turn = False

        if is_player_turn:
            player_turn(player, enemy)
            show_hp(player, enemy)
            input("> Continue")
            enemy_turn(player, enemy)
            if not is_player_dead(enemy):
                player_turn(player, enemy)
        else:
            enemy_turn(player, enemy)
            show_hp(player, enemy)
            print("> Continue")
            if not is_player_dead(player):
                player_turn(player, enemy)

def is_player_dead(player: Fighter):
    """
    Checks if character is dead
    :param player:
    :return:
    """
    if player.hp_remaining <= 0:
        return True
    return False

def damage_calculation(attacker: Fighter, defender: Fighter, base_damage):
    """
    Calculates the damage of an attack
    :param attacker:
    :param defender:
    :param base_damage:
    :return:
    """
    damage = base_damage + attacker.attack - defender.defense
    defender.hp_remaining -= damage
    if defender.hp_remaining < 0:
        defender.hp_remaining = 0
    return damage

def show_hp(player: Fighter, enemy: Fighter):
    """
    Displays the fighters current hp to the screen
    :param player:
    :param enemy:
    :return:
    """
    clear()
    draw_line()
    print("  " + player.name + " HP: " + str(player.hp_remaining))
    print("  " + enemy.name + " HP: " + str(enemy.hp_remaining))
    draw_line()

def player_turn(player: Fighter, enemy: Fighter):
    """
    Logic and flow for players turn, Displays attack menu and chooses an attack
    :param player:
    :param enemy:
    :return:
    """
    global is_player_turn
    is_player_turn = True
    global is_game_loop
    while is_player_turn:
        clear()
        draw_line()
        print("1: Punch")
        print("2: Kick")
        print("3: energy blast")
        print("0: quit")
        draw_line()
        player_move = input("> ")
        if player_move == "0":
            is_game_loop = False
            main()
        elif player_move == "1":
            damage_calculation(player, enemy, 40)
            is_player_turn = False
        elif player_move == "2":
            damage_calculation(player, enemy, 60)
            is_player_turn = False
        elif player_move == "3":
            damage_calculation(player, enemy, 20)
            is_player_turn = False
        else:
            is_player_turn = True


def enemy_turn(player: Fighter, enemy: Fighter):
    """
    chooses an attack for the computer
    :param player:
    :param enemy:
    :return:
    """
    global is_player_turn
    is_player_turn = False
    clear()
    draw_line()
    print("  Enemy Turn")
    draw_line()
    input("> Continue")
    if enemy.energy_blast_counter == 1:
        enemy_move = 4
    else:
        enemy_move = random.randint(1, 4)
    if str(enemy_move) == "1":
        damage_calculation(enemy, player, 35)
        is_player_turn = True
        show_hp(player, enemy)
        print("  " + enemy.name + " used punch")
        draw_line()
        input("> Continue")
        return
    elif str(enemy_move) == "2":
        damage_calculation(enemy, player, 30)
        is_player_turn = True
        show_hp(player, enemy)
        print("  " + enemy.name + " used Kick")
        draw_line()
        input("> Continue")
        return
    elif str(enemy_move) == "3":
        damage_calculation(enemy, player, 20)
        is_player_turn = True
        show_hp(player, enemy)
        print("  " + enemy.name + " used energy ball")
        draw_line()
        input("> Continue")
        return
    elif str(enemy_move) == "4":
        enemy.energy_blast_counter += 1
        print(enemy.energy_blast_counter)
        if enemy.energy_blast_counter == 2:
            damage_calculation(enemy, player, 50)
            is_player_turn = True
            show_hp(player, enemy)
            print("  " + enemy.name + " used energy blast")
            draw_line()
            input("> Continue")
            return
        else:
            is_player_turn = True
            show_hp(player, enemy)
            print("  " + enemy.name + " is storing energy")
            draw_line()
            input("> Continue")
            return
    else:
        clear()
        draw_line()
        print("  we have a problem")
        draw_line()
        input("> Continue")

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
