# :getWidth()

Returns width of the named loaded video file.

**Note: Currently L5 can only work with ogv (Ogg Theora) video files. Use an external program such as [Handbrake](https://handbrake.fr) or ffmpeg (command line) to convert mp4, avi, mkv, and mov codecs first.**

## Examples

```lua
require("L5")

function setup()
  windowTitle("loadVideo example")

  video = loadVideo("assets/heads.ogv")
  
  -- get the video file's pixel width
  print(video:getWidth())
  
  video:play()

  describe("A basic example of loading a video, then playing it by drawing frames in the draw loop. Prints video width.")
end

function draw()
  background(51) 
  
  image(video, 0, 0, width, height)
end 
```

## Syntax

```lua
videofile:getWidth()
```

## Returns

Number: width of video file

## Related

* [loadVideo()](loadVideo.md)
* [image()](image.md)
* [:getHeight()](video-getHeight.md)
* [:loop()](video-loop.md)
* [:pause()](video-pause.md)
* [:seek()](video-seek.md)


