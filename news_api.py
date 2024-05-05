import requests

# API URL

def news():
    url = "https://saurav.tech/NewsAPI/top-headlines/category/technology/in.json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        # articles = data.get('articles', [])
        return data





#     # Print information for each article
#     for article in articles:
#         print("Title:", article.get('title', 'N/A'))
#         print("Description:", article.get('description', 'N/A'))
#         print("Author:", article.get('author', 'N/A'))
#         print("URL:", article.get('url', 'N/A'))
#         print("Published At:", article.get('publishedAt', 'N/A'))
#         print("Content:", article.get('content', 'N/A'))
#         print()  # Add a newline for readability
# else:
#     # If request was not successful, print error message
#     print("Error fetching data. Status code:", response.status_code)

