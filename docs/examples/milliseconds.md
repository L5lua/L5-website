# Milliseconds

This example uses the `millis()` function to create color patterns that change based on elapsed time. Different vertical strips cycle through colors at different rates using the modulo operator.

It demonstrates:

- the `millis()` function to track elapsed time in milliseconds
- using the modulo operator (`%`) to create repeating time patterns
- the `colorMode()` function for dynamic color range control
- scaling and subdividing the screen
- creating time-based animation without explicit frame counting

From here, you can try:

- using milliseconds to animate object positions or sizes
- creating sound visualization based on elapsed time
- making patterns that synchronize to specific time intervals
- combining milliseconds with other time functions like `second()` and `minute()`

![animation of vertical color strips cycling at different rates](/assets/examples/milliseconds.gif "Vertical colored stripes that cycle through colors at different speeds based on elapsed milliseconds")

```lua
require("L5")

function setup()
    size(640, 360)
    windowTitle("Milliseconds")
    describe("How L5 keeps track of the number of milliseconds a program has run")

    noStroke()
    scale = width / 20
end

function draw()
    for i = 0, scale do
        colorMode(RGB, (i + 1) * scale * 10)
        fill(millis() % ((i + 1) * scale * 10))
        rect(i * scale, 0, scale, height)
    end
end
```
