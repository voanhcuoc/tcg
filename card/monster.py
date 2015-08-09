# Monster card definition
# Normal monster, Effect monster, Fusion monster, Ritual monster, Synchro monter, XYZ monster

from .card import Card

class Monster(Card):
    'Root class for monster card'
    def __init__(self, name, types, attr, descr, effs, location,
                 attack, defend, star):
        Card.__init__(self, name, types, attr, descr, effs, location)
        self.attack = attack
        self.defend = defend
        self.star = int(star)

    def __repr__(self):
        return Card.__repr__(self) + '\nStar: {} Attack: {} Defend: {}'.format(
            self.star, self.attack, self.defend)

    def discard(self):
        self.location.remove(self)

    def attack(self, other):
        battle(self, other)

    def normalSummon(self):
        self.location.summon(self)

    def set(self):
        self.location.set(self)

    def flip(self):
        self.location.flip(self)

class NormalMonster(Monster):
    'Normal monster does not have effect'
    def __init__(self, name, types, attr, descr, location,
                 attack, defend, star):
        Monster.__init__(self, name, types, attr, descr, (), location,
                         attack, defend, star)
