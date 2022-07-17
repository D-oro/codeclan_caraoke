class Room:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.guests_in_room = []
        self.songs = []
        
#Add guest to room
    def add_guest_to_room(self, guest):
        if len(self.guests_in_room) < self.capacity:
            self.guests_in_room.append(guest)
        else:
            return "room fully booked"

#Remove guest from room
    def remove_guest_from_room(self, guest):
        self.guests_in_room.remove(guest)

#Add Song to room
    def add_song_to_room(self, song):
        self.songs.append(song)