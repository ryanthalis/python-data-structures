"""A compact dynamic-array implementation."""

import ctypes


class ArrayList:
    """A sequence backed by a resizable contiguous array."""

    def __init__(self, iterable=()) -> None:
        self._num_items = 0
        self._elems = _new_array(1)
        for elem in iterable:
            self.append(elem)

    def __len__(self) -> int:
        return self._num_items

    def __iter__(self):
        for i in range(len(self)):
            yield self._elems[i]

    def __getitem__(self, i: int):
        if 0 <= i < len(self):
            return self._elems[i]
        raise IndexError("ArrayList: index out of range")

    def __repr__(self) -> str:
        return f"ArrayList({list(self)!r})"

    def __eq__(self, other: object) -> bool:
        return isinstance(other, ArrayList) and list(self) == list(other)

    def append(self, x) -> None:
        if len(self) == len(self._elems):
            self._resize()
        self._elems[self._num_items] = x
        self._num_items += 1

    def __delitem__(self, i: int) -> None:
        if not 0 <= i < len(self):
            raise IndexError("ArrayList: assignment index out of range")
        for index in range(i, self._num_items - 1):
            self._elems[index] = self._elems[index + 1]
        self._num_items -= 1
        self._elems[self._num_items] = None
        if len(self._elems) >= 3 * len(self):
            self._resize()

    def extend(self, iterable) -> None:
        for i in iterable:
            self.append(i)
        return None

    def index(self, x: any) -> int:
        for index in range(len(self)):
            if self._elems[index] == x:
                return index

        raise ValueError("ArrayList.index(x): x is not in list")

    def pop(self, i: int = -1) -> any:
        if self._num_items == 0:
            raise IndexError("ArrayList: pop from empty list")
        
        if i > self._num_items - 1 or i < 0 - self._num_items :
            raise IndexError("ArrayList: pop index out of range")
        
        if i >= 0:
            item = self.__getitem__(i)
            self.__delitem__(i)
            return item
        else:
            item = self.__getitem__(i + (self._num_items))
            self.__delitem__(i + (self._num_items))
            return item

    def __reversed__(self):
        for i in reversed(range(len(self))):
            yield self[i] 

    def _resize(self) -> None:
        new_array = _new_array(max(1, 2 * self._num_items))
        for i in range(self._num_items):
            new_array[i] = self._elems[i]
        self._elems = new_array


def _new_array(capacity: int):
    if capacity <= 0:
        raise ValueError("capacity must be positive")
    array_type = ctypes.py_object * capacity
    array = array_type()
    for i in range(capacity):
        array[i] = None
    return array
