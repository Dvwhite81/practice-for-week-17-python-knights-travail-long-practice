from tree import Node

class KnightPathFinder:
    def __init__(self, coords):
        self.coords = coords
        self._root = Node(coords)
        self._considered_positions = set(coords)

    def get_valid_moves(self, pos):
        moves = set()
        options = [
            (2, 1),
            (1, 2),
            (2, -1),
            (1, -2),
            (-2, 1),
            (-1, 2),
            (-2, -1),
            (-1, -2)
        ]

        # print('pos: ', pos)
        for option in options:
            # print('option: ', option)
            x = pos[0] + option[0]
            y = pos[1] + option[1]
            valid = 0 <= x < 8 and 0 <= y < 8

            if valid:
                moves.add((x, y))

        return moves

    def new_move_positions(self, pos):
        moves = self.get_valid_moves(pos)
        positions = moves - self._considered_positions
        self._considered_positions.update(positions)
        return positions


# Tests
# finder = KnightPathFinder((0, 0))
# print(finder.new_move_positions((0, 0)))

# f2 = KnightPathFinder((8, 8))
# print(f2.new_move_positions((8, 8)))

# f3 = KnightPathFinder((1, 8))
# print(f3.new_move_positions((1, 8)))
