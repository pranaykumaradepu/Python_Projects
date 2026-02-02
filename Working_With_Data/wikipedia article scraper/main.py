# wikipedia article scraper 

from bs4 import BeautifulSoup
import  requests


# fetch the article based on the user provided topic 
# prints title, heading, summary, links that are related

# step 1 : loading data from wiki 
def loading_data_from_wiki(topic):
    url = f'https://en.wikipedia.org/wiki/{topic.replace(' ', '_')}'

    headers = {
    "User-Agent": "MyLearningScript/1.0 (contact: example@email.com)"
    }

    response = requests.get(url,headers=headers)

    if response.status_code == 200:
        return response.text
    else:
        print(f'the webiste is not responding {response.status_code}')
        return None

# step 2 : extract article title
def get_artcile_title(soup):
    return soup.find('h1').text


# step 3: exctracting article summary 
def get_article_summary(soup):
    paragraph = soup.find_all('p')
    for para in paragraph:
        if para.text.strip():
            return para.text.strip()
    return "No summary found"

# step 4: extract heading
def get_headings(soup):
    headings = [heading.text.strip() for heading in soup.find_all(['h2','h3','h4'])]
    return headings

# step 5: extract links
def get_realted_links(soup):
    links = []
    for a_tag in soup.find_all('a', href=True):
        href = a_tag['href']
        if href.startswith('/wiki') and ':' not in href:
            links.append(f'https://en.wikipedia.org{href}')
    return list(set(links))[:5]       


# step 6: Main program
def main():
    topic = input('Enter a topic to search on wikipedia : ').strip()
    page_content = loading_data_from_wiki(topic)

    if page_content:
        soup = BeautifulSoup(page_content, 'html.parser')
        title = get_artcile_title(soup)
        summary = get_article_summary(soup)
        headings = get_headings(soup)
        links = get_realted_links(soup)

        print('\t\t\t----Wiki Article Details ---------')
        print(f'Title: {title}')
        print(f'Summary: {summary}')
        
        for heading in headings[:5]:
            print(f'- {heading}')

        print('\n---- Related Links ----')
        for link in links:
            print(f'- {link}')


if __name__ == '__main__':
    main()