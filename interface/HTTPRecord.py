from abc import ABC, abstractmethod

from interface.Record import Record


class HTTPRecord(Record):
    def __init__(self,url, method,req_params,req_body,resp_body):
        self.url = ""
        self.method = ""
        self.req_params = {}
        self.req_body = ""
        self.resp_body = ""
    @abstractmethod
    def serialize(self):
        pass
    @abstractmethod
    def deserialize(self):
        pass