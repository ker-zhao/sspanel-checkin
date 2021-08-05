# sspanel-autocheckin-py
SSPanel 流量自动签到脚本

## 相关说明

- 适用于使用 SSPanel 用户管理面板搭建的网站，网站页面底部会有 `Powered by SSPANEL` 字段
- 支持一日多次签到
- 支持推送签到信息到微信

## 使用方法

### 方式一：Github Actions（推荐）

> Fork 后的项目 Github Actions 默认处于关闭状态，需要手动开启 Actions，执行一次工作流。后续定时任务(cron)才会自动执行。具体操作信息看：[关于定时任务不执行](#关于定时任务不执行)。

Fork 该仓库，进入仓库后点击 `Settings`，右侧栏点击 `Secrets`，点击 `New secret`。添加以下值：
* USER_INFO: 格式：签到站点|邮箱|密码。 示例：https://abc.com|xiaoming@qq.com|password
* SEND_KEY（非必须）: 微信推送 ，填写自己申请[Server 酱](http://sc.ftqq.com/?c=code)的`SC KEY`。

定时任务将于每天上午 `9:30` 分和晚上 `20:30` 执行，如果需要修改请编辑 `.github/workflows/work.yaml` 中 `on.schedule.cron` 的值（注意，该时间时区为国际标准时区，国内时间比其快8个小时。）。

## 鸣谢
谢谢Mao Wang，此使用说明基本是从他那里搬过来。下面贴出他的项目地址，功能更多。我写的这个主要是个人练手使用，优点是python编写，而且代码非常的简短易读。

https://github.com/isecret/sspanel-autocheckin

谢谢zitto，此脚本参照了他的代码。下面贴出他的项目地址，也非常简单易懂，不过不支持github action运行。

https://github.com/zhjc1124/ssr_autocheckin
