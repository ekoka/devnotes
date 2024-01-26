- `class Meta` options are a way to configure a schema's behavior. 

    class Meta:
        fields = ('id', 'email', 'date_created')
        exclude = ('password', 'secret_attribute')

## available options
- `fields`
- `additional`
- `include`
- `exclude`
- `dateformat`
- `strict`
- `json_module`
- `ordered`
- `index_errors`
- `load_only`
- `dump_only`

 
## specifying the option class
- embedding a `class Meta` declaration

    class UserSchema(Schema):
        
        class Meta:
            fields = ('id', 'email', 'date_created')

- setting `OPTIONS_CLASS` to a `SchemaOpts` class

    from marshmallow import SchemaOpts, Schema
    
    class UserSchemaOptions(SchemaOpts):
        
        def __init__(self, meta):
            SchemaOpts.__init__(self, meta)
            self.email = getattr(meta, 'email', None)
    
    class Meta:
        fields = ('id', 'email', 'date_created')
    class UserSchema(Schema):
        
