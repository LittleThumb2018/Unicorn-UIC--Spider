import sqlite3

class deal_minerTable(object):
    def __init__(self):
        self.con=sqlite3.connect('uicbase.db')
        # 创建游标对象
        self.cur = self.con.cursor()

    def wallet_miner_order(self,num=200):
        sql='select author, sum(minerReward) from minerTable GROUP by author ORDER BY sum(minerReward) DESC'
        result=self.cur.execute(sql)
        temp=result.fetchmany(num)[:]
        temp_list = []
        for te in temp:
            te_temp = list(te)
            temp_list.append(te_temp)
        return temp_list
    def wallet_miner_order_all(self):
        sql='select author, sum(minerReward) from minerTable GROUP by author ORDER BY sum(minerReward) DESC'
        result=self.cur.execute(sql)
        temp=result.fetchall()[:]
        temp_list = []
        for te in temp:
            te_temp = list(te)
            temp_list.append(te_temp)
        return temp_list
     #按钱包地址挖矿排序
    def walletId_miner_order(self,num=200):
        sql='SELECT authorWalletId, sum(minerReward) FROM minerTable GROUP BY authorWalletId ORDER BY sum(minerReward) DESC'
        result=self.cur.execute(sql)
        temp = result.fetchmany(num)[:]
        temp_list = []
        for te in temp:
            te_temp = list(te)
            temp_list.append(te_temp)
        return temp_list
    def walletId_miner_order_all(self):
        sql='SELECT authorWalletId, sum(minerReward) FROM minerTable GROUP BY authorWalletId ORDER BY sum(minerReward) DESC'
        result=self.cur.execute(sql)
        temp = result.fetchall()[:]
        temp_list=[]
        for te in temp:
            te_temp=list(te)
            temp_list.append(te_temp)
        return temp_list

if __name__=='__main__':
    deal_miner=deal_minerTable()
    wallet_miner=deal_miner.wallet_miner_order()
    walletId_miner=deal_miner.walletId_miner_order()
    print(wallet_miner)
    deal_miner.con.close()
