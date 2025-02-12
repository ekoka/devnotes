ref: https://dart.dev/codelabs/iterables

- `Iterable` is an abstract class
- `List` and `Set` are `Iterable`, so they include the same methods and properties as the `Iterable` class.
- Elements of a `Map` can also be read from an iterable object, by using the map's `entries` or `values` property.

- you can declare a list with the `Iterable` type, but you won't have access to some `List`'s  methods and properties, including, the `[]` operator.

- you can read elements with `elementAt(index)`.
- using a `for - in` loop


    for (item in iterable) {
        pint(item);
    }
   
- `first` and `last` properties return the first and last item of an iterable. 
- accessing `last` requires traversing all elements (O(N))
- accessing  `first` or `last` on an empty `Iterable` results in a `StateError`

- to get the first element that satisfies a condition, use `firstWhere(predicateFunction)` 

    // e.g. return first name of length 5 
    final names = ["John", "Jerry", "Jane", "Jules", "Joe", ]
    names.firstWhere((item) => item.length==5 )`

- if no value satisfies the predicate, a default value can be returned from a second function passed as the `orElse` parameter. 
    firstWhere(
        (item) { /* should return true when item is found */ },
        orElse: () { /* returns default value */ }
    );

- if no value satisfies the predicate and no default function is provided, `firstWhere()` throws a `StateError`

- `singleWhere(predicate)` is similar to `firstWhere(predictate)`, but it expects that only one item satisfies the predicate. If more than one or no values match the predicate a `StateError` is thrown. 
- since `singleWhere()` traverses the whole `Iterable`, it can cause problems if the `Iterable` is large (or inifinite).

### checking conditions

- `every(predictate)` check that all elements satisfy a condition

    if (names.every(startWithUppercase) ) {
        print('Every name starts with an uppercase letter');
    }

- `any(predicate)` check that any elements satisfies a condition
    
    if ( names.any(startWithUppercase) ) {
        print('At least one name starts with an uppercase letter');
    }

---
## filtering 
### `where(predicate)` 
- finds all elements that satisfy a condition

    // find all names of length 5
    names.where( (n) => n.length==5 )

- the output of `where()` is also an `Iterable`

- if no item satisfies the predicate used with `where()`, the method returns an empty `Iterable`

### `takeWhile(predicate)` and `skipWhile(predicate)`
- iterates through `Iterable` and returns another `Iterable` that either *take* or *skip* elements of the first `Iterable`, until the predicate is `true`.

- the functions split the original `Iterable` in two parts, and place the first qualifying item in the second part.

- thus `takeWhile()` excludes the first qualifying item from its return value, whereas `skipWhile()` includes it.
    
    final negative =  sortedNumbers.takeWhile((item) => item < 0)
    final positive =  sortedNumbers.skipWhile((item) => item < 0)
    

---
## `map()`
- applies a function over each element and returns an `Iterable` of the transformation.

- `map()` returns a lazy `Iterable` that only processes the supplied function when the elements are iterated.

    Iterable<Transformation> newIterable = oldIterable.map((item){
    
        // process old item and return new item
        
    })
- equivalent to   

    Iterable<T> map<T> ( T toElement(E e) ) sync* {
        for (var v in this) {
            yield toElement(v);
        }
    }
    
