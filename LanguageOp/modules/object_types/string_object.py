from modules.object_types.object import Object


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
        self.content = self.content*other.content
        return self
