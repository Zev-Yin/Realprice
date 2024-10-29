import easyquotation
import time
import argparse

def realprice(code,refretime,yours,nums):
    quotation = easyquotation.use('tencent')
    while True:
        codeprice = {}
        if "sz" in code or "sh" in code:
           codeprice = quotation.stocks(code)[code[2:]]
        else:
           codeprice = quotation.stocks(code)[code]
        #print("\rcode:",codeprice['code'],",now:",codeprice['now'],",high:",codeprice['high'],",low:",codeprice['low'],end="",flush=True)
        print("\rnow:",codeprice['now'],",high:",codeprice['high'],",low:",codeprice['low'],",your price:",yours,",earn:",(float(codeprice['now'])-float(yours))*float(nums)*100,end="",flush=True)
        time.sleep(refretime)

def get_parser():
    parser = argparse.ArgumentParser(description="=======================start=======================")
    parser.add_argument('--code', dest='code', type=str, default="sz002119", help='stock code,default: sz002902')
    parser.add_argument('--flush', dest='flush', type=int, default=2, help="prices refre time(seconds),default: 2")
    parser.add_argument('--yours',dest="yours",type=float,default=0.0,help="your code price")
    parser.add_argument("--nums",dest="nums",type=int,default=0,help="your code nums (100)")
    args = parser.parse_args()
    return args

if __name__=="__main__":
    args = get_parser()
    realprice(args.code,args.flush,args.yours,args.nums)
