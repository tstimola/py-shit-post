# import random
import random
# ALPHABETICAL STRING CHECK
def alphacheck(string_a, string_b, precision = 100, result = False):
    # EMPTY STRING PRECHECK
    if len(string_a) == 0:
        if len(string_b) == 0: return result
        else: result = False ; return result
    elif len(string_b) == 0:
        if len(string_a) == 0: return result
        else: result = True  ; return result
    # chars to compare
    char_a = string_a[0]; char_b = string_b[0]
    # compare characters
    if char_a > char_b: result = True
    # shorten strings to recurse
    new_string_a = string_a[1:]
    new_string_b = string_b[1:]
    #    RECURSE
    if precision == 1: return result
    else: precision -= 1 # RECURSE IT
    return alphacheck(new_string_a, new_string_b, precision, result)
# ASSOCIATION
class Association:
    # initialize association class/struct
    def __init__(self, root, assoc, frequency = 1):
        self.root = root
        self.assoc = assoc
        self.frequency = frequency
    def __str__(self): # R: hello A: world F: 450713
        return (self.root + self.assoc + str(self.frequency))
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
        for association in self.assoc_list:
            if association.root == root:
                if association.assoc == assoc:
                    association.inc()
        self.assoc_list.append(Association(root, assoc, 1))
    # read from a file
    def read(self, read_file):
        # set carat begin and end
        carat_b = 0; carat_e = 0
        # set word list and new word buffer
        self.word_list = []; new_word = ""
        # iterate through it
        for line in read_file:
            for char in line:
                if char.isspace():       
                    self.word_list.append(new_word)
                    new_word = ""
                else: # add the char
                    new_word += char
    # convert loaded words to associations
    def convert(self): # and doooo it bruh
        last_word = None
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
    def getassoclist(self):
        return self.assoc_list
    def getfirstassoc(self, root): # get rand match assoc
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
        self.bank = bank # def bank and get list
        self.assoc_list = bank.getassoclist()
    def makepost(self, length = 100):
        post = "" # set empty
        last_word = None
        rand = 0
        last_rand = 0
        while len(post) < length:
            if last_word == None:
                rand = random.randrange(0, len(self.assoc_list))
                word = self.assoc_list[rand].root
            else: # 50% chance of random word vs associated
                if bool(random.getrandbits(1)):
                    word = self.bank.getfirstassoc(last_word)
                else: # set random
                    rand = random.randrange(0, len(self.assoc_list))
                    word = self.assoc_list[rand].root
            post += word + " "
            last_word = word
            last_rand = rand
        return post # DONE YO
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
