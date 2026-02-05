# loadTable()
 
Reads the contents of a file or URL and creates a table object with its values. The file's path should be specified relative to the sketch's folder. The file format can be a comma-separated (in CSV format), a tab-separated value (in TSV format), or a lua table (as a lua file). Table only looks for a header row if the 'header' option is included.

`#table` always returns the total rows in the imported table.

`#table.columns` always returns the total columns in the imported table. Without headers, a loaded table's column names are ordered for convenience, from 1 up to the total number of columns.

## Examples

loadTable example 1

```lua
-- Given the following CSV file called "mammals.csv"
-- located in the project's "assets" folder:
--
-- id,species,name
-- 0,Capra hircus,Goat
-- 1,Panthera pardus,Leopard
-- 2,Equus zebra,Zebra

--my table is comma separated value "csv"
--and has a header specifying the columns labels
local mammals = loadTable('assets/mammals.csv', 'header')

require("L5")

function setup()
  print(#mammals..' total rows in table')
  print(#mammals.columns..' total columns in table.')

  -- Print column names
  for _,header in ipairs(mammals.columns) do
    print(header)
  end

  -- cycle through the table
  for i, mammal in ipairs(mammals) do
    for _,colName in ipairs(mammals.columns) do
      print(mammal[colName])
    end
  end
end
```

loadTable example 2

```lua
-- Given the following CSV file called "mammals.csv"
-- located in the project's "assets" folder:
--
-- 0,Capra hircus,Goat
-- 1,Panthera pardus,Leopard
-- 2,Equus zebra,Zebra

--my table is comma separated value "csv"
--without headers
local data = loadTable('assets/mammals.csv')

require("L5")

function setup()
  print(#data..' total rows in table')
  print(#data.columns..' total columns in table.')

  -- cycle through the table
  for i, row in ipairs(data) do
    for _, value in ipairs(row) do
      print(value)
    end
  end
end
```

## Syntax

```lua
loadTable(filename [,header])
```

## Parameters

| Parameter |                                                    |
| -         | --                                                 |
| path      | String: path of the text file to be loaded.        |
| header    | String: "header" to indicate table has header row. |

## Returns

Table: new table of strings containing the loaded table data.

## Related

* [table](table.md)
* [saveStrings()](saveStrings.md)
* [saveTable()](saveTable.md)
* [for](for.md)


---

*This reference page contains content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).*
