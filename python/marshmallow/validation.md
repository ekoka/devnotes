
## validation errors
- the result of the loading (serialization) operation is a `collection.namedtuple` of the form `(data, errors)`, where `errors` is a dictionary of validation errors

    result = UserSchema().load({'email': 'foo'})
    # or 
    data, errors = UserSchema().load({'email': 'foo'})
    
    result.errors 
    # {'email': ['"foo" is not a valid email address']}

- with a collection

    user_data = [
        {'email': 'mick@stones.com', 'name': 'Mick'},
        {'email': 'invalid', 'name': 'Invalid'}, # invalid email
        {'email': 'keith@stones.com', 'name': 'Keith'},
        {'email': 'charlie@stones.com'}, # missing name
    ]

    result = UserSchema(many=True).load(user_data)

## augmenting field validation
- validation can be added to a field by passing it a validate callable (or a collection of callables, i.e. list, tuple, generator)

    class ValidateUserSchema(UserSchema):
        age = fields.Number(validate=lambda n: 18 <= n <= 40)

    
    data = {'name': 'Mick', 'email': 'mick@stones.com', 'age': 71}
    result = ValidateUserSchema().load(data)
    result.errors 
    # {
    #   'age': [
            'Validator <lambda>(71.0) is False'
        ]
    # }

## `ValidationError` and validation function return value
- validation function either return a boolean or raise a `ValidationError`.
- if a `ValidationError` is raised, its message is stored when validation fails.

    from marshmallow import ValidationError
    
    def validate_quantity(n):
        if n < 0:
            raise ValidationError('Quantity must be greater than 0')
        if n > 30:
            raise ValidationError('Quantity must not be greater than 30')
    
## validation during serialization

- `Schema.dump()` also returns a dictionary of errors, including any `ValidationErrors` raised during serialization. However, `required`, `allow_none`, `validate`, `@validates`, and `@validate_schema` only apply during deserialization.

## field validators as schema methods

    from marshmallow import Schema, fields, validates, ValidationError
    
    class ItemSchema(Schema):
        quantity = fields.Integer()

        @validates('quantity')
        def validate_quantity(self, value):
            if value < 0:
                raise ValidateError('Quantity must be greater than 0')
            if value > 30:
                raise ValidateError('Quantity must not be greater than 30')
            
## strict validation 

- setting `strict=True` either in the `Schema` constructor or as a `class Meta` option will raise an error when invalid data are passed in (as opposed to returning them as part of the result).

- the dictionary of validation errors is accessible from the `ValidationError.messages` attribute.

    try:
        UserSchema(strict=True).load({'email': 'foo'})
    except marshmallow.ValidationError as err:
        print(err.messages) # {'email': ['"foo" is not a valid email address']}


## error handlers 
- a custom error handler can be registered on the schema by overriding its `handle_error` method.

## validatin only
- to validate without deserializing, use the `Schema.validate()` method
    
    errors = UserSchema().validate({'name': 'Ron', 'email': 'invalid-email'})
