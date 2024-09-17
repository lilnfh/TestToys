from interface.HTTPRecord import HTTPRecord
from interface.Node import Node


class HTTPRecordNode(HTTPRecord, Node):
    def __init__(self, prev: 'Node', next: 'Node', input: HTTPRecord, output: HTTPRecord, url, method, req_params, req_body, resp_body):
        self.prev = prev
        self.next = next
        self.input = input
        self.output = output
        self.url = url
        self.method = method
        self.req_params = req_params
        self.req_body = req_body
        self.resp_body = resp_body

    def serialize(self):
        print("serialize")

    def deserialize(self):
        print("deserialize")