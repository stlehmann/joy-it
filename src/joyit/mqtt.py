from typing import NamedTuple


class MoveAxisParams(NamedTuple):
    axis: int
    position: int
    velocity: int


class MoveParams(NamedTuple):
    ax0: int
    ax1: int
    ax2: int
    ax3: int
    ax4: int
    ax5: int
    velocity: int


commands = {
    "move_axis": MoveAxisParams,
    "move": MoveParams,
}
