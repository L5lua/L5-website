# :seek()

Jumps to a specified time forward (in seconds) for playback. Calling `:seek()` multiple times on a video is additive.

**Note: Currently L5 can only play ogv (Ogg Theora) video files. Use an external program such as [Handbrake](https://handbrake.fr) or ffmpeg (command line) to convert mp4, avi, mkv, and mov codecs first.**

## Examples

```lua
require("L5")

function setup()
  windowTitle("loadVideo example")

  video = loadVideo("assets/heads.ogv")
  video:seek(2)
  video:play()

  describe("A basic example of loading a video, then jumping to 2 seconds in and beginning playback.")
end

function draw()
  background(51) 
  
  image(video, 0, 0, width, height)
end 
```

## Syntax

```lua
videofile:seek(time)
```

## Parameters

| Parameter |                                                                 |
| -         | --                                                              |
| time      | Number: number of seconds forward to move the playhead.         |


## Related

* [loadVideo()](loadVideo.md)
* [image()](image.md)
* [:loop()](video-loop.md)
* [:pause()](video-pause.md)
* [:play()](video-play.md)


