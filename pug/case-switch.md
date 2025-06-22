- `case` is a shorthand for JavaScript's `switch`

    ```
    - var friends = 10

    case friends
        when 0
            p you have no friends
        when 1
            p you have a friend
        default
            p you have #{friends} friends
    ```

## `case` fallthrough 
- works similar to JavaScript's `switch`, but unlike `switch`, it only works if the block is missing.

    case friends
        when 0 // empty block, fallthrough
        when 1
            p you have very few friends
        default
            p you have many friends

    case friends
        when 0  // block not empty, no fallthrough
            - break
        when 1
            p you have very few friends
        default
            p you have many friends

## block expansion 
        
    case friends
        when 0: p you have no friends
        when 1: p you have a friend
        default: p you have #{friends} friends
