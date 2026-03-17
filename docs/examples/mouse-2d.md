# Mouse 2D

Moving the mouse changes the position and size of each box.

![animation of two translucent squares moving in opposite directions](/assets/examples/mouse-2d.gif "Two translucent rectangles that move with the mouse, one following it directly and one moving in the inverse direction")

```lua
require("L5")

function setup()
    size(640, 360)
    windowTitle("Mouse 2D")
    describe("Moving the mouse changes the position and size of each box")

    noStroke()
    rectMode(CENTER)
end

function draw()
    background(0.0)

    fill(255, 204)
    rect(mouseX, height / 2, mouseY / 2 + 10, mouseY / 2 + 10)

    fill(255, 204)

    local inverseX = width - mouseX
    local inverseY = height - mouseY
    rect(inverseX, height / 2, (inverseY / 2) + 10, (inverseY / 2) + 10)
end
```

## Related Examples

* [Constrain](constrain.md)
* [Easing](easing.md)
* [Keyboard](keyboard.md)
* [Keyboard Functions](keyboard-functions.md)
* [Milliseconds](milliseconds.md)
* [Mouse 1D](mouse-1d.md)

---

Adapted from Processing examples. Adapted to L5 2025. Licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).
