from interface.Node import Node

class InpuNode(Node):
    # Using single quotes 'InpuNode' in type annotations is to avoid name resolution issues
    def __init__(self, prev: 'InpuNode', next: 'InpuNode', status: int):
        self.prev = prev
        self.next = next
        # show node status
        self.status = status
    def serialize(self):
        print("serialize")
    def deserialize(self):
        print("deserialize")