
### Constructor: `Object()`

    final obj = Object();


### Hash code of the object 

    `obj.hashCode`
    
- it may be worth overriding this getter to give a more fitting hash code.
- if overriding `hashCode`, it might be pertinent to also override the `==` operator.
    
### `obj.runtimeType`
a representation of the runtime type of the object.

## Instance methods
### `Object.toString()`
### `Object.noSuchMethod()`

## Static methods

#### Object.hash()

    Object.hash(Object? obj1, Object? obj2, ..., Object? obj20)
    
- creates a combined hash code for a number of objects
- hash code is computed for all arguments supplied, even if `null`, by combining the `Object.hashCode` of each argument.

#### Object.hashAll()
#### Object.hashAllUnordered()
