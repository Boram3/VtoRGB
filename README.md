# VtoRGB
Simple script from video to RGB frame binaries.  
Tested on Linux.

# Requirements
- ffmpeg
- python

# Example
This is how you would split bmps from a video
```py
import VtoRGB

WIDTH = 300
HEIGHT = 400

VtoRGB.vtobmps(
    "/your/absolute/path/to/video.mp4"
    , "/your/absolute/directory/to/output/"
    , WIDTH, HEIGHT
)
```


This is how you would glue splited bmps to one binary.
```py
import VtoRGB

VtoRGB.bmptobin(
    "/your/absolute/directory/to/workaround"
    , "/your/absolute/path/to/output/file"
)
```


This is how you would do this all once.
```py
import VtoRGB

VtoRGB.vtobin(
        "/your/absolute/path/to/video.mp4"          # Video
        , "/your/absolute/directory/to/workaround/"  # Where bmps stored
        , "/your/absolute/path/to/output/file"      # output file path
        )
```
