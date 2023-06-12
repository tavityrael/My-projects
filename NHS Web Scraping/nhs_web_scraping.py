import requests
from bs4 import BeautifulSoup
import pandas as pd

def nhs_services():
    url = 'https://digital.nhs.uk/services/a-to-z'
    # Use git function to extract info from URL
    response = requests.get(url)
    # If the response is 200 it means it's working
    response
    html = response.text
    # Parse 'html' via BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')
    # Find all 'tags' elements
    tags = soup.find_all('h2',{'class':'nhsd-t-heading-xs nhsd-!t-margin-bottom-1'})    # Indentify the number of the elements we are loocking for
    len(tags)
    # Create empty list for tags. Pass each element thru the loop by removing HTML element and striping the text 
    # to remove any gaps. After append to the list.
    tag_list = []
    for tag in tags:
        tag_list.append(tag.text.strip())
    # Find all 'description' elements
    description = soup.find_all('p',{'class':'nhsd-t-body'})
    descript_list = []
    for descript in description:
        descript_list.append(descript.text.strip())
    # convert two list into dictionarie
    lists_dict = dict(zip(tag_list, descript_list))

    
    return lists_dict
 

result = nhs_services()
# create a list with Pandas
df_tag = pd.DataFrame(result.keys())
df_des = pd.DataFrame(result.values())


# Create a dictionaries with Pandas
df_serv = pd.DataFrame(result.items(), columns=['Titles', 'Description'])

print(df_tag)
print(df_des)