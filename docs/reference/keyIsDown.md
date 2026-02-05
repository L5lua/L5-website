# keyIsDown()
 
Returns `true` if the key it’s checking is pressed and `false` if not.

`keyIsDown()` is helpful when checking for multiple different key presses. For example, `keyIsDown()` can be used to check if both `left` arrow and
`up` arrow are pressed:

```lua
if keyIsDown('left') and keyIsDown('up') then
  print('move diagonally')
end
```

## Examples

![keyIsDown example 1](assets/keyIsDown1.gif)

```lua
local x = 50
local y = 50

require("L5")

function setup()
  size(100, 100)

  background(200)

  describe(
    'A gray square with a black circle at its center. The circle moves when the user presses an arrow key. It leaves a trail as it moves.'
  )
end

function draw()
  -- Update x and y if an arrow key is pressed.
  if keyIsDown('left') == true then
    x = x - 1
  end

  if keyIsDown('right') == true then
    x = x + 1
  end

  if keyIsDown('up') == true then
    y = y - 1
  end

  if keyIsDown('down') == true then
    y = y + 1
  end

  -- Style the circle.
  fill(0)

  -- Draw the circle.
  circle(x, y, 5)
end

```

## Syntax

```lua
keyIsDown(keyname)
```

## Parameters

| Parameter |                                      |
| -         | --                                   |
| keyname   | String: keyname in quotes.           |


## Related

* [key](key.md)
* [keyPressed()](keyPressed.md)
* [keyReleased()](keyReleased.md)
* [keyIsPressed](keyIsPressed.md)
* [keyTyped()](keyTyped.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
