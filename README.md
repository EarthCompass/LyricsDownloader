# LyricsDownloader

**挺垃圾的 不是很好用**

使用Python2

使用 tinytag 请先安装

`pip install tinytag`

歌曲必须自带 歌手 歌名 信息

使用网易云api，目前只能下载flac歌曲歌词，搜索结果匹配规则很脑残，有不明错误未debug，语法稀烂，只在Windows上试用过

## 已知bug
* 有些目录内文件无法扫出
* 某些奇怪的歌名会出错(已做处理，程序不会终止但也不会下载)
* 有些纯音乐会下载歌词，无内容(很快会修复)

## TO DO LIST
* 多格式文件支持
* 匹配规则升级
* 让代码更优雅
