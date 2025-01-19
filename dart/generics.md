https://dart.dev/guides/language/language-tour#generics

### Restricting generic types

- make the type non-nullable by explicitly extending `Object` (the default is `Object?`)

    class Foo<T extends Object> {
    }

- restrict the type to a family of subtypes

    class Foo<T extends SomeBaseClass> { ... }

    class Extender extends SomeBaseClass { ... }

- you can then

    // with the base class
    final obj = Foo<SomeBaseClass>();
    // with the extended class
    final obj = Foo<Extender>();
    // or without the type
    final obj = Foo();

### Generic methods

- syntax

    T func<T> (T var, ...) {
        T foo = T();
    }

- the generic type parameter on `func<T>` allows to use the type in several places:
    - in the types of arguments 
    - within the function body
    - in the return value declaration
