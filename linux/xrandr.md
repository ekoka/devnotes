## List allowed resolutions 
    
    $ xrandr

    Screen 0: minimum 320 x 200, current 1440 x 810, maximum 8192 x 8192
    eDP-1 connected primary 1440x810+0+0 (normal left inverted right x axis y axis) 293mm x 165mm
    1920x1080     60.00 +  59.97    59.96    59.93  
    1680x1050     59.95    59.88  
    1600x1024     60.17  
    1400x1050     59.98  

Where "eDP-1" would be the name of the display.

## Apply one of the listed resolutions

    $ xrandr -s 1600x900

## Add a new mode

- first calculate the CVT of the desired (and supported) resolution

    $ cvt 1600 900 60
    # 1600x900 59.95 Hz (CVT 1.44M9) hsync: 55.99 kHz; pclk: 118.25 MHz
    Modeline "1600x900_60.00"  118.25  1600 1696 1856 2112  900 903 908 934 -hsync +vsync

- then add the above cvt mode by copying everything starting at the double quotes until the end of the line and run with `xrandr --newmode`
    

    $ xrandr --newmode "1600x900_60.00"  118.25  1600 1696 1856 2112  900 903 908 934 -hsync +vsync

- finally, add the new mode to "eDP-1" display 

    $ xrandr --addmode eDP-1 "1920x1080_60.00"

- the counterpart of the `--addmode` command is `--delmode`, thus removing the mode just added would simply be

    $ xrandr --delmode eDP-1 "1920x1080_60.00"

- the resolution is not kept after logout. If you wish to make it permanent you may want to add the two commands that create the new mode and add it to the display in a script that gets called by your .profile script.

    # e.g. ~/edp-1-1920x1080

    xrandr --newmode "1600x900_60.00"  118.25  1600 1696 1856 2112  900 903 908 934 -hsync +vsync
    xrandr --addmode eDP-1 "1920x1080_60.00"

