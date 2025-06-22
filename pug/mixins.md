Allow to create reusable blocks of pug

## declaration and usage
- declaration
    mixin list
        ul
            li foo
            li bar
            li baz

    // usage
    +list
    
    // renders as
    <ul>
        <li>foo</li>
        <li>bar</li>
        <li>baz</li>
    <ul>
    
- declaration with a parameter
    mixin pet(name)
        li.pet= name
        
    // usage
    ul
        +pet('cat')
        +pet('dog')
        +pet('pig')
        
    // renders as
    <ul>
        <li class="pet">cat</li>
        <li class="pet">dog</li>
        <li class="pet">pig</li>
    <ul>


## mixins can also take a block of pug as content

    mixin article(title)
        .article
            .article-wrapper
                h1= title
                if block
                    block
                else
                    p No content provided

    // usage
    +article('Hello world')

    // renders as
    <div class="article">
        <div class="article-wrapper">
            <h1>Hello world</h1>
            <p>No content provided</p>
        </div>
    </div>

    // usage with content block
    +article('Hello world')
        p This is my
        p Amazing article
    
    // renders as
    <div class="article">
        <div class="article-wrapper">
            <h1>Hello world</h1>
            <p>This is my</p>
            <p>Amazing article</p>
        </div>
    </div>

## mixin also have an implicit `attributes` argument, taken from attributes passed to the mixin

    mixin link(href, name)
        a(class!=attributes.class href=href)= name
    
    +link('/foo', 'foo')(class="btn")

    // <a class="btn" href="/foo">foo</a>
