# saveStrings()
 
Saves an ordered table array of strings to a file, one per line.

The first parameter, `list`, is an ordered table array with the strings to save.

The second parameter, `filename`, is a string that sets the file's name. For example, calling `saveStrings({'0', '01', '011'}, 'data.txt')` saves the array `{'0', '01', '011'}` to a file called `data.txt` on the user's computer.

## Examples

![saveStrings example 1](assets/saveStrings1.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(200)
  fill(0)

  -- Style the text.
  textAlign(LEFT, CENTER)
  textSize(12)

  -- Display instructions.
  text('Click to save', 5, 50, 90)

  describe('The text "Click to save" written in black on a gray background.')
end

-- Save the file when the user clicks.
function mousePressed()
  if mouseX > 0  and  mouseX < 100  and  mouseY > 0  and  mouseY < 100  then
    -- Create an array.
    local data = {'0', '01', '011'}

    -- Save the text file.
    saveStrings(data, 'data.txt')
  end
end

```

![saveStrings example 2](assets/saveStrings1.webp)

```lua
require("L5")

function setup()
  size(100, 100)

  background(200)
  fill(0)

  -- Style the text.
  textAlign(LEFT, CENTER)
  textSize(12)

  -- Display instructions.
  text('Click to save', 5, 50, 90)

  describe('The text "Click to save" written in black on a gray background.')
end

-- Save the file when the user double-clicks.
function mousePressed()
    -- Create an array.
    -- ASCII art courtesy Wikipedia:
    -- https:--en.wikipedia.org/wiki/ASCII_art
    local data = {' (\\_/) ', "(='.'=)", '(")_(")'}

    -- Save the text file.
    saveStrings(data, 'cat.txt')
end
```

## Syntax

```lua
saveStrings(list, filename)
```

## Parameters

| Parameter |                                                                               |
| -         | --                                                                            |
| list      | table: data to save                                                           |
| filename  | String: any sequence of letters and numbers, optionally with '.png' extension |


## Related

* [saveTable()](saveTable.md)
* [print()](print.md)
* [save()](save.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
