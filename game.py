class Hero ():
    def __init__(self, name, hp, gold):
        self.name = name
        self.hp = hp
        self.gold = gold

    def Who_Hero(self):
        print(self.name, self.hp, self.gold)

def main():
    main_hero = Hero("Tallun", 20, 100)
    main_hero.Who_Hero()

if __name__ == "__main__":
    main()