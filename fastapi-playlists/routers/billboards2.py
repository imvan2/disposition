from fastapi import APIRouter, Depends, Response
from typing import List, Optional, Union

import requests
import aiohttp
from bs4 import BeautifulSoup
import schedule
import time
import threading

from queries.billboards2 import (
    Error,
    BillboardIn,
    BillboardRepo,
    BillboardOut,
)

router = APIRouter()
# where this file is stored

@router.post("/billboard")
async def get_billboard(
    repo: BillboardRepo = Depends()):
    page = requests.get("https://www.billboard.com/charts/hot-100/")
    
    async with aiohttp.ClientSession() as session:
        async with session.get("https://www.billboard.com/charts/hot-100/") as response:
            html = await response.text()
            soup = BeautifulSoup(html, "html.parser")
            
            top100 = []
            
            for div_container in soup.find_all("div", {"class:", "o-chart-results-list-row-container"}):
                for ul_tag in div_container.find_all("ul", {"class": "a-chart-has-chart-detail"}):
                    # finding rank
                    li_rank_tag = ul_tag.find("li", {"class:", "o-chart-results-list__item // lrv-u-background-color-black lrv-u-color-white u-width-100 u-width-55@mobile-max u-width-55@tablet-only lrv-u-height-100p lrv-u-flex lrv-u-flex-direction-column@mobile-max lrv-u-flex-shrink-0 lrv-u-align-items-center lrv-u-justify-content-center lrv-u-border-b-1 u-border-b-0@mobile-max lrv-u-border-color-grey"})
                    span_tags = li_rank_tag.find("span", {"class:", "c-label a-font-primary-bold-l u-font-size-32@tablet u-letter-spacing-0080@tablet"})
                    rank = span_tags.text.split()
                    rank = int(rank[0])
                    
                    # getting album pic
                    if rank == 1:
                        li_pic_tag = ul_tag.find("li", {"class:", "o-chart-results-list__item // u-width-200 u-width-100@tablet-only u-width-67@mobile-max lrv-u-border-b-1 u-border-b-0@mobile-max lrv-u-border-color-grey u-flex-order-n1@mobile-max"})
                    else:
                        li_pic_tag = ul_tag.find("li", {"class:", "o-chart-results-list__item // u-width-100 u-width-67@mobile-max lrv-u-border-b-1 u-border-b-0@mobile-max lrv-u-border-color-grey u-flex-order-n1@mobile-max"})
                    images = li_pic_tag.findAll("img")
                    album_pic = images[0]["data-lazy-src"]

                    # getting song details
                    ul_details = ul_tag.find("ul", {"class:", "lrv-a-unstyle-list lrv-u-flex lrv-u-height-100p lrv-u-flex-direction-column@mobile-max"})
                    title = ul_details.findAll("h3")
                    title = title[0].text.strip()
                    artist = ul_details.findAll("span")
                    artist = artist[0].text.strip()
                    
                song = {
                    "rank": rank,
                    "title": title,
                    "artist": artist,
                    "album_pic": album_pic,
                    }
                repo.create_billboard(song)
                    
                    
            # HTML FOR BILLBOARD HOT 100
                # div container class = "o-chart-results-list-row-container"
                    # ul container class = "o-chart-results-list-row // lrv-a-unstyle-list lrv-u-flex u-height-100 lrv-u-background-color-white a-chart-has-chart-detail"
                        # li FOR RANK class = "o-chart-results-list__item // lrv-u-background-color-black lrv-u-color-white u-width-100 u-width-55@mobile-max u-width-55@tablet-only lrv-u-height-100p lrv-u-flex lrv-u-flex-direction-column@mobile-max lrv-u-flex-shrink-0 lrv-u-align-items-center lrv-u-justify-content-center lrv-u-border-b-1 u-border-b-0@mobile-max lrv-u-border-color-grey"
                            # span class = "c-label  a-font-primary-bold-l u-font-size-32@tablet u-letter-spacing-0080@tablet"
                        # li FOR PIC class = "o-chart-results-list__item // u-width-100 u-width-67@mobile-max lrv-u-border-b-1 u-border-b-0@mobile-max lrv-u-border-color-grey u-flex-order-n1@mobile-max"
                            # div class = "c-lazy-image  lrv-u-width-100 u-width-67@mobile-max"
                                # div class = "lrv-a-crop-1x1 a-crop-67x100@mobile-max"
                                    # img class = "c-lazy-image__img lrv-u-background-color-grey-lightest lrv-u-width-100p lrv-u-display-block lrv-u-height-auto"
                        # li IGNORE
                        # li FOR DETAILS class = lrv-u-width-100p
                            # ul class = "lrv-a-unstyle-list lrv-u-flex lrv-u-height-100p lrv-u-flex-direction-column@mobile-max"
                                # li FOR SONG INFO, ONLY USE THE FIRST class = "class="o-chart-results-list__item // lrv-u-flex-grow-1 lrv-u-flex lrv-u-flex-direction-column lrv-u-justify-content-center lrv-u-border-b-1 u-border-b-0@mobile-max lrv-u-border-color-grey-light lrv-u-padding-l-050 lrv-u-padding-l-1@mobile-max""
                                    # h3 id = "title-of-a-story"
                                    # span class = "c-label  a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only"
    return

@router.get("/top100")
def get_all(repo: BillboardRepo = Depends()):
    return repo.get_all()

@router.delete("/billboard/{rank}")
def delete_billboard():
    repo = BillboardRepo()
    for num in range(1,101):
        print("num:", num)
        repo.delete(rank=num)
    return 

    
def run_continuously(interval=1):
    """Continuously run, while executing pending jobs at each
    elapsed time interval.
    @return cease_continuous_run: threading. Event which can
    be set to cease continuous run. Please note that it is
    *intended behavior that run_continuously() does not run
    missed jobs*. For example, if you've registered a job that
    should run every minute and you set a continuous run
    interval of one hour then your job won't be run 60 times
    at each interval but only once.
    """
    cease_continuous_run = threading.Event()

    class ScheduleThread(threading.Thread):
        @classmethod
        def run(cls):
            while not cease_continuous_run.is_set():
                schedule.run_pending()
                time.sleep(interval)

    continuous_thread = ScheduleThread()
    continuous_thread.start()
    return cease_continuous_run

schedule.every().day.at("10:29").do(delete_billboard)
schedule.every().day.at("10:30").do(get_billboard)

stop_run_continuously = run_continuously()

time.sleep(10)

stop_run_continuously.set()