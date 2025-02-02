https://flutterigniter.com/checking-null-aware-operators-dart/
### `??` : default operator
set a default if value is `null`

    # idiom
    variable = value==null ? default : value

    # dart
    final variable = value ?? default;
    // or
    final variable = getValue() ?? default;
    
### `??=` : fallback assignment operator
set an init value if variable is `null`

    # idiom 
    if variable==null:
        variable = default

    # dart
    final variable ??= default;

since the statement is also an expression, it can be used as a return value
    
    e.g. a getter

    get value {
        return _value ??= _computeValue();
    }

### `?.` : safe navigation operator

if any of the attributes in the chain is `null`, the whole expression is `null` 

    # idiom
    if var1 && var1.var2: 
        return var1.var2.var3;
    return null;
    
    # dart
    return var1?.var2?.var3

### `...?` optional spread operator
spread list only if it's not `null`

    # idiom
    if l1!=null:
        l2 = [...l1]

    # dart
    final l1 = <String>['a', 'b', 'c'];
    final l2 = <String>[...l1];
    

### Non-nullable type declaration
this non-null declaration would throw an error, because no value is assigned
    int variable;

There are three solutions:
- set an initial value

    int variable = 0;
    
- delay the assignment

    late int variable;

- make the variable nullable by appending `?` to the type
    
    int? variable;
