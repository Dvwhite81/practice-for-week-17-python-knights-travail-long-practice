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


    def build_move_tree(self):
        moves = [self._root]

        while moves:
            current = moves[0]
            position = current.value
            new_moves = self.new_move_positions(position)

            for move in new_moves:
                node = Node(move)
                current.add_child(node)
                moves.append(node)

            moves.pop(0)


    def find_path(self, end_position):
        end_node = self._root.breadth_search(end_position)
        path = self.trace_to_root(end_node)

        return path


    def trace_to_root(self, end_node):
        trace = []
        current = end_node

        while current:
            trace.insert(0, current.value)
            current = current.parent

        return trace


# Tests
# finder = KnightPathFinder((0, 0))
# print(finder.new_move_positions((0, 0)))

# f2 = KnightPathFinder((8, 8))
# print(f2.new_move_positions((8, 8)))

# f3 = KnightPathFinder((1, 8))
# print(f3.new_move_positions((1, 8)))

# finder = KnightPathFinder((0, 0))
# finder.build_move_tree()
# print(finder._root.children)

finder = KnightPathFinder((0, 0))
finder.build_move_tree()
print(finder.find_path((2, 1))) # => [(0, 0), (2, 1)]
print(finder.find_path((3, 3))) # => [(0, 0), (2, 1), (3, 3)]
print(finder.find_path((6, 2))) # => [(0, 0), (1, 2), (2, 4), (4, 3), (6, 2)]
print(finder.find_path((7, 6))) # => [(0, 0), (1, 2), (2, 4), (4, 3), (5, 5), (7, 6)]
