#coding:utf-8
from Html_Downloader import HtmlDownloader
from Html_Parser import HtmlParser
from Data_Output import DataOutput
import csv
from multiprocessing import Process
import time

class SpiderMan(object):
    def __init__(self):
        self.downloader = HtmlDownloader()
        self.parser = HtmlParser()
        self.output = DataOutput()
    def crawl(self,filename):
        num = ["takeoff", "number", "timestamp", "hash",
               "parentHash", "author", "authorWalletId", "minerReward", "difficulty",
               "totalDifficulty", "nonce", "extraData", "udid", "lat", "lgt",
               "sha3Uncles", "transactionsRoot", "stateRoot", "miner", "size",
               "gasLimit", "gasUsed", "transactionsCount", "unclesCount"]
        try:
            with open(filename, 'r') as fr1:
                fr_reader = csv.reader(fr1)
                with open('uicbase_old.csv', 'w', newline='') as fw_old:
                    fw_old_writer = csv.writer(fw_old)
                    fw_old_writer.writerows(fr_reader)
            print('写入备份文件uicbase_old.csv')
        except Exception as e:
            print(e)
        # 获得旧文件中最后一个编号
        try:
            fr = open('uicbase_old.csv', 'r')
            fr_reader = csv.reader(fr)
            head_row = next(fr_reader)
            first_row = next(fr_reader)
            last_number = int(first_row[1])
            fr.close()
            print('last_number=%s' % last_number)
        except Exception as e:
            last_number = 1189
            print(e)
            print('last_number=%s' % last_number)
        ff = open(filename, 'w', newline='')
        ff_writer = csv.writer(ff)
        ff_writer.writerow(num)
        ff.close()

        appkey='9d423c8509bba0591d8dc73521270674'
        page=1
        page_size=400
        root_url = 'http://explorer.uicbase.io/expApi/blocksInfo' \
                   '?appkey=%s' \
                   '&page=%s' \
                   '&pageSize=%s' % (appkey, page,page_size)
        rank_content = self.downloader.download(root_url)
        #print(rank_content)
        current_page=self.parser.parser_json_page(rank_content)
        #print(current_page)
        total_page=self.parser.parser_json_totallines(rank_content)
        if page_size!=20:
            total_page = int(total_page/(total_page/page_size))
        print('total_page=%s'%total_page)
        #print('type')
        #print(type(total_page))
        # 构造一个链接
        for page in range(total_page):
            page+=1
            try:
                #t = time.strftime("%Y%m%d%H%M%S3282", time.localtime())
                root_url = 'http://explorer.uicbase.io/expApi/blocksInfo' \
                           '?appkey=%s' \
                           '&page=%s' \
                           '&pageSize=400' % (appkey,page)
                rank_content = self.downloader.download(root_url)
                if rank_content !=None:
                    #print(rank_content)
                    nums=self.parser.parser_json_datum(rank_content)
                    #print(nums[-1])
                    print('挖矿写入第:%s页'%page)
                    if nums[-1][1]>last_number:
                        #print('data_writerows')
                        self.output.data_writerows(filename, nums)
                    else:
                        #print('data_writerow')
                        done = False
                        for num in nums:
                            if num[1]>last_number:
                                self.output.data_writerow(filename,num)
                            else:
                                print('挖矿数据下载完成')
                                done = True
                                break
                        if done == True:
                            break
                else:
                    #return False
                    pass
            except Exception as e:
                print(e)
                return False
        try:
            fw = open(filename, 'a', newline='')
            fw_writer = csv.writer(fw)
            fr = open('uicbase_old.csv', 'r')
            reader = csv.reader(fr)
            next(reader)
            fw_writer.writerows(reader)
            fr.close()
            fw.close()
        except Exception as e:
            print(e)
    def crawl_deal(self,filename):
        num = ["blockNumber", "txhash", "timestamp", "from", "to", "value", "fee",
               "nonce", "data", "fromWalletId", "toWalletId", "gas", "gasPrice"]
        try:
            with open(filename, 'r') as fr1:
                fr_reader = csv.reader(fr1)
                with open('uicbase_deal_old.csv', 'w', newline='') as fw_old:
                    fw_old_writer = csv.writer(fw_old)
                    fw_old_writer.writerows(fr_reader)
            print('写入备份文件uicbase_deal_old.csv')
        except Exception as e:
            print(e)
        # 获得旧文件中最近时间
        try:
            fr = open('uicbase_deal_old.csv', 'r')
            fr_reader = csv.reader(fr)
            head_row = next(fr_reader)
            first_row = next(fr_reader)
            fr.close()
            #print('type(first_row[2])=%s'%type(first_row[2]))
            last_time = int(first_row[2])
            #print('old_deal_last_time=%s' % last_time)
        except Exception as e:
            last_time = 1522029555
            print(e)
            print('deal_last_time=%s' % last_time)
        ff = open(filename, 'w', newline='')
        ff_writer = csv.writer(ff)
        ff_writer.writerow(num)
        ff.close()

        page =1
        pageSize=200
        root_url = 'http://explorer.uicbase.io/expApi/txsInfo' \
                   '?appkey=9d423c8509bba0591d8dc73521270674' \
                   '&page=%s' \
                   '&pageSize=%s' \
                   '&blockNumber=NaN'%(page,pageSize)
        deal_content=self.downloader.download(root_url)
        #current_page = self.parser.parser_json_deal_page(deal_content)
        # print(current_page)
        total_page = self.parser.parser_json_deal_totallines(deal_content)
        if pageSize!=20:
            total_page = int(total_page/(total_page/pageSize))
        print('deal_total_page=%s' % total_page)
        for page in range(total_page):
            page += 1
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
                    #print(nums[-1][2])
                    print('交易数据写入第:%s页' % page)
                    if nums[-1]!=None:
                        #print(type(nums[-1][2]))
                        #print(type(last_time))
                        if nums[-1][2] > last_time:
                            #print('data_writerows')
                            self.output.data_writerows(filename, nums)
                        else:
                            #print('data_writerow')
                            done=False
                            for num in nums:
                                if num[2] > last_time:
                                    self.output.data_writerow(filename, num)
                                else:
                                    print('deal数据下载完成')
                                    done=True
                                    break
                            if done==True:
                                break
                    else:
                        print('nums[-1]=%s'%nums[-1][2])
                else:
                    pass
            except Exception as e:
                print('crawl_deal:%s'%e)
                return False

        try:
            fw = open(filename, 'a', newline='')
            fw_writer = csv.writer(fw)
            fr = open('uicbase_deal_old.csv', 'r')
            reader = csv.reader(fr)
            next(reader)
            fw_writer.writerows(reader)
            fr.close()
            fw.close()
        except Exception as e:
            print(e)


if __name__=='__main__':
    spider_man = SpiderMan()
    filename = '挖矿数据.csv'
    filename_deal ='交易数据.csv'
    #spider_man.crawl_deal(filename_deal)
    #spider_man.crawl(filename)
    P=Process(target= spider_man.crawl,args=(filename,))
    print('P1 will start')
    P.start()
    P = Process(target= spider_man.crawl_deal,args=(filename_deal,))
    print('P2 will start')
    P.start()
    P.join()
    print('---------END----------')



