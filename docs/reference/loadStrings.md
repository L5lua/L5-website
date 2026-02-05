# loadStrings()
 
Loads a text file and returns a `table`.

The first parameter, `path`, is always a string with the path to the file. Paths to local files should be relative, as in `loadStrings('assets/data.txt')`. 

## Examples

![loadStrings example 1](assets/loadStrings1.webp)

```lua
local myData
require("L5")

function setup()
  size(100, 100)
  
  -- Load the text and create an array.
  myData = loadStrings('assets/names.txt')

  background(200)
  fill(0)

  -- Select a random line from the text.
  local phrase = random(myData)

  -- Style the text.
  textAlign(LEFT, CENTER)
  textSize(12)

  -- Display the text.
  text(phrase, 10, 50, 90)

  describe('The text '..phrase..'written in black on a gray background.')
end
```

## Syntax

```lua
loadStrings(path)
```

## Parameters

| Parameter |                                             |
| -         | --                                          |
| path      | String: path of the text file to be loaded. |

## Returns

Table: new table of strings containing the loaded text.

## Related

* [table](table.md)
* [loadTable()](loadTable.md)
* [saveStrings()](saveStrings.md)
* [saveTable()](saveTable.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
