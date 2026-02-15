# 10PRINT variations

10PRINT is the name of a [one-liner](https://en.wikipedia.org/wiki/One-liner_program) program originally written in the BASIC language for Commodore computers and widely shared among early 1980s home computer users.

The original line of code was typed into the terminal and immediately executed:

```BASIC
10 PRINT CHR$(205.5+RND(1)); : GOTO 10
```

This single line, which begins with the line number 10, says to [print](/reference/print) out the ASCII character ([char](/reference/char)) of the enclosed number that follows. That number is 205.5 plus a [random](/reference/random) number between 0 and 1, which, results in a decimal ([float](/reference/float)) between 205.5 and 206.5. When converted to an ASCII character, the fractional ([fract](/reference/fract)) decimal value is automatically removed, with an implicit [floor](/reference/floor), and the equivalent character `'\'` or `'/'` is printed out. Finally, the program says to goto line number 10 (the beginning of the line), a loop, to begin again, in an infinite loop. This results in a twisty maze of passages created with just these two ASCII characters that spill out over the terminal screen in tumbling lines until the computer operator / programmer interrupts it.

Much more can be said about 10print, and in fact, an incredible and widely-lauded 324-page collaboratively-written book also titled [10 PRINT CHR$(205.5+RND(1)); GOTO 10](https://10print.org/) was published in 2012 by MIT Press. It can be purchased, and is available as a creative-commons licensed book and freely downloadable PDF.

And here, following in tradition, we attempt yet another port of the original 10print instruction into somewhat-equivalent functionality with L5. This is but one of many (infinite?) potential implementations, and adds a varying block size each frame. The slow (1 frame per second here) rate is needed as otherwise the redrawing rate would be too quick for our eyes to handle.

A main structure in this implementation are nested loops. This classic programming pattern is used everywhere from grid-based and patterned artworks to top down and sidescrolling tiled 2D videogames. The inner loop of incrementing x values advances the blocks across the page all the way to the right, where at that point the y value advances one block down the page, and begins looping through the x values again, drawing to the right, finally stopping drawing one complete iteration of the maze upon reaching the bottom of the window before drawing anew top to bottom again on the successive frame.

Ways you can build on the 10print code:

* Add color to the maze
* Alter the randomness percentage to be more likely to draw one kind of line or the other
* Change the block output to other line forms or shapes to make other kinds of mazes 
* Figure out an implementation that iteratively adds one line per frame rather than drawing the whole maze grid at once
* Apply more ideas you read about from [10Print](https://10print.org/) and ideas of your own

![a maze of changing corridor size](/assets/examples/10print.gif)

```lua
require ("L5")

function setup()
  size(600, 800)
  block = height / 40
  
  frameRate(1)
  
  describe("A maze of twisty little passages in each frame")
end

function draw()
  background(255)
  block = floor(random(10,140))
  for y = 1, height, block do
    for x = 1, width, block do
      if random() < 0.5 then
	line(x, y, x + block, y + block)
      else
	line(x + block, y, x, y + block)
      end
    end
  end
end
```

## Related References

* [for](/reference/for)
* [floor()](/reference/floor)
* [frameRate()](/reference/frameRate)
* [if](/reference/if)
* [line()](/reference/line.md)
* [draw()](/reference/draw)
* [random()](/reference/random)

## Related Examples

* [Animation with Events](animation-and-variables-animation-with-events.md) - Pause and resume animation.
* [Basic Pong](basic-pong.md) - A simple program demonstrating a basic implementation of pong with enemy AI player
* [Conditions](animation-and-variables-conditions.md) - Use if and else statements to make decisions while your sketch runs.
* [Copy Image Data](imported-media-copy-image-data.md) - Paint from an image file onto the canvas.
* [Conway's Game Of Life](conways-life.md) - An implementation of the zero-player game and simulation formulated by mathematician John Conway
* [Minimum Spanning Tree](min-span-tree.md) - An example of implementing Prim's algorithm for finding the shortest lengths to connect all randomly placed dots
* [Walking lines](walking-lines.md) - Visualizes randomly drawn lines bouncing around a box with their intersecting points highlighted

