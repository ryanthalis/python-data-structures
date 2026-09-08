"""A compact singly linked list implementation."""

from collections.abc import Iterable, Iterator
from typing import Any


class LinkedList:
    """A singly linked list supporting membership, equality, and removal."""

    class _Node:
        def __init__(self, item: Any, next_node=None) -> None:
            self.item = item
            self.next = next_node

    def __init__(self, values: Iterable[Any] = ()) -> None:
        self._first = LinkedList._Node(None)
        self._last = self._first
        self._num_items = 0
        for value in values:
            self.append(value)

    def __len__(self) -> int:
        return self._num_items

    def __iter__(self) -> Iterator[Any]:
        current = self._first.next
        while current is not None:
            yield current.item
            current = current.next

    def __repr__(self) -> str:
        return f"LinkedList({list(self)!r})"

    def append(self, value: Any) -> None:
        node = LinkedList._Node(value)
        self._last.next = node
        self._last = node
        self._num_items += 1

    def __contains__(self, x: any) -> bool:
        cursor = self.__iter__()
        for i in cursor:
            if i == x:
                return True

        return False

    def __eq__(self, other: 'LinkedList') -> bool:
        if not isinstance(other, LinkedList):
            return False

        if self._num_items != other._num_items:
            return False

        cursor = self.__iter__()
        cursor_2 = other.__iter__()

        for i,j in zip(cursor, cursor_2):
            if i != j:
                return False
        return True

    def __delitem__(self, i: int) -> None:
        if i < 0 or i >= len(self):
            raise IndexError("index is out of range")

        previous = self._first
        curr = self._first.next

        for _ in range(i):
            previous = previous.next
            curr = curr.next

        if curr is self._last:
            self._last = previous

        previous.next = curr.next

        self._num_items -= 1
        return None

    def remove(self, x: any) -> None:
        if len(self) == 0:
            raise ValueError("List is empty")

        if x not in self:
            raise ValueError("LinkedList.remove(x): x not in list")

        previous = self._first
        curr = self._first.next

        for _ in range(len(self)):
            if curr.item == x:
                break
            previous = previous.next
            curr = curr.next

        if curr is self._last:
            self._last = previous

        previous.next = curr.next
        self._num_items -= 1
