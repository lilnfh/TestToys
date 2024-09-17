from interface.HTTPRecord import HTTPRecord

class HTTPRecordData(HTTPRecord):
    def __init__(self,url, method,req_params,req_body,resp_body):
        self.url = ""
        self.method = ""
        self.req_params = {}
        self.req_body = ""
        self.resp_body = ""
    def serialize(self):
        print("serialize")
    def deserialize(self):
        print("deserialize")
