# key()
 
A `String` system variable that contains the value of the last key typed.

The key variable is helpful for checking whether a key has been typed. For example, the expression `key == 'a'` evaluates to `true` if the `a` key was typed and `false` if not. 

**Unlike p5.js and Processing, `key` *does* update for special keys such as `left` (left arrow), `return` (Enter key), `lshift` (left shift key), function keys, etc.**

The keyIsDown() function should be used to check for multiple different key presses at the same time.

## Examples

![key example 1](assets/key1.gif)

```lua
require("L5")

function setup()
  size(100, 100)

  describe(
    'A gray square. The last key pressed is displayed at the center.'
  )
end

function draw()
  background(200)
  fill(0)

  -- Style the text.
  textAlign(CENTER)
  textSize(16)

  -- Display the last key pressed.
  text(key, 50, 50)
end
```

![key example 2](assets/key2.gif)

```lua
local x = 50
local y = 50

require("L5")

function setup()
  size(100, 100)

  background(200)

  describe(
    'A gray square with a black circle at its center. The circle moves when the user presses the keys "w", "a", "s", or "d". It leaves a trail as it moves.'
  )
end

function draw()
  -- Update x and y if a key is pressed.
  if keyIsPressed == true then
    if key == 'w' then
      y = y - 1
    elseif key == 's' then
      y = y + 1
    elseif key == 'a' then
      x = x - 1
    elseif key == 'd' then
      x = x + 1
    end
  end

  -- Style the circle.
  fill(0)

  -- Draw the circle at (x, y).
  circle(x, y, 5)
end
```

## Related

* [keyPressed()](keyPressed.md)
* [keyIsPressed](keyIsPressed.md)
* [keyReleased()](keyReleased.md)
* [keyIsDown()](keyIsDown.md)
* [keyTyped()](keyTyped.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
