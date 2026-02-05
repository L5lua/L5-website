# :volume()

Sets the video volume.

Using the `:volume()` method on a video without an argument returns the current volume as a number in the range 0 (off) to 1 (maximum). 

The parameter, `vol`, is optional. It's a number that sets the volume from 0 (off) to 1 (maximum). For example, calling `video:volume(0.5)` sets the volume to half of its maximum.

**Note: Currently L5 can only play ogv (Ogg Theora) video files. Use an external program such as [Handbrake](https://handbrake.fr) or ffmpeg (command line) to convert mp4, avi, mkv, and mov codecs first.**

## Examples

```lua
require("L5")

function setup()
  windowTitle("loadVideo example")

  video = loadVideo("assets/heads.ogv")
  video:loop()

  describe("A basic example of playing a looping video. The volume playback is dependent on the mouse's horizontal position within the window. Pressing the mouse prints current volume level between 0 and 1.")
end

function draw()
  background(51) 

  -- map vol to mouse position within window
  local vol = map(mouseX,0,width,0,1)
  video:volume(vol)
  
  image(video, 0, 0, width, height)
end 

function mousePressed()
  print("volume: "..video:volume())
end
```

## Syntax

```lua
videofile:volume(level)
```

```lua
videofile:volume()
```

## Parameters

| Parameter |                                                                     |
| -         | --                                                                  |
| vol       | Number: number between 0 and 1 to specify total volume of video.    |


## Returns

Number: Total seconds since start of playback.

## Related

* [loadVideo()](loadVideo.md)
* [image()](image.md)
* [:loop()](video-loop.md)
* [:pause()](video-pause.md)
* [:play()](video-play.md)
* [:seek()](video-seek.md)
* [:time()](video-time.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*'
