## Methods at a glance
- `setAll(Iterable itr)`
- `add(value)`
- `addAll(Iterable itr)`
- `insert(value)`
- `insertAll(Iterable itr)`
- `fillRange(int start, int end, value)`
- `replaceRange(int start, int end, Iterable itr)`

## Appending
- only for growable lists

#### `addAll(Iterable itr)`

    final nums = <int>[1,2,3];
    nums.addAll([4,5,6]);
    print(nums); // [1, 2, 3, 4, 5, 6]

- appends all items from `itr` to the list

#### `add(value)`
- appends `value` to the list


## Inserting in the middle
- only for growable lists

#### `insert(int index, value)`

    final nums = <int> [1, 2, 3, 4];
    nums.insert(2, 10);
    print(nums); // [1, 2, 10, 3, 4] 
    
- inserts value at `index`
- increases the length of the list and shifts all object at or after `index` by one
- `index` must be valid: `0 <= i <= length`

#### `insertAll(int index, Iterable itr)`

    final nums = <int>[1, 2, 3, 4, 5];
    nums.insertAll(2, [10, 30, 50]);
    print(nums); // [1, 2, 10, 30, 50, 3, 4, 5]
    
- inserts all items of `itr` at position `index`
- increases the length of the list and shifts all later object by the length of `itr`
- `index` must be valid

## Setting and replacing

#### `setAll(Iterable itr)` method 
- works for both growable and non-growable lists
    list.setAll(startIndex, listOfValues);

    e.g.
    nums = List.fill(10, 0);    // [0, 0, 0, 0, 0, ... 0]
    nums.setAll(1, [1, 2, 3]);  // [0, 1, 2, 3, 0, ... 0]

#### `List[index] = value` 
- works for both growable and non-growable lists
- `index` must be valid : for `0 <= i < list.length`

#### `fillRange( int start, int end, value)`
- sets all positions in the range `[start:end]` with `value`
- list elements type is not nullable, `value` must be non-`null`

#### `replaceRange(int start, int end, Iterable itr)`

    final nums = <int> [1, 2, 3, 4, 5];
    final replacements = <int>[6, 7, 8];
    nums.replaceRange(2, 5, replacements);
    print(nums); // [1, 2, 6, 7, 8]
    
- only works for  growable lists, even if the range is within the list 
- to work with non-growable lists use `setRange()`
- replaces a range of elements with elements of `itr`
- provided range must be valid : `0 <= start <= end <= length`

#### `setRange(int start, int end, Iterable itr, int skipCount)`

    final nums1 = <int>[1, 2, 3, 4];
    final nums2 = <int>[5, 6, 7, 8, 9];
    const skipCount = 3;
    nums1.setRange(1, 3, nums2, skipCount);
    print(nums1); // [1, 8, 9, 4]
    nums1.setRange(1, 3);
- writes some items in `itr` into the range `[start:end]` (`end` excluded) of the list
- skips `skipCount` objects first from `itr`
- range must be valid : `0 <= start <= end <= length`
- empty range is valid : `start == end`
- `itr` must have enough items after `skipCount` elements to fill the range of the list
- if `itr` is also the original list, the replacement of `[start:end]` by `[skipCount:skipCount + (end-start)]` is properly applied, even if the two ranges overlap
