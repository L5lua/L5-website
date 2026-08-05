# :getHeight()

Returns height of the named loaded image or video.

**Note: Currently L5 can only work with ogv (Ogg Theora) video files. Use an external program such as [Handbrake](https://handbrake.fr) or ffmpeg (command line) to convert mp4, avi, mkv, and mov codecs first.**

## Examples

![image :getWidth() example 1](assets/loadImage1.webp)

```lua
local img
require("L5")

function setup()
  size(100, 100)
  windowTitle('image :getWidth() example')
  
  -- Load the image
  img = loadImage('assets/flower.jpg')
  -- Draw the image.
  image(img, 0, 0, width, height)
  -- Print the width of the image source, not the window
  print(img:getWidth())

  describe('Image of a pink flower in bloom.')
end
```

Video :getWidth() Example 


```lua
require("L5")

function setup()
  windowTitle("loadVideo example")

  video = loadVideo("assets/heads.ogv")
  
  -- get the video file's pixel height
  print(video:getHeight())
  
  video:play()

  describe("A basic example of loading a video, then playing it by drawing frames in the draw loop. Prints video height.")
end

function draw()
  background(51) 
  
  image(video, 0, 0, width, height)
end 
```

## Syntax

```lua
image:getHeight()
```

```lua
video:getHeight()
```

## Returns

Number: height of image or video file

## Related

* [loadImage()](loadImage.md)
* [loadVideo()](loadVideo.md)
* [image()](image.md)
* [:getWidth()](media-getWidth.md)


