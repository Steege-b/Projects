import random, sys

weapon_list = ('Rifle', 'Shotgun', 'Pistol', 'Axe', 'Knife', 'Hatchet')

head_armor = ('Bandanna', 'Fedora', 'Hard hat')
body_armor = ('Apron', 'Jacket', 'Football Pads')
leg_armor = ('Jeggings', 'JNCO jeans', 'Carhart pants')


def crit_calculator(dexterity, damage):  ###Main function used to roll crit chance

    def multiplier(damage):  ###Functionception to calculate crit damage if we get a crit
        crit_hit = (damage * 2)  ###Crit damage is equal to our damage parameter doubled
        return crit_hit

    crit_needed = (100 - random.randint(0, 100))  ###Crit score needed, randomly generated from 1-100
    crit_got = (10 + (dexterity * 1.5))  ###5% base crit chance with +1% per dex level.
    if crit_got >= crit_needed:  ###If dex + 5 is over the crit score needed, use multiplier func and return it
        print('Critical hit!')
        multiplier(damage)
        return multiplier(damage)
    else:  ###If no crit, pass nothing
        return damage


def sorter(list):
    print(', '.join(list[:-1]) + ', and ' + list[
        -1])  ###Print everything before the last item in the list, separated by commas.


def pretty_dict(dict):
    for item in dict.items():  ###Prints out a pretty list of our costs.
        key, value = item
        print(f'{key} : {value}')


def item_manager():
    def manager_sorter(list):
        info = (', '.join(list[:-1]) + ', or ' + list[
            -1])  ###Print everything before the last item in the list, separated by commas.
        return info

    while True:
        cat = input('What category do you want? Type \'Exit\' to quit.'
                    f'\nWeapons'
                    f'\nArmor\n').lower()  ###Getting item category
        if cat == 'weapons':
            cat = ''
            while True:  ###This page displays stats about your selected weapon
                weapon = input('Which weapon? Type \'back\' to go back.'
                               f'\nChoose from one of the following: {manager_sorter(weapon_list)}\n').lower()
                if weapon == 'shotgun':
                    print('The shotgun with buckshot ammo deals 0-7 damage, 10 on headshots, 7 times. it gets added up'
                          ' for a total damage output. The slug rounds in a shotgun will deal 15-40 damage, 50 on a'
                          ' headshot. \nThe shotgun can shoot from 2-3 distance')
                    continue
                elif weapon == 'rifle':
                    print('The rifle deals 0-25 damage, 40 on a headshot, and can shoot from 2-10 distance.')
                    continue
                elif weapon == 'pistol':
                    print('The pistol deals 0-15 damage, 25 on a headshot, and can shoot from 1-5 distance.')
                    continue
                elif weapon == 'knife':
                    print('The knife deals 0-10 damage, 20 on a critical hit, two times and has a range of 1.')
                    continue
                elif weapon == 'axe':
                    print('The axe deals 10-30 damage, 45 on a critical hit, and has a range of 2.')
                    continue
                elif weapon == 'hatchet':
                    print('The hatchet deals 10-25 damage, 35 on a critical hit, and has a range of 1. ')
                    continue
                elif weapon == 'back':
                    break

                print('<Enter a valid input>')
        elif cat == 'armor':  ###Giving stats about armor. asks for armor class first
            cat = ''
            while True:
                sub_cat = input('Head, body, or leg armor? Type \'back\' to go back.').lower()
                if sub_cat == 'head' or sub_cat == 'head armor':
                    print(manager_sorter(head_armor))
                    head = input('Which piece?').lower()
                    if head == 'bandanna':
                        print('Light armor, +1 CON')
                        continue
                    elif head == 'fedora':
                        print('Medium armor, +5 CHA +1 DEX')
                        continue
                    elif head == 'hard hat':
                        print('Heavy armor, +1 CON & DEF')
                        continue
                    else:
                        print('<Enter a valid input>')
                elif sub_cat == 'body' or sub_cat == 'body armor':
                    print(manager_sorter(body_armor))
                    body = input('Which piece?').lower()
                    if body == 'apron':
                        print('Light armor, +2 DEX ')
                        continue
                    if body == 'jacket':
                        print('Medium armor, +2 STR')
                        continue
                    if body == 'football pads' or body == 'pads' or body == 'football':
                        print('Heavy armor, +2 DEF +1 CON ')
                        continue
                    else:
                        print('<Enter a valid input>')

                elif sub_cat == 'leg' or sub_cat == 'leg armor':
                    print(manager_sorter(leg_armor))
                    leg = input('Which piece?').lower()
                    if leg == 'jeggings':
                        print('Light armor, +2 DEF ')
                        continue
                    if leg == 'jnco jeans' or leg == 'jeans' or leg == 'jnco':
                        print('Medium armor, +2 CON')
                        continue
                    if leg == 'carhart pants' or leg == 'pants' or leg == 'carhart':
                        print('Heavy armor, +2 STR +1 DEX ')
                        continue
                    else:
                        print('<Enter a valid input>')

                else:
                    if sub_cat == 'back':
                        break
                    else:
                        print('<Enter a valid input>')
                        continue  ###Giving stats about
        elif cat == 'exit':
            return ''
        elif cat != 'exit' or cat != 'weapons' or cat != 'armor':
            print('<Enter a valid input>')
            continue


def player_set():
    global strength, dexterity, charisma, defense, constitution
    while True:
        type = input('<Auto, light, or full>\n').lower()  ###Getting our stat rollers

        def player_set_full():
            global strength, dexterity, defense, charisma, constitution
            r1 = random.randint(1, 10)  ###Initializing
            r2 = random.randint(1, 10)  ###Initializing
            r3 = random.randint(1, 10)  ###Initializing
            r4 = random.randint(1, 10)  ###Initializing
            r5 = random.randint(1, 10)  ###Initializing
            r1start = r1  ###Initializing
            r2start = r2  ###Initializing
            r3start = r3  ###Initializing
            r4start = r4  ###Initializing
            r5start = r5  ###Initializing
            strength_start = 0  ###Initializing
            dexterity_start = 0  ###Initializing
            constitution_start = 0  ###Initializing
            defense_start = 0  ###Initializing
            charisma_start = 0  ###Initializing
            while True:
                print(  ###Initial menu, asks for input
                    f'\nType the name (or the 3 letter abbreviation(STR, DEX, CON, CHA, DEF)) of a stat to add a role to it. Type "Restart" '
                    f'if you make a mistake. Type "Exit" when you are done editing stats.'
                    f'\nYour rolls are {r1start}, {r2start}, {r3start}, {r4start} and {r5start} .')
                stat = input(
                    f'Strength: {strength_start}     Dexterity: {dexterity_start}     Constitution: {constitution_start}'
                    f'   Defense: {defense_start}    Charisma: {charisma_start}\n').lower()

                if stat == 'dexterity' or stat == 'dex':
                    roll_selector = input('\nWhich roll do you want to put in this stat?\n'
                                          f'R1: {r1start}    R2: {r2start}    R3: {r3start}    R4: {r4start}    R5: {r5start}\n').lower()
                    if roll_selector == 'r1':  ###For all of this part: if player wants this roll in this slot then swap variables and display
                        dexterity_start, r1start = r1start, dexterity_start  ###For all of this part: if player wants this roll in this slot then swap variables and display
                        continue
                    elif roll_selector == 'r2':  ###For all of this part: if player wants this roll in this slot then swap variables and display
                        dexterity_start, r2start = r2start, dexterity_start  ###For all of this part: if player wants this roll in this slot then swap variables and display
                        continue
                    elif roll_selector == 'r3':  ###For all of this part: if player wants this roll in this slot then swap variables and display
                        dexterity_start, r3start = r3start, dexterity_start  ###For all of this part: if player wants this roll in this slot then swap variables and display
                        continue
                    elif roll_selector == 'r4':  ###For all of this part: if player wants this roll in this slot then swap variables and display
                        dexterity_start, r4start = r4start, dexterity_start  ###For all of this part: if player wants this roll in this slot then swap variables and display
                        continue
                    elif roll_selector == 'r5':  ###For all of this part: if player wants this roll in this slot then swap variables and display
                        dexterity_start, r5start = r5start, dexterity_start  ###For all of this part: if player wants this roll in this slot then swap variables and display
                        continue
                elif stat == 'constitution' or stat == 'con':
                    roll_selector = input('\nWhich roll do you want to put in this stat?\n'
                                          f'R1: {r1start}    R2: {r2start}    R3: {r3start}    R4: {r4start}    R5: {r5start}\n').lower()
                    if roll_selector == 'r1':
                        constitution_start, r1start = r1start, constitution_start
                        continue
                    if roll_selector == 'r2':
                        constitution_start, r2start = r2start, constitution_start
                        continue
                    if roll_selector == 'r3':
                        constitution_start, r3start = r3start, constitution_start
                        continue
                    if roll_selector == 'r4':
                        constitution_start, r4start = r4start, constitution_start
                        continue
                    if roll_selector == 'r5':
                        constitution_start, r5start = r5start, constitution_start
                        continue
                    continue
                elif stat == 'defense' or stat == 'def':
                    roll_selector = input('\nWhich roll do you want to put in this stat?\n'
                                          f'R1: {r1start}    R2: {r2start}    R3: {r3start}    R4: {r4start}    R5: {r5start}\n').lower()
                    if roll_selector == 'r1':
                        defense_start, r1start = r1start, defense_start
                        continue
                    if roll_selector == 'r2':
                        defense_start, r2start = r2start, defense_start
                        continue
                    if roll_selector == 'r3':
                        defense_start, r3start = r3start, defense_start
                        continue
                    if roll_selector == 'r4':
                        defense_start, r4start = r4start, defense_start
                        continue
                    if roll_selector == 'r5':
                        defense_start, r5start = r5start, defense_start
                        continue
                    continue
                elif stat == 'charisma' or stat == 'cha':
                    roll_selector = input('\nWhich roll do you want to put in this stat?\n'
                                          f'R1: {r1start}    R2: {r2start}    R3: {r3start}    R4: {r4start}    R5: {r5start}\n').lower()
                    if roll_selector == 'r1':
                        charisma_start, r1start = r1start, charisma_start
                        continue
                    if roll_selector == 'r2':
                        charisma_start, r2start = r2start, charisma_start
                        continue
                    if roll_selector == 'r3':
                        charisma_start, r3start = r3start, charisma_start
                        continue
                    if roll_selector == 'r4':
                        charisma_start, r4start = r4start, charisma_start
                        continue
                    if roll_selector == 'r5':
                        charisma_start, r5start = r5start, charisma_start
                        continue
                    continue
                elif stat == 'strength' or stat == 'str':
                    roll_selector = input('\nWhich roll do you want to put in this stat?\n'
                                          f'R1: {r1start}    R2: {r2start}    R3: {r3start}    R4: {r4start}    R5: {r5start}\n').lower()
                    if roll_selector == 'r1':
                        strength_start, r1start = r1start, strength_start
                        continue
                    if roll_selector == 'r2':
                        strength_start, r2start = r2start, strength_start
                        continue
                    if roll_selector == 'r3':
                        strength_start, r3start = r3start, strength_start
                        continue
                    if roll_selector == 'r4':
                        strength_start, r4start = r4start, strength_start
                        continue
                    if roll_selector == 'r5':
                        strength_start, r5start = r5start, strength_start
                        continue
                    continue
                elif stat == 'restart':  ###Player can reset all rolls to their original values and re allocate stats
                    r1start = r1
                    r2start = r2
                    r3start = r3
                    r4start = r4
                    r5start = r5
                    strength_start = 0
                    dexterity_start = 0
                    constitution_start = 0
                    defense_start = 0
                    charisma_start = 0
                    continue
                else:
                    if r1start + r2start + r3start + r4start + r5start > 0:  ###Player can't back out without all stats bein allocated
                        print('Assign all rolls to stats')
                        continue
                    elif stat == 'exit':
                        print(f"\nStrength: {strength} (+{strength * 2} melee dmg)"  ###Specific buffs per stat
                              f"\nDexterity: {dexterity} (+{dexterity * 1.5} crit chance) "  ###Specific buffs per stat
                              f"\nCharisma: {charisma} (Used for social checks, 1 dice per point)"  ###Specific buffs per stat
                              f"\nDefense: {defense} (+{defense * 2} damage resistance))"  ###Specific buffs per stat
                              f"\nConstitution: {constitution} ({3 * constitution} bonus health)")  ###Specific buffs per stat
                        final = input(
                            f'Are you sure? You will not be able to change this in the future. <yes or no>\n').lower()
                        if final != 'yes':
                            continue
                        else:
                            strength_start, strength = strength, strength_start  ###Swaps the function stat with the real game one
                            constitution_start, constitution = constitution, constitution_start  ###Swaps the function stat with the real game one
                            dexterity_start, dexterity = dexterity, dexterity_start  ###Swaps the function stat with the real game one
                            charisma_start, charisma = charisma, charisma_start  ###Swaps the function stat with the real game one
                            defense_start, defense = defense, defense_start  ###Swaps the function stat with the real game one
                            print(f"\nStrength: {strength} (+{strength * 2} melee dmg)"
                                  f"\nDexterity: {dexterity} (+{dexterity * 1.5} crit chance) "
                                  f"\nCharisma: {charisma} (Used for social checks)"
                                  f"\nDefense: {defense} (+{defense * 2} damage resistance))"
                                  f"\nConstitution: {constitution} ({3 * constitution} bonus health)")
                            input('<Enter to continue>')
                            break
                    elif stat == 'exit':
                        break
                    print('Enter a valid input')
                    continue

        def player_set_light():
            global strength, dexterity, defense, charisma, constitution
            gamble = 0
            while True:
                if gamble != 3:
                    strength = random.randint(1, 10)  ###Stats all randomly assigned, player gets three rolls.
                    dexterity = random.randint(1, 10)
                    constitution = random.randint(1, 10)
                    defense = random.randint(1, 10)
                    charisma = random.randint(1, 10)
                    print(f"\nStrength: {strength} (+{strength * 2} melee dmg)"
                          f"\nDexterity: {dexterity} (+{dexterity * 1.5}% crit chance) "
                          f"\nCharisma: {charisma} (Used for social checks)"
                          f"\nDefense: {defense} (+{defense * 2} damage resistance)"
                          f"\nConstitution: {constitution} ({3 * constitution} bonus health)")
                    choice = input(f'Want to re-roll? {3 - gamble} re-rolls left. <yes or no>\n').lower()
                    if choice == 'yes':  ###If player re rolls then they get new stats and the process repeats.
                        gamble += 1
                        if gamble == 3:  ###Once the player used all of their rolls they get locked in with the stats seen below
                            strength = random.randint(1, 10)
                            dexterity = random.randint(1, 10)
                            constitution = random.randint(1, 10)
                            defense = random.randint(1, 10)
                            charisma = random.randint(1, 10)
                            input(f"\nStrength: {strength} (+{strength * 2} melee dmg)"
                                  f"\nDexterity: {dexterity} (+{dexterity * 1.5} crit chance) "
                                  f"\nCharisma: {charisma} (Used for social checks)"
                                  f"\nDefense: {defense} (+{defense * 2} damage resistance)"
                                  f"\nConstitution: {constitution} ({3 * constitution} bonus health)"
                                  f"\nThese are the stats you are stuck with. No more re-rolls.")
                            break
                    elif choice == 'no':
                        break
                    else:
                        if choice != 'no' or choice != 'yes':
                            print('<Enter a valid input>')
                            continue

        def player_set_auto():
            global strength, dexterity, defense, charisma, constitution
            strength = random.randint(1, 10)  ###Automatically assigns all stats
            dexterity = random.randint(1, 10)
            constitution = random.randint(1, 10)
            defense = random.randint(1, 10)
            charisma = random.randint(1, 10)
            print(f"\nStrength: {strength} (+{strength * 2} melee dmg)"
                  f"\nDexterity: {dexterity} (+{dexterity} crit chance) "
                  f"\nCharisma: {charisma} (Used for social checks, 1 dice per point)"
                  f"\nDefense: {defense} (+{defense * 2} damage reduction))"
                  f"\nConstitution: {constitution} ({3 * constitution} bonus health)")
            input('<Enter to continue>')

        if type == 'full':  ###These options are for initial input, selects stat function
            player_set_full()
            break
        if type == 'light':
            player_set_light()
            break
        if type == 'auto':
            player_set_auto()
            break
        else:
            if type != 'light' or type != 'auto' or type != 'full':
                print('<Choose from the options presented to you>')
                continue


def cha_check(player_skill, enemy_skill_score, name):
    def char_stat(enemy_skill_score):  ###Calculates the enemy skill check score
        character_total = (enemy_skill_score * 3.5)
        print('Enemy skill:', int(character_total))
        return character_total

    def roll(player_skill):  ###Generates player skill check
        results = [random.randint(1, 6) for n in range(player_skill)]
        print(f'Player skill: {sum(results)}')
        return sum(results)

    def checker(player, ai):
        if int(player) >= ai:
            check = 'pass'
        else:
            check = 'fail'
        if check == 'pass':
            input(f'You seduced {name}\n<Enter to continue>\n')
        else:
            input(f'You failed to seduce {name}, CHA too low.\n<Enter to continue>\n')
        return check

    ai = char_stat(enemy_skill_score)
    player = roll(player_skill)
    check = checker(player, ai)
    return check


def fight_loop(modifier):
    global distance, enemy_hp, hp, shotgun_shell_count, stamina, distance, damage_given, damage_taken
    global equipped_weapon, pistol_ammo_count, rifle_ammo_count, secondary, money, bandages

    distance = random.randint(2, 10)
    enemy_hp = random.randint(50, 100) + (int(modifier) * 5)
    stamina = 3
    while enemy_hp > 0:
        if equipped_weapon == 'shotgun':
            current_ammo = shotgun_shell_count
        elif equipped_weapon == 'rifle':
            current_ammo = rifle_ammo_count
        elif equipped_weapon == 'pistol':
            current_ammo = pistol_ammo_count
        else:
            current_ammo = 'N/A'
        hud = {'Enemy HP': enemy_hp, 'Player HP': hp, 'Current weapon': equipped_weapon, 'Secondary': secondary,
               'Ammo': current_ammo, 'Distance': distance, 'Stamina': stamina}
        print(f'\n  	    ಠ_ಠ\n    	<|>\n    	/ \\\n O\n<|>\n/ \\\n')
        pretty_dict(hud)
        move = input('Choices: Attack, block (reduces distance by 1), heal, move back, charge, (Swap) weapons'
                     ' \n<Enter Choice>\n').lower()
        if move == 'swap' or move == 'swap weapons':
            equipped_weapon, secondary = secondary, equipped_weapon
            print(f'You equip your {equipped_weapon}')
            pass
        elif move == 'charge':
            if distance <= 2:
                input('<Too close to enemy> \n<Enter to continue>')
                continue
            else:
                input('You rush towards the enemy \n<Enter to continue>')
                distance = int(distance / 2)
                continue
        elif move == 'block':
            print('You prepare yourself for an attack!')
            if distance > 1:
                distance -= 1
                continue
            elif distance == 1:
                shield = random.randint(1, 25)
                sword = random.randint(1, 45)
                damage_taken = sword - shield
                if damage_taken < 1:
                    input('You successfully block the attack! \n<Enter to continue>')
                    damage_given = 0
                    damage_taken = 0
                    continue
                else:
                    input(f'You blocked {shield} damage but still took {damage_taken} damage!\n<Enter to continue>')
                    swap_hp = hp - damage_taken
                    swap_hp, hp = hp, swap_hp
                    damage_taken = 0
                    damage_given = 0
                    continue

        elif move == 'move back':
            if distance == 10:
                input('You are too far away to move back\n<Enter to continue>')
                continue
            elif stamina == 0:
                input('You are out of stamina and can\'t do that anymore \n<Enter to continue>')
                continue

            elif (distance + 2) > 10:
                waste = input('Distance cap 10. Use stamina for less than full distance?\n<yes or no>\n').lower()
                if waste == 'yes':
                    if stamina == 3:
                        stamina -= 1
                        distance = 10
                        input('You dash backwards and feel a bit winded \n<Enter to continue>')
                        continue
                    elif stamina == 2:
                        stamina -= 1
                        distance = 10
                        input('You dash backwards and feel very winded \n<Enter to continue>')
                        distance = 10
                        continue
                    elif stamina == 1:
                        stamina -= 1
                        distance = 10
                        input('You dash backwards and almost collapse \n<Enter to continue>')
                        continue

                else:
                    continue
            elif stamina == 3:
                if distance >= 2:
                    distance += 3
                elif distance == 1:
                    distance += 2
                stamina -= 1
                print('You dash backwards and feel a bit winded \n<Enter to continue>')
            elif stamina == 2:
                if distance >= 2:
                    distance += 3
                elif distance == 1:
                    distance += 2
                stamina -= 1
                print('You dash backwards and feel very winded \n<Enter to continue>')
            elif stamina == 1:
                if distance >= 2:
                    distance += 3
                elif distance == 1:
                    distance += 2
                stamina -= 1
                print('You dash backwards and almost collapse \n<Enter to continue>')

        elif move == 'heal':
            if bandages > 0:
                gained = (random.randint(15, 50) + constitution)
                hp += gained
                if hp > 120:
                    hp = 120
                bandages -= 1
                print(f'You gained {gained} HP using a bandage. \nNew HP: {hp} \nNew bandage count: {bandages}')
            else:
                input('No more bandages!')
                continue
        elif move == 'attack':
            if equipped_weapon == 'rifle':
                if distance == 1:
                    input('Too close to target\n<Enter to continue>')
                    continue
                elif rifle_ammo_count > 0:
                    damage_given = random.randint(5, 25)
                    rifle_ammo_count -= 1
                    current_ammo -= 1
                else:
                    input('No more ammo\n<Enter to continue>')
                    continue

            elif equipped_weapon == 'shotgun':
                if distance == 1:
                    input('Too close to target\n<Enter to continue>')
                    continue
                if distance >= 4:
                    input(f'Too far from target. Get {distance - 3} distance closer\n<Enter to continue>')
                    continue
                else:
                    if shotgun_shell_count == 0:
                        input('No more ammo\n<Enter to continue>')
                        continue
                    else:
                        buck_shot = [random.randint(0, 7) for shots in range(7)]
                        damage_given = sum(buck_shot)
                        shotgun_shell_count -= 1
                        current_ammo -= 1


            elif equipped_weapon == 'pistol':
                if distance >= 6:
                    input(f'Too far from target. Get {distance - 5} distance closer\n<Enter to continue>')
                    continue
                elif pistol_ammo_count > 0:
                    shot = random.randint(6, 18)
                    if distance == 1:
                        damage_given = shot + 10
                    else:
                        damage_given = shot
                    pistol_ammo_count -= 1
                    current_ammo -= 1
                else:
                    input('No more ammo\n<Enter to continue>')
                    continue

            elif equipped_weapon == 'knife':
                if distance >= 2:
                    input(f'Too far from target. Get {distance - 1} distance closer\n<Enter to continue>')
                    continue
                else:
                    stabs = [random.randint(5, 15) for stabbies in range(2)]
                    damage_given = sum(stabs)

            elif equipped_weapon == 'hatchet':
                if distance >= 2:
                    input(f'Too far from target. Get {distance - 1} distance closer\n<Enter to continue>')
                else:
                    damage_given = random.randint(10, 25)

            elif equipped_weapon == 'axe':
                if distance >= 3:
                    input(f'Too far from target. Get {distance - 2} distance  \n<Enter to continue>')
                else:
                    damage_given = random.randint(0, 35)
        else:
            input('<Enter a valid input>')
            continue

        if damage_given > 0:
            if equipped_weapon == 'knife' or equipped_weapon == 'hatchet' or equipped_weapon == 'axe':
                damage_given += (strength * 2)
            critical = crit_calculator(dexterity, damage_given)
            if critical > damage_given:
                critical, damage_given = damage_given, critical
        if distance > 1 and move != 'block':
            distance -= 1
        else:
            damage_taken = (random.randint(0, 25) - defense)
            damage_taken += (int(modifier) * 1.25)

        if damage_given > 0 and damage_taken > 0:
            input(f'You dealt {damage_given} damage and took {int(damage_taken)} damage! \n<Enter to continue>')
            swap_enemy = enemy_hp - damage_given
            swap_enemy, enemy_hp = enemy_hp, swap_enemy
            swap_hp = hp - int(damage_taken)
            swap_hp, hp = hp, swap_hp
            if hp < 1:
                input(f'You died. Kills = {kills}')
                sys.exit()

        elif damage_taken > 0:
            input(f'You took {int(damage_taken)} damage! \n<Enter to continue>')
            swap_hp = hp - int(damage_taken)
            swap_hp, hp = hp, swap_hp
            if hp < 1:
                input('You died')
                sys.exit()

        elif damage_given > 0:
            input(f'You dealt {damage_given} damage! \n<Enter to continue>')
            swap_enemy = enemy_hp - damage_given
            swap_enemy, enemy_hp = enemy_hp, swap_enemy

        else:
            input('No damage dealt this turn \n<Enter to continue>')
        damage_given = 0
        damage_taken = 0

        if enemy_hp < 1:
            money_up = random.randint(10, 100)
            ammo_up = int(random.randint(1, 7))
            if ammo_up < 0:
                ammo_up = 0
            current_ammo += int(ammo_up)
            if equipped_weapon == 'shotgun':
                shotgun_shell_count += int(ammo_up)
            elif equipped_weapon == 'rifle':
                rifle_ammo_count += int(ammo_up)
            elif equipped_weapon == 'pistol':
                pistol_ammo_count += int(ammo_up)
            money += money_up
            input(f'You killed the enemy and found ${money_up} and scavenged {ammo_up} bullets off of their body.')


def shopping_guns():
    global hp, shotgun_shell_count, money, bandages, pistol_ammo_count, rifle_ammo_count, equipped_weapon, secondary
    bandage_cost = random.randint(25, 150)
    healing_cost = random.randint(40, 200)
    pistol_ammo_cost = random.randint(5, 20)
    rifle_ammo_cost = random.randint(7, 25)
    shotgun_shell_cost = random.randint(10, 30)
    shotgun_cost = random.randint(120, 250)
    rifle_cost = random.randint(100, 225)
    pistol_cost = random.randint(80, 200)
    while True:
        goods = input(
            'Doctor: "What do you need? Since you just healed, I\'ll offer you some extra items!\nPrices are:\n'
            f'Bandages for ${bandage_cost} dollars'
            f'\nI can heal 40-100 hp you for ${healing_cost}. (120 HP limit).'
            f'\nPistol rounds for ${pistol_ammo_cost} per round\nA pistol for ${pistol_cost}'
            f'\nRifle rounds for ${rifle_ammo_cost} per round\nA rifle for ${rifle_cost}'
            f'\nShotgun shells for ${shotgun_shell_cost} per shell\nA shotgun for ${shotgun_cost}"'
            f'\nMoney: ${money}\n<(Heal) me, bandages, ammo, shotgun, rifle, pistol or exit>\n').lower()
        if goods == 'heal' or goods == 'heal me':
            health_up = random.randint(40, 100)
            hp += health_up
            if hp > 120:
                hp = 120
            money -= healing_cost
            input(
                f'I managed to heal you for {health_up} health. Your new HP is {hp} and you have ${money}. \n<Enter to continue>')
            continue
        elif goods == 'bandages':
            bandage_cap = money // bandage_cost
            bandage_amount = input(
                f'How many? You can afford {bandage_cap} bandages. Type \'back\' to go back.').lower()
            if bandage_amount == 'back':
                continue
            bandage_price = int(bandage_amount) * bandage_cost
            print(bandage_price)

            if money > int(bandage_price):
                money -= bandage_price
                bandages += int(bandage_amount)
                input(f'You now have {bandages} bandages and ${money} dollars \n<Enter to continue>')
                continue
            elif money < int(bandage_price):
                print(f'Doctor: "You don\'t have that kind of money."')
                continue

        elif goods == 'ammo':
            gun = input('Doctor: "Which weapon?" \n<pistol, rifle, shotgun, or back>').lower()
            try:
                if gun == 'pistol':
                    pistol_cap = money // pistol_ammo_cost
                    pistol_amount = input(f'Doctor: "How many? You can afford {pistol_cap}.\n Type \'back\' to go back'
                                          f'or enter a number.').lower()
                    if pistol_amount == 'back':
                        continue

                    pistol_price = (int(pistol_amount) * pistol_ammo_cost)
                    if pistol_price > money:
                        print(f'Doctor: "You can only afford {pistol_cap} pistol rounds."')
                        continue
                    else:
                        double = input(
                            f'You are about to spend ${pistol_price} on ammo. Are you sure?\n<Yes or no>').lower()
                        if double == 'no':
                            continue
                        else:
                            money -= pistol_price
                            pistol_ammo_count += int(pistol_amount)
                            input(f'You now have {pistol_ammo_count} pistol rounds and ${money} \n<Enter to continue>')

                elif gun == 'shotgun':
                    shotgun_cap = money // shotgun_shell_cost
                    shotgun_amount = input(f'How many? You can afford {shotgun_cap} \nType \'back\' to go back.'
                                           f'or enter a number.').lower()
                    if shotgun_amount == 'back':
                        continue
                    else:
                        shotgun_price = (int(shotgun_amount) * shotgun_shell_cost)
                    if shotgun_price > money:
                        print(f'Doctor: "You can only afford {shotgun_cap} shotgun shells."')
                        continue
                    else:
                        double = input(f'You are about to spend ${shotgun_price} on ammo. Are you sure?').lower()
                        if double == 'no':
                            continue
                        else:
                            money -= shotgun_price
                            shotgun_shell_count += int(shotgun_amount)
                            input(
                                f'You now have {shotgun_shell_count} Shotgun shells and ${money}  \n<Enter to continue>').lower()
                            continue

                elif gun == 'rifle':
                    rifle_cap = money // rifle_ammo_cost
                    rifle_amount = input(
                        f'How many? You can only afford {rifle_cap} rifle rounds.\nType \'back\' to go back.'
                        f'or enter a number.').lower()
                    if rifle_amount == 'back':
                        continue
                    rifle_price = (int(rifle_amount) * rifle_ammo_cost)
                    if rifle_price > money:
                        print(f'Doctor: "You can only afford {rifle_cap} rifle rounds."')
                        continue
                    else:
                        double = input(f'You are about to spend ${rifle_price} on ammo. Are you sure?').lower()
                        if double == 'no':
                            continue
                        else:
                            money -= rifle_price
                            rifle_ammo_count += int(rifle_amount)
                            input(
                                f'Rifle rounds now at {rifle_ammo_count} and money at ${money}  \n<Enter to continue>').lower()
                            continue
                else:
                    if gun == 'back':
                        break
                    input('<Enter a valid input>')
            except ValueError:
                input('<Enter a valid input>')

        elif goods == 'shotgun':
            if shotgun_cost > money:
                input('Doctor: "That costs too much"')
                continue
            final = input(f'Are you sure? You are about to spend ${shotgun_cost}. \n<Yes or no>').lower()
            if final == 'yes':
                money -= shotgun_cost
                while True:
                    swap = input('Which weapon would you like to swap this with?'
                                 f'<{equipped_weapon} or {secondary}>').lower()
                    if swap == equipped_weapon:
                        equipped_weapon = 'shotgun'
                        input(f'You now have a {equipped_weapon} and a {secondary}')
                        break
                    elif swap == secondary:
                        secondary = 'shotgun'
                        input(f'You now have a {equipped_weapon} and a {secondary}')
                        break
                    else:
                        print('Enter a valid input')

        elif goods == 'pistol':
            if pistol_cost > money:
                input('Doctor: "That costs too much"')
                continue
            final = input(f'Are you sure? You are about to spend ${pistol_cost}. \n<Yes or no>').lower()
            if final == 'yes':
                money -= pistol_cost
                while True:
                    swap = input('Which weapon would you like to swap this with?'
                                 f'<{equipped_weapon} or {secondary}>').lower()
                    if swap == equipped_weapon:
                        equipped_weapon = 'pistol'
                        input(f'You now have a {equipped_weapon} and a {secondary}')
                        break
                    elif swap == secondary:
                        secondary = 'pistol'
                        input(f'You now have a {equipped_weapon} and a {secondary}')
                        break
                    else:
                        print('Enter a valid input')

        elif goods == 'rifle':
            if rifle_cost > money:
                input('Doctor: "That costs too much"')
                continue
            final = input(f'Are you sure? You are about to spend ${rifle_cost}. \n<Yes or no>').lower()
            if final == 'yes':
                money -= rifle_cost
                while True:
                    swap = input('Which weapon would you like to swap this with?'
                                 f'<{equipped_weapon} or {secondary}>').lower()
                    if swap == equipped_weapon:
                        equipped_weapon = 'rifle'
                        input(f'You now have a {equipped_weapon} and a {secondary}')
                        break
                    elif swap == secondary:
                        secondary = 'rifle'
                        input(f'You now have a {equipped_weapon} and a {secondary}')
                        break
                    else:
                        print('Enter a valid input')
        else:
            if goods == 'exit':
                double = input('Are you sure? You will not be able to come back for a while. \n<Yes or no>').lower()
                if double == 'yes':
                    input('Thank you, come again! \n<Enter to continue>')
                    break
                elif double == 'no':
                    continue
                else:
                    print('<Enter a valid input>')
            input('<Enter a valid input>')


def shopping():
    global hp, shotgun_shell_count, money, bandages, pistol_ammo_count, rifle_ammo_count
    bandage_cost = random.randint(75, 150)
    healing_cost = random.randint(100, 200)
    pistol_ammo_cost = random.randint(5, 20)
    rifle_ammo_cost = random.randint(7, 25)
    shotgun_shell_cost = random.randint(10, 30)
    tries = 0
    while True:
        goods = input('Doctor: "Welcome back! I\'m happy to see you are still alive. And I\'m not just saying'
                      'that because I like the business.\nPrices are: \n'
                      f'Bandages for ${bandage_cost} '
                      f'\nI can heal 40-100 hp for ${healing_cost}. (120 HP max)'
                      f'\nPistol rounds for ${pistol_ammo_cost} per round'
                      f'\nRifle rounds for ${rifle_ammo_cost} per round'
                      f'\nShotgun shells for ${shotgun_shell_cost} per shell"'
                      f'\n<Seduce character, CHA 8>'
                      f'\n${money}\n<(Heal) me, bandages, ammo, seduce, or exit>\n').lower()
        if goods == 'seduce' and tries < 1:
            check = cha_check(charisma, 8, 'Doctor')
            if check == 'pass':
                shopping_guns()
                break
            else:
                print('Doctor: "Nope, I don\'t have any special deals at the moment..."')
                tries = 1
                continue

        elif goods == 'heal' or goods == 'heal me':
            if money < healing_cost:
                health_up = random.randint(40, 100)
                hp += health_up
                money -= healing_cost
                if hp > 120:
                    hp = 120
                input(
                    f'I managed to heal you for {health_up} health. Your new HP is {hp} and you have ${money}. '
                    f'\n<Enter to continue>')
                continue
            else:
                print('You can\'t afford that')


        elif goods == 'bandages':
            bandage_cap = money // bandage_cost
            bandage_amount = input(
                f'How many? You can afford {bandage_cap} bandages. Type \'back\' to go back.\n').lower()
            if bandage_amount == 'back':
                continue
            bandage_price = int(bandage_amount) * bandage_cost
            if money > int(bandage_price):
                money -= bandage_price
                bandages += int(bandage_amount)
                input(f'You now have {bandages} bandages and ${money} dollars \n<Enter to continue>')
                continue
            elif money < int(bandage_price):
                input(f'Doctor: "You don\'t have that kind of money."')
                continue
        elif goods == 'ammo':
            gun = input('Doctor: "Which weapon?" \n<pistol, rifle, shotgun, or back>\n').lower()
            try:
                if gun == 'pistol':
                    pistol_cap = money // pistol_ammo_cost
                    pistol_amount = input(f'Doctor: "How many? You can afford {pistol_cap}.\n Type \'back\' to go back'
                                          f'or enter a number.\n').lower()
                    if pistol_amount == 'back':
                        continue
                    pistol_price = (int(pistol_amount) * pistol_ammo_cost)
                    if pistol_price > money:
                        print(f'Doctor: "You can only afford {pistol_cap} pistol rounds."')
                        continue
                    else:
                        double = input(
                            f'You are about to spend ${pistol_price} on ammo. Are you sure?\n<Yes or no>\n').lower()
                        if double == 'no':
                            continue
                        else:
                            money -= pistol_price
                            pistol_ammo_count += int(pistol_amount)
                            input(f'You now have {pistol_ammo_count} pistol rounds and ${money} \n<Enter to continue>')
                elif gun == 'shotgun':
                    shotgun_cap = money // shotgun_shell_cost
                    shotgun_amount = input(f'How many? You can afford {shotgun_cap} \nType \'back\' to go back.'
                                           f'or enter a number.\n').lower()
                    if shotgun_amount == 'back':
                        continue
                    else:
                        shotgun_price = (int(shotgun_amount) * shotgun_shell_cost)
                    if shotgun_price > money:
                        print(f'Doctor: "You can only afford {shotgun_cap} shotgun shells."')
                        continue
                    else:
                        double = input(
                            f'You are about to spend ${shotgun_price} on ammo. Are you sure?\n<Yes or no>\n').lower()
                        if double == 'no':
                            continue
                        else:
                            money -= shotgun_price
                            shotgun_shell_count += int(shotgun_amount)
                            input(
                                f'You now have {shotgun_shell_count} Shotgun shells and ${money}  \n<Enter to continue>').lower()
                            continue

                elif gun == 'rifle':
                    rifle_cap = money // rifle_ammo_cost
                    rifle_amount = input(
                        f'How many? You can only afford {rifle_cap} rifle rounds.\nType \'back\' to go back.'
                        f'or enter a number.\n').lower()
                    if rifle_amount == 'back':
                        continue
                    rifle_price = (int(rifle_amount) * rifle_ammo_cost)
                    if rifle_price > money:
                        print(f'Doctor: "You can only afford {rifle_cap} rifle rounds."')
                        continue
                    else:
                        double = input(
                            f'You are about to spend ${rifle_price} on ammo. Are you sure?\n<Yes or no>\n').lower()
                        if double == 'no':
                            continue
                        else:
                            money -= rifle_price
                            rifle_ammo_count += int(rifle_amount)
                            input(
                                f'Rifle rounds now at {rifle_ammo_count} and money at ${money}  \n<Enter to continue>').lower()
                            continue
                else:
                    if gun == 'back':
                        break
                    input('<Enter a valid input>')
            except ValueError:
                input('<Enter a valid input>')
        else:
            if goods == 'exit':
                double = input('Are you sure? You will not be able to come back for a while. \n<Yes or no>\n').lower()
                if double == 'yes':
                    input('Thank you, come again! \n<Enter to continue>')
                    break
                elif double == 'no':
                    continue
                else:
                    print('<Enter a valid input>')


strength = 0
dexterity = 0
defense = 0
charisma = 0
constitution = 0
bandages = 0
equipped_weapon = ''
secondary = ''
stamina = 0
pistol_ammo_count = 0
rifle_ammo_count = 0
shotgun_shell_count = 0
enemy_hp = 0
distance = 0
damage_taken = 0
damage_given = 0
hp = 60

while True:
    answer = input('   W E L C O M E\n'
                   ' A D V E N T U R E R'
                   '\n\n\nStart a new game or view items?'
                   '\n<Start or items>\n').lower()
    if answer == 'items':
        item_manager()
    else:
        if answer == 'start':
            break
        else:
            input('We are not off to a very good start if you can\'t follow simple instructions. \n<Enter to continue>')
name = input("Hello adventurer, what's your name? People call me the nurse.\n")
print(f'Nurse: "It\'s good to meet you, {name}. Have you allocated your stats yet? No?! It\'s kind of fun to'
      f' gamble your stats, you should try it!\nYou get random skill sets up to 3 times and get to decide if you want'
      f' to keep that skill set or re-roll! That\'s light customization!"')

player_set()

while True:
    print('\nNurse: "There you go, good as new. What do you want to do now?"'
          "\n<Seduce Character, CHA 3>"
          "\n<Wait>")
    seduce = input(f'\nYou are given multiple options to choose from in most encounters.'
                   f' The command to execute the option is listed in <these> at the bottom of your screen.'
                   f'\nThis character is able to be seduced! When you see the <seduce character> prompt, you can seduce'
                   f' that character. \nCharisma checks are done by comparing the AI charisma score against yours. '
                   f'You get one die per charisma level and have to roll the minimum skill check to pass!\n'
                   f'Skill-checked dialogue options can reveal new items, or choices.Try it now by typing \'seduce\''
                   f' and pressing enter! \n<Seduce or wait>\n').lower()
    if seduce == 'seduce':
        check = cha_check(charisma, 3, 'Nurse')
        if check == 'pass':
            input('\nNurse:"I usually don\'t do this but... '
                  '\n+1 Bandage\n<Enter to continue>')
            bandages = 1
            break
        else:
            print('Nurse: "Shut up."')
            input('<Enter to continue>')
            break
    if seduce == 'wait':
        break
    else:
        input('<Enter a valid input>')
        continue
print('*KNOCK KNOCK KNOCK*'
      f'\nDoctor: "I hope I wasn\'t interrupting anything!" '
      f'\nDoctor: "Hi {name}, I\'m the Doctor. It looks like you took a hit to the head and got sent here. Do you'
      f' remember what is going on?"'
      f'\n<Seduce character, CHA 8>')
money = 0
while money == 0:
    choice = input('<seduce or no>\n')
    if choice == 'seduce':
        check = cha_check(charisma, 8, 'Doctor')
        if check == 'pass':
            print('*Debt cleared*\n+ $150 ')
            input('Doctor: "Maybe I will just lose those hospital bills...')
            money = 150
            break
        else:
            choice = 'no'
    if choice == 'no':
        print(
            'Doctor: "Monsters are attacking! You got brought in here with some weapons so I assumed you'
            ' were supposed to do something about that." \n"Here are your things back. Oh, don\'t forget'
            ' to pay your bills!" \n + $50 ')
        money = 50
        break
    input('<Enter a valid input>')

print(f'\nDoctor: "Looks here like you came in with...if I could just find them..."')
input('<Enter to continue>')
primary_start = ['rifle', 'shotgun', 'pistol', 'pistol', 'rifle', 'pistol', 'pistol', 'rifle']
equipped_weapon = random.choice(primary_start)
secondary_start = ['knife', 'knife' 'knife', 'knife', 'knife', 'axe', 'hatchet', 'hatchet', 'hatchet']
secondary = random.choice(secondary_start)
print(
    f'\n\nDoctor: "Hah! Found them! Looks like you had a {equipped_weapon} and {secondary}'
    f' when you got brought here. \nLooks like you also had a bag of ammo with you too! all sorts of sizes and shapes!')
pistol_ammo_count = random.randint(10, 25)
rifle_ammo_count = random.randint(7, 25)
shotgun_shell_count = random.randint(4, 10)
print(f'pistol ammo + {pistol_ammo_count}\nRifle ammo + {rifle_ammo_count}\nShotgun shells + {shotgun_shell_count}\n\n'
      f'Doctor: "Did I mention I also run a little side business? If you need any ammo or bandages just find me."\n'
      '<Shop or leave>\n')
bandage_cost = random.randint(75, 150)
healing_cost = random.randint(100, 200)
pistol_ammo_cost = random.randint(5, 20)
rifle_ammo_cost = random.randint(7, 25)
shotgun_shell_cost = random.randint(10, 30)
while True:
    fight = input().lower()
    if fight == 'leave':
        double = input('You are about to enter a dangerous area, are you sure?')
        if double == 'yes':
            break
        else:
            continue

    if fight == 'shop':
        shopping()
        break
    else:
        print('<Enter a valid input>')

input(f'Doctor: "Good luck, {name}. If you survive the next three nights come back and see me!"'
      f'\n\nYou are about to start your first fight. after every fight the enemies get stronger. See how long you can'
      f' survive.\n<Enter to continue>')
kills = 0

fight_loop(0)
kills = 1
input('\n\nGet ready for round 2! \n<Enter to continue>')
fight_loop(1)
kills = 2
input('Another one is coming! \n<Enter to continue>')
fight_loop(2)
kills = 3
print('It looks like you held them off. Let\'s get back to the hospital')
input('Doctor: "I\'m glad to see you back! Prepare for the boss fight."')
shopping()
fight_loop(5)
kills = 4
print('Congratulations! You have beaten the game (for now)! Feel free to enjoy endless mode.')
cont = input('Want to play more? \n<Yes or no>')
if cont == 'yes':
    while hp > 0:
        input(f'current kill count at {kills}. Good luck.\n<Enter to continue>')
        mod = 2
        fight_loop(mod)
        kills += 1
        mod += 1
        print(f'New kill count at {kills}')
        quit = input('Continue? \n<Yes or no>\n')
        if quit == 'no':
            input(f'You did well. {kills} kills is impressive. Until next time, {name}')
            sys.quit
        shopping()
