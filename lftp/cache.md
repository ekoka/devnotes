
### Syntax

    cache [subcommand]


### Subcommands

- print status (default command)

    ~> cache status

    // or 

    ~> cache

- turn cache on/off

    ~> cache on

- flush cache

    ~> cache flush

- set memory limit (in bytes)

    // 200,000 bytes
    ~> cache size 2000000

    // unlimited
    ~> cache size -1

- set expiration time 

    // to 300 seconds
    ~> cache expire 300s 

    // to 10 minutes
    ~> cache expire 10m 

    // to 2 hours
    ~> cache expire 2h 

    // to 5 days
    ~> cache expire 5d 
