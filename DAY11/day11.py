import random

player_hp = 100
monster_hp = 100
potions = 3

def attack():
    return random.randint(10, 20)

def monster_attack():
    return random.randint(8, 18)

while True:
    print("\n====== MONSTER BATTLE ======")
    print(f"Your HP: {player_hp}")
    print(f"Monster HP: {monster_hp}")
    print(f"Potions: {potions}")

    print("\n1. Attack")
    print("2. Heal")
    print("3. Quit")

    choice = input("Choose: ")

    if choice == "1":
        damage = attack()
        monster_hp -= damage

        if monster_hp < 0:
            monster_hp = 0

        print(f"\nYou attacked the monster for {damage} damage!")

    elif choice == "2":
        if potions > 0:
            heal = random.randint(15, 30)
            player_hp += heal

            if player_hp > 100:
                player_hp = 100

            potions -= 1
            print(f"\nYou healed {heal} HP.")
        else:
            print("\nNo potions left!")

    elif choice == "3":
        print("\nThanks for playing!")
        break

    else:
        print("\nInvalid choice.")
        continue

    if monster_hp <= 0:
        print("\n🎉 You defeated the monster!")
        break

    damage = monster_attack()
    player_hp -= damage

    if player_hp < 0:
        player_hp = 0

    print(f"The monster attacked you for {damage} damage!")

    if player_hp <= 0:
        print("\n💀 You were defeated!")
        break