import pandas as pd
from datetime import datetime

""" ONLY FOR MYSQL DUMP MODULES
import pymysql
from sqlalchemy import create_engine

db_user = "your_db_user"
db_password = "your_db_pw"
host = "your_db_address"
db_name = "db_name"
db_table = "db_table" # If table doesn't exists, will create. If Exist, will append

engine = create_engine(f"mysql+pymysql://{db_user}:{db_password}@{host}/{db_name}?charset=utf8mb4")
connection = pymysql.connect(host=host,
                             user=db_user,
                             password=db_password,
                             db=db_name,
                             charset="utf8mb4")
"""
now = datetime.now()
date = now.strftime("%m-%d-%Y-%H-%M-%S")
date2 = now.strftime('%Y-%m-%dT%H:%M:%SZ')

def export_data(videos, q):

    all_data = []

    for video in videos:
        video_frame = pd.DataFrame({
            "Query date_object ": now,
            "Query date_string": date2,
            "Query": video.seed,
            "rank": video.rank,
            "Id": video.videoId,
            "type": video.type,
            "publishedAt": video.publishedAt,
            "title": video.title,
            "description": video.description,
            "kind": video.kind,
            "channelId": video.channelId,
            "channelTitle": video.channelTitle,
            "liveBroadcastContent": video.liveBroadcastContent,
            "viewCount": video.viewCount,
            "likeCount": video.likeCount,
            "dislikeCount": video.dislikeCount,
            "favoriteCount": video.favoriteCount,
            "commentCount": video.commentCount,
            "link": "https://www.youtube.com/watch?v=" + video.videoId,
            "duration": video.duration,
            "dimension": video.dimension,
            "definition": video.definition,
            "caption": video.caption,
            "licensedContent": video.licensedContent,
        }, index=[0])

        all_data.append(video_frame)

    final_df = pd.concat(all_data, ignore_index=True)

    """ PANDAS MYSQL DUMP
    final_df.to_sql(db_table, index=False, con=engine, if_exists='append', chunksize=1000, method='multi')
    """

    final_df.to_excel(f"{date}-{q}.xlsx")
