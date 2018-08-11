import sqlite3
import operator
class dealwith_dealTable(object):
    def __init__(self):
        self.con=sqlite3.connect('uicbase.db')
        # 创建游标对象
        self.cur = self.con.cursor()
    #按卖出数量排名降序输出
    def sell_wallet_order_all(self):
        sql = 'select "from" ,sum(value) from dealTable GROUP BY "from" ORDER BY sum(value) DESC'
        result = self.cur.execute(sql)
        temp=result.fetchall()[:]
        #print(len(temp))
        return temp
    def sell_wallet_order(self,num=20):
        sql = 'select "from" ,sum(value) from dealTable GROUP BY "from" ORDER BY sum(value) DESC'
        result = self.cur.execute(sql)
        #print('卖出钱包，卖出数量')
        temp=result.fetchmany(num)[:]
        return temp
    # 按买入数量排名降序输出
    def buy_wallet_order_all(self):
        sql = 'select "to" ,sum(value) from dealTable GROUP BY "to" ORDER BY sum(value) DESC'
        result = self.cur.execute(sql)
        temp=result.fetchall()[:]
        #print(len(temp))
        return temp
    def buy_wallet_order(self,num=20):
        sql = 'select "to" ,sum(value) from dealTable GROUP BY "to" ORDER BY sum(value) DESC'
        result = self.cur.execute(sql)
        #print('买入钱包，买入数量')
        temp = result.fetchmany(num)[:]
        return temp

    def deal_balance(self,sell,buy):
        temp_sell = []
        temp_buy =[]
        deal_balance=[]
        for se in sell:
            listsell = list(se)[:]
            temp_sell.append([listsell[0], -listsell[1]])
        for bu in buy:
            listbuy=list(bu)
            temp_buy.append(listbuy)
        #print(temp_sell)
        #print(temp_buy)
        for temp_se in temp_sell:
            for temp_bu in temp_buy:
                if temp_se[0]==temp_bu[0]:
                    #print('...')
                    temp_se[1]+=temp_bu[1]
                    temp_buy.remove(temp_bu)
        deal_balance=temp_sell[:]
        deal_balance.extend(temp_buy)
        deal_balance.sort(key=operator.itemgetter(1),reverse=True)
        #print(deal_balance)
        return deal_balance


if __name__=='__main__':
    dealwith_deal=dealwith_dealTable()
    #buy=dealwith_deal.buy_wallet_order(num=20)
    #sell=dealwith_deal.sell_wallet_order(num=20)
    sell=dealwith_deal.sell_wallet_order_all()
    buy=dealwith_deal.buy_wallet_order_all()
    #交易余额
    deal_balance=dealwith_deal.deal_balance(sell,buy)
    i=0
    for deal_b in deal_balance:
        i+=1
        print('[%s]%s'%(i,deal_b))

    dealwith_deal.con.close()

