import requests
from bs4 import BeautifulSoup
import os
import re
from googlesearch import search

def google_search(query):
       # 使用googlesearch库进行搜索
    results = search(query, num_results=1, lang="zh-cn")  # 获取第一个搜索结果
    for result in results:
        print(result)
    return results  # 返回第一个结果的链接

def fetch_novel_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    chapters = soup.find_all('a', href=re.compile(r'/chapter/'))  # 假设章节链接包含'/chapter/'
    
    for chapter in chapters:
        chapter_title = chapter.text.strip()
        chapter_url = chapter['href']
        chapter_content = fetch_chapter_content(chapter_url)
        save_chapter(chapter_title, chapter_content)

def fetch_chapter_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    content = soup.find('div', class_='chapter-content').text  # 假设章节内容在这个div中
    return content

def save_chapter(title, content):
    # 清理标题以���用作文件名
    safe_title = re.sub(r'[<>:"/\\|?*]', '', title)
    with open(f"{safe_title}.txt", 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    # novel_name = input("请输入小说名称: ")
    search_urls = google_search("斗破苍穹")
    print(search_urls)
    # fetch_novel_content(search_url)
