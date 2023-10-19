<h1 align="center">Blade Virtual Module</h1>

<div align="center">
<a href="https://github.com/Sryml/blade-virtual-module/releases" target="_blank">
  <img alt="GitHub release (latest by date)" src="https://img.shields.io/github/v/release/sryml/blade-virtual-module?style=social">
</a>

  <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/sryml/blade-virtual-module?style=social">

</div>

<br>

### ✨ Blade of Darkness virtual python module for code completion

This python package is used to provide code completion and type hints in the IDE (e.g VSCode).

<img src="https://github.com/Sryml/blade-virtual-module/blob/main/demo1.gif" width="800" />

## 🌟 Requirements

- Python version >= 3.8

## 📖 Install

```batch
pip install Bladex
```

#### Code completion for other modules (such as Raster) requires manually adding paths (vscode configuration):

1. Create the folder `.vscode` in the game root directory
2. Create the file `.vscode/settings.json`
3. Copy the following content into the file and modify the python path

```json
{
  "python.autoComplete.extraPaths": [
    "~/AppData/Local/Programs/Python/Python39/Lib/site-packages/Bladex/__ext__"
  ],
  "python.analysis.extraPaths": [
    "~/AppData/Local/Programs/Python/Python39/Lib/site-packages/Bladex/__ext__"
  ]
}
```

The `Python39` folder is the python version used by this project. If the version you are using is not py3.9, you will need to modify the path. You can use `pip show Bladex` to view the installation location of the package.

## 🐞 Issues

To report bugs/discuss functions, please use [issues](https://github.com/Sryml/blade-virtual-module/issues).

## 📄 Reference

- Blade of Darkness Scripts

## 💗 Thanks

- Rebel Act Studios, Fire Falcom, General Arcade
- SNEG
- smartblade
