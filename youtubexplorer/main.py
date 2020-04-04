import argparse

import youtubexplorer.video.get_videos as v
import youtubexplorer.data.dataframing as frame

""" EXAMPLES
query = ["coronavirus"]
seed_list = ["Z2mw6aglRuM"]

max_results = 1		## Nº of results in search 
get_related = True 	## ¿Want related videos? False / True (respect upper case in capital)
max_related = 1		## Max nº of related videos 
iteration_n = 1		## Nº of iterations over get related function

Query example:
python3 main.py --search "coronavirus" --more_related true --max 1 --iter 0

"""

def explore_search(query, max_results, get_related, iteration_n):

		videos = v.explore_videos(query, max_results, get_related, iteration_n)

		frame.export_data(videos)

def explore_related(seed_list, max_results, iteration_n):

		videos = v.explore_related(seed_list, max_related, iteration_n)

		frame.export_data(videos)

		
if __name__ == "__main__":

	parser = argparse.ArgumentParser(description='Explore YouTube Videos and related Videos')

	search = parser.add_argument_group("search")
	search.add_argument('--search', required=False, type=str, nargs="+", help='the query to search')

	related = parser.add_argument_group("related")
	related.add_argument('--related', required=False, type=str, nargs="+", help='the video ID')

	parser.add_argument('--more_related', type=str, nargs="+", help='True or False')
	parser.add_argument('--max', type=int, help='max related videos')
	parser.add_argument('--iter', type=int, help='max iterations videos')

	args = parser.parse_args()

	search = args.search
	related = args.related

	max_results = args.max
	get_related = args.more_related
	iteration_n = args.iter

	if args.search:

		print("Your Query is: "+str(search))
		print("Get related videos: "+str(get_related))
		print("Results Nº: "+str(max_results))
		print("iteration over related videos: " +str(iteration_n))

		explore_search(search, max_results, get_related, iteration_n)

	elif args.related:

		print(related)
		print(max_results)
		print(iteration_n)
		explore_related(related, max_results, iteration_n)
	else:
		print("error")

