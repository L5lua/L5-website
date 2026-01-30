# windowTitle()
 
Adds a text label to the window's title bar.

Calling windowTitle without an argument returns the current window title, or "Untitled" if it hasn't been set.

## Examples

![windowTitle example 1](assets/windowTitle1.webp)

```lua
function setup()
  size(100,100)
  windowTitle("windowTitle example")
  
  describe("A default gray window with the title windowTitle example")
end
```

![windowTitle example 2](assets/windowTitle1.webp)

```lua
function setup()
  size(100,100)
  windowTitle("windowTitle example")
  
  describe("A default gray window with the title windowTitle example. Pressing the mouse prints 'title is windowTitle example.'")
end

function mousePressed()
  print("title is: "..windowTitle())
end
```

## Syntax

```lua
windowTitle(title)
```

```lua
windowTitle()
```

## Parameters

| Parameter |                                |
| -         | --                             |
| title     | String: text for window title. |

## Returns

String: Name of window from title bar.

## Related

* [describe()](describe.md)
* [print()](print.md)
* [printToScreen()](printToScreen.md)

