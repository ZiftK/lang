class Object:

    def __init__(self, content=None, name: str = ""):
        self.content = content
        self.name = name

    def copy(self, other):
        other: Object
        self.content = other.content

    def __str__(self):
        return str(self.content)