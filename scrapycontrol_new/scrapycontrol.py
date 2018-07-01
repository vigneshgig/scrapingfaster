import os
import time
import subprocess
pages= [15,5,14,9,3,1,6,2,2]
url = ['https://www.*******.com/all-wedding-invitations?categoryId=all&orderby=&page=',
    'https://www.********.com/hindu-wedding-cards-invitations?categoryId=all&orderby=&page=',
    'https://www.******.com/indian-wedding-invitations?categoryId=all&orderby=&page=',
    'https://www.*********.com/designer-wedding-cards-invitations?categoryId=all&orderby=&page=',
    'https://www.*******.com/muslim-wedding-cards-invitations?categoryId=all&orderby=&page=',
    'https://www.********.com/scroll-wedding-cards-invitations?categoryId=all&orderby=&page=',
    'https://www.*********.com/cheap-wedding-invites-online?categoryId=all&orderby=&page=',
    'https://www.************.com/elegant-wedding-invitations?categoryId=all&orderby=&page=',
    'https://www.****************.com/traditional-wedding-invitations?categoryId=all&orderby=&page=']
    
final_lists = [str(i[0]) + str(j) for i in zip(url,pages) for j in range(1,i[1]+1) ]
onetimerun=0
for i in range(5,57,5):
    if onetimerun == 0:
        j = 0
    onetimerun = 1
    pages = final_lists[j:i]
    pagess = ','.join(pages)
    # print(pagess)
    # print('////////////////////////////////')
    # print('////////////////////////////////')
    # print('////////////////////////////////')
    # print('////////////////////////////////')
    # print('////////////////////////////////')
    # print('////////////////////////////////')
    with open('/path/to/texfile/scrapydomain.txt','+w') as f:
            f.write(pagess)
    cmd  = 'scrapy runspider /path/to/spider/spidername.py'
    subprocess.call(cmd,shell=True)
    time.sleep(4)
    j = i
    print(i,j)
time.sleep(4)
pages = final_lists[55:57]
pages = ','.join(pagess)
with open('/path/to/texfile/scrapydomain.txt','+w') as f:
    f.write(pagess)
# os.system or subprocess we can use, but subprocess as more features
os.system('scrapy runspider /path/to/spider/spidername.py')

