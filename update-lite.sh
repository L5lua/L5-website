#!/bin/bash

# This script updates the offline documentation without images, for downloading
# URL for the downloadable zip is linked at https://l5lua.org/download/#offline-documentation

echo "Updating gh-pages-lite..."
git fetch origin gh-pages
git checkout gh-pages-lite
git merge origin/gh-pages
rm -rf assets/images/ assets/examples/ assets/tutorials/ reference/assets/
git add -A
git commit -m "Update lite version (remove images)"
git push origin gh-pages-lite
git checkout main
echo "Done! gh-pages-lite updated."
