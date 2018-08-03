from pytube import YouTube

def downloadVideo(link):
    yt = YouTube(link)


    '''
        itag is id for quality and format of YouTube video stream.
        all_streams - stores all possible itags for given video
    '''
    all_streams = yt.streams.all()


    '''Since we are working with images we would require video only (MPEG-4)'''
    filtered_streams = yt.streams.filter(file_extension ='mp4').all()


    '''
        We would chose Stream : itag = "18"
        Given are specification of the Stream :
        -mime_type="video/mp4"
        -res="360p" fps="30fps"
        -vcodec="avc1.42001E"
        -acodec="mp4a.40.2"
    '''
    stream_by_itag = yt.streams.get_by_itag(18)


    '''We would download video to resources directory in parent directory'''
    stream_by_itag.download('../resources/Video/')

#Wario
downloadVideo('https://www.youtube.com/watch?v=ZJuxdR0KH-s')
#Mario
downloadVideo('https://www.youtube.com/watch?v=lXMJt5PP3kM')
