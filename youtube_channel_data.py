import requests
import json


class YoutubeChannelData:
    def __init__(self):
        self.lang = 'en'

    def _generate_body(self, browseId):
        return {
            "context": {
                "client": {
                    "hl": self.lang,
                    "clientName": "WEB",
                    "clientVersion": "2.20211014.05.00",
                },
            },
            "browseId": browseId,
            "params": "EgZ2aWRlb3M%3D"
        }

    def find_channel_data(self, browseId):
        body = self._generate_body(browseId)
        r = requests.post(
            'https://www.youtube.com/youtubei/v1/browse?key=AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8',
            json=body
        )
        data = json.loads(r.text)
        return data

    def display_video_uploaded_date(self, channel_data):
        """
        Support only EN lang, must change 'Videos' constants to variable if want to do with other languages
        """
        for tab in channel_data['contents']['twoColumnBrowseResultsRenderer']['tabs']:
            if 'tabRenderer' in tab and tab['tabRenderer']['title'] == 'Videos':
                items = tab['tabRenderer']['content']['sectionListRenderer']['contents'][0]['itemSectionRenderer']['contents'][0]['gridRenderer']['items']
                for item in items:
                    if 'gridVideoRenderer' in item:
                        print(item['gridVideoRenderer']['title']['runs'][0]['text'])
                        if 'publishedTimeText' in item['gridVideoRenderer']:
                            print('Uploaded:', item['gridVideoRenderer']['publishedTimeText']['simpleText'])
                        elif 'thumbnailOverlays' in item['gridVideoRenderer']:
                            print(
                                item['gridVideoRenderer']['thumbnailOverlays'][0]['thumbnailOverlayTimeStatusRenderer'][
                                    'text']['runs'][0]['text'])
                        print('----' * 10)


youtube_channel_data = YoutubeChannelData()
