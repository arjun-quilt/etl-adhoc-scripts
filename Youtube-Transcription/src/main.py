"""
This module defines the `main()` coroutine for the Apify Actor, executed from the `__main__.py` file.

Feel free to modify this file to suit your specific needs.

To build Apify Actors, utilize the Apify SDK toolkit, read more at the official documentation:
https://docs.apify.com/sdk/python
"""

from apify import Actor
from youtube_transcript_api import YouTubeTranscriptApi as yta
from httpx import AsyncClient
import json

async def main() -> None:
    """
    The main coroutine is being executed using `asyncio.run()`, so do not attempt to make a normal function
    out of it, it will not work. Asynchronous execution is required for communication with Apify platform,
    and it also enhances performance in the field of web scraping significantly.
    """
    async with Actor:
        actor_input = await Actor.get_input() or {}
        video_url = actor_input.get('url')
        #print(video_url)
        # Extract the video id from url 
        if video_url is not None:

            video_id = video_url.split('=')[-1]
            if video_id:
                video_id=video_id
            else:
                print('invalid youtube url')

            #youtube_url = f"https://www.youtube.com/watch?v={video_id}"
            transcription = yta.get_transcript(video_id)
            transcript_paragraph = " ".join(value['text'] for value in transcription)
            transcript_data = {'transcript': transcript_paragraph}
            # json_transcript = json.dumps(transcript_data, indent=2)
            # print(type(json_transcript))
            

            await Actor.push_data([transcript_data])






