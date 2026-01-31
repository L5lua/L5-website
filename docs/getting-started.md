You can run L5 programs from your downloaded folder or via the command line or an Integrated Development Environment (IDE).

IDEs such as ZeroBrane Studio, Sublime Text, VS Code, Notepad++, and SciTE all support launching LÖVE programs (the underlying framework used by L5), though require additional setup configuration not covered here.

## Running L5 from the desktop

The easiest way to run your L5 program is to drag the **folder** containing your main.lua onto the Love2d application. Remember to drag the **folder** containing `main.lua`, and not `main.lua` itself. 

It should launch and open a new window with your sketch running in it, or print an error message. If you're running the L5 Starter program, you should see a square window with a yellow background. Congratulations.

**By default, `print()` output only appears if you run your program from the command line. To display print output directly in your sketch window add `printToScreen()` to your `setup()` function.**

*Once you have a sucessfully running program, you're ready for your next steps writing programs with L5. Check out [L5 for Processing-p5.js programmers](/L5-for-processingp5), [tutorials](/tutorials) or the [reference](/reference).*

## Running L5 from the command line

Running L5 from the command line allows you to see the output of `describe()`, `print()` and any error messages in the console.

### Linux command line

In the Terminal, you can run `love path/to/L5-starter`. Or if you are in the folder with your program, run `love .` to launch your project from the current directory.

### Windows command line

You can launch your programs from the command line and add the `--console` flag to be able to see print() and error() output as well:
```
"C:\Program Files\LOVE\love.exe" --console "C:\Users\<YourUsername>\Desktop\L5-starter"
```

Replace `<YourUsername>` and `Desktop\L5-starter` with your actual username and the location of your program folder.

### macOS command line

There are a few extra steps to smoothly set up command line usage for L5 in the command line on Mac. 

If Love is installed in your applications folder you can run:

```sh
open -n -a love "~/path/to/my-program"
```

This will not send debugging and print information to the Terminal nor any `describe()` text. To see printed text in the command line you need to run the Love program from Applications, like this:

```sh
/Applications/love.app/Contents/MacOS/love ~/path/to/my-program
```

You can set up an alias in your Terminal session to call the binary when you use love by adding an alias to your `~/.zshrc` file (Z shell configuration file).

Open the file with:

```sh
open -a TextEdit ~/.zshrc
```

You may have to create the file first if it does not yet exist.

```sh
touch ~/.zshrc
```

Then paste in the following code and save the file:

```sh
# alias to love
alias love="/Applications/love.app/Contents/MacOS/love"
```

Now you can call love from the command line like Linux and Windows:

```sh
love ~/path/to/my-program
```

If this doesn't works you should reload the .zshrc file and then try running the program again.

```sh
source ~/.zshrc
love ~/path/to/my-program
```

---

*Instructions adapted from [Love2d wiki: Getting Started](https://www.love2d.org/wiki/Getting_Started), GNU Free Documentation License 1.3.*
