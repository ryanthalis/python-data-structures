"""An array-backed binary max-heap."""


def left(i: int) -> int:
    return 2 * i + 1


def right(i: int) -> int:
    return 2 * (i + 1)


def parent(i: int) -> int:
    return (i - 1) // 2


class BinaryMaxHeap:
    """Store comparable values with the largest value at the root."""

    def __init__(self, iterable=()) -> None:
        self._elems = []
        for elem in iterable:
            self.add(elem)

    def __len__(self) -> int:
        return len(self._elems)

    def __iter__(self):
        return iter(self._elems)

    def __repr__(self) -> str:
        return f"BinaryMaxHeap({self._elems!r})"

    def add(self, x: any) -> None:
        self._elems.append(x)
        self._bubble_up(len(self) - 1)

    def _bubble_up(self, i: int) -> None:
        p = parent(i)
        while i > 0 and self._elems[i] > self._elems[p]:
            self._elems[i], self._elems[p] = self._elems[p], self._elems[i]
            i = p
            p = parent(i)

    def remove(self) -> any:
        if len(self) == 0:
            raise IndexError('remove: empty heap')

        x = self._elems[0]
        self._elems[0] = self._elems[len(self) - 1]
        self._elems.pop()
        self._trickle_down(0)

        return x

    delete_max = remove

    def _trickle_down(self, i: int) -> None:
        n = len(self)
        while i >= 0:
            j = -1
            r = right(i)
            if r < n and self._elems[r] > self._elems[i]:
                l = left(i)
                if self._elems[l] > self._elems[r]:
                    j = l
                else:
                    j = r
            else:
                l = left(i)
                if l < n and self._elems[l] > self._elems[i]:
                    j = l

            if j >= 0:
                self._elems[j], self._elems[i] = self._elems[i], self._elems[j]

            i = j

    def peek(self) -> any:
        if len(self) == 0:
            raise IndexError("peek: empty heap")
        return self._elems[0]
