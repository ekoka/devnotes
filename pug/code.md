## Unbuffered code
- starts with `-`
    // e.g. output 3 list items
    
    -   for (var x=0; x < 3; x++) 
        li item

- block unbuffered code

    - 
        var list = ["uno", "dos", "tres"]
    each item in list
        li= item
      
## Buffered code
- starts with `=`
- evaluates the JavaScript and outputs result
- HTML escaped

    p 
        = 'This code is escaped!'
    // renders as
    <p>This code is &lt;escaped&gt;!</p>

- can also be written inline

    p= 'This code is' + '<escaped>!'
    // <p>This code is &lt;escaped&gt;!</p>
     
    p(style="background: blue")= 'A message with a ' + 'blue' + ' background'
    // <p style="background: blue">A message with a blue background</p>
    
## Unescaped buffered code
- starts with `!=`
- like buffered code, but does not perform any escaping

    p
        != 'This code is <strong>not</strong> escaped!'
    // <p>This code is <strong>not</strong> escaped!</p>

    p!= 'This code is <strong>not</strong> escaped!'
    // <p>This code is <strong>not</strong> escaped!</p>
