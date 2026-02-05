# millis()
 
Returns the number of milliseconds since a sketch started running.

`millis()` keeps track of how long a sketch has been running in milliseconds (thousandths of a second). This information is often helpful for timing events and animations.

## Examples

![millis example 1](assets/millis1.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(200)
  fill(0)

  -- Get the number of milliseconds the sketch has run.
  local ms = millis()

  -- Style the text.
  textAlign(LEFT, CENTER)
  textSize(10)

  -- Display how long it took setup() to be called.
  text('Startup time: '..round(ms, 2)..'ms', 5, 50, 90)

  describe(
    'The text "Startup time: '..round(ms, 2)..'ms" written in black on a gray background.'
  )
end
```

![millis example 2](assets/millis2.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  describe('The text "Running time: S sec" written in black on a gray background. The number S increases as the sketch runs.')
end

function draw()
  background(200)
  fill(0)

  -- Get the number of seconds the sketch has run.
  local s = millis() / 1000

  -- Style the text.
  textAlign(LEFT, CENTER)
  textSize(10)

  -- Display how long the sketch has run.
  text('Running time: \n'..str(round(s,1))..' sec', 5, 50, 90)
end
```

![millis example 3](assets/millis3.gif)

```lua
require("L5")

function setup()
  size(100, 100)

  describe('A white circle oscillates left and right on a gray background.')
end

function draw()
  background(200)

  -- Get the number of seconds the sketch has run.
  local s = millis() / 1000

  -- Calculate an x-coordinate.
  local x = 30 * sin(s) + 50

  -- Draw the circle.
  circle(x, 50, 30)
end
```

## Returns

Number: number of milliseconds since starting the sketch.

## Related

* [day()](day.md)
* [hour()](hour.md)
* [minute()](minute.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
