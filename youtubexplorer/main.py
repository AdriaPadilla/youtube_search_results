import capturer.crawler as c
import export as e

queries = ["coronavirus"] # You can use this as a list
max_results = 5 ## Nº of results in search

def main(q, max_results):
            videos = c.explore_videos(q, max_results)
            e.export_data(videos, q)

if __name__ == "__main__":
    for q in queries:
        main(q, max_results)
