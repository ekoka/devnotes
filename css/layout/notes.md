see: https://developer.mozilla.org/en-US/docs/Web/CSS/display

### `display` property
- Formally, the display property sets an element's inner and outer display types:
    - The outer type sets an element's participation in flow layout; whether an element is treated as a `block` or `inline` box.
    - the inner type sets the layout of children, such as `flow` layout, `grid` or `flex`.


    /* precomposed values */
    display: block;
    display: inline;
    display: inline-block;
    display: flex;
    display: inline-flex;
    display: grid;
    display: inline-grid;
    display: flow-root;

    /* box generation */
    display: none;
    display: contents;

    /* multi-keyword syntax */
    display: block flex;
    display: block flow;
    display: block flow-root;
    display: block grid;
    display: inline flex;
    display: inline flow;
    display: inline flow-root;
    display: inline grid;

    /* other values */
    display: table;
    display: table-row; /* all table elements have an equivalent CSS display value */
    display: list-item;

    /* Global values */
    display: inherit;
    display: initial;
    display: revert;
    display: revert-layer;
    display: unset;


- Some values of `display` are fully defined in their own individual specifications; for example the detail of what happens when `display: flex` is declared is defined in the _CSS Flexible Box Model specification_.
