import youtube_dl
import requests

OUTPUTPATH = str('Downloads/')

def vid_dl(vidid, formt):
    if formt == 'audio':
        print('Download audio from video')
        opt = {
        'outtmpl': str(OUTPUTPATH + str(vidid) + '.%(ext)s'),
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192'
        }],
        'quiet': True,
        'ignoreerrors' : True,
        'no_warnings' : True,
        'restrictfilenames': True}
    if formt == 'video':
        print('Download full video')
        opt = {
        'outtmpl' : str(OUTPUTPATH + str(vidid) + '.%(ext)s'),
        'format' : 'bestvideo+bestaudio/best',
        'quiet' : True,
        'ignoreerrors' : True,
        'restrictfilenames' : True}
    
    link = 'https://www.youtube.com/watch?v=' + str(vidid)
    ydl = youtube_dl.YoutubeDL(opt)
    ydl.download([link])

def get_vidid(search):
    srchlnk = 'https://www.youtube.com/results?search_query=' + search
    response = requests.get(srchlnk+search).content
    ii = response.find(b'/watch?v=')
    vidid = str(response[ii+9:ii+20])[2:-1]
    return vidid

def get_inputs():
    print('''########################################
#     PLEASE ENTER THE INFO BELOW       #''')
    art = input('Enter the artist name: ')
    trk = input('Enter song name: ')
    formt = input("Type 'audio' to get an MP3 or 'video' to download full video")
    search = art + '+' + trk
    search = "+".join(search.strip().split())
    vidid = get_vidid(search)
    vid_dl(vidid, formt)
    if vidid in str(os.listdir('Downloads/')):
        print(f"file from video {art} - {trk} downloaded succesfully")
        input('press enter to exit')
        exit()
    else:
        print("Could not download video")
        input('press enter to exit')
        exit()
    
if __name__ == '__main__':
    get_inputs()