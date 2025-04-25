# # # from search_tool import search_web
# # # from scraper_tool import scrape_content
# # # from analyzer_tool import analyze_content
# # # from synthesizer_tool import synthesize_summary

# # # def main():
# # #     print("🤖 Welcome to the Web Research Agent!")
    
# # #     # Step 1: Get the research query from the user
# # #     query = input("🔍 Enter your research question: ")
    
# # #     # Step 2: Generate search results
# # #     print("\n🔎 Generating search results...")
# # #     search_results = search_web(query)
    
# # #     # Step 3: Scrape content from the top links
# # #     print("🌐 Found URLs. Scraping content...")
# # #     scraped_data = scrape_content(search_results)
    
# # #     # Step 4: Analyze the scraped content
# # #     print("📊 Analyzing content...")
# # #     analyzed_data = analyze_content(scraped_data)
    
# # #     # Step 5: Synthesize the final research summary
# # #     print("🧠 Synthesizing final report...")
# # #     summary = synthesize_summary(analyzed_data)
    
# # #     # Output the final summary
# # #     print("\n✅ Here is your research summary:\n")
# # #     for point in summary:
# # #         print(f"- {point}")

# # # if __name__ == "__main__":
# # #     main()

# # # main.py

# # from search_tool import search_web
# # from scraper_tool import scrape_urls
# # from analyzer_tool import analyze_content
# # from synthesizer_tool import synthesize_summary

# # def main():
# #     print("🤖 Welcome to the Web Research Agent!")
# #     while True:
# #         query = input("🔍 Enter your research question: ").strip()
# #         if not query:
# #             break

# #         print("\n🔎 Generating search results...")
# #         urls = search_web(query)
# #         print(f"🌐 Found {len(urls)} URLs. Scraping content...")

# #         contents = scrape_urls(urls)
# #         print("📊 Analyzing content...")
# #         relevant_info = analyze_content(contents)

# #         print("🧠 Synthesizing final report...")
# #         summary = synthesize_summary(relevant_info)

# #         print("\n✅ Here is your research summary:\n")
# #         print(summary)
# #         print("\n")

# # if __name__ == "__main__":
# #     main()
# # import logging

# # # Create a logger
# # logger = logging.getLogger(__name__)
# # logger.setLevel(logging.INFO)

# # # Create a file handler and a stream handler
# # file_handler = logging.FileHandler('research_agent.log')
# # stream_handler = logging.StreamHandler()

# # # Create a formatter and set it for the handlers
# # formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# # file_handler.setFormatter(formatter)
# # stream_handler.setFormatter(formatter)

# # # Add the handlers to the logger
# # logger.addHandler(file_handler)
# # logger.addHandler(stream_handler)

# # def main():
# #     logger.info("Welcome to the Web Research Agent!")
# #     while True:
# #         query = input("Enter your research question: ").strip()
# #         if not query:
# #             break

# #         logger.info("Generating search results...")
# #         urls = search_web(query)
# #         logger.info(f"Found {len(urls)} URLs. Scraping content...")

# #         contents = scrape_urls(urls)
# #         logger.info("Analyzing content...")
# #         relevant_info = analyze_content(contents)

# #         logger.info("Synthesizing final report...")
# #         summary = synthesize_summary(relevant_info)

# #         logger.info("Here is your research summary:")
# #         logger.info(summary)
# #         logger.info("")

# # if __name__ == "__main__":
# #     main()

# import logging
# from search_tool import search_web
# from scraper_tool import scrape_urls
# from analyzer_tool import analyze_content
# from synthesizer_tool import synthesize_summary

# # # Create a logger
# # logger = logging.getLogger(__name__)
# # logger.setLevel(logging.INFO)

# # # Create a file handler and a stream handler
# # file_handler = logging.FileHandler('research_agent.log')
# # stream_handler = logging.StreamHandler()

# # # Create a formatter and set it for the handlers
# # formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# # file_handler.setFormatter(formatter)
# # stream_handler.setFormatter(formatter)

# # # Add the handlers to the logger
# # logger.addHandler(file_handler)
# # logger.addHandler(stream_handler)

# import logging
# import sys

# # Set up logging with Unicode handling
# def setup_logging():
#     handler = logging.StreamHandler()
#     handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    
#     # Ensure Unicode output is handled correctly
#     handler.stream = open(sys.stdout.fileno(), mode='w', encoding='utf-8')
    
#     logger = logging.getLogger(__name__)
#     logger.addHandler(handler)
#     logger.setLevel(logging.INFO)
    
#     return logger

# # Set up


# def main():
#     logger.info("🤖 Welcome to the Web Research Agent!")
#     while True:
#         query = input("🔍 Enter your research question: ").strip()
#         if not query:
#             break

#         logger.info(f"\n🔎 Generating search results for: {query}...")
#         urls = search_web(query)
#         logger.info(f"🌐 Found {len(urls)} URLs. Scraping content...")

#         contents = scrape_urls(urls)
#         logger.info("📊 Analyzing content...")

#         relevant_info = analyze_content(contents)

#         logger.info("🧠 Synthesizing final report...")
#         summary = synthesize_summary(relevant_info)

#         logger.info("\n✅ Here is your research summary:\n")
#         logger.info(summary)
#         print("\n✅ Here is your research summary:")
#         print(summary)

# if __name__ == "__main__":
#     main()


import logging
import sys
from search_tool import search_web
from scraper_tool import scrape_urls
from analyzer_tool import analyze_content
from synthesizer_tool import synthesize_summary

# Set up logging with Unicode handling
def setup_logging():
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    
    # Ensure Unicode output is handled correctly
    handler.stream = open(sys.stdout.fileno(), mode='w', encoding='utf-8')
    
    logger = logging.getLogger(__name__)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    
    return logger

# Initialize the logger
logger = setup_logging()

# Main program function
def main():
    logger.info("🤖 Welcome to the Web Research Agent!")
    while True:
        query = input("🔍 Enter your research question: ").strip()
        if not query:
            break

        logger.info(f"\n🔎 Generating search results for: {query}...")
        urls = search_web(query)
        logger.info(f"🌐 Found {len(urls)} URLs. Scraping content...")

        contents = scrape_urls(urls)
        logger.info("📊 Analyzing content...")

        relevant_info = analyze_content(contents)

        logger.info("🧠 Synthesizing final report...")
        summary = synthesize_summary(relevant_info)

        logger.info("\n✅ Here is your research summary:\n")
        logger.info(summary)
        print("\n✅ Here is your research summary:")
        print(summary)

if __name__ == "__main__":
    main()
