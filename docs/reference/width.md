# width
 
A `Number` variable that stores the width of the canvas in pixels.

`width`'s default value is 100. Calling `size()` or
`resizeWindow()` changes the value of
`width`. 

## Examples

![width example 1](assets/width1.webp)

```lua
require("L5")

function setup()
  size(100, 100)
  background(200)

  -- Display the canvas' width.
  text(width, 42, 54)

  describe('The number 100 written on a gray square.')
end
```

## Syntax

```lua
width
```

## Related

* [height](height.md)
* [size()](size.md)
* [displayWidth](displayWidth.md)
* [displayHeight](displayHeight.md)
* [fullscreen()](fullscreen.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
