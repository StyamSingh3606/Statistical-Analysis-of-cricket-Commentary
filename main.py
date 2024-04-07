from bs4 import BeautifulSoup
import requests

def fetch_comm():
    html_text = requests.get('https://www.india.com/cricket/series/australia-in-india-2019-200884/live-score-5th-odi-match/india-vs-australia/commentary/186566/innings/1/').text

    soup = BeautifulSoup(html_text, 'lxml')
    sections = soup.find_all('section', class_ = 'runoverlist iwpl-sm-12')

    for index, section in enumerate(sections):
        if index > 7:
           break
        
        with open('./trial_comm.txt', 'a') as f:
            endover = section.find('section', class_ = 'endover')
            if endover != None:
                info = endover.find_all('aside', class_ = 'iwpl-sm-4')
                score = info[0].text
                batsmen = info[1].find_all('p')
                dat = ''
                for ele in batsmen:
                    dat = dat + ele.text + ' '
                f.write(f"Runs: {score}\tBatsmen: {dat}\n")

            delivery = section.find('aside', class_ = 'runoverl iwpl-sm-4')
            comm = section.find('aside', class_ = 'runoverr iwpl-sm-8')
            if delivery != None:
                ball = delivery.find('p', class_ = 'ron').text
                from_to = delivery.find('h3').text
                f.write(f"Ball: {ball}\tDelivery: {from_to}\n")
            
            if comm != None:
                commentary = comm.find('p').text
                f.write(f"Commentary: {commentary}\n\n")
        print(f"File saved. Number of account: {index}")

if __name__ == '__main__':
    fetch_comm()