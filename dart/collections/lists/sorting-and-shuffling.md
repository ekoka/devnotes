## `myList.sort(cmp)` 
sort a list with the help of a comparison function that takes two items and compares them.

    e.g. 

    var fruits = ['banana', 'avocado', 'apple'];
    // alphabetical
    fruits.sort( (x,y) => x.compareTo(y) );
    print(fruits); // [apple, avocado, banana]
    // length
    fruits.sort( (x,y) => x.length.compare(y.length) );
    print(fruits); // [apple, banana, avocado]

- `cmp(x, y)` must return: 
    - zero if `x` is considered equal to `y`,
    - a negative integer if `x < y` 
    - a positive integer if `x > y` 
    

#### `shuffle()`
