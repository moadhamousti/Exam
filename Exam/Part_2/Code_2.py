# Original Code That needs Debuging :


# import webbrowser
# import re
# def search_google(query):
#     """Search for the given query on Google and open the first result in a web
# browser."""
#     url = f'https://www.google.com/search?q={query}'
#     response = webbrowser.open(url)
#     if not response:
#         return 'Unable to open web browser'
#     html = webbrowser.get().open(url).read().decode('utf-8')
#     pattern = re.compile(r'<a href="(https?://.*?)"')
#     match = pattern.search(html)
#     if not match:
#         return 'No search results found'
#     result_url = match.group(2)
#     response = webbrowser.open(result_url)
#     if not response:
#         return 'Unable to open web browser'
#     return 'Success'
# if __name__ == '__main__':
#     query = None
#     result = search_google(query)
#     print(result)





# The Fixed Version :

import webbrowser
import re
def search_google(query):
    """Search for the given query on Google and open the first result in a web
browser."""
    url = f'https://www.google.com/search?q={query}'
    response = webbrowser.open(url)
    if not response:
        return 'Unable to open web browser'
    html = webbrowser.get().open(url).read().decode('utf-8')
    pattern = re.compile(r'<a href="(https?://.*?)"')
    match = pattern.search(html)
    if not match:
        return 'No search results found'
    result_url = match.group(2)
    response = webbrowser.open(result_url)
    if not response:
        return 'Unable to open web browser'
    return 'Success'
if __name__ == '__main__':
    query = input("Enter Your Google Search Here: ")
    result = search_google(query)
    print(result)