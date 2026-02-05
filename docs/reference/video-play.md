# :play()

Plays a movie one time and stops at the last frame.

**Note: Currently L5 can only play ogv (Ogg Theora) video files. Use an external program such as [Handbrake](https://handbrake.fr) or ffmpeg (command line) to convert mp4, avi, mkv, and mov codecs first.**

## Examples

```lua
require("L5")

function setup()
  windowTitle("loadVideo example")

  video = loadVideo("assets/heads.ogv")
  video:play()

  describe("A basic example of loading a video, then playing it by drawing frames in the draw loop")
end

function draw()
  background(51) 
  
  image(video, 0, 0, width, height)
end 
```

## Syntax

```lua
videofile:play()
```

## Related

* [loadVideo()](loadVideo.md)
* [image()](image.md)
* [:loop()](video-loop.md)
* [:pause()](video-pause.md)
* [:seek()](video-seek.md)


