
from urllib.request import urlopen
from bs4 import BeautifulSoup

while True:
    try:
        
    
        ask =  input("Do you want to find the synonym or antonym(s/a): ")
        if ask =="S" or ask == "s":
            
            syn = input("Enter the word, you want the synonym of: ")

            url = 'http://www.thesaurus.com/browse/' + syn.lower()

            page_html = urlopen(url)
            page_soup = BeautifulSoup(page_html, "html.parser")

            synonym = page_soup.find("div", {"class": "relevancy-list"})
            syn_new = synonym.get_text()
        
            final = syn_new.replace("star", " ")
            print(final)

            ask2 = input("DO YOU WANT TO SAVE IT IN A FILE?(y/n): ")
            if ask2 == "y" or ask2 =="Y":
                F = open(("D:/"+"Synonym-" +str(syn)+".txt"), 'w')
                F.write("SYNONYMS OF " +str(syn).upper()+ final)
                F.close()
                print("Created A Text File in D:/")
        elif ask =="A" or ask =="a":
            ant = input("Enter the word, you want the antonym of: ")
            url = 'http://www.thesaurus.com/browse/' + ant.lower()
            page_html = urlopen(url)
            page_soup = BeautifulSoup(page_html, "html.parser")

            synonym = page_soup.find("div", {"class": "list-holder"})
            syn_new = synonym.get_text()
        
            #final = syn_new.replace("star", " ")
            print(syn_new)
            
            ask2 = input("DO YOU WANT TO SAVE IT IN A FILE?(y/n): ")
            if ask2 == "y" or ask2 =="Y":
                F = open(("D:/"+"Antonym-" +str(ant)+".txt"), 'w')
                F.write("Antonyms OF " +str(ant).upper()+ syn_new)
                F.close()
                print("Created A Text File in D:/")
    
    except:
        print("Something Went Wrong.")

