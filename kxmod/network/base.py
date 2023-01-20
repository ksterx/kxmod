import uuid


class Network:
    def __init__(self):
        self.nodes = set()
        self.links = set()

    def __repr__(self) -> str:
        return f"Network({self.links})"

    def show(self):
        pass

    def connect(self, node1, node2, is_from=None, weight=1):
        self.nodes.add(node1)
        self.nodes.add(node2)
        if is_from is None:
            node1.add_nondir(node2)
        elif is_from == "parent":
            node2.add_parent(node1)
        elif is_from == "child":
            node1.add_parent(node2)
        link = Link(node1, node2, is_from=is_from, weight=weight)
        self.links.add(link)

    def max_degree(self):
        pass

    def min_degree(self):
        pass


class Node:
    def __init__(self, value, type=None):

        available_types = [str, int, float]
        if type is not None and type not in available_types:
            available_types.append(type)
        if not isinstance(value, tuple(available_types)):
            raise ValueError(f"Value must be one of {available_types}")

        self.value = value
        self.id = uuid.uuid4()
        self.parents = set()
        self.childs = set()
        self.nondir = set()

    def __len__(self):
        return len(self.links)

    def __repr__(self):
        return f"Node({self.value})"

    def __eq__(self, other) -> bool:
        return self.id == other.id

    def __hash__(self) -> int:
        return hash(self.id)

    def add_parent(self, other):
        self.parents.add(other)
        if self not in other.childs:
            other.add_child(self)

    def add_child(self, other):
        self.childs.add(other)
        if self not in other.parents:
            other.add_parent(self)

    def add_nondir(self, other):
        self.nondir.add(other)
        if self not in other.nondir:
            other.add_nondir(self)

    def _ancestors(
        node,
        list_,
    ):
        for parent in node.parents:
            if parent not in list_:
                list_.append(parent)
                parent._ancestors(parent, list_)

    def ancestors(self):
        return self._ancestors(self, [])

    def remove_duplicate(self, target):
        a = list(set(target))
        print(len(a) == len(target))
        return a

    def generation(self):
        return len(self.ancestors()) + 1


class Link:
    def __init__(self, node1: Node, node2: Node, is_from, weight: float = 1.0):
        """Link between two nodes.

        Args:
            node1 (Node): Node 1
            node2 (Node): Node 2
            is_from (str/None): Direction of the link.
                ===============================
                | "parent": node1 -> node2   |
                | "child" : node1 <- node2   |
                | None    : node1 <-> node2  |
                ===============================
            weight (float, optional): Link weight. Defaults to 1.0.
        """

        self.node1 = node1
        self.node2 = node2
        self.is_from = is_from
        self.weight = weight
        self.id = uuid.uuid4()
        self._normalize()

    def __repr__(self):
        if self.is_from == "parent":
            return f"{self.node1} -> {self.node2}"
        elif self.is_from == "child":
            return f"{self.node1} <- {self.node2}"
        elif self.is_from is None:
            return f"{self.node1} <-> {self.node2}"
        else:
            raise ValueError("Direction must be either parent/child/None.")

    def __eq__(self, other):
        if self.is_from == other.direction:
            return (self.node1, self.node2) == (other.node1, other.node2)
        elif self.is_from is None and other.direction is None:
            return (self.node1, self.node2) == (other.node2, other.node1)
        elif ((self.is_from, other.direction) == ("parent", "child")) or (
            (self.is_from, other.direction) == ("child", "parent")
        ):
            return (self.node1, self.node2) == (other.node2, other.node1)
        else:
            return False

    def __hash__(self):
        return hash(self.id)

    def _normalize(self):
        if self.is_from == "child":
            self.node1, self.node2 = self.node2, self.node1
            self.is_from = "parent"
        elif self.is_from is None and self.node1.id < self.node2.id:
            self.node1, self.node2 = self.node2, self.node1

    def get_node_ids(self):
        return self.node1.id, self.node2.id
