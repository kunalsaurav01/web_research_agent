# # def search_web(query):
# #     print(f"[Mock Search] Searching the web for: {query}")
# #     # In a real-world scenario, you'd integrate a search engine API like Google or Bing.
# #     # For now, we'll return some mock URLs.
# #     return [
# #         "https://example.com/article1",
# #         "https://example.com/article2",
# #         "https://example.com/article3"
# #     ]

# # search_tool.py

# import os
# # from serpapi import GoogleSearch
# from google_search_results import GoogleSearch


# SERPAPI_API_KEY = "89de182362e0571aa034973bfbc1153a7f42b2fd65de77a6bfecc91c340cfe7b"  # <-- Replace with your actual API key

# def search_web(query):
#     print(f"🔍 [Search] Searching for: {query}")
#     params = {
#         "engine": "google",
#         "q": query,
#         "api_key": SERPAPI_API_KEY,
#         "num": 5,
#     }
#     search = GoogleSearch(params)
#     results = search.get_dict()
#     links = []
#     for result in results.get("organic_results", []):
#         if "link" in result:
#             links.append(result["link"])
#     return links

# search_tool.py

# from google_search_results import GoogleSearch
from serpapi import GoogleSearch

SERPAPI_API_KEY = "89de182362e0571aa034973bfbc1153a7f42b2fd65de77a6bfecc91c340cfe7b"  # <-- Replace with your real API key

def search_web(query):
    print(f"🔍 [Search] Searching for: {query}")
    params = {
        "engine": "google",
        "q": query,
        "api_key": SERPAPI_API_KEY,
        "num": 5,
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    links = []
    for result in results.get("organic_results", []):
        if "link" in result:
            links.append(result["link"])
    return links
