from django.shortcuts import render
from news_api import news
from text_summarization import query, image_query
import requests
import io
from PIL import Image, UnidentifiedImageError
# Create your views here.


def home(request):
    news_data = news()
    for key, value in news_data.items():
        print(key)

    articles = news_data.get('articles', [])
    news_details_list = []

    # Iterate over each article
    for article in articles:
        news_details = {
            'title': article.get('title', 'N/A'),
            'description': article.get('description', 'N/A'),
            'author': article.get('author', 'N/A'),
            'url': article.get('url', 'N/A'),
            'publishedAt': article.get('publishedAt', 'N/A'),
            'content': article.get('content', 'N/A'),
            'image_url': article.get('urlToImage', 'N/A'),
            'publishedAt': article.get('publishedAt', 'N/A'),
        }
        news_details_list.append(news_details)

    context = {
        'news_list': news_details_list  # Sending a list of news details to the template
    }
    return render(request, 'home.html', context)

def text_summary(request):
    news_data = news()
    for key, value in news_data.items():
        print(key)

    articles = news_data.get('articles', [])
    news_details_list = []

    # Iterate over each article
    for article in articles:
        news_details = {
            'title': article.get('title', 'N/A'),
            'description': article.get('description', 'N/A'),
            'author': article.get('author', 'N/A'),
            'url': article.get('url', 'N/A'),
            'publishedAt': article.get('publishedAt', 'N/A'),
            'content': article.get('content', 'N/A'),
            'image_url': article.get('urlToImage', 'N/A'),
            'publishedAt': article.get('publishedAt', 'N/A'),
        }
        news_details_list.append(news_details)
    if request.method=="POST":
        content=request.POST.get("content")
        print(content)
        output = query({
            "inputs": f"{content}",
        })
        print(output)
        context={
            'result':output,
            'news_list': news_details_list 
        }
        return render(request,'home.html',context)
    return render(request,'home.html',{'news_list':news_details_list})

def image_generator(request):
    news_data = news()

    articles = news_data.get('articles', [])
    news_details_list = []

    # Iterate over each article
    for article in articles:
        news_details = {
            'title': article.get('title', 'N/A'),
            'description': article.get('description', 'N/A'),
            'author': article.get('author', 'N/A'),
            'url': article.get('url', 'N/A'),
            'publishedAt': article.get('publishedAt', 'N/A'),
            'content': article.get('content', 'N/A'),
            'image_url': article.get('urlToImage', 'N/A'),
            'publishedAt': article.get('publishedAt', 'N/A'),
        }
        news_details_list.append(news_details)
    if request.method=="POST":
        content=request.POST.get("content")
        print(content)
        
        image_bytes = image_query({
            "inputs": f"{content}",
        })
        print(image_bytes)
        # image_bytes = bytes(image_bytes)

        try:
            image = Image.open(io.BytesIO(image_bytes))
            print("Image loaded successfully")
            image.save("static/assets/generated/generated_image.jpg")
            print("Image saved successfully")
        except UnidentifiedImageError as e:
            print("Error loading image:", e)
        context={
            'news_list':news_details_list,
            'download_image':True
        }
        return render(request,'home.html',context)
    return render(request,'home.html',{'news_list':news_details_list})


    