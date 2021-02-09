rm -rf data/*jsonlines
# 阿美語 ami
scrapy runspider crawler.py -t jsonlines -a lang=ami -o data/ami.jsonlines --logfile ami.log

# 泰雅語 tay
scrapy runspider crawler.py -t jsonlines -a lang=tay -o data/tay.jsonlines --logfile tay.log

# 排灣語 pwn
scrapy runspider crawler.py -t jsonlines -a lang=pwn -o data/pwn.jsonlines --logfile pwn.log

# 布農語 bnn
scrapy runspider crawler.py -t jsonlines -a lang=bnn -o data/bnn.jsonlines --logfile bnn.log

# 卑南語 pyu
scrapy runspider crawler.py -t jsonlines -a lang=pyu -o data/pyu.jsonlines --logfile pyu.log

# 魯凱語 dru
scrapy runspider crawler.py -t jsonlines -a lang=dru -o data/dru.jsonlines --logfile dru.log

# 鄒語 tsu
scrapy runspider crawler.py -t jsonlines -a lang=tsu -o data/tsu.jsonlines --logfile tsu.log

# 賽夏語 xsy
scrapy runspider crawler.py -t jsonlines -a lang=xsy -o data/xsy.jsonlines --logfile xsy.log

# 雅美語 tao
scrapy runspider crawler.py -t jsonlines -a lang=tao -o data/tao.jsonlines --logfile tao.log

# 邵語 ssf
scrapy runspider crawler.py -t jsonlines -a lang=ssf -o data/ssf.jsonlines --logfile ssf.log

# 噶瑪蘭語 ckv
scrapy runspider crawler.py -t jsonlines -a lang=ckv -o data/ckv.jsonlines --logfile ckv.log

# 太魯閣語 trv
scrapy runspider crawler.py -t jsonlines -a lang=trv -o data/trv.jsonlines --logfile trv.log

# 撒奇萊雅語 ais
scrapy runspider crawler.py -t jsonlines -a lang=ais -o data/ais.jsonlines --logfile ais.log

# 賽德克語 sdq
scrapy runspider crawler.py -t jsonlines -a lang=sdq -o data/sdq.jsonlines --logfile sdq.log

# 拉阿魯哇語 sxr
scrapy runspider crawler.py -t jsonlines -a lang=sxr -o data/sxr.jsonlines --logfile sxr.log

# 卡那卡那富語 xnb
scrapy runspider crawler.py -t jsonlines -a lang=xnb -o data/xnb.jsonlines --logfile xnb.log
