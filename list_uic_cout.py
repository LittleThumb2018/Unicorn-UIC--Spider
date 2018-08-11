import dealwith_dealTable
import dealwith_minerTable
import operator
from matplotlib import pyplot as plt
import pygal
import time

#交易与挖矿余额
def list_uic_cout(deal_list,miner_list):
    for deal_li in deal_list:
        for miner_li in miner_list:
            if deal_li[0] == miner_li[0]:
                deal_li[1] += miner_li[1]
                miner_list.remove(miner_li)
    temp=deal_list[:]
    temp.extend(miner_list)
    temp.sort(key=operator.itemgetter(1),reverse=True)
    return temp

if __name__=='__main__':
    deal_miner=dealwith_minerTable.deal_minerTable()
    deal_deal = dealwith_dealTable.dealwith_dealTable()

    miner =deal_miner.walletId_miner_order_all()
    #print('miner=%s'%miner)

    deal_sell=deal_deal.sell_wallet_order_all()
    deal_buy = deal_deal.buy_wallet_order_all()
    deal= deal_deal.deal_balance(deal_sell,deal_buy)
    #print('deal=%s'%deal)

    list_count=list_uic_cout(deal,miner)
    temp=[]
    count = [0,0,0,0,0,0,0,0,0,0]
    print(count)
    i=0
    for list_co in list_count:
        i+=1
        print('[%s]%s'%(i,list_co))
        temp.append(list_co[1])
    for te in temp:
        if te<-20000:
            count[0]+=1
        elif -20000<=te<0:
            count[1]+=1
        elif 0<=te<500:
            count[2]+=1
        elif 500<=te<1000:
            count[3]+=1
        elif 1000<=te<1500:
            count[4]+=1
        elif 1500<=te<5000:
            count[5]+=1
        elif 5000<=te<10000:
            count[6]+=1
        elif 10000<=te<20000:
            count[7]+=1
        elif 20000<=te<100000:
            count[8]+=1
        else:
            count[9]+=1

    deal_miner.con.close()


    #plt.scatter([1,2,3,4,5,6,7,8,9,10],count)
    #plt.show()

    #钱包持币数量分布 直方图
    hist=pygal.Bar()
    hist.x_labels=['<-2000','-2000-0','0-500','500-1000','1000-1500','1500-5000',
                   '5000-10000','10000-20000','20000-100000','>100000']
    hist.x_title='持UIC币数量(个)'
    hist.y_title='钱包数量(个)'
    hist.title='UIC钱包持币数量分析'
    hist.add('',count)
    hist.show_y_guides=True
    hist.x_label_rotation=-45
    hist.render_to_file('UIC钱包持币数量分析%s.svg'%str(time.strftime('%Y%m%d%H%M%S',time.localtime())))
    #hist.render_in_browser()
