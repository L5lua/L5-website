# cursor()
 
Changes the cursor's appearance.

The first parameter, `type`, sets the type of cursor to display. The built-in options are `ARROW`, `IBEAM`, `WAIT`, `CROSSHAIR`, `WAITARROW`, `SIZENWSE`, `SIZENESW`, `SIZEWE`, `SIZENS`, `SIZEALL`, `NO`, `HAND`.

If the path to an image is passed, as in `cursor('/assets/target.png')`, then the image will be used as the cursor. Images should generally be at most 32 by 32 pixels large.

The parameters `x` and `y` are optional. If an image is used for the cursor, `x` and `y` set the location pointed to within the image. They are both 0 by default, so the cursor points to the image's top-left corner. `x` and `y` must be less than the image's width and height, respectively.

## Examples

![cursor example 1](assets/cursor1.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  windowTitle("Cursors")
  describe('A gray square. The cursor appears as crosshairs.')
end

function draw()
  background(200)

  -- Set the cursor to crosshairs: +
  cursor(CROSSHAIR)
end
```

![Cursor example 2](assets/cursor2.gif)

```lua
require("L5")

function setup()
  size(100, 100)

  describe('A gray square divided into quadrants. The cursor image changes when the mouse moves to each quadrant.')
end

function draw() 
  background(200)

  -- Divide the canvas into quadrants.
  line(50, 0, 50, 100)
  line(0, 50, 100, 50)

  -- Change cursor based on mouse position.
  if mouseX < 50 and mouseY < 50 then
    cursor(CROSSHAIR)
  elseif mouseX > 50 and mouseY < 50 then
    cursor(WAIT)
  elseif mouseX > 50 and mouseY > 50 then
    cursor('assets/purplecurves.png');
   else 
    cursor(NO)
  end
end
```

## Syntax

```lua
cursor(type, [x], [y])
```

## Parameters

| Parameter |                                                                      |
| -         | --------------------------------------------------                   |
| type      | Constant/String: Built-in names of cursor, or path to cursor image.  |
| x         | Number: x-coordinate of the center of the ellipse.                   |
| y         | Number: y-coordinate of the center of the ellipse.                   |


## Related

* [noCursor()](noCursor.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
