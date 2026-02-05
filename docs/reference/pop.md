# pop()

Ends a drawing group that contains its own transformations.

**Note that L5's push() and pop() work differently than p5.js and Processing. In L5, push() and pop() only save and restore the transformation matrix state but not the style effects.**

[push()](push.md) and `pop` contain the effects of the following functions:

* translate()
* rotate()
* scale()
* applyMatrix()

By default, transformations such as [rotate()](rotate.md) are applied to all drawing that follows. The [push()](push.md) and `pop()` functions can limit the effect of transformations to a specific group of shapes, images, and text. For example, a group of shapes could be translated to follow the mouse without affecting the rest of the sketch:

```lua
-- Begin the drawing group.
push()

-- Translate the origin to the mouse's position.
translate(mouseX, mouseY)

-- Style the face.
noStroke()
fill('green')

-- Draw the face.
circle(0, 0, 60)

-- Style the eyes.
fill('white')

-- Draw the left eye.
ellipse(-20, -20, 30, 20)

-- Draw the right eye.
ellipse(20, -20, 30, 20)

-- End the drawing group.
pop()

-- Draw a bug.
local x = random(0, 100)
local y = random(0, 100)
fill(0)
text('X', x, y)
```

In the code snippet above, the bug's position isn't affected by `translate(mouseX, mouseY)` because that transformation is contained between push() and `pop()`. The bug moves around the entire canvas as expected.

Note: push() and `pop()` are always called as a pair. Both functions are required to begin and end a drawing group.

push() and `pop()` can also be nested to create subgroups. For example, the code snippet above could be changed to give more detail to the frog’s eyes:

```lua
-- Begin the drawing group.
push()

-- Translate the origin to the mouse's position.
translate(mouseX, mouseY)

-- Style the face.
noStroke()
fill('green')

-- Draw a face.
circle(0, 0, 60)

-- Draw the left eye.
push()
translate(-20, -20)
fill('white')
ellipse(0, 0, 30, 20);
fill('black')
circle(0, 0, 8)
pop()

-- Draw the right eye.
push()
translate(20, -20)
fill('white')
ellipse(0, 0, 30, 20)
fill('black')
circle(0, 0, 8)
pop()

-- End the drawing group.
pop()

-- Draw a bug.
local x = random(0, 100)
local y = random(0, 100)
text('X', x, y)
```

In this version, the code to draw each eye is contained between its own push() and `pop()` functions. Doing so makes it easier to add details in the correct part of a drawing.


## Examples

![pop example 1](assets/pop1.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(200)

  -- Draw the left circle.
  circle(25, 50, 20)

  -- Begin the drawing group.
  push()

  -- Translate the origin to the center.
  translate(50, 50)

  -- Style the circle.
  strokeWeight(5)
  stroke('royalblue')
  fill('orange')

  -- Draw the circle.
  circle(0, 0, 20)

  -- End the drawing group.
  pop()

  -- Style the right circle since
  -- styles aren't encapsulated by push() and pop() in L5
  strokeWeight(1)
  stroke('black')
  fill(255)

  -- Draw the right circle.
  circle(75, 50, 20)

  describe(
    'Three circles drawn in a row on a gray background. The left and right circles are white with thin, black borders. The middle circle is orange with a thick, blue border.'
  )
end
```

![pop example 2](assets/pop2.gif)

```lua
require("L5")

function setup()
  size(100, 100)

  -- Slow the frame rate.
  frameRate(24)

  describe('A mosquito buzzes in front of a green frog. The frog follows the mouse as the user moves.')
end

function draw()
  background(200)

  -- Begin the drawing group.
  push()

  -- Translate the origin to the mouse's position.
  translate(mouseX, mouseY)

  -- Style the face.
  noStroke()
  fill('green')

  -- Draw a face.
  circle(0, 0, 60)

  -- Draw the left eye.
  push()
  translate(-20, -20)
  fill('white')
  ellipse(0, 0, 30, 20)
  fill('black')
  circle(0, 0, 8)
  pop()

  -- Draw the right eye.
  push()
  translate(20, -20)
  fill('white')
  ellipse(0, 0, 30, 20)
  fill('black')
  circle(0, 0, 8)
  pop()

  -- End the drawing group.
  pop()

  -- Draw a bug.
  local x = random(0, 100)
  local y = random(0, 100)
  text('X', x, y)
end
```

## Related

* [push()](push.md)
* [draw()](draw.md)
* [isLooping()](isLooping.md)
* [loop()](loop.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
