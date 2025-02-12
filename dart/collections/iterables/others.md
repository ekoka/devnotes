## `forEach(fnc)` 
- invokes `fnc()` for each item
- signature: 

    void forEach(
        void fnc( E element )
    )

    e.g. print all items
    numbers.forEach(print);

---

## `join( [String separator=""] )`
- converts each elements to string and concatenate them using the separator as glue (defaults separator is empty string).

    e.g.
    
    final fruits = <String>["guava", "mango", "cherry"]; 
    vowels.join(" # "); // "guava # mango # cherry"
    
---

## `reduce()`  (see also `fold()`)
- signature: `E reduce ( E combine ( E value, E element) {})`

- reduces collection to a single value by successively combining elements of the collection using a combining function.

- `Iterable` must yield at least one value.

    final sum = numbers.reduce((a, b) => a + b);


## `fold()`
- signature: 
    T fold<T>(
        T initialValue, 
        T combine( 
            T previousValue, 
            E element
        ) {}
    )

- similar to `reduce()`, but uses an `initialValue` which may not be present in the `Iterator`

---

## `take(int count)`
- returns a lazy `Iterable` of the first `count` (or less) elements.

## `skip(int count)` 
- returns an `Iterable` that provides all but the first `count` elements.

---

## `whereType<T>()`
- returns a new iterable with all elements that have type `T` 
    
---

## `followedBy( Iterable other)`
- lazy concatenation of this iterable and `other`

    final planets = <String>['Mercury', 'Venus'];
    final updated = planets.followedBy(['Earth', 'Mars']);
    print(updated); // ['Mercury', 'Venus', 'Earth', 'Mars']

---

## `Iterable<T> castFrom<S, T>( S source )`
- adapts `source` to be an `Iterable<T>`
- any time the iterable produces an item that isn't `T` an exception is thrown.
    
---

## `expand( Iterable toElements( E element) )` 
- flattens or expands an `Iterable` 

    e.g. flattening a two-dimensional integer Iterable

    Iterable<int> flatten( Iterable<int> numbers ) sync* {
        for (n in numbers) {
            yield n;
        }
    }

    final integers = <List<int>>[ [12, 33, 4], [5, 92, 3], [8, 22, 7]];
    integers.expand(flatten); // [12, 33, 4, 5, 92, 3, 8, 22, 7]

