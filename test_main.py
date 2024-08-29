from abc import *
from dataclasses import dataclass, field

import pytest
import string


class Piece(ABC):
    ...


class Pawn(Piece):
    ...


def test_pawn():
    p = Pawn()
    # assert type(p) is Piece
    assert isinstance(p, Piece)


Position = tuple[str, int]

X_VALUES = set(string.ascii_letters[:8])
Y_VALUES = {v for v in range(1, 9)}


def validate_pos(pos):
    if len(pos) != 2:
        raise ValueError("Two elements in position required.")
    x, y = pos
    if x not in X_VALUES:
        raise ValueError("Invalid x.")
    if y not in Y_VALUES:
        raise ValueError("Invalid y.")


@dataclass
class Board:
    _pieces: dict[Position, Piece] = field(default_factory=dict)

    def __getitem__(self, pos: Position):
        validate_pos(pos)
        return self._pieces[pos]

    def __setitem__(self, pos: Position, piece: Piece):
        validate_pos(pos)
        self._pieces[pos] = piece


@pytest.mark.parametrize('invalid_pos', [("h", 1, 1), ('a',), ('a', 0), ('i', 1),])
def test_invalid_pos(invalid_pos):
    b1 = Board()
    with pytest.raises(ValueError):
        _ = b1[*invalid_pos]





