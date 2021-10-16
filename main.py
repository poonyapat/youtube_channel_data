from youtube_channel_data import youtube_channel_data


if __name__ == '__main__':
    channel_data = youtube_channel_data.find_channel_data('<channelId>')
    youtube_channel_data.display_video_uploaded_date(channel_data)
