# Downloads

L5 is free open source software available for Linux, Mac, Windows, Android and iOS.

L5 programs run using LÖVE (also called Love2d), a free, open-source framework. Love2d is a game framework, just like Godot, Unity, or Unreal, which provides support for graphics, audio and other parts used by L5. You will use Love2d to run your L5 scripts. This is similar to using a browser to run HTML code.

Covered by this download tutorial:

* Download and Install a text editor
* Download and Install Love2d
* Download and Open L5 Starter Folder

## Step-by-step install guides

### Install text editor

We will first need a text editor, which is where we write the actual L5 code on our computer. For those starting out, we suggest downloading [VSCodium](https://vscodium.com/) or [Visual Studio Code (VS Code)](https://code.visualstudio.com/), available for macOS, Windows and Linux. But any preferred text editor is fine. 

**Note**: If you use iCloud, VSCodium will have significant lag and it is recommended to install VS Code instead. 

IDEs such as ZeroBrane Studio, Sublime Text, Notepad++, and SciTE all support launching LÖVE programs (the engine to run our L5 scripts), though require additional setup configuration not covered here.

#### Install L5lua Extension for VSCodium / VS Code

If you have VSCodium or VS Code code editor, open the editor. 

Click to open the extensions tab. Search for *L5* and install the extension. 

![Open the extension menu on the left side and search L5 on the top](/assets/tutorials/install/extension1.webp "Open the extension menu on the left side and search L5 on the top")

![Search for L5 in the search bar](/assets/tutorials/install/extension2.webp "Search for L5 in the search bar")

![Press install](/assets/tutorials/install/extension3.webp "Press install")


### Install Love2d

L5 uses the Love framework to power its library. There are current installation instructions for [macOS](install-mac.md), [Windows](install-windows.md), and [Linux](install-linux.md).

=== "Install Windows"

    This tutorial walks you through installing L5 with the Love (Love2d) framework on your Windows computer.

    1. Go to the [Love website](https://love2d.org) and click to download the 64-bit zipped Windows program.
    2. Your browser may show a warning. Click **"Keep"** or **"Save anyway"** to proceed with the download. It will download to your _Downloads_ folder by default.
    3. From the L5lua.org Download page, [download the L5 Starter project](/L5-starter.zip).
    4. Click **"Save"** when it asks you to save the L5-starter.zip file.
    5. Return to your _Downloads_ folder on your computer. **Right click** on the Love zip file and choose **"Extract All"**. Click **"Extract"** to extract it to your Downloads folder.
    6. Open the extracted Love folder and **double-click** the **love.exe** application to run it. Windows may show a security warning saying "Windows protected your PC". Click **"More info"** and then click **"Run anyway"**.
    7. You should see a window open with a flying bird-shaped balloon and clouds, verifying that Love is now properly installed on your computer. **At this point you can close the window.**
    8. Go to your *Downloads* folder and **right click** on the L5-Starter.zip file and click to **"Extract"**.

=== "Install macOS"

    This tutorial walks you through installing L5 with the Love (Love2d) framework on your Macintosh computer.

    **Video Tutorial**

    <a href="https://youtu.be/AP1zTY_w9IU" id="yt"><img src="/assets/tutorials/install/video.webp" width="560" height="315" alt="Play video"></a>

    **Text and Screenshot Tutorial**

    1. Love is the underlying Framework that will allow L5 code to run on your computer. Go to the [Love website](https://love2d.org) and click to download the 64-bit zipped Mac program.
    ![Love2d website with downloads](/assets/tutorials/install/mac1.webp 'Love2d website with downloads')
    2. Click **"Allow"** if it asks 'Do you want to allow downloads on "love2d.org"?' It should download to your _Downloads_ folder by default.
    ![Alert box asking permission to download Love2d](/assets/tutorials/install/mac2.webp 'Alert box asking permission to install Love2d')
    3. Now on your desktop (called "Finder" on macOS) open up your _Downloads_ folder. You can right click and choose Open (see screenshot) or double click on Love to launch it.
    ![Folder with love application and L5 Starter folder](/assets/tutorials/install/mac3.webp 'Folder with love application and L5 Starter folder')
    4. A warning popup box opens to say the program and code is not verified by Apple. **DO NOT** move to the trash.
    ![Alert box stating macOS cannot verify the developer of love. The correct option is Open.](/assets/tutorials/install/mac4.webp 'Alert box stating macOS cannot verify the developer of love. The correct option is Open')
    5. Go to your computer's System Settings > Privacy &amp; Security. Scroll down to the **Security** section and next to **"love" was blocked to protect your Mac.** choose **Open Anyway**.
    ![System settings showing the Privacy and Security settings. Scroll down to Security and next to "love" was blocked to protect your mac, click to "Open Anyway".](/assets/tutorials/install/mac5.webp 'Alert box stating macOS cannot verify the developer of love. The correct option is Open')
    6. Now go back to your Downloads folder and **Double click** on Love. We only need to do this once! It's to verify Love works on your computer, which will allow L5 to run your custom code. You should see a window open with a flying bird-shaped balloon and clouds, verifying that Love is now properly installed on your computer. **At this point you can close the window.** Usually on a Mac we place our applications into the Applications folder, so you may want to move it there. 
    ![A flying bird-shaped balloon and cartoon clouds](/assets/tutorials/install/mac6.webp 'A flying bird-shaped balloon and cartoon clouds')
    7. After that, move your Love application to your applications folder. 

=== "Install Linux"

    This tutorial walks you through installing L5 with the Love (Love2d) framework on your Linux computer.

    On Linux, installation through the command line is common, but it can also be downloaded through the Love website. Since Linux is an open source family of operating systems the exact process may need to be altered for your particular Linux distribution.

    Installing Love differs based on which Linux distribution you have.

    **Simplest method: Installing Love through the web browser**
    
    Visit the [Love website](https://love2d.org/) and download the Linux AppImage. This is a format to allow the installation of Linux software that is independent of specific distribution methods. Once downloaded you may have to right click and choose *Properties* and then select *Executable as Program* if this is not already checked. The exact method or wording can vary by Linux distribution. Then double click on Love. We only need to do this once! It's to verify Love works on your computer, which will allow L5 to run your custom code. You should see a window open with a flying bird-shaped balloon and clouds, verifying that Love is now properly installed on your computer. **At this point you can close the window.**
    
    *Alternatively, if you are accustomed to using your Linux distribution's package manager, you can install through the command line:*

    **Installing Love on Debian/Ubuntu-based distributions with apt**

    ```sh
    sudo add-apt-repository ppa:bartbes/love-stable
    sudo apt update
    sudo apt install love
    ```

    **Install Love on Arch-based distributions with Pacman**

    ```sh
    sudo pacman -S love
    ```

    **Installing Love on Red Hat/Fedora/CentOS**

    ```sh
    sudo dnf install love
    ```

    **Installing Love on Void Linux**

    ```sh
    sudo xbps-install -S love
    ```

    **Additional options for installing Love**

    Love can also be found in the package manager for [most other distributions](https://repology.org/project/love/versions), including BSD and Haiku OS, or installed via [FlatPak](https://flathub.org/en/apps/org.love2d.love2d), or built from source. See the [Love2d](https://love2d.org) website or check your package manager for more information.

    **Download the L5 Starter project**

    You can download the [L5 Starter](https://l5lua.org/L5-starter.zip) (right click -> choose Save As) or from the command line by navigating to the directory where you'd like to save the L5-Starter folder: 

    ```sh
    cd path/to/folder
    wget https://l5lua.org/L5-starter.zip
    ```

    Uncompress it

    ```
    unzip L5-starter.zip
    ```

<script>
document.getElementById('yt').addEventListener('click', function(e) {
  e.preventDefault();
  this.outerHTML = '<iframe width="560" height="315" src="https://www.youtube.com/embed/AP1zTY_w9IU?autoplay=1" allow="autoplay" allowfullscreen></iframe>';
});
</script>

---

Congratulations! You've now installed Love and have the L5 Starter on your computer. 

**Next, see how to [run your L5 programs](running.md).** 

You can also download the L5 source code and the offline documentation below.

### Source code

The [L5 repository](https://github.com/L5lua/L5) is accessible for anyone interested in viewing or modifying the L5 source code. See [contributing](/contributing.md) for ways to contribute to the library or this site.

**Latest version of L5.lua:** [Download L5.lua](https://raw.githubusercontent.com/L5lua/L5/main/L5.lua)

### Offline Documentation

This L5 documentation site is available for download to run offline, with or without images.

* [Download L5lua.org with images (12mb zip)](https://github.com/L5lua/L5-website/archive/refs/heads/gh-pages.zip)
* [Download L5lua.org without images (2mb zip)](https://github.com/L5lua/L5-website/archive/refs/heads/gh-pages-lite.zip)

After downloading, extract the ZIP and serve the folder with a local web server. For a quick local server, navigate to the extracted folder in your command line and run `python -m http.server` (Python 3) or `python -m SimpleHTTPServer` (Python 2).
