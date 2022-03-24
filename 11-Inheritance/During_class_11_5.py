class Music:
    def __init__(self, artist, track, album, year):
        self.artist = artist
        self.track = track
        self.album = album
        self.year = year
        
    def __str__(self):
        return "Performer: " + str(self.artist) + "\n" + "Song: " + str(self.track).ljust(12) + "\n" + "Album: " + str(self.album) + "\n" + "Year: " + str(self.year)
    
mymusic = Music("Ed Sheeran", "Hearts Don't Break Around Here", "Divide", 2017)
print(mymusic)