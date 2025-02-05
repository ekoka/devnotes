    class SomeObject {
        final Object a, b, c;

        SomeObject(this.a, this.b, this.c);

        bool operator ==(Object other) =>
            other is SomeObject 
            && a==other.a 
            && b==other.b 
            && c==other.c;
        
    }
