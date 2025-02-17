https://dart.dev/guides/libraries/library-tour#collections
## creating an empty list

    var grain = [];
    
- a list of strings
    
    // literal
    var grain = <String>[];
    
    // constructor
    var grain = List<String>();

## create and fill a list with the same value 

    var veggies = List.filled(99, 'broccoli')
    assert(veggies.every((v) => v=='broccoli'));

    

    
