# Installation on Linux

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

Congratulations! You've now installed Love and have the L5 Starter on your computer. 


**Next, see how to [run your L5 programs](running.md).**
