class Node:
    def __init__(self, value):
        self._value = value
        self._parent = None
        self._children = []

    @property
    def value(self):
        return self._value

    @property
    def children(self):
        return self._children

    def add_child(self, node):
        if node not in self._children:
            self._children.append(node)

            if node.parent is not self:
                node.parent = self

    def remove_child(self, node):
        if node in self._children:
            self._children.pop(self._children.index(node))

            if node.parent is not None:
                node.parent = None

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, node):
        if self._parent:
            self._parent.remove_child(self)
            self._parent = None
        if node is not None:
            self._parent = node
            node.add_child(self)

    def depth_search(self, value):
        if self.value == value:
            return self

        if self.children:
            for child in self.children:
                check = child.depth_search(value)
                if check:
                    return check

        return None

    def breadth_search(self, value):
        if self.value == value:
            return self

        if self.children:
            kids = self.children

            while kids:
                if kids[0].value == value:
                    return kids[0]
                else:
                    grandkids = kids[0].children
                    if grandkids:
                        for kid in grandkids:
                            kids.append(kid)
                    kids.pop(0)

# node1 = Node("root1")
# node2 = Node("root2")
# node3 = Node("root3")

# node3.parent = node1
# node3.parent = node2

# print(node1.children)
# print(node2.children)
