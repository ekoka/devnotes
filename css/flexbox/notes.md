### Sources
https://flexboxfroggy.com/
https://css-tricks.com/snippets/css/a-guide-to-flexbox/#aa-background

- some properties are meant to be set on the parent element (i.e. "flex container"), while others are meant for children (i.e. "flex items").

### Declaring a flexbox container
- set `display: flex` on the container.


###  Justify content: `justify-content`:
- `flex-start`: Items align to the left side of the container.
- `flex-end`: `right|end` Items align to the right side of the container.
- `center`: Items align at the center of the container.
- `space-between`: Items display with equal spacing between them.
- `space-around`: Items display with equal spacing around them.

- note that `right` and `end` are not necessarily equivalent to `flex-end`. When the `flex-direction` is reversed (with `row-reverse`), `justify-content:flex-end` will also change to remain consistent with it, whereas `justify-content:right|end` would still designate their original position.

- `justify-content` is relative to `flex-direction`, that is when the latter is set to `row` and thus _horizontal_, the former affects items in that direction, likewise when `flex-direction` is `column` and therefore _vertical_, `justify-content` affects items thus oriented. `align-items` is similarly affected.

### Align content:
- `align-content` sets the spacing between multiple lines. Possible values:
    - `flex-start`: Lines are packed at the top of the container.
    - `flex-end`: Lines are packed at the bottom of the container.
    - `center`: Lines are packed at the vertical center of the container.
    - `space-between`: Lines display with equal spacing between them.
    - `space-around`: Lines display with equal spacing around them.
    - `stretch`: Lines are stretched to fit the container.

- `align-content` determines the spacing between *lines*, while `align-items` determines how the _items_ as a whole are aligned within the container. When there is only one line, `align-content` has no effect.

### Align items: `align-items`:
- `flex-start`: Items align to the top of the container.
- `flex-end`: Items align to the bottom of the container.
- `center`: Items align at the vertical center of the container.
- `baseline`: Items display at the baseline of the container.
- `stretch`: Items are stretched to fit the container.

- `align-items` is relative to `flex-direction`, that is when the latter is horizontal, the former affects items vertically, likewise when `flex-direction` is horizontal, `align-items` is adjusted to affect items horizontally. `justify-content` is similarly reoriented.

### Align single item: `align-self`
- takes the same values as `align-items`.


### Direction: `flex-direction`:
- `row`: Items are placed the same as the text direction.
- `row-reverse`: Items are placed opposite to the text direction.
- `column`: Items are placed top to bottom.
- `column-reverse`: Items are placed bottom to top.

- see above how `flex-direction` affects `justify-content` and `align-items`.

### Order: `order`:
- the default `order` value for any item is `0`.
- an integer value can be used to affect the order of any given item.

    .first-item {
        order: -50;
    }

    .last-item {
        order: 50;
    }

### Wrapping : `flex-wrap` and `flex-flow`
- `nowrap`: Every item is fit to a single line.
- `wrap`: Items wrap around to additional lines.
- `wrap-reverse`: Items wrap around to additional lines in reverse.

- `flex-flow`: is a shorthand propery that combines `flex-direction` and `flex-wrap`. It takes their respective values. E.g `flex-direction: column; flex-wrap: wrap;` is equivalent to this ` flex-flow: column wrap;`
