# 为 PaddleGame 做出你的贡献🏅

&emsp;  欢迎大家对我们提出宝贵意见🥰！我们期待大家为PaddleGame做出贡献，可以是：

- ⁉错误报告
- 🔖讨论代码的当前状态
- 🎯提交代码修复
- 🧩提出新的产品和功能
- 🕹成为维护者

&emsp;  由于我们社区开发者们的共同努力，PaddleGame 运行良好，对于您贡献的每一个小改进，您都将帮助推动 AI 的前沿发展😃!

## ⭕提交拉取请求 (PR)⚙

&emsp;  提交 PR 很容易😀！你可以通过提交pr提出新的产品和功能、提交代码修复等贡献，此处演示两种提交PR的方式：

### 🔻方式一：在线直接提交

#### &emsp;  1. 选择要更新的文件

&emsp;  通过在 GitHub 中单击它来选择更新。`requirements.txt`

#### &emsp;  2. 点击“编辑此文件”

&emsp;  该按钮位于右上角。

#### &emsp;  3. 进行更改

&emsp;  将版本从 更改为 。`matplotlib``3.2.2``3.3`

#### &emsp;  4. 预览更改并提交 PR

&emsp;  单击**“预览更改**”选项卡以验证更新。在屏幕底部选择“为此提交创建新分支”，为您的**分支**分配一个描述性名称，例如，然后单击绿色的**提议 “更改”**按钮。全部完成，您的 PR 现在已提交给 YOLOv5 进行审核和批准`fix/matplotlib_version`😇!

### 🔻方式二：本地修改提交

&emsp;  本地修改提交适合较大的改动或增加新文件、调试代码等情况，该方法要求按装Git.

#### &emsp;  1. fork开源项目

&emsp;  找到要提交PR的项目，先将该项目fork自己的代码仓。

#### &emsp;  2. 克隆开源项目

&emsp;  将需要提交PR的项目克隆到本地。

```
//打开CMD或者打开Git Bash Here
git clone git@github.com:user_name/PaddleGame.git
```

#### &emsp;  3.创建新的分支

&emsp;  提交PR时需要.为了防止在主分支上修改影响主分支代码，此处创建一个分支用于代码的修改。

```
cd PaddleGame // 切换到项目路径
git checkout -b mybranch //创建名为mybranch的分支
git branch //查看已经创建的分支 如图有mybranch和main两个分支
git checkout mybranch // 切换到分支
```

&emsp;  切换好分支后就可以直接根据自己需求修改项目。

#### &emsp;  4. 修改提交项目代码

&emsp;  将代码修改后，执行``git status`` 命令查看修改了哪些文件，接着使用``git add 修改的文件名``添加到暂存区，最后使用``git commit -m "日志信息" 文件名``提交到本地库。

```
git status // 查看库状态
git add 文件名 // 将修改的文件存放到暂存区
git commit -m "日志信息" 文件名 // 将修改的文件提交到本地库
```

&emsp;  最后将本地项目代码提交到远程GitHub上

```
git push --set-upstream main mybranch
```

&emsp;  进入GitHub项目，切换到mybranch分支，查看是否修改成功。



&emsp;  切换到**主分支**，将分支mybranch代码合并到主分支，查看是否可以与主分支合并成功。

```
git checkout main // 切换到主分支
git merge mybranch  // 合并派生分支到主分支
```

&emsp;  合并成功后，将主分支推送到代码仓。

```
git add .  // 将修改的文件存放到暂存区
git commit -m "日志信息" // 将修改的文件提交到本地库
git push origin main // 推送到远程仓库
```

&emsp;  在GitHub切换到master主分支，查看是否合并成功

#### &emsp;  4.提交pr请求

&emsp;  进入自己`fork`的项目中，点击`Pull requests`



&emsp;  点击`Create pull requests`



&emsp;  最后点击`Create pull request`，提交后开源人将会收到你的合并请求。



&emsp;  若采纳了你提交的pr，`Contributors`一栏将会显示你的头像 😃



## ⭕提交错误报告🐛

如果您发现 PaddleGame 存在问题，您可以提交错误报告！

为了更好的解决该问题，请您提供详细的问题描述以及出现问题的情况。如果你能提供错误的解决方案或者一个小的案例，这是再好不过的。针对使用中发现的各种错误，可以通过提交[Issues ](https://github.com/guojin-yan/PaddleGame/issues)等待技术人员进行解决。

## ⭕编码规范📇

&emsp;  为保证项目编码风格一致，在提交PR时，要遵守该项目编码规范。

##### 🔻代码样式

&emsp;  我们的所有代码遵循Google 开源项目风格指南，包括C/C++、Python。

&emsp;  🔸C++ 风格指南：[中文 ](https://zh-google-styleguide.readthedocs.io/en/latest/google-cpp-styleguide/contents/)  [English](https://google.github.io/styleguide/cppguide.html)

&emsp;  🔸Python 风格指南：[中文](https://zh-google-styleguide.readthedocs.io/en/latest/google-python-styleguide/contents/)  [English](https://google.github.io/styleguide/pyguide.html)

## ⭕许可证🉑

您所提交的贡献，默认您同意采用[Apache-2.0 license](https://github.com/PaddlePaddle/Paddle/blob/develop/LICENSE).