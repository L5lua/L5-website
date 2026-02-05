# keyReleased()
 
A function that's called once when any key is released.

Declaring the function `keyReleased()` sets a code block to run once automatically when the user releases any key:

```lua
function keyReleased() 
  -- Code to run.
end
```

The key variables will be updated with the most recently released value when `keyReleased()` is called by L5:

```lua
function keyReleased() 
  if key == 'c' then
    -- Code to run.
  end

  if key == 'return' then
    -- Code to run.
  end
end
```

## Examples

![keyReleased example 1](assets/keyPressed1.gif)

```lua
local value = 0

require("L5")

function setup()
  size(100, 100)

  describe(
    'A gray square with a black square at its center. The inner square changes color when the user releases a key.'
  )
end

function draw()
  background(200)

  -- Style the square.
  fill(value)

  -- Draw the square.
  square(25, 25, 50)
end

-- Toggle value when the user releases a key.
function keyReleased()
  if value == 0 then
    value = 255
  else 
    value = 0
  end
end
```

![keyReleased example 2](assets/keyReleased2.gif)

```lua
local value = 0

require("L5")

function setup()
  size(100, 100)

  describe(
    'A gray square with a black square at its center. The inner square becomes white when the user releases the "w" key.'
  )
end

function draw()
  background(200)

  -- Style the square.
  fill(value)

  -- Draw the square.
  square(25, 25, 50)
end

-- Set value to 255 the user releases the 'w' key.
function keyReleased()
  if key == 'w' then
    value = 255
  end
end
```

![keyRelease example 3](assets/keyReleased2.gif)

```lua
local value = 0

require("L5")

function setup()
  size(100, 100)

  describe(
    'A gray square with a black square at its center. The inner square turns white when the user presses and releases the left arrow key. It turns black when the user presses and releases the right arrow key.'
  )
end

function draw()
  background(200)

  -- Style the square.
  fill(value)

  -- Draw the square.
  square(25, 25, 50)
end

-- Toggle the background color when the user releases an arrow key.
function keyReleased()
  if key == 'left' then
    value = 255
  elseif key == 'right' then
    value = 0
  end
end
```

## Syntax

```lua
keyReleased()
```

## Related

* [key](key.md)
* [keyPressed()](keyPressed.md)
* [keyIsDown()](keyIsDown.md)
* [keyIsPressed](keyIsPressed.md)
* [keyTyped()](keyTyped.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
