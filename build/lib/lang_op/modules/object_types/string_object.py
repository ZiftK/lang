from lang_op.modules.object_types.object import Object
from lang_op.modules.object_types.alph_object import Alph
import itertools


class String(Object):

    def __init__(self, content: str = "", name: str = ""):
        super().__init__(content, name)

    def __str__(self):
        return self.content

    def __eq__(self, other):
        other: String
        return self.content == other.content

    def __add__(self, other):
        other: String
        new = self.content + other.content
        return new
    
    def __mul__(self, other):
        other: int
        if other.content < 0:
            self.content = self.content[::-1]

        return self.content * abs(other.content)

    def __len__(self):
        return len(self.content)

    def calc_prefix(self, alph: Alph = None, include_lamba: bool = True):
        if not alph:
            init_count = 0 if include_lamba else 1
            return [self.content[0:n] for n in range(init_count, len(self.content) + 1)]

    def calc_suffix(self, alph: Alph = None, include_lambda: bool = True):
        if not alph:
            include = [self.content, ""] if include_lambda else [self.content]
            return include + [self.content[-n:] for n in range(1, len(self.content) + 1)]

    def calc_sub_sequences(self, alph: Alph = None):
        suffix = self.calc_suffix(alph)
        prefix = self.calc_prefix(alph)
        return suffix + prefix

    def calc_sub_strings(self, alph: Alph = None):
        if not alph:
            subsequences = [
                ''.join(comb)
                for i in range(1, len(self.content) + 1)
                for comb in itertools.combinations(self.content, i)
            ]
            return subsequences
