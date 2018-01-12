# TopSup-for-iOSAndMac

在 macOS 上更优雅的使用答题辅助脚本, 基于 [TopSup](https://github.com/Skyexu/TopSup) 修改，删除了安卓平台相关代码

## 说明

Mac 和 iOS 双平台虽然可以使用 [WDA](https://github.com/facebook/WebDriverAgent) 来到达获取屏幕当前截图的目的，但是经体验 WDA 不仅安装非常多坑，譬如获取不到 ip、证书 或 端口转发 等问题，而且在 iPhone X 机型上经常无故断开，导致无法获取截图。基于这种情况所有想到了那外一种解决方案，利用 **QuickTime**。这里仅仅提供一种思路，可以参考后然后基于原仓库修改。

概况:
1. 利用 QuickTime(或 AirServer 其他方案) 将 iPhone 投屏到 Mac 上
2. 利用 macOS 自带的 **screencapture** 命令截图图片
3. 利用原脚本完成剩余操作


## 具体步骤

#### 一、 利用 QuickTime(或 AirServer 其他方案) 将 iPhone 投屏到 Mac 上 
打开 **QuickTime Player.app**， 点击菜单栏->文件->新建影片录制, 点击录制按钮旁边的小箭头，选择你的 iPhone 即可，[具体教程](https://jingyan.baidu.com/article/59703552e714e48fc007402d.html)

![](http://ojpb4w81b.bkt.clouddn.com/18-1-12/84684463.jpg)

#### 二、利用 macOS 自带 screencapture 命令截图图片

**macOS** 中内置了一个截图命令，既 **screencapture**，可通过 ```screencapture --help``` 查看帮助，其中有个 **-R** 参数可以指定截图区域，既 x,y,w,h。用过该命令获取 问题 和 答案选项 区域的截图

```
$ screencapture -R"20,190,310,100" ./question_screenshot.png
```

通过 **Python** os 模块中的 system 来调用 **shell** 命令

```
import os
os.system("screencapture -R\"20,190,310,100\" ./question_screenshot.png")
```


#### 三、参考[原脚本说明](https://github.com/Skyexu/TopSup) 配置/安装 ocr 及相应库即可
参考[原脚本说明](https://github.com/Skyexu/TopSup) 配置/安装 ocr 及相应库。

参考 **getQuestionAnswer.py** 删除 WDA 相关代码，修改自己的坐标值，建议将 QuickTime 的窗口缩小再测量。



⚠️ 此 Demo 不会保持与原仓库的更新，仅供参考思路
