
## Basic declaration

    from app.models import UserModel
    from marshmallow import Schema, fields
    
    class UserSchema(Schema):
        name = fields.Str()
        email = fields.Email()
        date = fields.DateTime()

