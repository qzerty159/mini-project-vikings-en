# With a correction already implemented: dont forget to initialize an instance of Class "War"


from vikingsClasses import Soldier, Viking, Saxon, War, Necromancer
import random


viking_soldier_names = ["albert","andres","archie","dani", "david","gerard","german","graham","imanol","laura"]
great_war = War()
necromancer_names = ["morthos", "valtor", "selene", "draegor", "nyx", "ezrath", "morgath", "lyrion", "kaelis", "vorgrim"]
saxon_soldier_names = ["aelfred", "ceolwulf", "osric", "beorn", "wulfgar", "edric", "leofwine", "ceorl", "oswald", "godric"]


# Create 5 Vikings
for i in range(5):
    great_war.addViking(Viking(viking_soldier_names[random.randint(0,9)], 100, random.randint(0,100)))

# Add Viking necromancer
great_war.addViking(Necromancer(necromancer_names[random.randint(0,9)], 100, random.randint(0,100)))

# Create 5 Saxons
for i in range(5):
    great_war.addSaxon(Saxon(saxon_soldier_names[random.randint(0,9)], 100, random.randint(0,100)))

# Add Saxon necromancer
great_war.addSaxon(Necromancer(necromancer_names[random.randint(0,9)], 100, random.randint(0,100)))  

round = 0
while great_war.showStatus() == "Vikings and Saxons are still in the thick of battle.":

    print(f"\n===== ROUND {round} =====")

    # Viking attack
    print("\nViking Attack Phase:")
    print(great_war.vikingAttack())

    # Necromancer action
    print("\nNecromancer Phase:")
    print(great_war.necromancerResurrect())
    great_war.cleanupDead()

    # Saxon attack
    print("\nSaxon Attack Phase:")
    print(great_war.saxonAttack())

    # Necromancer action
    print("\nNecromancer Phase:")
    print(great_war.necromancerResurrect())
    great_war.cleanupDead()

    # Army status
    print("\nArmy Status:")
    print(f" Vikings remaining: {len(great_war.vikingArmy)}")
    print(f" Saxons remaining:  {len(great_war.saxonArmy)}")

    # Battle status
    print("\nStatus:", great_war.showStatus())

    round += 1

print("\nFINAL RESULT")
print(great_war.showStatus())
