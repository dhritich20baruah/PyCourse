from requests_html import HTMLSession

session = HTMLSession()

r = session.get('https://python.org/')

# print(r.text)
# print(r.html.links)

# about = r.html.find('#about', first=True)
# about = r.html.find('.tier-2', first=True)
about = r.html.find('.tier-2')

print(about[0].text)