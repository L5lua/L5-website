## How to Contribute to the L5 Website

Thanks for your interest in contributing to L5 documentation.

Use this repository if you want to:

* Improve reference pages
* Write or edit tutorials
* Add screenshots or examples
* Improve wording, structure, or beginner explanations

If you discover a bug or have an idea for a new feature on the website you'd like to add, please begin by submitting an issue so that we can discuss it.

**For contributing to the L5 library** instead of the website, visit the [L5 code repository](https://github.com/L5lua/L5).

## Working on the site locally

The documentation site is built with [Material for mkdocs](https://squidfunk.github.io/mkdocs-material/).

1. **Fork** this repo so that you have your own independent copy located at *github.com/YOUR-USERNAME/L5-website*.
2. **Clone** your repository to your computer, with GitHub Desktop or in the command line:
```bash
git clone https://github.com/YOUR-USERNAME/L5-website.git
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
* On GitHub open a *Pull Request* from your fork to the main website repo

You do **not** need special permission to fork, and you do **not** need to create a branch in the main repository.

Most contributors work directly on the `main` branch of **their fork**.

### Notes for Contributors

* Don't commit the `site/` folder (it's auto-generated).
* Only edit files in `docs/` (and `mkdocs.yml` if adding a main navigation page)
* The live site is automatically built by GitHub Actions when Pull Requests are merged

### Branches

* [main](https://github.com/L5lua/L5-website/tree/main) is where the site is edited
* [gh-pages](https://github.com/L5lua/L5-website/tree/gh-pages) is built automatically through a [workflow](https://github.com/L5lua/L5-website/blob/main/.github/workflows/deploy.yml) action from main. It serves the github pages site.
* [gh-pages-lite](https://github.com/L5lua/L5-website/tree/gh-pages-lite) is a manually-built branch holding the offline version of the website, without images, for downloading through the [Offline Documentation](https://l5lua.org/download/#offline-documentation) section of the Download page. 

