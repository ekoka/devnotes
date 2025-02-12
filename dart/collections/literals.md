## Conditional in collection literals

### add item based on condition

    // List 
    [
        ...
        if (condition) "this string added if condition is true",
        ...
    ]
    
    // Map
    {
        ...
        if (condition) "foo": "bar",
        ...
    {

### append a collection based on condition

- the spread operator comes after the `if (condition)` statement

    // List
    [
        ...
        if (condition) ...["some", "collection", "to", "append"],
        ...
    ]

    # Map
    {
        ...
        if (condition) ...{1:"some", 2:"collection", 3:"to", 4:"append"},
        ...
    }

### iterate collection and append processed items to a collection literal

    # List
    [
        ...
        for (var i in collectionOfItems) process(i),
        ...
    ]

    # Map
    {
        ...
        for (var i in collectionOfItems) '$i': process(i),
        ...
    }
