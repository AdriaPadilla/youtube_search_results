import youtubexplorer.extraction.get_search as qy
import youtubexplorer.extraction.get_search as qr


queries = ["vacunas"]
max_results = 2

def youtubexplore(queries, max_results):
	for query in queries:
		search_results = qy.get_search_results(query, max_results)
		related_results = qr.get_related_results(search_results)
		

		print(search_results)

if __name__ == "__main__":
	youtubexplore(queries, max_results)


