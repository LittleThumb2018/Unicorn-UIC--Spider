#coding:utf-8
from Html_Downloader import HtmlDownloader
from Html_Parser import HtmlParser
from db_output import db_output
import csv
from multiprocessing import Process
import time

class SpiderMan(object):
    def __init__(self):
        self.db_name='uicbase.db'
        self.table_miner_name='minerTable'
        self.table_deal_name ='dealTable'
        self.downloader = HtmlDownloader()
        self.parser = HtmlParser()
        self.db_output = db_output(self.db_name)
        self.db_output.creat_miner_table(self.table_miner_name)
        self.db_output.creat_deal_table(self.table_deal_name)
    def miner_crawl(self):
        appkey='9d423c8509bba0591d8dc73521270674'
        page=1
        page_size=400
        root_url = 'http://explorer.uicbase.io/expApi/blocksInfo' \
                   '?appkey=%s' \
                   '&page=%s' \
                   '&pageSize=%s' % (appkey, page,page_size)
        rank_content = self.downloader.download(root_url)
        #print(rank_content)
        #current_page=self.parser.parser_json_page(rank_content)
        #print(current_page)
        total_lines=self.parser.parser_json_totallines(rank_content)
        total_page=int(total_lines/page_size)+1
        print('total_page=%s'%total_page)
        # 构造一个链接
        for page in range(total_page):
            #page=1600+page1
            page +=1
            try:
                #t = time.strftime("%Y%m%d%H%M%S3282", time.localtime())
                root_url = 'http://explorer.uicbase.io/expApi/blocksInfo' \
                           '?appkey=%s' \
                           '&page=%s' \
                           '&pageSize=%s' % (appkey,page,page_size)
                rank_content = self.downloader.download(root_url)
                if rank_content !=None:
                    #print(rank_content)
                    nums=self.parser.parser_json_datum(rank_content)
                    #print(nums[-1])
                    print('挖矿写入第:%s页'%page)
                    self.db_output.insert_datum(self.table_miner_name,nums)
                    self.db_output.commit()
                    if self.db_output.miner_repeat>500:
                        #数据连续重复数量大于500，判定数据更新完成
                        print('挖矿数据更新完成')
                        break
                else:
                    print('挖矿数据获取为空')
            except Exception as e:
                print('miner_crawl:%s'%e)
        return True

    def deal_crawl(self):
        page =1
        pageSize=400
        root_url = 'http://explorer.uicbase.io/expApi/txsInfo' \
                   '?appkey=9d423c8509bba0591d8dc73521270674' \
                   '&page=%s' \
                   '&pageSize=%s' \
                   '&blockNumber=NaN'%(page,pageSize)
        deal_content=self.downloader.download(root_url)
        #current_page = self.parser.parser_json_deal_page(deal_content)
        # print(current_page)
        total_lines = self.parser.parser_json_deal_totallines(deal_content)
        total_page = int(total_lines/pageSize)+1
        print('deal_total_page=%s' % total_page)
        for page in range(total_page):
            page += 1
            #page=total_page-page1
            try:
                root_url = 'http://explorer.uicbase.io/expApi/txsInfo' \
                           '?appkey=9d423c8509bba0591d8dc73521270674' \
                           '&page=%s' \
                           '&pageSize=%s' \
                           '&blockNumber=NaN' % (page, pageSize)
                deal_content = self.downloader.download(root_url)
                if deal_content!=None:
                    # print(rank_content)
                    nums = self.parser.parser_json_deal_datum(deal_content)
                    print('交易数据写入第:%s页' % page)
                    self.db_output.insert_deal_datum(self.table_deal_name, nums)
                    self.db_output.commit()
                    if self.db_output.deal_repeat>400:
                        #数据连续重复数量大于400，判定数据更新完成
                        print('交易数据更新完成')
                        break
                else:
                    print('交易数据获取为空')
            except Exception as e:
                print('deal_crawl:%s' %e)

if __name__=='__main__':
    spider_man = SpiderMan()
    spider_man.miner_crawl()
    spider_man.deal_crawl()
    spider_man.db_output.db_close()
    '''
    P=Process(target= spider_man.miner_crawl)
    print('miner_crawl will start')
    P.start()
    P = Process(target= spider_man.crawl_deal)
    print('deal_crawl will start')  
    P.start() 
    P.join()
    '''
    print('---------END----------')



