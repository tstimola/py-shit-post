# import random
import random

# ASSOCIATION
class Association:
    
    # initialize association class/struct
    def __init__(self, root, assoc, frequency = 1):
        self.root = root
        self.assoc = assoc
        self.frequency = frequency
        
    def __str__(self): # hello world 4
        return (self.root + " " + self.assoc + " " + str(self.frequency))
    
    def inc(self): # increment assoc
        self.frequency += 1 # inc
        
# ASSOCIATIONBANK
class AssociationBank:
    
    # init assoc bank
    def __init__(self):
        self.word_list = []
        self.assoc_list = []
        
    # add association function
    def add(self, root, assoc):

        # iterate through all; inc if assoc exists
        for association in self.assoc_list:
            if association.root == root:
                if association.assoc == assoc:
                    association.inc()

        # append and sort list
        self.assoc_list.append(Association(root, assoc, 1))
        
    # read from a file
    def read(self, read_file):
        
        # set carat begin and end
        carat_b = 0;
        carat_e = 0
        
        # set word list and new word buffer
        self.word_list = [];
        new_word = ""
        
        # iterate through it
        for line in read_file:
            for char in line:
                if char.isspace():       
                    self.word_list.append(new_word)
                    new_word = ""
                else: # add the char
                    new_word += char
                    
    # convert loaded words to associations
    def convert(self):

        # declare last word
        last_word = None

        # set last word if not already
        for word in self.word_list:
            if last_word != None:
                self.add(last_word, word)
                last_word = word
            else: # else if not
                last_word = word
                
    # write all data to a file
    def write(self, write_file):
        
        for assoc in self.assoc_list:
            write_file.write(str(assoc) + "\n")

    # return association list
    def getassoclist(self):
        return self.assoc_list

    # get random association of those found for input
    def getrandassoc(self, root):
        for assoc in self.assoc_list:
            if assoc.root == root:
                return assoc.assoc
        if len(match_list) == 0:
            return root # fail is repeating word
        elif len(match_list) == 1:
            return match_list[0].assoc
        else: # else choose first match
            r_range = len(match_list)
            rand = random.randrange(0, r_range)
            return match_list[rand].assoc
        
# SENTENCE BOT
class SentenceBot:
    def __init__(self, bank):

        # set bank and then
        self.bank = bank # get assoc list
        self.assoc_list = bank.getassoclist()

    # create post of length, default 100
    def makepost(self, length = 100):

        # post, and last word
        post = "" # in post
        last_word = None

        # random number, and
        rand = 0 # last used
        last_rand = 0

        # while not too long
        while len(post) < length:

            # if last word doesn't exist
            if last_word == None:

                # generate a random number from length of bank list
                rand = random.randrange(0, len(self.assoc_list))
                word = self.assoc_list[rand].root # and set word
                
            else: # otherwise

                # if random boolean is TRUE
                if bool(random.getrandbits(1)):

                    # get a random association 
                    word = self.bank.getrandassoc(last_word)
                
                else: # otherwise

                    # generate a random number from length of bank list
                    rand = random.randrange(0, len(self.assoc_list))
                    word = self.assoc_list[rand].root

            # add word to post
            post += word + " "

            # set last vars
            last_word = word
            last_rand = rand

        # return final
        return post
    
            # ENTRY POINT #
            
# load read and write buffers
r_buffer = open('read_buffer.txt', 'r');
w_buffer = open('write_buffer.txt', 'w')

# initialize association bank
assoc_bank = AssociationBank()

# read, convert and write
assoc_bank.read(r_buffer)
assoc_bank.convert()
assoc_bank.write(w_buffer)

# create and use sentence bot
sentence_bot = SentenceBot(assoc_bank)
print(sentence_bot.makepost())
