# month()
 
Returns the current month as a number from 1–12.

## Examples

![month example 1](assets/month1.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(200)
  fill(0)

  -- Get the current month.
  local m = month()

  -- Style the text.
  textAlign(LEFT, CENTER)
  textSize(12)

  -- Display the month.
  text('Current month: '..m, 10, 50, 80)

  describe('The text "Current month: '..m..'" written in black on a gray background.')
end
```

## Returns

Integer: current month between 1 and 12.

## Related

* [year()](year.md)
* [day()](day.md)
* [hour()](hour.md)
* [minute()](minute.md)
* [second()](second.md)



---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
