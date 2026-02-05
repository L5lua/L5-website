# :time()

Reports current playback position in seconds. 

With specified number argument jumps to a specified time forward (in seconds) for playback, similar to [:seek()](video-seek.md). Unlike `seek()`, calling `:time()` multiple times on a video is not additive.

**Note: Currently L5 can only play ogv (Ogg Theora) video files. Use an external program such as [Handbrake](https://handbrake.fr) or ffmpeg (command line) to convert mp4, avi, mkv, and mov codecs first.**

## Examples

```lua
require("L5")

function setup()
  windowTitle("loadVideo example")

  video = loadVideo("assets/heads.ogv")
  video:play()

  describe("A basic example of loading a video, then beginning playback. Pressing the mouse returns total time since start of playback.")
end

function draw()
  background(51) 
  
  image(video, 0, 0, width, height)
end 

function mousePressed()
  print("Time since start "..video:time())
end
```

## Syntax

```lua
videofile:time(time)
```

```lua
videofile:time()
```

## Parameters

| Parameter |                                                                     |
| -         | --                                                                  |
| time      | Number: number of seconds from start of video to move the playhead. |


## Returns

Number: Total seconds since start of playback.

## Related

* [loadVideo()](loadVideo.md)
* [image()](image.md)
* [:loop()](video-loop.md)
* [:pause()](video-pause.md)
* [:play()](video-play.md)
* [:seek()](video-seek.md)


