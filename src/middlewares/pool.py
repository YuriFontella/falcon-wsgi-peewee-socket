from config.db.pool import db

class Pool:
    def process_request(self, req, resp):
        db.connect(reuse_if_open=True)

    def process_response(self, req, resp, resource, params):
        db.close()
