# print()
 
Displays text in the command line console.

`print()` is helpful for printing values while debugging. Each call to `print()` creates a new line of text.

To enable the output of print to display in the window, you can call `printToScreen()` in setup to turn this on.

Note: Call `print()` on its own to print a blank line. 

## Examples

![print example 1](assets/print1.webp)

```lua
function setup()
  -- Prints "hello, world" to the console.
  print('hello, world')
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

---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
