# Mouse Press

Move the mouse to position the shape. Press the mouse button to invert the color. Note that L5 and p5.js both have a `mouseIsPressed` boolean, which is different than in Processing's *mousePressed* convention.

![animation of a crosshair that changes color when mouse button is pressed](/assets/examples/mouse-press.gif "A white and black crosshair following the mouse that inverts colors when the mouse button is pressed")

```lua
require("L5")

function setup()
    size(640, 360)
    windowTitle("Mouse Press")
    describe("Move and press the mouse button to position the shape and invert the color")

    noSmooth()
    fill(126)
    background(102)
end

function draw()
    if mouseIsPressed then
        stroke(255)
    else
        stroke(0)
    end

    line(mouseX - 66, mouseY, mouseX + 66, mouseY)
    line(mouseX, mouseY - 66, mouseX, mouseY + 66)
end
```

## Related Examples

* [Constrain](constrain.md)
* [Easing](easing.md)
* [Keyboard](keyboard.md)
* [Keyboard Functions](keyboard-functions.md)
* [Milliseconds](milliseconds.md)
* [Mouse 2D](mouse-2d.md)

---

Adapted from Processing examples. Adapted to L5 2025. Licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).
