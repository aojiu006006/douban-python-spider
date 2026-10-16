# douban-python-spider
python爬虫应用：豆瓣数据采集与导出
# 豆瓣Top250数据采集与导出工具

这是一个基于 Python 的实战爬虫项目，适用于接取数据采集、信息爬取等相关外包需求。

## 🛠️ 技术栈
* 语言：Python 3
* 网络请求：Requests
* 网页解析：BeautifulSoup4
* 数据处理：Pandas

## ✨ 功能特点
* **自动翻页**：支持抓取豆瓣Top250全部10页共250条数据。
* **防IP频控**：内置 `time.sleep` 节流机制，保证运行稳定。
* **异常捕获**：内置容错处理，遇到缺失数据的条目自动跳过。
* **结构化导出**：自动清洗数据并导出为 Excel 可直接打开的 `CSV` 文件（UTF-8-sig 编码，中文无乱码）。

## 🚀 使用方法
1. 安装依赖：
   `pip install requests beautifulsoup4 pandas lxml`
2. 运行代码：
   `python douban.py`
3. 运行完成后，当前目录下会生成 `豆瓣Top250.csv` 文件。

## 📬 联系我
如果你有数据采集、爬虫定制等需求，欢迎联系我。
