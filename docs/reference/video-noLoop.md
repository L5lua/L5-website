# :noLoop()

Changes video playback to only play once and then stop.

**Note: Currently L5 can only play ogv (Ogg Theora) video files. Use an external program such as [Handbrake](https://handbrake.fr) or ffmpeg (command line) to convert mp4, avi, mkv, and mov codecs first.**

## Examples

```lua
require("L5")

function setup()
  windowTitle("loadVideo example")

  video = loadVideo("assets/heads.ogv")
  video:loop()

  describe("A basic example of loading a video, then playing it by drawing frames in the draw loop until the user stops it from looping with a mouse press.")
end

function draw()
  background(51) 
  
  image(video, 0, 0, width, height)
end 

function mousePressed()
  --Click on the window will change from looping to only play once and then stopping
  video:noLoop()
end
```

## Syntax

```lua
videofile:noLoop()
```

## Related

* [loadVideo()](loadVideo.md)
* [image()](image.md)
* [:loop()](video-loop.md)
* [:pause()](video-pause.md)
* [:play()](video-play.md)
* [:seek()](video-seek.md)


