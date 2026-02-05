# loadFont()

Loads a font and creates a font object. `loadFont()` can load fonts in either Truetype (`.ttf`) or Bitmap Fonts. The filepath to the BMFont's image file must be specified inside the BMFont file. OpenType fonts (`.otf`) work as well but some features may not be supported. Loaded fonts are used to style text in the window. The default font without loading a custom font is `Noto Sans` size 13.

The parameter `path` is the path to a font file. Paths to local files should be relative. For example, `'assets/inconsolata.otf'`. The Inconsolata font used in the following examples can be downloaded for free [here](https://www.fontsquirrel.com/fonts/inconsolata/).

## Examples

![loadFont example 1](assets/loadFont1.webp)

```lua
local font
require("L5")

function setup()
  size(100,100)
  fill('deeppink')
  font = loadFont('assets/inconsolata.otf')
  textFont(font)
  textSize(36)
  background(255)
  text('L5', 10, 50)

  describe('The text "L5" written in pink on a white background.')
end
```

## Parameters

| Parameter |                                                    |
| -         | --                                                 |
| path      | String: path of the font to be loaded.             |

## Related

* [textFont()](textFont.md)
* [text()](text.md)
* [textWidth()](textWidth.md)
* [textAlign()](textAlign.md)



---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
