# L5 website

Documentation site for [L5](https://github.com/L5lua/L5), the Processing-like creative coding library in Lua.

Visit the site at [L5lua.org](https://l5lua.org).

## TODO

* [X] Finish editing all reference pages and adding screenshots
* [X] Add tutorial and example pages
* [ ] Add information on contributions and being listed as a contributor

## How to Contribute

This is the website for the L5 documentation site, including the reference. If you'd like to start working on an existing issue, it's suggested you make an issue. 

For contributing to L5 itself (not the website), visit the [L5](https://github.com/L5lua/L5) repo.

If you discover a bug or have an idea for a new feature *on the website* you'd like to add, please begin by submitting an issue so that we can discuss it.

### Working on the site locally

The documentation site is built with [Material for mkdocs](https://squidfunk.github.io/mkdocs-material/).

1. Fork the repository on Github.
2. Clone the repository to your computer. Command line description follows but this could also be done in Github Desktop.
```bash
git clone https://github.com/L5lua/L5-website.git
cd L5-website
```
3. Install dependencies
```bash
pip install mkdocs-material
```
*If you are working on an OS with an externally-managed python environment, you may have additional steps. For example, in Debian/Ubuntu-based systems:*
```sh
sudo apt install pipx
pipx ensurepath
# then restart shell or source your config
source ~/.bashrc  # or your shell config
pipx install mkdocs
pipx inject mkdocs mkdocs-material
```

*Or in Void Linux:* 
```sh
sudo xbps-install -S python3-pipx
pipx install mkdocs
pipx inject mkdocs mkdocs-material
```

4. Make your edits
* Edit markdown files in the `docs/` folder
* `mkdocs.yml` lists all pages in the nav
5. Test locally
```bash
mkdocs serve
```
Visit `http://localhost:8000` to preview changes.  
6. Commit and push to your fork
```bash
git add .
git commit -m "Description of changes"
git push origin main
```
7. Create a pull request
* On GitHub open a Pull Request from your fork to the main website repo

## Notes for Contributors

* Don't commit the `site/` folder (it's auto-generated).
* Only edit files in `docs/` (and `mkdocs.yml` if adding a main navigation page)
* The live site is automatically built by GitHub Actions when Pull Requests are merged

### Working with images

We use the compressed webp file format for most images, as well as a second version of the same image in jpg format. *webp* generally allows the smallest image size, for faster page loading. But as a fallback, if someone's browser can't display webp images then it will show a *jpg* file. **You should add both a webp image and an equivalently named jpg image for all static images**. We have the *image_fallback.py* hook script that the static site generator runs that adds the special `<picture>` tag for all webp images rendered into HTML pages.

### Branches

* [main](https://github.com/L5lua/L5-website/tree/main) is where the site is edited
* [gh-pages](https://github.com/L5lua/L5-website/tree/gh-pages) is built automatically through a [workflow](https://github.com/L5lua/L5-website/blob/main/.github/workflows/deploy.yml) action from main. It serves the github pages site.
* [gh-pages-lite](https://github.com/L5lua/L5-website/tree/gh-pages-lite) is a manually-built branch holding the offline version of the website, without images, for downloading through the [Offline Documentation](https://l5lua.org/download/#offline-documentation) section of the Download page. It is built and deployed via the update-lite.sh script.

## License

This website uses the MIT license, with the exception of pages listing other licenses. Reference pages contain content adapted from [p5.js](https://p5js.org/) and [Processing](https://processing.org) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). 

Tutorial and example pages are MIT licensed unless otherwise noted. Pages adapted from other sources include license and attribution at the bottom.

Love2d installation instructions have been adapted from the Love2d wiki: Getting Started, GNU Free Documentation License 1.3.
