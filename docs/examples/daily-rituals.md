# Daily Rituals

This program is inspired by game designer Michael Brough's [VESPER.5](https://mightyvision.blogspot.com/2012/08/vesper5.html) (also see [this interview](https://www.gamedeveloper.com/design/road-to-the-igf-michael-brough-s-i-vesper-5-i-) with Michael), as well as the [instruction works](https://en.wikipedia.org/wiki/Instructions_for_Paintings) of Yoko Ono, the long-running exhibition series [Do It](https://curatorsintl.org/exhibitions/8593-do-it-1997) and the small exhibition and objects [#Fortune](http://stfj.net/index2.php?year=2013&project=art/2013/Fortune) by artist and game designer Zach Gage. 

Daily rituals uses L5's [loadStrings()](/reference/loadStrings) function to load a text file `things.txt` with 31 meditative artistic tasks, one for each possible day of a month.

The [text file can be downloaded](https://gist.github.com/lee2sman/43709f948a2c4be1132774e082a5ee0a) for use with the L5 program, or you can write your own. Be sure to place it in the same folder of your Daily Rituals project. It should have at least 31 lines of text. The font file [Frijole-Regular](https://fonts.google.com/specimen/Frijole) can be downloaded and placed in the same folder.

The program labels the window with the current day, loads the font and sets up text styling. Then it loads the lines of text from the text file into an array with as many elements as total days in a month. Finally, it draws some random lines for texture, grabs the current day of the month, and displays the day's ritual. 

![the text 'Close Your Eyes and Think of a Past Rainstorm - Sound, Taste. Name it.'](/assets/examples/daily-rituals.webp "The text: Close Your Eyes and Think of a Past Rainstorm - Sound, Taste. Name it.")

```lua
require("L5")

function setup()
  local date=(year().." "..month().." "..day())
  
  windowTitle("Daily ritual "..date)

  f = loadFont("Frijole-Regular.ttf")

  textFont(f)
  textSize(48)

  things = loadStrings("things.txt")

  background("blue")

  stroke("grey")

  -- adds some texture
  for i = 1, floor(random(12) + 1) do
    strokeWeight(random(1, 12))
    line(random(width), random(height), random(width), random(height))
  end

  fill("yellow")

  -- activity by day of the month
  local today = things[day()]

  text(today, 25, 25, width - 50)
end
```

## Related References

* [day()](/reference/day)
* [floor()](/reference/floor)
* [loadFont()](/reference/loadFont)
* [loadStrings()](/reference/loadStrings)
* [local](/reference/local)
* [random()](/reference/random)
* [year()](/reference/year)

## Related Examples

* [10print variations](10print.md) - An implementation of the classic maze-drawing algorithm
* [Animation with Events](animation-and-variables-animation-with-events.md) - Pause and resume animation.
* [Conditions](animation-and-variables-conditions.md) - Use if and else statements to make decisions while your sketch runs.
* [Copy Image Data](imported-media-copy-image-data.md) - Paint from an image file onto the canvas.
