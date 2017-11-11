class Item():
    def __init__(self, item_name):
        self.name = item_name
        self.readable_name = None
        self.description = None
        self.location = None
        
    def set_name(self, item_name):
        self.name = item_name

    def set_readable_name(self, readable_name):
        self.readable_name = readable_name

    def get_readable_name(self):
        return self.readable_name

    def get_name(self):
        return self.name
    
    def set_description(self, item_description):
        self.description = item_description

    def get_description(self):
        return self.description

# Describe this item
    def describe(self):
        print("Tu vois " + self.readable_name)
        print(self.description + "\n")
