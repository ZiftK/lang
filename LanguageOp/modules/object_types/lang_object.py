from itertools import chain


class Lang:
    def __init__(self, content: list | set):
        self._content: set = set(content) if content.__class__ is list else content
        self.__kleene_clau = [[""]]
        self.__len_pattern = ""

    def has(self, value: str):
        return value in self._content

    def get_content(self) -> set:
        return self._content

    def get_flat_kleene_clau(self):
        return list(chain(*self.__kleene_clau))

    def calc_kleene_clau(self, steps: int = 1):

        if steps == 0:
            return Lang(self.get_flat_kleene_clau())

        current = self.__kleene_clau[-1]

        aux = []
        if current == [""]:
            aux = [x for x in self._content]
        else:
            for word in self._content:
                for word2 in self._content:
                    aux.append(word + word2)

        self.__kleene_clau.append(aux)

        return self.calc_kleene_clau(steps - 1)

    def __str__(self):
        cont = list(self._content)
        cont.sort()
        string = "', '".join(cont)
        string = "{'" + string + "'}"
        return string

    def union(self, lang):
        lang: Lang
        return Lang(self._content | lang.get_content())

    def concat(self, lang):
        lang: Lang
        other_content: set = lang.get_content()

        new_content = []
        for word in self._content:
            for word2 in other_content:
                new_content.append(word + word2)
        return Lang(new_content)

    def pow(self, count: int):

        aux_lang = Lang([])

        def _pow(lang: Lang, _count: int):
            if _count == 0:
                return lang

            lang.concat(self)
            return _pow(lang, _count - 1)

        return _pow(aux_lang, count)
