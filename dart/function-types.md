- syntax

    returnType Function([paramType1 [, paramType2...]])

- async function types

    Future[<FutureParamType1 [, FutureParamType2 ...]] 
        Function([FunctionParamType1 [, FunctionParamType2 ...]])
    
- prefer inline function types over typedefs

- if function type is particularly long or frequently used, it might be worth defining a type. 

- for parameter prefer the inline function type syntax

    # Dart 1: 
    Iterable<T> where(bool foo(T element)) => ...

    # Dart 2: verbose syntax, but consistent with other places where it must thusly be used
    Iterable<T> where(bool Function(T) foo) => ...
    
- function typedefs

    typedef Compare<T> = int Function(T a, T b);

    int IntSort(int a, int b) => a - b;

    void main(){
        assert(IntSort is Compare);
    }

