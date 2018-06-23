import os
import time
import subprocess

# pages list holds the number of pages provided in individual domains, 
# which is shown below in another list holding respective domains 


pages = [219,238,105,292,240,210,213,471,84,79,8,103,35,100,5,9]

# domains list holds the links for the respective domains under the website.

domains = ["http://www.examplewebsites.com/food-beverages-",
            "http://www.examplewebsites.com/beauty-grooming-",
            "http://www.examplewebsites.com/wedding-planners-contractors-",
            "http://www.examplewebsites.com/tours-travels-",
            "http://www.examplewebsites.com/honeymoon-packages-",
            "http://www.examplewebsites.com/apparel-accessories-",
            "http://www.examplewebsites.com/astrology-religious-services-",
            "http://www.examplewebsites.com/wedding-venues-",
            "http://www.examplewebsites.com/hotels-accommodation-",
            "http://www.examplewebsites.com/jewellery-",
            "http://www.examplewebsites.com/decorators-",
            "http://www.examplewebsites.com/photographers-",
            "http://www.examplewebsites.com/wedding-cards-",
            "http://www.examplewebsites.com/background-verification-detective-services-",
            "http://www.examplewebsites.com/marriage-counsellors-",
            "http://www.examplewebsites.com/music-entertainment-",
            "http://www.examplewebsites.com/wedding-gifts-",
            "http://www.examplewebsites.com/health-wellness-",
            "http://www.examplewebsites.com/ghodi-wale-",
            "http://www.examplewebsites.com/home-furnishings-"]

# here is an empty list named final_lists

final_lists = []

# here zip combines the two lists, pages and domains into a new tuple,
#  and it is being appended into the final_list

for i in zip(domains,pages):

# here this for loop makes iteration of range provided, 
# and creating as much pages numbers respective to their domains required
  
    for j in range(1,i[1]+1):
# at last the final link with page number is created and its being appended in the new list final_lists        
        
        final_lists.append(str(i[0])+str(j))

k=0
# For loop works with the range provided and here in our website as after 35 request hitting regularly, there is a block,
# we have choosen the range from 35 and its your option depending upon the requirement to choose and set the value
for i in range(35,2411,35):
# just as from the start, we have initialized k and j variable to 0, 
# after first iteration, it gets assigned with other values
# depending upon the runtime and its number count
    if k == 0:
        j = 0

    k = 1
# pages get a new list with first set of links to be parsed without getting blocked instantly
    pages = final_lists[j:i]
# each elements get concatenated with ',' and stored in pagess variable
    pagess = ','.join(pages)

# cmd variable holds the root path and list of string urls which has to be parsed 
    
    cmd  = 'scrapy/path/to/spider_script<here spider.py> -a pages='+ str(pagess)
# now subprocess is called with the variable cmd which holds the url links
    
    subprocess.call(cmd,shell=True)

    time.sleep(4)
# j is assigned with the new value after each iteration to parse other set of url's
    j = i


time.sleep(4)
pages = final_lists[2380:2411]
pages = ','.join(pagess)
os.system('scrapy runspider /path/to/spider_script<here spider.py> -a pages='+ str(pagess))
