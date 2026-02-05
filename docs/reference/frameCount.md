# frameCount()
 
A `Number` variable that tracks the number of frames drawn since the sketch started.

`frameCount`'s value is 0 inside setup(). It increments by 1 each time the code in draw() finishes executing.

## Examples

![frameCount example 1](assets/frameCount1.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(200)

  -- Display the value of
  -- frameCount.
  textSize(30)
  textAlign(CENTER, CENTER)
  fill(0)
  text(frameCount, 50, 50)

  describe('The number 0 written in black in the middle of a gray square.')
end
```

![frameCount example 2](assets/frameCount2.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  -- Set the frameRate to 30.
  frameRate(30)

  textSize(30)
  textAlign(CENTER, CENTER)

  describe('A number written in the middle of a gray square. Its value increases rapidly.')
end

function draw() 
  background(200)

  -- Display the value of
  -- frameCount.
  text(frameCount, 50, 50)
end
```

## Related

* [frameRate()](frameRate.md)
* [deltaTime()](deltaTime.md)
* [millis()](millis.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
