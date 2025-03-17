import random
import time
money=1000
sushilist={
    "Common": ["Salmon", "Maguro", "California Roll", "Ebi", "Ika", "Inari", "Tamago", "Tako"],
    "Uncommon": ["Bintoro", "Hamachi", "Harasu", "Taramayo", "Maguroyuke", "Saba", "Kani"],
    "Rare": ["Anago", "Akagai", "Katsuo", "Ankimo", "Engawa", "Iwashi"],
    "Legendary": ["Ikura", "Hotate", "Buri", "Fugu", "Aji"],
    "Mythic":["Awabi", "Kaibashira", "Chutoro", "Madai"],
    "Godly": ["Uni", "Ootoro", "Unagi"],
}
droprates={
    "Common": 50,
    "Uncommon": 28,
    "Rare": 14.3,
    "Legendary": 5,
    "Mythic": 2.5,
    "Godly": 0.2
}
player_collection={}
def wait_exit():
    while True:
        user_input=input("\nType 'exit' to return: ").strip().lower()
        if user_input == "exit":
            break
        else:
            print("Invalid input. Type 'exit' to go back.")
def add_xp(sushi,xp_gain):
    sushi_data=player_collection[sushi]
    sushi_data["xp"]+=xp_gain
    initial=sushi_data["lv"]
    while sushi_data["xp"]>=10*(2**(sushi_data["lv"]-1)):
        sushi_data["xp"]-=10*(2**(sushi_data["lv"]-1))
        sushi_data["lv"]+=1
    if (initial!=sushi_data["lv"]):
        print(f"{sushi} leveled up! Now Level {sushi_data['lv']}")
def gacha(roll):
    global player_collection
    for _ in range(roll):
        rarity = random.choices(list(droprates.keys()), weights=list(droprates.values()), k=1)[0]
        sushi = random.choice(sushilist[rarity]) 
        if sushi in player_collection:
            print(sushi)
            add_xp(sushi, 1000)
        else:
            player_collection[sushi]={"lv":1,"xp":0}
            print(f"NEW!!! {sushi}")
    wait_exit()
def show_collection(collection):
    print("\nYour Sushi Collection:")
    if not collection:
        print("Your collection is empty.")
    else:
        for sushi, data in collection.items():
            xp_required=10*(2**(data["lv"]-1))
            print(f"{sushi}: Level {data['lv']} (XP: {data['xp']}/{xp_required})")
    wait_exit()
def sushi_minigame():
    global money, player_collection
    if not player_collection:
        print("\nYour collection is empty! Roll some gacha first to get sushi.")
        return
    print("\n🎮 Welcome to the Sushi Mini-Game! 🎮")
    print("You have 60 seconds to match/type sushi name.")
    print("Each correct match earns combos")
    print("Type 'exit' any time you want to leave")
    game_duration=60
    reward_money=2
    reward_xp=10
    streak=0
    total_xp=0
    all_sushi_list = ["Salmon", "Maguro", "California Roll", "Ebi", "Bintoro", "Inari", "Tamago", "Tako", "Ika", "Hamachi", "Harasu", "Taramayo", "Maguroyuke", "Saba", "Kani", "Anago", "Akagai", "Katsuo", "Ankimo", "Engawa", "Iwashi", "Ikura", "Hotate", "Buri", "Fugu", "Aji", "Awabi", "Kaibashira", "Chutoro", "Madai", "Uni", "Ootoro", "Unagi"]
    sushi_names=list(player_collection.keys())
    print("\nYour Sushi Collection:")
    for i, sushi in enumerate(sushi_names, 1):
        print(f"{i}. {sushi}")
    while True:
        choice=input("\nWhich sushi do you want to level up? Enter the number: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(sushi_names):
            selected_sushi = sushi_names[int(choice) - 1]
            print(f"You selected {selected_sushi} to level up.")
            break
        else:
            print("Invalid choice. Please enter a valid number.")
    print("\nStarting game... Match the sushi names!")
    start_time=time.time()
    while time.time()-start_time<game_duration:
        streak_bonus=1+(streak)*(streak)*0.1
        target_sushi=random.choice(all_sushi_list)
        print(f"\nMatch this sushi: {target_sushi}")
        user_input = input("Your answer: ").strip()
        if user_input.lower() == "exit":
            print("Exiting Sushi Matcher. Good job!")
            break
        if user_input == target_sushi:
            # Correct match
            earned_money=int(reward_money*streak_bonus)
            earned_xp=int(reward_xp*streak_bonus)
            money+=earned_money
            total_xp+=earned_xp
            print(f"Correct! You earned ${earned_money} and {earned_xp} XP!")
            streak += 1
        else:
            print(f"Wrong!")
            streak=0
    print(f"\nTime's up! You earned a total of {total_xp} XP for {selected_sushi} and ${money}.")
    add_xp(selected_sushi, total_xp)
def SushiNoah():
    global money
    print("\n🍣Welcome to Noah's Kaitenzushi!🍣")
    while True:
        print(f"\nCurrent money: ${money}")
        print("\nOptions:")
        print("1. Roll gacha")
        print("2. View your collection")
        print("3. Play Sushi game to earn money")
        choice = input("\nWhat do you want to do? ").strip()
        if choice == "1":
            max_rolls = money // 100
            if max_rolls <= 0:
                print("You don't have enough money to roll!")
                continue
            while True:
                rolls = input(f"How many rolls would you like? (Max: {max_rolls}) ").strip()
                if rolls.isdigit() and 0 < int(rolls) <= max_rolls:
                    rolls = int(rolls)
                    break
                print("Please enter a valid number of rolls.")
            gacha(rolls)
            money -= 100 * rolls
        elif choice == "2":
            show_collection(player_collection) 
        elif choice == "3":
            sushi_minigame()
        else:
            print("Invalid choice. Please try again.")
SushiNoah()