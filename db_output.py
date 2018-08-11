import sqlite3
class db_output(object):
    def __init__(self,db_name):
        #创建、打开数据库
        self.con = sqlite3.connect(db_name)
        #创建游标对象
        self.cur = self.con.cursor()
        self.miner_repeat =0
        self.deal_repeat =0
    #建挖矿数据表
    def creat_miner_table(self,table_name):
        #建表
        try:
            self.cur.execute('CREATE TABLE %s'
                             '(takeoff integer,'
                             'number integer PRIMARY KEY , '
                             'timestamp varchar(30), '
                             'hash varchar(200),'
                             'parentHash varchar(200), '
                             'author varchar(100), '
                             'authorWalletId varchar(50), '
                             'minerReward decimal(10,8), '
                             'difficulty integer,'
                             'totalDifficulty integer, '
                             'nonce varchar(50), '
                             'extraData varchar(500), '
                             'udid varchar(50), '
                             'lat decimal(10,8),'
                             'lgt decimal(10,8),'
                             'sha3Uncles varchar(100), '
                             'transactionsRoot varchar(100), '
                             'stateRoot varchar(100), '
                             'miner varchar(100), '
                             'size integer,'
                             'gasLimit integer, '
                             'gasUsed integer, '
                             'transactionsCount integer, '
                             'unclesCount integer)'%table_name)
        except Exception as e:
            print(e)
            print('挖矿数据表已存在')
    #插入挖矿数据
    def insert_miner_data(self,table_name,num):
        # 插入数据
        try:
            self.cur.execute('INSERT INTO %s VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'%table_name,
                             (num[0],num[1],num[2],num[3],num[4],num[5],num[6],num[7],num[8],num[9],num[10],num[11],num[12],
                              num[13],num[14],num[15],num[16],num[17],num[18],num[19],num[20], num[21],num[22],num[23]))
            self.miner_repeat=0#数据连续重复次数
            #print('写入数据库成功')
        except Exception as e:
            self.miner_repeat+=1
            #print(e)

    def insert_datum(self,table_name,nums):
        for num in nums:
            # 插入数据
            self.insert_miner_data(table_name,num)
    #创建交易数据表
    def creat_deal_table(self,table_name):
        #建表
        try:
           # num = ["blockNumber", "txhash", "timestamp", "from", "to", "value", "fee",
           #        "nonce", "data", "fromWalletId", "toWalletId", "gas", "gasPrice"]
            self.cur.execute('CREATE TABLE %s'
                             '(blockNumber integer,'
                             'txhash varchar(100) PRIMARY KEY , '
                             'timestamp varchar(30), '
                             '"from" varchar(100),'
                             '"to" varchar(100), '
                             'value decimal(20,8), '
                             'fee decimal(20,8), '
                             'nonce varchar(50), '
                             'data varchar(500),'
                             'fromWalletId varchar(100), '
                             'toWalletId varchar(100), '
                             'gas integer, '
                             'gasPrice decimal(20,8))'%table_name)
        except Exception as e:
            print(e)
            print('交易数据表已存在')

    def insert_deal_data(self,table_name,num):
        # 插入数据
        try:
            self.cur.execute('INSERT INTO %s VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)'%table_name,
                             (num[0],num[1],num[2],num[3],num[4],num[5],num[6],num[7],num[8],num[9],num[10],num[11],num[12]))
            self.deal_repeat=0 #交易数据连续重复次数置0
        except Exception as e:
            self.deal_repeat+=1 #交易数据连续重复次数+1
            #print('insert_deal_data:%s'%e)

    def insert_deal_datum(self,table_name,nums):
        for num in nums:
            # 插入数据
            self.insert_deal_data(table_name,num)

    #提交操作
    def commit(self):
        self.con.commit()
    #回滚
    def roolback(self):
        self.con.rollback()

    def db_close(self):
        self.con.close()


'''
test =db_output('uicbase.db')
test.creat_table('minerTable2')

#test.quchong('minerTable2')
num=[14, 782982, 'Mon Aug  6 18:32:05 2018', '0x6ee087d2ad4f28579ea092d9ba1892669689fb64c6ac1b192e729d53dddf22f2', '0xb7ce522b2aada56907bfa1e3304e711be13573d88dda51076a8a555fa569bf93', 'ux68e6b7494c7d1669bc5da46db5712163cea83b08', '5b1faaa340e1f01e16caf11c', 15, 252283243, 57592679912333, '0x2f333fcc8c736762', '0x526a42454e4467334d6a6735516a55334e5441344d7a5130516b5a424d30524552544d344d555243515549734b4445794d4334344d5463734d6a6b754e546b314f436b3d', 'F0D487289B57508344BFA3DDE381DBAB', 120.817, 29.5958, '0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347', '0x56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421', '0x6d31cc86ef12dfc8ae23911b9f6f57678f46cf4c1c13b24ba5dab5502be99f27', '0x68e6b7494c7d1669bc5da46db5712163cea83b08', 0, 210000000, 0, 0, 0]
test.insert_data('minerTable2',num)
num=[14, 782983, 'Mon Aug  6 18:32:05 2018', '0x6ee087d2ad4f28579ea092d9ba1892669689fb64c6ac1b192e729d53dddf22f2', '0xb7ce522b2aada56907bfa1e3304e711be13573d88dda51076a8a555fa569bf93', 'ux68e6b7494c7d1669bc5da46db5712163cea83b08', '5b1faaa340e1f01e16caf11c', 15, 252283243, 57592679912333, '0x2f333fcc8c736762', '0x526a42454e4467334d6a6735516a55334e5441344d7a5130516b5a424d30524552544d344d555243515549734b4445794d4334344d5463734d6a6b754e546b314f436b3d', 'F0D487289B57508344BFA3DDE381DBAB', 120.817, 29.5958, '0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347', '0x56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421', '0x6d31cc86ef12dfc8ae23911b9f6f57678f46cf4c1c13b24ba5dab5502be99f27', '0x68e6b7494c7d1669bc5da46db5712163cea83b08', 0, 210000000, 0, 0, 0]

test.insert_data('minerTable2',num)
num=[14, 782984, 'Mon Aug  6 18:32:05 2018', '0x6ee087d2ad4f28579ea092d9ba1892669689fb64c6ac1b192e729d53dddf22f2', '0xb7ce522b2aada56907bfa1e3304e711be13573d88dda51076a8a555fa569bf93', 'ux68e6b7494c7d1669bc5da46db5712163cea83b08', '5b1faaa340e1f01e16caf11c', 15, 252283243, 57592679912333, '0x2f333fcc8c736762', '0x526a42454e4467334d6a6735516a55334e5441344d7a5130516b5a424d30524552544d344d555243515549734b4445794d4334344d5463734d6a6b754e546b314f436b3d', 'F0D487289B57508344BFA3DDE381DBAB', 120.817, 29.5958, '0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347', '0x56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421', '0x6d31cc86ef12dfc8ae23911b9f6f57678f46cf4c1c13b24ba5dab5502be99f27', '0x68e6b7494c7d1669bc5da46db5712163cea83b08', 0, 210000000, 0, 0, 0]

test.insert_data('minerTable2',num)
test.insert_data('minerTable2',num)
test.commit()
test.db_close()

#test.cur.execute('select * from minerTable WHERE number=%s'%num)
#test.cur.execute('SELECT * FROM minerTable WHERE number=782637')
#res = test.cur.fetchall()
#if res!=None:
#    print(len(res))
print('ok')
'''
