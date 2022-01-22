from bs4 import BeautifulSoup
import requests
import time


print('Put some skill: ')
unfamilar_skills= input('>')
print(f'Filtering out {unfamilar_skills}')

def jobs():
    html_text=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup=BeautifulSoup(html_text,'lxml')
    jobs=soup.find_all('li',class_='clearfix job-bx wht-shd-bx')
    
    for index, job in enumerate(jobs): 
         #job_published_date=job.find('span',class_='sim-posted').text
    
        company_name=job.find('h3',class_='joblist-comp-name').text.replace(' ','')
        skills=job.find('span',class_ = 'srp-skills').text.replace(' ','')
        more_info=job.header.h2.a['href']
        if unfamilar_skills not in skills:
            with open (f'{index}.txt','w')as f:
                
                f.write(f" Company Name: {company_name.strip()}" )
                f.write(f"  Skills: {skills.strip()}")
                f.write(f" More Info:{more_info}")
        print(f'File saved:{index}')

if __name__=='__main__':
    while True:
        jobs()
        time_wait=10
        print(f'Waiting {time_wait} seconds...')
        time.sleep(time_wait*60)