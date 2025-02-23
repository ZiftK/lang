from lang_op.modules.object_types.object import Object


class Int(Object):
    def __init__(self, content: int = 0, name: str = ""):
        super().__init__(content, name)

    def __str__(self):
        return str(self.content)

    def __repr__(self):
        return f"Int({self.content}, name='{self.name}')"

    def __eq__(self, other):
        if isinstance(other, Int):
            return self.content == other.content
        elif isinstance(other, int):
            return self.content == other
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, Int):
            return Int(self.content + other.content)
        elif isinstance(other, int):
            return Int(self.content + other)
        return NotImplemented

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, Int):
            return Int(self.content - other.content)
        elif isinstance(other, int):
            return Int(self.content - other)
        return NotImplemented

    def __rsub__(self, other):
        if isinstance(other, int):
            return Int(other - self.content)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Int):
            return Int(self.content * other.content)
        elif isinstance(other, int):
            return Int(self.content * other)
        return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, Int):
            return Int(self.content / other.content)
        elif isinstance(other, int):
            return Int(self.content / other)
        return NotImplemented

    def __rtruediv__(self, other):
        if isinstance(other, int):
            return Int(other / self.content)
        return NotImplemented

    def __floordiv__(self, other):
        if isinstance(other, Int):
            return Int(self.content // other.content)
        elif isinstance(other, int):
            return Int(self.content // other)
        return NotImplemented

    def __rfloordiv__(self, other):
        if isinstance(other, int):
            return Int(other // self.content)
        return NotImplemented

    def __mod__(self, other):
        if isinstance(other, Int):
            return Int(self.content % other.content)
        elif isinstance(other, int):
            return Int(self.content % other)
        return NotImplemented

    def __rmod__(self, other):
        if isinstance(other, int):
            return Int(other % self.content)
        return NotImplemented

    def __divmod__(self, other):
        if isinstance(other, (Int, int)):
            quotient = self.__floordiv__(other)
            remainder = self.__mod__(other)
            return (quotient, remainder)
        return NotImplemented

    def __pow__(self, power, modulo=None):
        if isinstance(power, Int):
            exp = power.content
        elif isinstance(power, int):
            exp = power
        else:
            return NotImplemented

        if modulo is None:
            return Int(int(self.content ** exp))
        else:
            if isinstance(modulo, Int):
                mod = modulo.content
            elif isinstance(modulo, int):
                mod = modulo
            else:
                return NotImplemented
            return Int(pow(self.content, exp, mod))

    def __rpow__(self, other):
        if isinstance(other, int):
            return Int(other ** self.content)
        return NotImplemented

    def __neg__(self):
        return Int(-self.content)

    def __abs__(self):
        return Int(abs(self.content))
