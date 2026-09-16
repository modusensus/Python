"""
Tree_sort algorithm.
Build a Binary Search Tree and then iterate thru it to get a sorted list.
"""

from __future__ import annotations

from collections.abc import Iterable, Iterator
from dataclasses import dataclass
from typing import Any, Protocol


class Comparable(Protocol):
    def __lt__(self, other: Any, /) -> bool: ...


@dataclass
class Node[T: Comparable]:
    val: T
    left: Node[T] | None = None
    right: Node[T] | None = None

    def __iter__(self) -> Iterator[T]:
        if self.left:
            yield from self.left
        yield self.val
        if self.right:
            yield from self.right

    def __len__(self) -> int:
        return sum(1 for _ in self)

    def insert(self, val: T) -> None:
        if val < self.val:
            if self.left is None:
                self.left = Node(val)
            else:
                self.left.insert(val)
        elif self.right is None:
            self.right = Node(val)
        else:
            self.right.insert(val)


def tree_sort[T: Comparable](arr: Iterable[T]) -> tuple[T, ...]:
    """
    Build a Binary Search Tree from an iterable of mutually comparable items
    and iterate thru it to get a sorted tuple.

    :param arr: iterable of mutually comparable items
    :return: tuple of all the items ordered by ascending

    Time complexity: best O(n log n), average O(n log n), worst O(n^2)
    Space complexity: O(n)

    >>> tree_sort([])
    ()
    >>> tree_sort((1,))
    (1,)
    >>> tree_sort((1, 2))
    (1, 2)
    >>> tree_sort([5, 2, 7])
    (2, 5, 7)
    >>> tree_sort((5, -4, 9, 2, 7))
    (-4, 2, 5, 7, 9)
    >>> tree_sort([5, 6, 1, -1, 4, 37, 2, 7])
    (-1, 1, 2, 4, 5, 6, 7, 37)
    >>> tree_sort(range(10, -10, -1)) == tuple(sorted(range(10, -10, -1)))
    True
    >>> tree_sort(["pear", "apple", "fig"])
    ('apple', 'fig', 'pear')
    >>> tree_sort([2.5, 1, 3.5, -1])
    (-1, 1, 2.5, 3.5)
    >>> tree_sort([3, 3, 1, 2, 2, 1])
    (1, 1, 2, 2, 3, 3)
    """
    iterator = iter(arr)
    try:
        first = next(iterator)
    except StopIteration:
        return ()

    root = Node(first)
    for item in iterator:
        root.insert(item)
    return tuple(root)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print(f"{tree_sort([5, 6, 1, -1, 4, 37, -3, 7]) = }")
