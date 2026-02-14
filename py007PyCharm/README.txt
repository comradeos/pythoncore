`PyCharmMiscProject` directory is always created in $HOME, not default project dir

It's very annoying that a useful function like New Notebook or New Project clutters the home directory with files

Steps to Reproduce 
Set a default project directory (Settings/System Settings) e.g. ~/projects

Restart PyCharm to make sure it's picked up as the new default

Create New Notebook or New Project

Expected Result 
PyCharmMiscProject to be created in ~/projects

Actual Result 
PyCharmMiscProject is created in ~/