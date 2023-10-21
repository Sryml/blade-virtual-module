<div align="left">
  <b>语言:</b><br />
  <a title="English" href="https://github.com/Sryml/blade-virtual-module/blob/v1.0.4/README.md">
    <img alt="🇺🇸" width="33" src="https://cdn.jsdelivr.net/npm/country-flag-emoji-json@2.0.0/dist/images/US.svg" />
  </a>
  <a title="中文" href="#">
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

### ✨ 用于代码补全和类型提示的 BOD 虚拟 Python 模块

此 Python 包在 IDE（例如 VSCode）中提供 C/C++扩展模块的代码补全和类型提示，能够有效提高开发人员的编码效率和准确率。

<img src="https://github.com/Sryml/blade-virtual-module/blob/main/demo1.gif?raw=true" width="800" />

## 🌟 需求

- Python 版本 >= 3.8

## 📖 安装

1. 从命令行安装`Bladex`包
   ```batch
   pip install Bladex
   ```
2. 在 VSCode 中安装`Python`和`Pylance`扩展
3. 在 VSCode 工作区中右键项目根目录并打开文件夹设置  
   搜索设置`python.analysis.typeCheckingMode`然后将其设置为`basic`即可

**要更新包可运行:**

```batch
pip install --upgrade Bladex
```

#### 对于其它模块的代码补全(例如 Raster)需手动添加路径:

1. 在项目根目录创建文件`.vscode/settings.json`
2. 添加以下内容到文件并修改 Python 安装路径:

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

`Python39`文件夹是该项目使用的 Python 版本。如果你安装的是不同版本，则要相应的修改路径。  
可以使用`pip show Bladex`查看包的安装位置。

_`settings.json`文件遵循 json 语法，确保你的编辑是正确的_

## 📃 变更日志

参阅 [ChangeLog.md](https://github.com/Sryml/blade-virtual-module/blob/v1.0.4/docs/zh-CN/ChangeLog.md)

## 💡 问题

要反馈错误/讨论功能，请使用[Issues](https://github.com/Sryml/blade-virtual-module/issues)

## 📄 参考

- Blade of Darkness 脚本

## 💗 致谢

- Rebel Act Studios, Fire Falcom, General Arcade
- SNEG
- smartblade
- OpenAI 的 ChatGPT
