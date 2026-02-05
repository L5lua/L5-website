# keyIsPressed()
 
A boolean variable that's `true` if any key is currently pressed and `false` if not.

## Examples

![keyIsPressed example 1](assets/keyPressed1.gif)

```lua
require("L5")

function setup()
  size(100, 100)

  describe(
    'A gray square with a white square at its center. The white square turns black when the user presses a key.'
  )
end

function draw()
  background(200)

  -- Style the square.
  if keyIsPressed == true then
    fill(0)
  else 
    fill(255)
  end

  -- Draw the square.
  square(25, 25, 50)
end
```

![keyIsPressed example 2](assets/keyPressed1.gif)

```lua
require("L5")

function setup()
  size(100, 100)

  describe(
    'A gray square with a white square at its center. The white square turns black when the user presses a key.'
  )
end

function draw()
  background(200)

  -- Style the square.
  if keyIsPressed then
    fill(0)
  else 
    fill(255)
  end

  -- Draw the square.
  square(25, 25, 50)
end
```

![keyIsPressed example 3](assets/keyIsPressed3.gif)

```lua
require("L5")

function setup()
  size(100, 100)

  describe(
    'A gray square with the word "false" at its center. The word switches to "true" when the user presses a key.'
  )
end

function draw()
  background(200)
  fill(0)

  -- Style the text.
  textAlign(CENTER)
  textSize(16)

  -- Display the value of keyIsPressed.
  text(keyIsPressed, 50, 50)
end
```

## Syntax

```lua
keyIsPressed
```

## Related

* [key](key.md)
* [keyPressed()](keyPressed.md)
* [keyReleased()](keyReleased.md)
* [keyIsDown()](keyIsDown.md)
* [keyTyped()](keyTyped.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
