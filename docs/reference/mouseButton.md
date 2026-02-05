# mouseButton
 
A String system variable that contains the value of the last mouse button pressed.

The `mouseButton` variable is either `LEFT`, `RIGHT`, or `CENTER`, depending on which button was pressed last.

*Note that the mouse must be pressed on the window to be detected and reported.*

## Examples

![mouseButton example 1](assets/mouseButton1.webp)

```lua
-- Click on the window to detect the mouseButton
require("L5")

function setup()
  size(100, 100)

  describe(
    'A gray square. Black text appears and changes to either "left" or "right" when the user clicks a mouse button on the window.'
  )
end

function draw()
  background(200)
  fill(0)

  -- Style the text.
  textAlign(CENTER)
  textSize(16)

  -- Display the mouse button.
  text(mouseButton, 50, 50)
end
```

![mouseButton example 2](assets/mouseButton2.gif)

```lua
require("L5")

function setup()
  size(100, 100)

  describe(
    "A gray square. Different shapes appear at its center depending on the mouse button that's clicked."
  )
end

function draw() 
  background(200)

  if mouseIsPressed == true  then
    if mouseButton == LEFT then
      circle(50, 50, 50)
    end
    if mouseButton == RIGHT then
      square(25, 25, 50)
    end
    if mouseButton == CENTER then
      triangle(23, 75, 50, 20, 78, 75)
    end
  end
end
```

## Syntax

```lua
mouseButton
```

## Returns

STRING: Either, LEFT ('left'), CENTER ('center') or RIGHT ('right')

## Related

* [mouseClicked()](mouseClicked.md)
* [mouseMoved()](mouseMoved.md)
* [mousePressed()](mousePressed.md)
* [mouseReleased()](mouseReleased.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
