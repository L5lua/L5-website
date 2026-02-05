# mouseReleased()

A function that's called once when a mouse button is released.

Declaring the function `mouseReleased()` sets a code block to run automatically when the user releases a mouse button after having pressed it:

```lua
function mouseReleased() 
  -- Code to run.
end
```

The mouse system variables, such as mouseX and mouseY, will be updated with their most recent value when `mouseReleased()` is called by L5:

```lua
function mouseReleased() 
  if mouseX < 50 then
    -- Code to run if the mouse is on the left.
  end

  if mouseY > 50 then
    -- Code to run if the mouse is near the bottom.
  end
end
```

Note: mousePressed(), `mouseReleased()`, and mouseClicked() are all related. mousePressed() runs as soon as the user clicks the mouse. `mouseReleased()` runs as soon as the user releases the mouse click. mouseClicked() runs immediately after `mouseReleased()`.

## Examples

![mouseReleased example 1](assets/mousePressed1.gif)

```lua
local value = 0

require("L5")

function setup()
  size(100, 100)

  describe(
    'A gray square with a black square at its center. The inner square becomes lighter when the user presses and releases a mouse button.'
  )
end

function draw()
  background(200)

  -- Style the square.
  fill(value)

  -- Draw the square.
  square(25, 25, 50)
end

function mouseReleased()
  -- Update the grayscale value.
  value = value + 5

  -- Reset the grayscale value.
  if value > 255 then
    value = 0
  end
end
```

![mouseReleased example 2](assets/mouseClicked2.gif)

```lua
require("L5")

function setup()
  size(100, 100)

  -- Style the circle.
  fill('orange')
  stroke('royalblue')
  strokeWeight(10)

  describe(
    'An orange circle with a thick, blue border drawn on a gray background. When the user presses and holds the mouse, the border becomes thin and pink. When the user releases the mouse, the border becomes thicker and changes color to blue.'
  )
end

function draw()
  background(220)

  -- Draw the circle.
  circle(50, 50, 20)
end

-- Set the stroke color and weight as soon as the user clicks.
function mousePressed()
  stroke('deeppink')
  strokeWeight(3)
end

-- Set the stroke and fill colors as soon as the user releases
-- the mouse.
function mouseReleased()
  stroke('royalblue')

  -- This is never visible because fill() is called
  -- in mouseClicked() which runs immediately after
  -- mouseReleased()
  fill('limegreen')
end

-- Set the fill color and stroke weight after
-- mousePressed() and mouseReleased() are called.
function mouseClicked()
  fill('orange')
  strokeWeight(10)
end
```

## Syntax

```lua
mouseReleased()
```

## Related

* [mouseButton](mouseButton.md)
* [mousePressed()](mousePressed.md)
* [mouseClicked()](mouseClicked.md)
* [mouseIsPressed](mouseIsPressed.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
