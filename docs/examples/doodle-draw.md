# Drawing Software

This is a basic implementation of a program to draw doodles, using random colors.

It demonstrates:

* working with colors
* random RGB color selection
* input and event handling
* current and previous frame mouse positioning

From here, you can add additional features such as:

* buttons to select different colors and brush sizes
* draw with stamps or photos
* the ability to save one's drawing to the computer
* a reset button to clear the screen
* randomly selected prompts that suggest what to draw
* a symmetrical drawing mode
* more experimental features!

For more ideas, check out [Meeting Mr. Kid Pix](https://youtu.be/BxoY-_HQOK0?si=8LWjmoNAkNWWydSk).

![Various doodle lines of different colors are drawin in the window](/assets/examples/drawing-software.gif "Various doodle lines in different colors are drawn in the window")

```lua
require("L5")

function setup()
  size(800,600)
  windowTitle("Drawing software")

  background("midnightblue")
  strokeWeight(5)
end

function mouseDragged()
  line(mouseX, mouseY, pmouseX, pmouseY)
end

function mousePressed()
  stroke(random(255),random(255),random(255))
end

```

## Related References

* [mouseDragged()](/reference/mouseDragged) 
* [mousePressed()](/reference/mousePressed)
* [mouseX](/reference/mouseX)
* [mouseY](/reference/mouseY)
* [pmouseX](/reference/pmouseX)
* [pmouseY](/reference/pmouseY)

## Related Examples

* [Basic Pong](/examples/basic-pong)

