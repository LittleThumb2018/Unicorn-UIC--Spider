# Unicorn-UIC--Spider
这是一个用Python写的长虹R8手机挖矿数据爬虫。从服务器中下载挖矿与交易数据，并保存在本地。提供两种存储方式：1：存储在sqlite3数据库中；2：存储在csv文件中。同时包含部分数据分析。
文件描述：
1、Html_Downloader.py为网页下载器，提供多种代理访问。超时设定为200秒，并且最多尝试10次。成功返回服务器数据，失败返回None
2、Html_Parser.py为数据解析器。解析由网页下载器返回的数据。文件中提供6个函数，分别为
      def parser_json_page(self,response)  解析挖矿数据当前页码，返回当前页码
      def parser_json_totallines(self, response)解析挖矿数据总行数，返回挖矿数据总行数
      def parser_json_datum(self,response)解析返回的有用数据，返回挖矿数据列表
      def parser_json_deal_page(self,response)解析交易数据当前页码，返回交易数据当前页码
      def parser_json_deal_totallines(self, response)解析交易数据总行数，返回交易数据总行数
      def parser_json_deal_datum(self,response)解析交易数据，返回交易数据列表
      
3、Data_Output.py为数据存储器，将下载的数据存储为csv文件
4、UIC_Spider.py为爬虫调度器，调用下载器、解析器、存储器，下载交易与挖矿数据，并存储为csv文件

5、db_output.py为数据库存储器，实现将下载解析出来的数据存储到数据库中。
6、UIC_db.py为数据库版爬虫和调度器
7、dealwith_dealTable.py处理数据库中交易数据
8、dealwith_minerTable.py处理数据库中挖矿数据
9、list_uic_cout.py处理交易与挖矿数据，画出UIC钱包持币数量分析的直方图
