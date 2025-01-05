### Year

    Code    Example 	        Description
    %y 	    13 	                Year without century as a zero-padded decimal number.
    %Y 	    2013 	            Year with century as a decimal number.
    
### Month

    Code    Example 	        Description
    %b 	    Sep 	            Month as locale’s abbreviated name.
    %B 	    September 	        Month as locale’s full name.
    %m 	    09 	                Month as a zero-padded decimal number.
    %-m 	9 	                Month as a decimal number. (Platform specific)
    
### Day

    Code    Example 	        Description
    %a 	    Sun 	            Weekday as locale’s abbreviated name.
    %A 	    Sunday 	            Weekday as locale’s full name.
    %w 	    0 	                Weekday as a decimal number, where 0 is Sunday and 6 is Saturday.
    %d 	    08 	                Day of the month as a zero-padded decimal number.
    %-d     8 	                Day of the month as a decimal number. (Platform specific)
    %j 	    251 	            Day of the year as a zero-padded decimal number.
    %-j     251 	            Day of the year as a decimal number. (Platform specific)
    
### Hour

    Code    Example 	        Description
    %H 	    07 	                Hour (24-hour clock) as a zero-padded decimal number.
    %-H 	j7 	                Hour (24-hour clock) as a decimal number. (Platform specific)
    %I 	    07 	                Hour (12-hour clock) as a zero-padded decimal number.
    %-I 	7 	                Hour (12-hour clock) as a decimal number. (Platform specific)

### Minute

    Code    Example 	        Description
    %M 	    06 	                Minute as a zero-padded decimal number.
    %-M 	6 	                Minute as a decimal number. (Platform specific)
### Second

    Code    Example 	        Description
    %S 	    05 	                Second as a zero-padded decimal number.
    %-S 	5 	                Second as a decimal number. (Platform specific)

### Microsecond

    Code    Example 	        Description
    %f 	    000000 	            Microsecond as a decimal number, zero-padded to 6 digits.

### AM/PM

    Code    Example 	        Description
    %p 	    AM 	                Locale’s equivalent of either AM or PM.

### UTC offset and timezone

    Code    Example 	Description
    %z 	    +0000 	    UTC offset in the form ±HHMM[SS[.ffffff]] (empty string if the object is naive).
    %Z 	    UTC 	    Time zone name (empty string if the object is naive).

### Localized

    Code    Example 	                Description
    %c 	    Sun Sep 8 07:06:05 2013 	Locale’s appropriate date and time representation.
    %x 	    09/08/13 	                Locale’s appropriate date representation.
    %X 	    07:06:05 	                Locale’s appropriate time representation.

### Literals

    Code    Example 	Description
    %% 	    % 	        A literal '%' character.
