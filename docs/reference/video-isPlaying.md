# :isPlaying()

Returns a boolean `true` or `false` depending on whether named video file is currently playing.

**Note: Currently L5 can only play ogv (Ogg Theora) video files. Use an external program such as [Handbrake](https://handbrake.fr) or ffmpeg (command line) to convert mp4, avi, mkv, and mov codecs first.**

## Examples

```lua
require("L5")

function setup()
  windowTitle("loadVideo example")

  video = loadVideo("assets/heads.ogv")
  video:play()

  describe("A basic example of loading a video, then playing it by drawing frames in the draw loop. When the user clicks it reports whether the video is currently playing or has stopped.")
end

function draw()
  background(51) 
  
  image(video, 0, 0, width, height)
end 

function mousePressed()
  if video:isPlaying() then
    print("Video playing.")
  else
    print("Video stopped.")
  end
end
```

## Syntax

```lua
videofile:isPlaying()
```

## Returns

Boolean: 'true' or 'false' depending on current status of video file playing

## Related

* [loadVideo()](loadVideo.md)
* [image()](image.md)
* [:loop()](video-loop.md)
* [:pause()](video-pause.md)
* [:seek()](video-seek.md)

