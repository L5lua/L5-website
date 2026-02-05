# :stop()

Stops playing video file and rewinds to start.

**Note: Currently L5 can only play ogv (Ogg Theora) video files. Use an external program such as [Handbrake](https://handbrake.fr) or ffmpeg (command line) to convert mp4, avi, mkv, and mov codecs first.**

## Examples

```lua
-- Create the global variables: playing, video, and buttonText.
-- Set playing to false so the video loads in as paused.
local playing = false
local video
local buttonText = 'play'

require("L5")

function setup()
  size(400,400)
  windowTitle('Video player')

  -- for styling our button
  textAlign(CENTER, CENTER)

  -- Upload the video in the assets directory, and
  -- use the loadVideo() function to load in the video to the code.
  video = loadVideo('assets/fingers.ogv')
  video:play()
  
  describe("Plays a video file on start. Pressing the mouse stops the video, or starts it again from the beginning.")
end

function draw()
  image(video, 0, 0, width, height)
 -- apply grayscale filter
  filter(GRAY)
end

function mousePressed()
  if video:isPlaying() then
    video:stop()
  else
    video:play()
  end
end
```

## Syntax

```lua
videofile:stop()
```

## Related

* [loadVideo()](loadVideo.md)
* [image()](image.md)
* [:loop()](video-loop.md)
* [:pause()](video-pause.md)
* [:play()](video-play.md)
* [:seek()](video-seek.md)


