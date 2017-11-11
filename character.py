class Character():

    # Create a character
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None

    # Describe this character
    def describe(self):
        print(self.name + " est là!")
        print(self.description + "\n")

    # Set what this character will say when talked to
    def set_conversation(self, conversation):
        self.conversation = conversation


    # Talk to this character
    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " dit]: " + self.conversation)
        else:
            print(self.name + " ne veut pas parler avec vous!")


    # Fight with this character
    def fight(self, combat_item):
        print(self.name + " ne veut pas se battre avec vous!")
        return True

class Enemy(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None

    def set_weakness(self, weakness):
        self.weakness = weakness

    def get_weakness(self):
        return self.weakness

    def fight(self, combat_item):
        if combat_item == self.weakness:
            print("Tu as repoussé " + self.name + " avec le " + combat_item)
            return True
        else:
            print(self.name + " t'a écrasé, petit aventurier.")
            return False

class Friend(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)