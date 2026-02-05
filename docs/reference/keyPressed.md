# keyPressed()
 
A function that's called once when any key is pressed.

Declaring the function `keyPressed()` sets a code block to run once automatically when the user presses any key:

```lua
function keyPressed()
  -- Code to run
end
```

The key variable will be updated with the most recently typed value when `keyPressed()` is called by L5:

```lua
function keyPressed() 
  if key == 'c' then
    -- Code to run.
  end

  if key == 'return' then
    -- Code to run.
  end
end
```

## Examples

![keyPressed example 1](assets/keyPressed1.gif)

```lua
local value = 0

require("L5")

function setup()
  size(100, 100)

  describe(
    'A gray square with a black square at its center. The inner square changes color when the user presses a key.'
  )
end

function draw()
  background(200)

  -- Style the square.
  fill(value)

  -- Draw the square.
  square(25, 25, 50)
end

-- Toggle the background color when the user presses a key.
function keyPressed()
  if value == 0 then
    value = 255
  else 
    value = 0
  end
end
```

![keyPressed example 2](assets/keyPressed1.gif)

```lua
local value = 0

require("L5")

function setup()
  size(100, 100)

  describe(
    'A gray square with a white square at its center. The inner square turns black when the user presses the "b" key. It turns white when the user presses the "a" key.'
  )
end

function draw()
  background(200)

  -- Style the square.
  fill(value)

  -- Draw the square.
  square(25, 25, 50)
end

-- Reassign value when the user presses the 'a' or 'b' key.
function keyPressed()
  if key == 'a' then
    value = 255
  elseif key == 'b' then
    value = 0
  end
end
```

![keyPressed example 3](assets/keyPressed1.gif)

```lua
local value = 0

require("L5")

function setup()
  size(100, 100)

  describe(
    'A gray square with a black square at its center. The inner square turns white when the user presses the left arrow key. It turns black when the user presses the right arrow key.'
  )
end

function draw()
  background(200)

  -- Style the square.
  fill(value)

  -- Draw the square.
  square(25, 25, 50)
end

-- Toggle the background color when the user presses an arrow key.
function keyPressed()
  if key == 'left' then
    value = 255
  elseif key == 'right' then
    value = 0
  end
end
```

## Syntax

```lua
keyPressed()
```

## Related

* [key](key.md)
* [keyIsDown()](keyIsDown.md)
* [keyReleased()](keyReleased.md)
* [keyIsPressed](keyIsPressed.md)
* [keyTyped()](keyTyped.md)



---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
