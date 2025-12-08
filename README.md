# L5 website

Documentation site for [L5](https://github.com/L5lua/L5), the Processing-like creative coding library in Lua.

Visit the site at [L5lua.org](https://l5lua.org).

## TODO

* [X] Finish editing all reference pages and adding screenshots
* [ ] Add tutorial and example pages
* [ ] Add information on contributions and being listed as a contributor

## How to Contribute

This is the website for the L5 documentation site, including the reference. If you'd like to start working on an existing issue, it's suggested you make an issue. 

For contributing to L5 itself (not the website), visit the [L5](https://github.com/L5lua/L5) repo.

If you discover a bug or have an idea for a new feature *on the website* you'd like to add, please begin by submitting an issue so that we can discuss it.

### Working on the site locally

The documentation site is built with [Material for mkdocs](https://squidfunk.github.io/mkdocs-material/).

1. Clone the repository
```bash
git clone https://github.com/L5lua/L5-website.git
cd L5-website
```
2. Install dependencies

```bash
pip install mkdocs-material
```
3. Make your edits
* Edit markdown files in the `docs/` folder
* `mkdocs.yml` lists all pages in the nav
4. Test locally
```bash
mkdocs serve
```
Visit `http://localhost:8000` to preview changes.  
5. Commit and push to your fork
```bash
git add .
git commit -m "Description of changes"
git push origin main
```
6. Create a pull request
* On GitHub open a Pull Request from your fork to the main website repo

### Notes for Contributors

* Don't commit the `site/` folder (it's auto-generated).
* Only edit files in `docs/` (and `mkdocs.yml` if adding a main navigation page)
* The live site is automatically built by GitHub Actions when Pull Requests are merged

### Branches

* [main](https://github.com/L5lua/L5-website/tree/main) is where the site is edited
* [gh-pages](https://github.com/L5lua/L5-website/tree/gh-pages) is built automatically through a [workflow](https://github.com/L5lua/L5-website/blob/main/.github/workflows/deploy.yml) action from main. It serves the github pages site.
* [gh-pages-lite](https://github.com/L5lua/L5-website/tree/gh-pages-lite) is a manually-built branch holding the offline version of the website, without images, for downloading through the [Offline Documentation](https://l5lua.org/download/#offline-documentation) section of the Download page. It is built and deployed via the update-lite.sh script.

## License

This website and its original content are licensed under the [MIT License](LICENSE).

**Exception:** The Reference and Examples pages contain content adapted from [Processing](https://processing.org) and [p5.js](https://p5js.org/) by [p5.js Contributors](https://github.com/processing/p5.js?tab=readme-ov-file#contributors) and [Processing Foundation](https://processingfoundation.org/people), which is licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). 

Love2d installation instructions have been adapted from the Love2d wiki: Getting Started, GNU Free Documentation License 1.3.
