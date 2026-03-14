# Easing

This example demonstrates smooth animation by moving a shape toward the mouse position with easing. The shape doesn't jump directly to the cursor but gradually glides toward it.

It demonstrates:

- creating smooth, natural-looking motion
- calculating the difference between current and target positions
- applying easing factors to create gradual movement
- following the mouse position without snap
- simple animation principles

From here, you can try:

- varying the easing value to create different speeds and smoothness levels
- having multiple shapes with different easing values
- creating easing toward different target positions (not just the mouse)
- implementing other interpolation methods like lerp or acceleration/velocity

![animation of a circle smoothly following the mouse cursor](/assets/examples/easing.gif "A white circle that glides toward the mouse cursor with smooth easing")

```lua
require("L5")

local x = 0
local y = 0
local easing = 0.05

function setup()
    size(640, 360)
    windowTitle("Easing")
    describe(" Move the mouse across the screen and the symbol will follow.")

    noStroke()
end

function draw()
    background(51)

    -- Change the position of the drawn ellipse to the position of the mouse with easing

    targetX = mouseX
    dx = targetX - x
    x = x + dx * easing

    targetY = mouseY
    dy = targetY - y
    y = y + dy * easing

    ellipse(x, y, 66)
end
```
