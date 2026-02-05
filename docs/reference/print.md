# print()
 
Displays text in the command line console.

`print()` is helpful for printing values while debugging. Each call to `print()` creates a new line of text.

**Calling `printToScreen()` will turn on displaying the output of `print()` functions in your program window.** This is particularly helpful if you are running your L5 program without a text console output, for example by dragging and dropping your program's folder onto the Love application.

Note: Call `print()` on its own to print a blank line. 

## Examples

![print example 1](assets/print1.webp)

```lua
require("L5")

function setup()
  size(100, 100)
  
  -- Prints "hello, world" to the console.
  print('hello, world')
  
  -- Turns on print console display on program window
  printToScreen()
end
```

## Syntax

```lua
print(contents)
```

## Parameters

| Parameter |                                       |
| -         | --                                    |
| contents  | Any: content to print to the console. |


## Related

* [printToScreen()](printToScreen.md)
* [cursor()](cursor.md)
* [deltaTime](deltaTime.md)
* [describe()](describe.md)
* [text()](text.md)
* [windowTitle()](windowTitle.md)

---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
