from bs4 import BeautifulSoup

with open('index.html', 'r') as html_file:
    content = html_file.read()
    
    soup = BeautifulSoup(content, 'lxml')
    # tags = soup.find_all('li')
    # project_titles = soup.find_all('h5')
    # for titles in project_titles:
    #     print(titles.text)

    project_cards = soup.find_all('p', class_='card-text')
    for projects in project_cards:
        project_text = projects.text.split()[-1] #will give the last value in the string
        print(f'"{project_text}" is the last word in the project description.')