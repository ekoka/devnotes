https://dart.dev/guides/language/language-tour#typedefs

- typedefs are a type alias
- a concise way to refer to a type

    typedef IntList = List<Int>

    IntList il = [1, 2, 3];

- a `typedef` can have type parameters

    # declare typedef
    typedef ListMapper<X> = Map<X, List<X>>;

    # verbose declaration
    Map<String, List<String>> strListMap = {};

    # with the `ListMapper` typedef
    ListMapper<String> strListMap = {
        "foo": ["a", "b", "c"],
        "bar": ["z", "y", "x"],
    };

    ListMapper<int> intListMap = {
        1: [1,2,3],
        2: [10, 9, 8],
    }

- function typedefs

    typedef Compare<T> = int Function(T a, T b);

    int IntSort(int a, int b) => a - b;

    void main(){
        assert(IntSort is Compare);
    }
