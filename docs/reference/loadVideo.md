# loadVideo()

Loads and returns a video file for simple audio/video playback.

**Note: Currently L5 can only play ogv (Ogg Theora) video files. Use an external program such as [Handbrake](https://handbrake.fr) or ffmpeg (command line) to convert mp4, avi, mkv, and mov codecs first.**

*Differences from Processing and p5.js*: Processing requires a separate Video library but can work with more codecs. p5.js requires creating a DOM Video element separate from the canvas and playing once loaded asyncronously. L5's load and play functions are simple and syncronous.

## Examples

![loadVideo example 1](assets/loadVideo1.webp)

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
loadVideo(file)
```

## Related

* [pause()](video-pause.md)
* [play()](video-play.md)
* [stop()](video-stop.md)

---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
