# focused()
 
A `Boolean` variable that's `true` if the window is focused and `false` if not.

Note: The window can only receive input if it's focused.

## Examples

![focused example 1](assets/focused1.gif)

```lua
-- Open this example in two separate browser
-- windows placed side-by-side to demonstrate.

require("L5")

function setup()
  size(100, 100)

  describe('A square changes color from green to red when the window is out of focus.')
end

function draw()
  -- Change the background color
  -- when the window
  -- goes in/out of focus.
  if focused then
    background(0, 255, 0)
  else 
    background(255, 0, 0)
  end
end

```

## Related

* [cursor()](cursor.md)
* [mousePressed()](mousePressed.md)
* [mouseReleased()](mouseReleased.md)
* [keyPressed()](keyPressed.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
