from classes.game import Person,bcolors

magic =[{"name": "Fire", "cost": 10, "dmg": 100},
        {"name": "Thunder", "cost": 10, "dmg": 124},
        {"name": "Blizzard", "cost": 10, "dmg": 100}]

player = Person(1460, 65, 60, 34, magic)

enemy = Person(1200, 65, 45, 25, magic)

running = True


print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)

while running:
    print("================")
    player.choose_action()
    choice = input("Choose action: ")
    index = int(choice) - 1

    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked for: ", dmg,)
    elif index == 1:
        player.choose_magic()
        magic_choice = int(input("Choose magic: ")) -1
        magic_dmg = player.generate_spell_damage(magic_choice)
        spell = player.get_spell_name(magic_choice)
        cost = player.get_spell_mp_cost(magic_choice)

        current_mp = player.get_mp()

        if cost > current_mp:
            print(bcolors.FAIL + "\nNot enough MP\n" + bcolors.ENDC)
            continue

        player.reduce_mp(cost)
        enemy.take_damage(magic_dmg)
        print(bcolors.OKBLUE + "\n" + spell + " deals", str(magic_dmg), "points of damage" + bcolors.ENDC)

    enemy_choice = 1



    edmg = enemy.generate_damage()
    player.take_damage(edmg)
    print("The enemey has attacked you for: ", edmg,)

    print("--------------------------")

    print("Enemy HP:", bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + bcolors.ENDC + "\n")

    print("Your HP:", bcolors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_max_hp()) + bcolors.ENDC + "\n")
    print("Your MP: ", bcolors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_max_mp()) +bcolors.ENDC + "\n")

    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "You Win" + bcolors.ENDC)
    elif player.get_hp() == 0:
        print(bcolors.FAIL + "Your enemy has defeated you!" + bcolors.ENDC)
        running = False


