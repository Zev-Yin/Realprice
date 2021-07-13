import easyquotation
import time
import argparse

def realprice(code,refreshtime):
    quotation = easyquotation.use('tencent')
    while True:
        codeprice = {}
        if "sz" in code or "sh" in code:
           codeprice = quotation.stocks(code)[code[2:]]
        else:
           codeprice = quotation.stocks(code)[code]
        print("\rcode:",codeprice['code'],",now:",codeprice['now'],end="",flush=True)
        time.sleep(refreshtime)

def get_parser():
    parser = argparse.ArgumentParser(description="=======================start=======================")
    parser.add_argument('--code', dest='code', type=str, default="sz002902", help='stock code,default: sz002902')
    parser.add_argument('--flush', dest='flush', type=int, default=2, help="prices refresh time(seconds),default: 2")
    args = parser.parse_args()
    return args

if __name__=="__main__":
    args = get_parser()
    realprice(args.code,args.flush)
