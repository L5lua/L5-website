# windowResized()
 
A function that's called when the window is resized.

Code placed in the body of `windowResized()` will run when the window's size changes. 

## Examples

![windowResized example 1](assets/windowResized1.webp)

```lua

require("L5")

function setup()
  windowTitle("windowResized example")
  text("Welcome",width/2,height/2)
  textAlign(CENTER)

  describe('A default sized gray canvas with text "Welcome" at its center. When clicked to resize the text changes to say "Resized".')
end

function mousePressed()
  resizeWindow(200,200)
end

-- Called when window resized
function windowResized()
  text("Resized",width/2,height/2)
end
```

## Syntax

```lua
windowResized()
```

## Related

* [resizeWindow()](resizeWindow.md)
* [size()](size.md)
* [fullscreen()](fullscreen.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
