'''import webbrowser
import random

def open_random_youtube_video(video_links):
    # Shuffle the video links randomly
    random.shuffle(video_links)

    # Pick the first video from the shuffled list
    chosen_video = video_links[0]

    # Open the chosen video in the default web browser
    webbrowser.open(chosen_video)

    # Remove the chosen video from the list
    video_links.remove(chosen_video)

if __name__ == "__main__":
    # List of YouTube video links
    youtube_links = [
        "https://youtu.be/inpok4MKVLM?si=iqCzv3j_vAHQ8C2v",
        "https://youtu.be/r7atAuEprl4?si=1lOhr4mYWjlOmfvM",
        "https://youtu.be/F5KfygRRtrg?si=G5sKv4KL1dHpp6yk",
        "https://youtu.be/PIzWG8kkr6w?feature=shared",
        "https://youtu.be/geYYteAXLPQ?feature=shared",
        "https://youtu.be/_YAgCAhVtss?feature=shared",
        "https://youtu.be/OrfVe80_wlU?feature=shared",
        "https://youtu.be/CMDbxLnShg4?feature=shared",
        "https://youtu.be/qQXW6k86mwk?feature=shared",
        "https://youtu.be/ztTexqGQ0VI?si=cZobcCChonAi2xdU",
        "https://youtu.be/7WnZisfYMsE?si=9exXW-uLrQwLGopS",
        "https://youtu.be/psx_NGVO4JQ?si=mSTzoteL5wwi7Rjg",
        "https://youtu.be/yu64O1jdVIk?si=1-UePmb7uPoWsTDY",
        "https://youtu.be/qQXW6k86mwk?si=0Ds1c90WAkv6PjHv",
        "https://youtu.be/9GWnQXVEiJM?si=Kl30O_gf2l1VksZO",
        "https://youtu.be/BXD7Mn_Fz1o?si=soS1ByUG11cfJdys",
        "https://youtu.be/gU_ABFUAVAs?feature=shared",
        "https://youtu.be/9HNt6kp0JN8?si=17tUqI9TAiHb55gm",
        "https://youtu.be/ciOInp7Ymps?si=pj99ghCvmH0UjkIV",
        "https://youtu.be/pINfS7ImWec?si=CbrqdhBAoV2E8T_6",
        "https://youtu.be/BVZS8XqNyEY?si=hfawwdbEI5XmBua7",
        "https://youtu.be/TCuI-AG2k3s?si=GdTC8e26XGhPRihN"
    ]

    open_random_youtube_video(youtube_links)
'''

import random
import webbrowser
from googleapiclient.discovery import build

# Define your YouTube API key here
YOUTUBE_API_KEY = "YOUR_API_KEY"

def get_random_youtube_video():
    # List of YouTube video links
    youtube_links = [
        "https://youtu.be/inpok4MKVLM?si=iqCzv3j_vAHQ8C2v",
        "https://youtu.be/r7atAuEprl4?si=1lOhr4mYWjlOmfvM",
        "https://youtu.be/F5KfygRRtrg?si=G5sKv4KL1dHpp6yk",
        "https://youtu.be/PIzWG8kkr6w?feature=shared",
        "https://youtu.be/geYYteAXLPQ?feature=shared",
        "https://youtu.be/_YAgCAhVtss?feature=shared",
        "https://youtu.be/OrfVe80_wlU?feature=shared",
        "https://youtu.be/CMDbxLnShg4?feature=shared",
        "https://youtu.be/qQXW6k86mwk?feature=shared",
        "https://youtu.be/ztTexqGQ0VI?si=cZobcCChonAi2xdU",
        "https://youtu.be/7WnZisfYMsE?si=9exXW-uLrQwLGopS",
        "https://youtu.be/psx_NGVO4JQ?si=mSTzoteL5wwi7Rjg",
        "https://youtu.be/yu64O1jdVIk?si=1-UePmb7uPoWsTDY",
        "https://youtu.be/qQXW6k86mwk?si=0Ds1c90WAkv6PjHv",
        "https://youtu.be/9GWnQXVEiJM?si=Kl30O_gf2l1VksZO",
        "https://youtu.be/BXD7Mn_Fz1o?si=soS1ByUG11cfJdys",
        "https://youtu.be/gU_ABFUAVAs?feature=shared",
        "https://youtu.be/9HNt6kp0JN8?si=17tUqI9TAiHb55gm",
        "https://youtu.be/ciOInp7Ymps?si=pj99ghCvmH0UjkIV",
        "https://youtu.be/pINfS7ImWec?si=CbrqdhBAoV2E8T_6",
        "https://youtu.be/BVZS8XqNyEY?si=hfawwdbEI5XmBua7",
        "https://youtu.be/TCuI-AG2k3s?si=GdTC8e26XGhPRihN"
    ]

    # Randomly choose a video from the list
    chosen_video = random.choice(youtube_links)

    return chosen_video

def open_youtube_video(video_url):
    # Open the chosen video in the default web browser
    webbrowser.open(video_url)

if __name__ == "__main__":
    # Get a random YouTube video URL
    random_video_url = get_random_youtube_video()

    # Open the YouTube video in the default web browser
    open_youtube_video(random_video_url)
