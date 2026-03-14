# Constrain

This example demonstrates constraining a shape's movement within a bounded area. A circle follows the mouse with easing applied, keeping it within a rectangular box.

It demonstrates:

- the `constrain()` function to limit values within a range
- smooth motion with easing
- mouse tracking with gradual animation
- using `abs()` to check for minimum movement thresholds
- different drawing modes with `ellipseMode()` and `rectMode()`

From here, you can try:

- creating multiple constrained objects that interact with each other
- using different easing values to create different speeds
- constraining to circular or other shaped boundaries
- adding keyboard controls to move the constrained object

![animation of a circle following the mouse within a bounded box](/assets/examples/constrain.gif "A white circle that follows the mouse while staying constrained within a rectangular boundary")

```lua
require("L5")

local mx = 0
local my = 0
local easing = 0.05
local radius = 24
local edge = 100
local inner = edge + radius

function setup()
    size(640, 360)
    windowTitle("Constrain")
    describe(" Move the mouse across the screen to move the circle. The program constrains the circle to its box.")

    noStroke()
    ellipseMode(RADIUS)
    rectMode(CORNERS)
end

function draw()
    background(51)

    -- Change the position of the drawn ellipse to the position of the mouse with easing
    if (abs(mouseX - mx) > 0.1) then
        mx = mx + (mouseX - mx) * easing
    end

    if (abs(mouseY - my) > 0.1) then
        my = my + (mouseY - my) * easing
    end

    -- Constrain the position of the ellipse to the inner rectangle
    mx = constrain(mx, inner, width - inner)
    my = constrain(my, inner, height - inner)
    fill(76)
    rect(edge, edge, width - edge, height - edge)
    fill(255)
    ellipse(mx, my, radius, radius)
end
```
