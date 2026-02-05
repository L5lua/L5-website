# mouseIsPressed()
 
A `Boolean` system variable that's `true` if the mouse is pressed and
`false` if not.

## Examples

![mouseIsPressed example 1](assets/mouseIsPressed1.gif)

```lua
require("L5")

function setup()
  size(100, 100)

  describe(
    'A gray square with the word "false" at its center. The word changes to "true" when the user presses a mouse button.'
  )
end

function draw()
  background(200)
  fill(0)

  -- Style the text.
  textAlign(CENTER)
  textSize(16)

  -- Display the mouseIsPressed variable.
  text(mouseIsPressed, 25, 50)
end
```

![mouseIsPressed example 2](assets/keyPressed1.gif)

```lua
require("L5")

function setup()
  size(100, 100)

  describe(
    'A gray square with a white square at its center. The inner square turns black when the user presses the mouse.'
  )
end

function draw()
  background(200)

  -- Style the square.
  if mouseIsPressed == true then
    fill(0)
  else 
    fill(255)
  end

  -- Draw the square.
  square(25, 25, 50)
end
```

## Syntax

```lua
mouseIsPressed
```

## Returns

Boolean: true or false.

## Related

* [mouseButton](mouseButton.md)
* [mouseWheel()](mouseWheel.md)
* [mouseMoved()](mouseMoved.md)
* [mouseDragged()](mouseDragged.md)
* [mouseX](mouseX.md)
* [mouseY](mouseY.md)
* [movedX](movedX.md)
* [movedY](movedY.md)
* [pmouseX](pmouseX.md)
* [pmouseY](pmouseY.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
