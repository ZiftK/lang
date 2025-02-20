from modules.object_types.object import Object


class Boolean(Object):

    def __init__(self, content: bool = None, name: str = ""):
        super().__init__(content, name)

    def __str__(self):
        return str(self.content)

    def __or__(self, other):
        return self.content or other.content

    def __and__(self, other):
        return self.content and other.content

