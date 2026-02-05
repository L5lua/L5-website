# day()
 
Returns the current day as a number from 1–31.

## Examples

![day example 1](assets/day1.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(200)
  fill(0)

  -- Get the current day.
  local d = day()

  -- Style the text.
  textAlign(LEFT, CENTER)
  textSize(12)

  -- Display the day.
  text("Current day: "..d, 20, 50, 60)

  describe('The text "Current day: '..d..'" written in black on a gray background.')
end

```

## Returns

Integer: current day between 1 and 31.

## Related

* [year()](year.md)
* [month()](month.md)
* [minute()](minute.md)
* [hour()](hour.md)
* [second()](second.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
