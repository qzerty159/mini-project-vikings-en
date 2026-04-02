import random

# Soldier


class Soldier:
    def __init__(self, health, strength, resurrection_chance=0.25):
        self.health = health
        self.strength = strength
        self.resurrection_chance = resurrection_chance
    
    def attack(self):
        return self.strength

    def tryResurrect(self):
        """Attempt a random resurrection."""
        if random.random() < self.resurrection_chance:
            # Successful resurrection
            self.health = 100  # regains 100 HP
            self.strength = 150
            return "A soldier has resurrected with renewed strength!"
        else:
            # failed resurrection
            return "A soldier has died permanently."
        
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health <= 0:
            resurrected = self.tryResurrect()
            if resurrected:
                return "A soldier has resurrected with renewed strength!"
            return "A soldier has died permanently."

        return f"A soldier has received {damage} points of damage"

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength, resurrection_chance=0.25):
        super().__init__(health, strength, resurrection_chance)
        self.name = name
        
    def battleCry(self):
        return "Odin Owns You All!"

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:

            # attempt at resurrection
            if random.random() < self.resurrection_chance:
                self.health = 100
                self.strength = 150
                return f"{self.name} has resurrected by Odin's will and returns to battle more strongly!"
            else:
                return f"{self.name} has died in act of combat"

# Saxon

class Saxon(Soldier):
    def __init__(self, name, health, strength, resurrection_chance=0.25):
        super().__init__(health, strength, resurrection_chance)
        self.name = name

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            if random.random() < self.resurrection_chance:
                self.health = 100
                self.strength = 150
                return "A Saxon has resurrected and returns to battle more strongly!"
            else:
                # attempt at resurrection
                if random.random() < self.resurrection_chance:
                    self.health = 100
                    self.strength = 150
                    return f"{self.name} has resurrected by Woden's will and returns to battle more strongly!"
                else:
                    return f"{self.name} has died in act of combat"

# Necromancy

class Necromancer(Soldier):
    def __init__(self, name, health, strength, magic_power=50, resurrection_chance=0.5):
        """
        magic_power: determines how strong the necromancer is
        resurrection_chance: probability to resurrect a fallen ally
        """
        super().__init__(health, strength, resurrection_chance)
        self.name = name
        self.magic_power = magic_power

    def resurrect(self, army):
        """
        Try to resurrect a fallen soldier from the given army.
        The necromancer can only resurrect soldiers that have died in battle.
        """
        # Filter soldiers that are dead (health <= 0)
        dead_soldiers = [soldier for soldier in army if soldier.health <= 0]

        # If no dead soldiers, nothing happens
        if not dead_soldiers:
            return "The Necromancer found no dead soldiers to resurrect."

        # Choose one dead soldier randomly
        target = random.choice(dead_soldiers)

        # Attempt resurrection
        if random.random() < self.resurrection_chance:
            # Successful resurrection
            target.health = 40 + self.magic_power // 2  # resurrected with partial health
            target.strength  = 40 + self.magic_power // 2  # resurrected with partial strength
            return "A fallen warrior has been resurrected by dark magic!"
        else:
            return "The Necromancer failed to resurrect the fallen warrior."


        
# THE BATTLE

class War():
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
    

    def addViking(self, viking):
        self.vikingArmy.append(viking)
    

    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)
    

    def necromancerResurrect(self):
        logs = []
        # If a necromancer exists in either army, he attempts to resurrect a fallen ally.
        # # Check Viking necromancers
        for soldier in self.vikingArmy:
            if isinstance(soldier, Necromancer):
                result = soldier.resurrect(self.vikingArmy)
                logs.append(f"Necromancer {soldier.name} resurrects for Vikings: {result}")

        # Check Saxon necromancers
        for soldier in self.saxonArmy:
            if isinstance(soldier, Necromancer):
                result = soldier.resurrect(self.saxonArmy)
                logs.append(f"Necromancer {soldier.name} resurrects for Saxons: {result}")

        if logs:
            return "\n".join(logs)
        else :
            return "No necromancer is present in either army."


    def vikingAttack(self):
        if not self.vikingArmy or not self.saxonArmy:
            return "No attack possible."
        
        attacker = random.choice(self.vikingArmy)
        defender = random.choice(self.saxonArmy)
        
        # Log BEFORE attack
        log = f"Viking Attack: {attacker.name} " \
            f"(HP:{attacker.health}, STR:{attacker.strength}) attacks " \
            f"{defender.name} " \
            f"(HP:{defender.health}, STR:{defender.strength})\n"

        # Perform attack
        result = defender.receiveDamage(attacker.attack())
        log += " → " + result
        
        return log


    def saxonAttack(self):
        if not self.vikingArmy or not self.saxonArmy:
            return "No attack possible."
        
        attacker = random.choice(self.saxonArmy)
        defender = random.choice(self.vikingArmy)
        
        # Log BEFORE attack
        log = f"Saxon Attack: {attacker.name} " \
            f"(HP:{attacker.health}, STR:{attacker.strength}) attacks " \
            f"{defender.name} " \
            f"(HP:{defender.health}, STR:{defender.strength})\n"

        # Perform attack
        result = defender.receiveDamage(attacker.attack())
        log += " → " + result
        
        return log


    def cleanupDead(self):
        self.vikingArmy = [s for s in self.vikingArmy if s.health > 0]
        self.saxonArmy = [s for s in self.saxonArmy if s.health > 0]


    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
    pass
