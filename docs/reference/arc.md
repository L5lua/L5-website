# arc()

Draws an arc.

An arc is a section of an ellipse defined by the `x`, `y`, `w`, and `h` parameters. `x` and `y` set the location of the arc's center. `w` and `h` set the arc's width and height. See `ellipse()` and `ellipseMode()` for more details.

The fifth and sixth parameters, `start` and `stop`, set the angles between which to draw the arc. Arcs are always drawn clockwise from start to stop. By default, angles are given in radians, but if angleMode(DEGREES) is set, the function interprets the values in degrees.

The seventh parameter, mode, is optional. It determines the arc's fill style. The fill modes are a semi-circle (OPEN), a closed semi-circle (CHORD), or a closed pie segment (PIE).

*Note: The fill mode of arc() does not render exactly the same as Processing and p5.js.*


## Examples

![arc example 1](assets/arc1.webp)

```lua
function setup() 
  size(100, 100)

  background(200)

  arc(50, 50, 80, 80, 0, PI + HALF_PI)

  describe('A white circle on a gray canvas. The top-right quarter of the circle is missing.')
end
```

![Arc example 2](assets/arc2.webp)

```lua
function setup()
  size(100, 100)

  background(200)

  arc(50, 50, 80, 40, 0, PI + HALF_PI)

  describe('A white ellipse on a gray canvas. The top-right quarter of the ellipse is missing.')
end
```

![Arc example 3](assets/arc3.webp)

```lua
function setup() 
 size(100, 100)

  background(200)

  -- Bottom-right.
  arc(50, 55, 50, 50, 0, HALF_PI,PIE);

  noFill()

  -- Bottom-left.
  arc(50, 55, 60, 60, HALF_PI, PI,OPEN)

  -- Top-left.
  arc(50, 55, 70, 70, PI, PI + QUARTER_PI,OPEN)

  -- Top-right.
  arc(50, 55, 80, 80, PI + QUARTER_PI, TWO_PI,OPEN)

  describe(
    'A shattered outline of an circle with a quarter of a white circle at the bottom-right.'
  )
end
```

![Arc example 4](assets/arc4.webp)

```lua
function setup() 
  size(100, 100)

  background(200)

  -- Default fill mode.
  arc(50, 50, 80, 80, 0, PI + QUARTER_PI)

  describe('A white circle with the top-right third missing. The shape is outlined in black.')
end
```

![Arc example 5](assets/arc5.webp)

```lua
function setup() 
  size(100, 100);

  background(200);

  -- Default fill mode.
  arc(50, 50, 80, 80, 0, PI + QUARTER_PI, OPEN);

  describe('A white circle missing a section from the top-right. The bottom is outlined in black.')
end
```

![Arc example 6](assets/arc6.webp)

```lua
function setup() 
  size(100, 100)

  background(200)

  -- CHORD fill mode.
  arc(50, 50, 80, 80, 0, PI + QUARTER_PI, CHORD)

  describe('A white circle with a black outline missing a section from the top-right.')
end
```

![Arc example 7](assets/arc7.webp)

```lua
function setup() 
  size(100, 100)

  background(200)

  -- PIE fill mode.
  arc(50, 50, 80, 80, 0, PI + QUARTER_PI, PIE)

  describe('A white circle with a black outline. The top-right third is missing.')
end
```

![Pacman](assets/pacman.gif)

```lua
function setup() 
  size(100,100)

  describe('A yellow circle on a black background. The circle opens and closes its mouth.')
end

function draw()
 background(0)

  -- Style the arc.
  noStroke()
  fill(255, 255, 0)

  -- Update start and stop angles.
  biteSize = PI / 16
  startAngle = biteSize * sin(frameCount * 0.1) + biteSize
  endAngle = TWO_PI - startAngle

  -- Draw the arc.
  arc(50, 50, 80, 80, startAngle, endAngle, PIE)
end
```

## Syntax

```lua
arc(x, y, w, h, start, stop, [mode])
```

## Parameters

| Parameter |                                                                                          |
| -         | --------------------------------------------------                                       |
| x         | Number: x-coordinate of the arc's ellipse.                                               |
| y         | Number: y-coordinate of the arc's ellipse.                                               |
| w         | Number: width of the arc's ellipse.                                                      |
| h         | Number: height of the arc's ellipse.                                                     |
| start     | Number: angle to start the arc, in radians.                                              |
| stop      | Number: angle to stop the arc, in radians.                                               |
| mode      | Constant: Optional parameter specifying the way of drawing the arc: CHORD, PIE, or OPEN. |

## Related

* [ellipse()](ellipse.md)
* [ellipseMode()](ellipseMode.md)
* [radians()](radians.md)
* [degrees()](degrees.md)
