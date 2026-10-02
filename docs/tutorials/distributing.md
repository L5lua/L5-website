# Distributing your L5 project

There are several methods for distributing projects made with L5.

Your options are:

1. Distribute your L5 project as a *love* file that anyone with LOVE installed can run
2. Distribute your L5 project *fused* with the LOVE application for macOS and/or for Windows, including needed library files, which creates an executable application so someone doesn't have to separately install LOVE on their machine.
3. Use a LoveJS Builder to compile your project as a webassembly html file that can be hosted online and played from a website (such as on Itch.io)

## Distributing a *love* file

This is the simplest distribution method.

Because L5 is built with LOVE, anyone who has LOVE installed on their computer can run your L5 project.

Here's how to take your project and make it into a *love* file so that others can run it.

The main idea is you want to take your project files (including L5.lua, main.lua and anything else) and compress them into a `.zip file`, then rename the extension from `.zip` to `.love`. **Tip:** Make sure you don't just zip your folder but instead zip up the **contents of your L5 project's folder**!

### Windows

Inside your project folder, select all of the project files, then right click and choose *Send to > Compressed zip folder*. It will create that zipped file right there. Then right click on it and choose to rename it. Change the `.zip` ending to `.love`. If you don't see the zip extension, you can choose the View Menu > Show > Filename Extensions.

### Mac

Inside your project folder, select the files (and any needed asset folders), right-click/Ctrl+click and pick *Compress n items*. Then rename the resulting `.zip` file to have a `.love` ending.

Alternatively, you can use the terminal. Navigate inside the project folder. You can do this by opening the Terminal, typing `cd ` (that's cd with a space after) and then drag in the folder you want to navigate to and then hit enter.

Then type in and run the following (hit enter after typing or copy/pasting this exactly):

```
zip -r ProjectName.love .
```

Change the ProjectName to whatever your project name should be. You can find that love file on your desktop/file system and upload that.

### Linux

Assuming your current directory is ProjectName/ you can create the `.love` file from the command line directly by navigating to the folder and using:

```
zip -r ProjectName.love .
```

Once you have this *love* file, you can share your projects on a USB or upload it online. Anyone with LOVE on their computer can run your L5 program as a *love* file.

## Distributing an application for macOS or Windows

Once you have packed project into a .love file you can create a project executable that directly runs your project. The advantage of this is that you can send your project to someone else's computer and they don't need to have already installed LOVE on their machine. You will fuse your love file to the LOVE application, which you can then distribute to others.

### Windows

For this you have to append your .love file to the love.exe file that comes with the official LÖVE .zip file. The resulting file is your program executable.

Once you have your program executable you can pack it together with all the other DLL files of the official LÖVE .zip file into a new .zip file and share this with the world. 

See [Instructions for creating a Windows executable](https://www.love2d.org/wiki/Game_Distribution#Creating_a_Windows_Executable) for full details.

### macOS

See [Creating a macOS Application](https://www.love2d.org/wiki/Game_Distribution#Creating_a_macOS_Application) for details. There is also a [video tutorial](https://www.youtube.com/watch?v=SU2RpGdezP4).

### Linux

There are multiple methods for creating a standalone executable application. One method [detailed](https://www.love2d.org/wiki/Game_Distribution#AppImages) is to fuse the LOVE appimage with your project.

## Creating a web build of your project

There are multiple tools to create WASM we builds out of love files. Alex J. Griffith's [LoveJS Builder](https://alexjgriffith.itch.io/lovejs-player) can take your love file and output a (rather large) single html file that holds your L5 project along with a working web runtime of LOVE to power your project. The resulting file can be put online on your own website or uploaded somewhere, such as on Itch.io. Note there are some limitations and gotchas to be aware of for this method.

*Some instructions on this page are adapted from LOVE's [Game Distribution](https://www.love2d.org/wiki/Game_Distribution) GNU FDL 1.3.*
