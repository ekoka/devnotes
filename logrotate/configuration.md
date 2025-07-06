- comments may appear anywhere in the config file as long as the first 
non-space character on the line is `#`.


- local configurations override global ones

    # global
    compress
    weekly

    /var/log/messages {
        # local config overrides global weekly rotation
        daily
    }

### multiple paths. 

    
    "/var/log/httpd/access.log" /var/log/httpd/error.log {
        ...
    }

- Wildcards `*` must be used with caution, as any files it matches is rotated, including already rotated ones. It's recommended to use them in conjunction with `olddir` or in a format that makes the match more specific e.g. `*.log`. 

    /var/log/news/* {
        ...
        # place old files here
        olddir /var/log/news/old
    }
    
    ~/log/*.log {
        ...
    }



# Some config options of interest


### `rotate`

    # remove log after 5 weekly rotations   
    rotate 5 
    weekly
    
### `weekly`, `daily`, `monthly`, etc

### `create`



### `compress`
    # compress old versions of the file (with gzip by default) 

### `postrotate`
- execute `<command>` after rotation, but before `compress`
    postrotate
        <command>

### `size` 

    # rotate when larger than 100k
    size 100k
   
### `mail` 
    # mail old file to recipient (instead of deleting them) after going through 5 rotations
    
    rotate 5
    mail recipient@example.org

### 
 

    
