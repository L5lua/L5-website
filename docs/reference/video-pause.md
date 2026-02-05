# :pause()

Pauses playing video file.

**Note: Currently L5 can only play ogv (Ogg Theora) video files. Use an external program such as [Handbrake](https://handbrake.fr) or ffmpeg (command line) to convert mp4, avi, mkv, and mov codecs first.**

## Examples

```lua
require("L5")

function setup()
  windowTitle("loadVideo example")

  video = loadVideo("assets/heads.ogv")
  video:loop()

  describe("A basic example of loading a video, then looping it playing by drawing frames in the draw loop until the user clicks to pause.")
end

function draw()
  background(51) 
  
  image(video, 0, 0, width, height)
end 

function draw()
  video:pause()
end
```

## Syntax

```lua
videofile:pause()
```

## Related

* [loadVideo()](loadVideo.md)
* [image()](image.md)
* [:loop()](video-loop.md)
* [:play()](video-play.md)
* [:seek()](video-seek.md)


