class Room():
    def __init__(self, room_name):
        self.name = room_name
        self.description = None
        self.linked_rooms = {}
        self.character = None
        self.item = None

# Get and set the name
    def set_name(self, room_name):
        self.name = room_name

    def get_name(self):
        return self.name


# Get and set the description
    def set_description(self, room_description):
        self.description = room_description

    def get_description(self):
        return self.description
    
    def describe(self):
        print(self.description)


# Get and set the people inside the room
    def set_character(self, room_character):
        self.character = room_character

    def get_character(self):
        return self.character


# Get and set the items inside the room
    def set_item(self, room_item):
        self.item = room_item

    def get_item(self):
        return self.item


# Set the linked rooms
    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link
        # print( self.name + " linked rooms :" + repr(self.linked_rooms) )



# Get the details
    def get_details(self):
        print("Nous sommes dans", self.name)
        print("--------------------")
        print(self.description + "\n")
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print(room.get_name() + " est direction " + direction)
        print("\n")


# Move from room to room
    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("Vous ne pouvez pas aller par là.")
            return self
                  
