<div align="left">
  <b>Language:</b><br />
  <a title="English" href="#">
    <img alt="🇺🇸" width="33" src="https://cdn.jsdelivr.net/npm/country-flag-emoji-json@2.0.0/dist/images/US.svg" />
  </a>
  <a title="中文" href="README_CN.md">
    <img alt="🇨🇳" width="33" src="https://cdn.jsdelivr.net/npm/country-flag-emoji-json@2.0.0/dist/images/CN.svg" />
  </a>
</div>

<h1 align="center">Blade Virtual Module</h1>

<div align="center">
  <a href="https://github.com/Sryml/blade-virtual-module/releases" target="_blank">
    <img alt="GitHub release (latest by date)"
      src="https://img.shields.io/github/v/release/sryml/blade-virtual-module?style=social">
  </a>

  <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/sryml/blade-virtual-module?style=social">

</div>

<br>

### ✨ Blade of Darkness Virtual Python Module for Code Completion and Type Hints

This Python package provides code completion and type hints for C/C++ extension modules in IDEs like VSCode.  
It effectively enhances developers' coding efficiency and accuracy.

<img src="https://github.com/Sryml/blade-virtual-module/blob/main/demo1.gif" width="800" />

## 🌟 Requirements

- Python version >= 3.8

## 📖 Installation

1. Install the `Bladex` package from the command line.
   ```batch
   pip install Bladex
   ```
2. Install the `Python` and `Pylance` extensions in VSCode.
3. Right-click on the project root directory in VSCode and open folder settings.  
   Search for `python.analysis.typeCheckingMode` and set it to `basic`.

#### For code completion with other modules (e.g Raster), you need to add the path manually:

1. Create a file named `.vscode/settings.json` in the project's root directory.
2. Add the following content to the file and modify the Python installation path:

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

The `Python39` folder represents the Python version used in this project. If you have a different version installed, you should modify the path accordingly.
You can use `pip show Bladex` to check the package's installation location.

_The `settings.json` file follows JSON syntax, ensure that your edits are correct._

## 💡 Issues

To report bugs or discuss features, please use [Issues](https://github.com/Sryml/blade-virtual-module/issues) section.

## 📄 Reference

- Blade of Darkness Scripts

## 💗 Thanks

- Rebel Act Studios, Fire Falcom, General Arcade
- SNEG
- smartblade
- OpenAI's ChatGPT
