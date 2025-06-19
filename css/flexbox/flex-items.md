## Flexbox children properties (items)

### Sources
```
https://flexboxfroggy.com/
https://css-tricks.com/snippets/css/a-guide-to-flexbox/#aa-background
https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Flexbox
```

### Flex items and other css layout settings
- `float`, `clear` and `vertical-align` have no effect on a flex item.

### `order`
- By default, flex items are laid out in the source order, the `order` property can override their order in their flex parent container

    .item {
        order: 5; /* default is 0 */
    }

- Items with the same order revert to source order.

### `flex-grow`
- describes the proportion occupied by a flex item in relation to its siblings.
- accepts a unitless value that indicate what amount of the available space inside its flex container parent an item should take up relative to its siblings.

E.g. in the illustration below the container has total space of 6, first child has `flex-grow:1`, second has `flex-grow:3`, third has `flex-grow:2`.

        +-----------------------------------------------+
        |   1   |           3           |       2       |
        +-----------------------------------------------+

- Negative numbers are not valid.

### `flex-shrink`
- defines the ability for a flex item to shrink if necessary.

    .item {
        flex-shrink: 3; /* default 1 */
    }

- Negative numbers are invalid.

### `flex-basis`
- sets the default size of an element before the remaining space is distributed.
- can be a length (e.g. `20%`, `5rem`, etc.) or a keyword.
- the value `auto` relies on the item's `width` or `height` properties.
- `content` relies on the item's content for sizing. The keyword is not yet generally well supported.

    .item {
        flex-basis:  | auto; /* default auto */
    }

- If set to `0`, the extra space around content isn’t factored in.
- If set to `auto`, the extra space is distributed based on its `flex-grow` value.

### `flex`

-shorthand to set `flex-grow`, `flex-shrink` and `flex-basis`.
- The second and third parameters (`flex-shrink` and `flex-basis`) are optional.
- The default is `0 1 auto`, but if you set it with a single number value (e.g. `flex: 2;`) `flex-basis` becomes `0%`. Thus  `flex:1` is equivalent to  `flex-grow: 1; flex-shrink: 1; flex-basis: 0%;`.

    .item {
        flex: none | [ <'flex-grow'> <'flex-shrink'>? || <'flex-basis'> ]
    }

### `align-self`
- allows to override individual items's default alignment (or the one specified by their parent's `align-items`).
- an item with a `align-self` is positioned along the bottom of its flex parent instead of the top where its sibling items are.
- takes the same values as the flex container's `align-items`.

    .item {
        align-self: auto | flex-start | flex-end | center | baseline | stretch;
    }
