from modules.object_types.object import Object
from modules.object_types.alph_object import Alph


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
        self.content += other.content
        return self

    def __mul__(self, other):
        other: int
        if other.content < 0:
            self.content = self.content[::-1]

        self.content = self.content * abs(other.content)
        return self

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

    def calc_sub_sequences(self, alp: Alph = None):
        suffix = self.calc_suffix(alp)
        prefix = self.calc_prefix(alp)
        return suffix + prefix