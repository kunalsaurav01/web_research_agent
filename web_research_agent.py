# # Import necessary libraries
# import requests
# from bs4 import BeautifulSoup
# from sklearn.feature_extraction.text import TfidfVectorizer
# def scrape_webpage(url):
#     response = requests.get(url)  # Fetch the webpage content
#     soup = BeautifulSoup(response.content, 'html.parser')  # Parse the HTML content
    
#     # Extract all paragraph texts from the page
#     paragraphs = soup.find_all('p')  # Find all <p> tags
#     content = ' '.join([p.get_text() for p in paragraphs])  # Combine the text from all paragraphs
    
#     return content
# def analyze_text(content):
#     # Using TF-IDF Vectorizer to extract important keywords
#     vectorizer = TfidfVectorizer(stop_words='english')  # Remove common stopwords
#     tfidf_matrix = vectorizer.fit_transform([content])  # Convert content to a matrix
    
#     feature_names = vectorizer.get_feature_names_out()  # Get the feature names (words)
#     dense = tfidf_matrix.todense()  # Convert the matrix to a dense format
#     text_array = dense.tolist()  # Convert to list format
    
#     # Combine words with their corresponding scores
#     scores = list(zip(feature_names, text_array[0]))
    
#     # Sort keywords by their importance (highest TF-IDF score first)
#     sorted_keywords = sorted(scores, key=lambda x: x[1], reverse=True)[:10]  # Get top 10 keywords
    
#     return sorted_keywords
# def web_research_agent(url):
#     # Step 1: Scrape the content from the URL
#     scraped_content = scrape_webpage(url)
    
#     # Step 2: Analyze the scraped content for important keywords
#     keywords = analyze_text(scraped_content)
    
#     # Step 3: Return the results as a dictionary
#     return {
#         "url": url,
#         "scraped_content": scraped_content,
#         "keywords": keywords
#     }
# if __name__ == "__main__":
#     # Test with an example URL
#     # url = "https://example.com"  # Replace with the URL you want to test
#     # result = web_research_agent(url)
#     url = "https://en.wikipedia.org/wiki/Machine_learning"
#     result = web_research_agent(url)

#     # Print the result
#     print("URL:", result['url'])
#     print("Scraped Content:", result['scraped_content'])
#     print("Top 10 Keywords:", result['keywords'])
# Import necessary libraries

import requests
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import TfidfVectorizer
from transformers import pipeline  # <-- Add this import

# def scrape_webpage(url):
#     # existing code...
#     return content
def scrape_webpage(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract all paragraph texts from the page
    paragraphs = soup.find_all('p')
    content = ' '.join([p.get_text() for p in paragraphs])
    
    return content

# def analyze_text(content):
#     # existing code...
#     return sorted_keywords
def analyze_text(content):
    from sklearn.feature_extraction.text import TfidfVectorizer
    
    # Vectorize text using TF-IDF
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform([content])
    
    feature_names = vectorizer.get_feature_names_out()
    dense = tfidf_matrix.todense()
    text_array = dense.tolist()
    
    # Pair words with their TF-IDF scores
    scores = list(zip(feature_names, text_array[0]))
    
    # Sort and get top 10 keywords
    sorted_keywords = sorted(scores, key=lambda x: x[1], reverse=True)[:10]
    
    return sorted_keywords

def summarize_text(text, max_chunk_length=1000):  # <-- Add this here
    # summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn", framework="pt")

    text_chunks = [text[i:i+max_chunk_length] for i in range(0, len(text), max_chunk_length)]
    summary = ""
    for chunk in text_chunks:
        summary += summarizer(chunk, max_length=150, min_length=40, do_sample=False)[0]['summary_text'] + "\n"
    return summary.strip()

def web_research_agent(url):
    scraped_content = scrape_webpage(url)
    keywords = analyze_text(scraped_content)
    summary = summarize_text(scraped_content)  # <-- New step

    return {
        "url": url,
        "scraped_content": scraped_content,
        "summary": summary,                # <-- Include summary in output
        "keywords": keywords
    }

if __name__ == "__main__":
    url = "https://en.wikipedia.org/wiki/Machine_learning"
    result = web_research_agent(url)

    print("URL:", result['url'])
    print("\nScraped Content:\n", result['scraped_content'][:1000], "...")  # Preview first 1000 chars
    print("\nSummary:\n", result['summary'])  # <-- Print the summary
    print("\nTop 10 Keywords:", result['keywords'])
