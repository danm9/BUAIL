import requests
from bs4 import BeautifulSoup

def download_file(url):
    # Creates a filename to write to; assumes we'll put the downloaded files in a folder called Output - make sure you create this folder first...
    # The filename is the last bit of the URL
    print("Download found! Let's smash " + url) 
    filename = 'Output/' + url.split('/')[-1]

    print("Downloading " + url + " to " + filename)

    # Uses requests again to actually grab the file and save it
    r = requests.get(url, stream=True)
    with open(filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024): 
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
    print("Done!")

def search_pi():
    print("Opening site...")

    f = requests.get('https://www.raspberrypi.org/magpi/issues/')
    soup = BeautifulSoup(f.text,'lxml')

    print("Hunting...")

    for link in soup.find_all('a'):
        url = link.get('href')
        if url is not None:
            if url.endswith('.pdf'):
                download_file(url)

    print("Hunt complete!")

print("Hello, World!")
print("Let's do some mad scraping")
search_pi()
print("Finished")