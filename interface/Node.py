from abc import ABC, abstractmethod

class Node(ABC):
    # Using single quotes 'Node' in type annotations is to avoid name resolution issues
    def __init__(self, prev: 'Node', next: 'Node', status: int):
        self.prev = prev
        self.next = next
        # show node status
        self.status = status
    @abstractmethod
    def serialize(self):
        pass
    @abstractmethod
    def deserialize(self):
        pass