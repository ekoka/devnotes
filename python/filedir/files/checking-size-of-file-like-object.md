
### should work on all file-like objects    

    import os
    from io import BytesIO

    b = BytesIO()
    b.write(b'some file-like object')
    b.seek(0, os.SEEK_END)
    print(b.tell())
