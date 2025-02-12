### Summary
`itr.moveNext()` move to next value
`itr.current` get current value

### Using an iterator

    final colors = <String>['red', 'green', 'blue'];
    
    // explicitly
    final colorsIter = colors.iterator;
    while (colorsIter.moveNext()) {
        print(colorsIter.current);
    }

    // implicitly with for-in
    for (color in colors) { 
        print(color);
    }


- Interface for getting items, one at a time, from an object.

- the `for-in` construct transparently uses `Iterator` to get each item, and to test the end of the iteration.

- if the object iterated over is changed during iteration, the behavior is unspecified.

- the `Iterator` is initially positioned before the first element. It must therefore be advanced to point to the first element (with `moveNext()`.

- if no element is left to iterate over `moveNext()` returns `false`, so do further calls to `moveNext()`.


### `itr.current`
- if `moveNext()` has not yet been called or if the iterator has been moved past the last element of the `Iterable`, `current` is unspecified (may throw error, or return a default value).
- current should keep its value until next call to `moveNext()`, even if an underlying collection changes.

### `itr.moveNext()`
- advance the iterator to the next element of the iteration
- should be called before reading `current`
- if the call to `moveNext()` returns `true` then `current` will point to the next element of the iteration. 
- if `moveNext()` returns `false` then there are no further items and `current` should not be used anymore .
- it's safe to call `moveNext()` again after it has returned `false`.
- `moveNext()` may throw an exception for various reasons, such as concurrent change to the underlying collection, during iteration. If that happens, consider the iterator in an inconsistent state, and further behavior is unsspecified.
