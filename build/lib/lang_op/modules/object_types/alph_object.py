import re
from lang_op.modules.object_types.lang_object import Lang


class Alph(Lang):

    def __init__(self, content: list = None, name: str = ""):
        if not content:
            content = []
        super().__init__(content, name)

        self.compile_len_pattern()

    def add_element(self, element: str):
        self.content.add(element)
        self.compile_len_pattern()

    def len_on(self, word: str):
        return len(re.findall(self.__len_pattern, word))

    def compile_len_pattern(self):
        pattern = "(" + ")|(".join(self.content) + ")"
        self.__len_pattern = re.compile(pattern)

    def __str__(self):
        return super().__str__()
