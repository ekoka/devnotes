
- specifying a function or method as handlers for field's value

    from marshmallow import fields

    def get_foo_value(model_object):
        item = model_object.foo
        return transform(item)

    class UsrerSchema(BaseSchema):

        foo = fields.Function(get_foo_value)

        bar = fields.Method('get_bar_value')

        def get_bar_value(self, model_object):
            if self.many:
                # do something if we're in a collection context
                return "I'm the beginning and the end. The first and last"
            return "I'm one of many"
