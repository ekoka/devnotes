- pass the nested schema class to the `Nested` field 

    from marshmallow import Schema, fields
    
    class UserSchema(Schema):
        ...

    class BlogSchema(Schema):
        ...
        author = fields.Nested(UserSchema)

    blog = Blog(...,author=User(...))
    result, errors = BlogSchema().dump(blog)

- pass `many=True` for a nested collection

    class BlogSchema(Schema):
        ...
        author = fields.Nested(UserSchema, many=True)
    
    
- limit which fields to nest with `exclude` and `only`.
- attributes of deeply nested objects can be represented using dot delimiters

    class SiteSchema(Schema):
        blog = fields.Nested(BlogSchema2)
        
    schema = SiteSchema(only=['blog.author.email'])
    result, errors = schema.dump(site)
    result
    # {
    #     'blog': {
    #         'author': {'email': u'monty@python.org'}
    #     }
    # }
