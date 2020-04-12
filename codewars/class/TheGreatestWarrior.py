# level 1 - 100
# ranks = "Pushover", "Novice", "Fighter", "Warrior", "Veteran", "Sage", "Elite", "Conqueror", "Champion", "Master", "Greatest"
# experience = 100 - 10000

class Warrior():
    def __init__(self):
        self.level = 1
        self.rank = 'Pushover'
        self.experience = 100
        self.achievements = []

    def getRank(self):
        RANKS = ["Pushover", "Novice", "Fighter", "Warrior", "Veteran", "Sage", "Elite", "Conqueror", "Champion", "Master", "Greatest"]
        self.rank = RANKS[self.level // 10]
        return self.rank

    def getExperience(self, experience):
        if self.experience < 10000:
            self.experience += experience
        if self.experience > 10000:
            self.experience = 9999
        return self.experience

    def training(self, arrya):
        discription, experience, level = arrya
        if level > self.level:
            return 'Not strong enough'
        self.achievements.append(discription)
        self.experience = self.getExperience(experience)
        self.level += experience // 100
        self.rank = self.getRank()
        return discription

    def battle(self, level):
        if level > 100 or level < 1:
            return 'Invalid level'
        if self.level == level:
            self.experience = self.getExperience(10)
        elif self.level > level:
            if self.level - level == 1:
                self.experience = self.getExperience(5)
            elif self.level - level >= 2:
                self.experience = self.getExperience(0)
        else:
            if level - self.level > 4 and level // 10 - self.level // 10 > 0 or level // 10 - self.level // 10 > 0:
                return "You've been defeated"
            else:
                diff = level - self.level
                k = 20 * diff * diff
                self.experience = self.getExperience(k)
        if self.level == level or self.level == level + 1:
            result = 'A good fight'
        elif self.level - level >= 2:
            result = 'Easy fight'
        else:
            result = 'An intense fight'

        self.level = self.experience // 100
        self.rank = self.getRank()
        return result


if __name__ == '__main__':
    test = Warrior()
    print(test.level)
    print(test.experience)
    print(test.rank)
    print(test.achievements)
    test.training(["Defeated Chuck Norris", 500, 1])
    print('*'*50)
    print(test.level)
    print(test.experience)
    print(test.rank)
    print(test.achievements)
    print(test.battle(2))
    print('*' * 50)
    print(test.level)
    print(test.experience)
    print(test.rank)
    # test.training(["Defeated Bruce Li", 1000, 7])
    # print('*' * 50)
    # print(test.level)
    # print(test.experience)
    # print(test.rank)
    # print(test.achievements)
    # print(test.battle(3))



