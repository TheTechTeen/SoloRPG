from secrets import choice
import theme as t
from pc import pcs
from random import choice, randint

class Organization():
    def __init__(self, npc=False, thread=False):
        if npc:
            self.theme = npc.theme
        elif thread:
            self.theme = thread.theme
        else:
            self.theme = choice(t.themes)

        self.relationships = {}

        for pc in pcs:
            if npc and pc in npc.relationships.keys():
                self.relationships[pc] = npc.relationships[pc]
            else:
                base = t.RELATIONSHIPS[self.theme].get(pc.theme)
                base += randint(-1, 1)
                self.relationships[pc] = base + randint(-1, 1)