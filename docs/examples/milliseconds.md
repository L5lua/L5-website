# Milliseconds

A millisecond is 1/1000 of a second. Processing keeps track of the number of milliseconds a program has run. By modifying this number with the modulo(%) operator, different patterns in time are created.

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

## Related Examples

* [Clock](clock.md)
* [Constrain](constrain.md)
* [Easing](easing.md)
* [Keyboard](keyboard.md)
* [Keyboard Functions](keyboard-functions.md)
* [Mouse 1D](mouse-1d.md)

---

Adapted from Processing examples. Adapted to L5 2025. Licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).
