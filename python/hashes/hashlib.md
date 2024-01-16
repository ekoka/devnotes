#### how to use

    import hashlib
    
    h = hashlib.md5()
    h.update("You can't ")
    h.update("handle the truth!")
    h.digest()
    # '\xbbd\x9c\x83\xdd\x1e ... \xe9'
    
    h.digest_size
    # 16

    h.block_size
    # 64


#### one-liner

    hashlib.md5("You can't handle the truth!").hexdigest()
    
- e.g. md5 of a file

    readme_hash = hashlib.md5(open('/path/to/readme.txt').read()).hexdigest()
    
#### algorithms

- constructor methods for each type of hash, all returning a hash object.

    md5()       
    sha1()      
    sha224()    
    sha256()
    sha384()
    sha512()

- other algorithms may be available (machine and OpenSSL lib dependent):

    h = hashlib.new('ripemd160')
    h.update("You can't handle the truth!")
    h.hexdigest()

- list of algorithms guaranteed to be supported

    hashlib.algorithms # (version 2.7)

#### digest methods

- digest string. may contain non-ascii characters, including null-bytes.

    d = h.digest()

- hexdigest strings similar to digest strings, but contain only hexdecimal digits.

    hd = h.hexdigest()

#### hash objects

- You can add text to the hash object

    h = hashlib.sha1()
    h.update("You can't ")
    h.update("handle the truth!")

- then you can call `digest()` or `hexdigest()` to see the hash of the concatenated message.

    h.digest()
    h.hexdigest()

- clone a hash object

    new_hash = old_hash.clone()

