
# Dumping (aka Serializing) objects
- takes a data object and serializes it into a dictionary or JSON string.
- `dump()` for dictionary  and `dumps()` for JSON string.
- includes validation by default, but can be skipped.

    usr = get_db_user(user_id)
    schema = UserSchema()
    result = schema.dump(usr)
    pprint(result.data)
    # {"name": "Monty",
    #  "email": "monty@python.org",
    #  "created_at": "2014-08-17T14:54:16.04959..."}

### Filter which fields to output 
- use the `only` and `exclude` parameters.

    summary_schema = UserSchema(only=('name', 'email'))
    print(summary_schema.dump(usr).data)
    # {"name":"Monty", "email": "monty@python.org"}


# Loading object (aka Deserializing)
- takes a dictionary as input and loads it to an application-level data structure (by default, also a dictionary)

    result = UserSchema().load({
        "created_at": "2014-08-11T...",
        "email": u"ken@yahoo.com",
        "name": u"ken",
    })
    pprint(result.data)
    {
        "created_at": datetime.datetime(2014, 8, 11, ...), # <-- became a datetime object
        "email": "ken@yahoo.com",
        "name": "ken",
    }
    
- to deserialize to an object, decorate a method in the schema with `post_load`

    from app.models import User
    from marshmallow import Schema, post_load, fields

    class UserSchema(Schema):

        name = fields.Str()
        ...

        @post_load
        def populate_user(self, data):
            return User(**data)
        

# Handling collections 
- serializing

    usr1 = User(name='Mick', email='mick@stones.com')
    usr2 = User(name='Keith', email='keith@stones.com')
    result = UserSchema(many=True).dump([usr1, usr2])
    result.data
    # [{"name": u"Mick", 
    #   "email": u"mick@stones.com",
    #   "created_at": "2014-08-17T14:58..."},
    #  {"name": u"Keith",
    #   "email": u"keith@stones.com",
    #   "created_at": "2014-08-17T14:58..."}]

- deserializing
    
    user_data = [
        {'email': 'mick@stones.com', 'name': 'Mick'},
        {'email': 'keith@stones.com', 'name': 'Keith'},
    ]

    users, errors = UserSchema(many=True).load(user_data)
    
