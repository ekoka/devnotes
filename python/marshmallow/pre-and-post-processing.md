- data pre-processing and post-processing can be registered using `pre_load`, `post_load`, `pre_dump`, `post_dump` decorators

    from marshmallow import Schema, fields, pre_load
    
    class UserSchema(Schema):
        name = fields.Str()
        slug = fields.Str()
        
        @pre_load
        def slugify(self, in_data):
            in_data['slug'] = in_data['slug'].lower().strip().replace(' ', '-')
            return in_data
        
- pre and post-processing receive one object/datum at a time
- to receive the input collection when `many=True`, add `pass_many=True` to the decorators

    @pre_load(pass_many=True)
    def pre_processor(self, data, many):
        if many:
            handle_many_items(data)
        else:
            handle_single_item(data)


