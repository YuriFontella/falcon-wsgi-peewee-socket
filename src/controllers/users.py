import falcon, json

from src.models.users import Users
from src.hooks.secure import secure

@falcon.before(secure)
class UsersResource:
    def on_get(self, req, resp):
        print(req.get_param('id', False))
        print(req.params)

        users = Users.select(Users.name).limit(1).dicts()
        users = [user for user in users.iterator()]

        resp.media = len(users)
    
    def on_post(self, req, resp):
        try:
            print(req.media)
            user = Users.insert(req.media)

        except Exception as e:
            raise Exception(e)
        
        else:
            user = user.execute()
            
            resp.status = falcon.HTTP_201
            resp.text = json.dumps(user)
        
    def on_get_user(self, req, resp, id):
        user = Users.select().where(Users.id == id).dicts()
        resp.media = user.get()
