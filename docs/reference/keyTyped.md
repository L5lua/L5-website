# keyTyped()
 
A function that's called once when keys with printable characters are pressed.

Declaring the function `keyTyped()` sets a code block to run once automatically when the user presses any key with a printable character such as `a` or `1`.

```lua
function keyTyped()
  -- Code to run
end
```

The key variable will be updated with the most recently released value when `keyTyped()` is called by L5:

```lua
function keyTyped() 
  -- Check for the "c" character using key.
  if key == 'c' then
    -- Code to run.
  end
end
```

## Examples

![keyTyped example 1](assets/keyPressed1.gif)

```lua
require("L5")

function setup()
  size(100, 100)

  describe(
    'A gray square with a white square at its center. The inner square changes color when the user presses a key.'
  )
end

function draw()
  background(200)

  -- Style the square.
  fill(value)

  -- Draw the square.
  square(25, 25, 50)
end

-- Toggle the square's color when the user types a printable key.
function keyTyped()
  if value == 0 then
    value = 255
  else 
    value = 0
  end
end
```

![keyTyped example 2](assets/keyPressed1.gif)

```lua
local value = 0

require("L5")

function setup()
  size(100, 100)

  describe(
    'A gray square with a white square at its center. The inner square turns black when the user types the "b" key. It turns white when the user types the "a" key.'
  )
end

function draw()
  background(200)

  -- Style the square.
  fill(value)

  -- Draw the square.
  square(25, 25, 50)
end

-- Reassign value when the user types the 'a' or 'b' key.
function keyTyped()
  if key == 'a' then
    value = 255
  elseif key == 'b' then
    value = 0
  end
end
```

## Syntax

```
keyTyped()
```

## Related

* [key](key.md)
* [keyPressed()](keyPressed.md)
* [keyIsDown()](keyIsDown.md)
* [keyReleased()](keyReleased.md)
* [keyIsPressed](keyIsPressed.md)



---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
