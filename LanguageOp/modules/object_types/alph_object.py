import re
from modules.object_types.lang_object import Lang


class Alph(Lang):

    def __init__(self, content: list):

        super().__init__(content)

        self.compile_len_pattern()

    def add_element(self, element: str):
        self._content.add(element)
        self.compile_len_pattern()

    def len_on(self, word: str):
        return len(re.findall(self.__len_pattern, word))

    def compile_len_pattern(self):
        pattern = "(" + ")|(".join(self._content) + ")"
        self.__len_pattern = re.compile(pattern)

    def __str__(self):
        return super().__str__()
