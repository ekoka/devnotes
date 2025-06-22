

- compiling a pug template

    pug = require('pug')
    compiledFunction =  pug.compileFile('template.pug')

- reuse compiled template

    str1 = compiledFunction({foo: 123, bar: 'xyz'}) 
    str2 = compiledFunction({foo: 456, bar: 'abc'}) 

- compiling and rendering in one operation

    str3 = pug.render('template.pug', {foo: 789, bar: 'ijk'})
