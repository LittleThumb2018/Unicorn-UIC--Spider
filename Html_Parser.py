# coding:utf-8
import json
import time

class HtmlParser(object):
    def parser_json_page(self,response):
        '''
        解析挖矿数据当前页码
        :param response: 下载器返回数据
        :return:
        '''
        if response !=None:
            try:
                value = json.loads(response)
                page = value.get('resData').get('page')
                return page
            except Exception as e:
                print('parser_json_page error:%s'%e)
                return None
        return None
    def parser_json_totallines(self, response):
        '''
        解析挖矿数据总行数
        :param response: 下载器返回数据
        :return: 挖矿数据总行数
        '''
        if response!=None:
            try:
                value = json.loads(response)
                total = value.get('resData').get('total')
                return total
            except Exception as e:
                print('parser_json_totalpage:%s'% e)
                return None
        else:
            return  None

    def parser_json_datum(self,response):
        '''
        #从动态加载的链接中提取需要的字段
        解析响应
        :param response:下载器返回数据
        :return:
        '''
        if response!=None:
            try:
                value = json.loads(response)
                lists=value.get('resData').get('list')
                #len_list =len(lists)
                '''
                num = ["takeoff", "number", "timestamp", "hash",
                       "parentHash", "author", "authorWalletId", "minerReward", "difficulty",
                       "totalDifficulty", "nonce", "extraData", "udid", "lat","lgt",
                       "sha3Uncles", "transactionsRoot", "stateRoot", "miner", "size",
                       "gasLimit", "gasUsed", "transactionsCount", "unclesCount"]
                '''
                nums=[]
                for list in lists:
                    takeoff=list.get('takeoff')
                    #区块高度
                    number = list.get('number')
                    #print(number)
                    #区块产生时间
                    timestamp =time.ctime(list.get('timestamp'))
                    #timestamp = time.strftime('%Y%m%d%H%M%S',)
                    #hash值
                    hash = list.get('hash')
                    #父hash值
                    parentHash = list.get('parentHash')
                    #矿工
                    author = list.get('author')
                    #设备指纹
                    authorWalletId= list.get('authorWalletId')
                    #奖励
                    minerReward = list.get('minerReward')
                    #区块难度
                    difficulty = list.get('difficulty')
                    #总难度
                    totalDifficulty = list.get('totalDifficulty')

                    nonce = list.get('nonce')
                    extraData = list.get('extraData')
                    udid = list.get('udid')
                    lat = list.get('lat')
                    lgt = list.get('lgt')
                    sha3Uncles = list.get('sha3Uncles')
                    #logsBloom= list.get('logsBloom')
                    transactionsRoot= list.get('transactionsRoot')
                    stateRoot= list.get('stateRoot')
                    miner = list.get('miner')
                    size= list.get('size')
                    gasLimit= list.get('gasLimit')
                    gasUsed= list.get('gasUsed')
                    transactionsCount= list.get('transactionsCount')
                    unclesCount= list.get('unclesCount')
                    num = [takeoff, number, timestamp, hash,
                           parentHash, author, authorWalletId, minerReward, difficulty,
                           totalDifficulty, nonce, extraData, udid, lat,lgt,
                           sha3Uncles, transactionsRoot, stateRoot, miner, size,
                           gasLimit, gasUsed, transactionsCount, unclesCount]
                    #print(num)
                    nums.append(num)
                return nums
            except Exception as e:
                print('parser_json_datum error :%s'%e)
                return None
        else:
            return None

    def parser_json_deal_page(self,response):
        '''
        解析交易数据当前页码
        :param response: 下载器返回数据
        :return: 交易数据当前页码
        '''
        if response!=None:
            try:
                value = json.loads(response)
                page = value.get('resData').get('page')
                return page
            except Exception as e:
                print('parser_json_deal_page error:%s'%e)
                return None
        else:
            return None

    def parser_json_deal_totallines(self, response):
        '''
        解析交易数据总行数
        :param response: 下载器获取的数据
        :return: 交易数据总行数
        '''
        if response!=None:
            try:
                value = json.loads(response)
                total = value.get('resData').get('total')
                return total
            except Exception as e:
                print('parser_json_totalpage:%s'% e)
                return None
        else:
            return None

    def parser_json_deal_datum(self,response):
        '''
        #从动态加载的链接中提取需要的字段
        解析响应
        :param response:下载器数据
        :return:交易数据列表
        '''
        if response!=None:
            try:
                value = json.loads(response)
                lists=value.get('resData').get('list')
                #len_list =len(lists)
                num = ["blockNumber", "txhash","timestamp","from","to","value","fee",
                       "nonce","data","fromWalletId","toWalletId","gas","gasPrice"]
                len_num=len(num)
                nums=[]

                #nums.append(num)
                for list in lists:
                    temp = []
                    for n in range(len_num):
                        temp.append(list.get(num[n]))
                    nums.append(temp)
                    #print('temp=%s'%temp)
                #print('nums=%s'%nums)
                return nums
            except Exception as e:
                print('parser_json_deal_datum error :%s'%e)
                return None
        else:
            return None



