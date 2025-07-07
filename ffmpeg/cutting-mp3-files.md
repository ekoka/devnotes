ref: https://askubuntu.com/questions/27574/how-can-i-split-a-mp3-file

### start time to end time:

    ffmpeg -i input.mp3 -vn -acodec copy -ss 00:00:00 -to 00:01:32 output.mp3

### start time + duration time:

    ffmpeg -i input.mp3 -vn -acodec copy -ss 00:00:00 -t 00:01:32 output.mp3

### start of record till end time:

    ffmpeg -i input.mp3 -vn -acodec copy -to 00:01:32 output.mp3

### start time till end of record:

    ffmpeg -i input.mp3 -vn -acodec copy -ss 00:01:32 output.mp3

one can also include milliseconds with e.g. `00:00:00.000`.
