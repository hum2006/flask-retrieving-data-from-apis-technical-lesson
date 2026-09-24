import requests


class Search:
    def get_search_results(self, search_term):
        URL = "https://openlibrary.org/search.json"

        response = requests.get(
            URL,
            params={
                "title": search_term,
                "fields": "title,author_name",
                "limit": 1
            }
        ).json()

        response_formatted = (
            f"Title: {response['docs'][0]['title']}\n"
            f"Author: {response['docs'][0]['author_name'][0]}"
        )

        return response_formatted


search_term = input("Enter a book title: ")

result = Search().get_search_results(search_term)

print("Search Result:\n")
print(result)