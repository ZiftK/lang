from itertools import chain
from lang_op.modules.object_types.object import Object
from lang_op.modules.object_types.int_object import Int


class Lang(Object):
    def __init__(self, content: list | set = None, name: str = ""):

        if not content:
            content = []
        content: set = set(content) if content.__class__ is list else content
        super().__init__(content, name)
        self.__kleene_clau = [[""]]
        self.__len_pattern = ""

    def has(self, value: str):
        return value in self.content

    def get_content(self) -> set:
        return self.content

    def _get_flat_kleene_clau(self, length=None):
        if not length:
            length = len(self.__kleene_clau)-1
        return list(chain(*(self.__kleene_clau[:length+1])))

    def get_kleene_clau(self, steps: Int):
        steps += 1
        if len(self.__kleene_clau) >= steps.content:
            flat_list = self._get_flat_kleene_clau(steps.content)
            return flat_list

        steps -= len(self.__kleene_clau)
        return self.calc_kleene_clau(steps)

    def get_positive_clau(self, steps: Int):
        steps += 1
        if len(self.__kleene_clau) >= steps.content:
            flat_list = self._get_flat_kleene_clau()[1:steps.content]
            return flat_list

        steps -= len(self.__kleene_clau)
        return self.calc_kleene_clau(steps, include_lambda=False)

    def calc_kleene_clau(self, steps: Int, include_lambda=True):

        if steps.content == 0:
            result = self._get_flat_kleene_clau()
            result = result if include_lambda else result[1:]
            return result

        current = self.__kleene_clau[-1]

        aux = []
        if current == [""]:
            aux = [x for x in self.content]
        else:
            for word in current:
                for word2 in self.content:
                    aux.append(word + word2)

        self.__kleene_clau.append(aux)

        return self.calc_kleene_clau(steps - 1, include_lambda=include_lambda)

    def __str__(self):
        cont = list(self.content)
        cont.sort()
        string = "', '".join(cont)
        string = "{'" + string + "'}"
        return string

    def union(self, lang):
        lang: Lang
        return self.content | lang.get_content()

    def concat(self, lang):
        lang: Lang
        other_content: set = lang.get_content()

        new_content = []
        for word in self.content:
            for word2 in other_content:
                new_content.append(word + word2)
        return new_content

    def pow(self, count: Int):

        if len(self.__kleene_clau) >= count.content:
            return self.__kleene_clau[count.content]

        aux_lang = Lang(content=[""])

        def _pow(lang: Lang, _count: int):

            if _count == 0:
                return lang.content

            lang = Lang(content=lang.concat(self))
            return _pow(lang, _count - 1)

        return _pow(aux_lang, count)
