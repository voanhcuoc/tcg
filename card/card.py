# Card Definition

class Card:
    'Card Definition'
    def __init__(self, name, types, attr, descr, effs, location, pos=None):
        'A general-purpose card has name, types, attribute, description'
        ', effects list location and position'
        self.name = name
        self.types = types
        self.attr = attr
        self.descr = descr
        self.effs = effs
        self.location = location
        # Ex: deck, extra deck, one side of the field, graveyard
        self.pos = pos
        # EX: face up, face down, face up attack, face up defense, face down defense

    def __repr__(self):
        return '\n'.join((
            '{}',
            'Attribute: {}',
            'Type: {}',
            'Description: {}',
            'Position: {}',
            'Location: {}',
            )).format(self.name, self.attr, ', '.join(self.types), self.descr,
                      self.pos, self.location)
