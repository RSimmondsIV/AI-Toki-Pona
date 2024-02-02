punctuation = [',','.',':',"'",'"','-','!','?']

class vectorization(object):
    # Class that, given a csv file of words, finds the amount of times that word is used in some text 
        # In this case, for Simplicity, Toki Pona is used.
    def __init__(self, wordfile, poem):
        """
        :type wordfile: file (csv)
        :type poem: String
        """
        self.wordfile = wordfile
        self.poem = poem
        self.punctuation = punctuation # This is global and easy to modify
        
    def pona_words(self) -> list:
        """
        :type file: file
        :rtype: List [str]
        """
        # Open the file with known words,
        # using encoding to remove the UTF-8 Byte Order Mark, which is what shows up as ï»¿
            # senshin - https://stackoverflow.com/questions/34399172/why-does-my-python-code-print-the-extra-characters-%C3%AF-when-reading-from-a-tex
        read_file = open(self.wordfile,'r',encoding='utf-8-sig')
        # Read lines TODO: Figure out why the first 3 characters are special and nonalphanumeric
        toki_pona_words = read_file.readline()[:-1].split(',')
        # print(toki_pona_words)
        read_file.close()
        return toki_pona_words

    def make_vectors(self) -> list:
        """
        :type poem: String
        :type file: file
        :rtype: List [int]
        """
        # Get tested words from previous method
        toki_pona_words = self.pona_words() 
        # Make an empty array containing all possible words
        out_array = [0] * len(toki_pona_words)
        new_poem = self.poem # This is for string modification
        # remove all numeric characters
        new_poem = ''.join([i for i in self.poem if not i.isdigit()])
        # remove all known punctuations, these can also be special characters.
        for i in self.punctuation:
            new_poem = new_poem.replace(i,'')
        
        # Split on spaces, assumes that there are no typos, or lacks of space
            #ie. for English:
                # I am a student - This is good
                # Iamastudent - This would not read as known words, unless specified in given csv.
        new_poem = new_poem.split(' ')
        
        # given a string TODO: allow for file input.
        for word in new_poem:
            # If word is in known word list, increase value at given index, TODO: Normalize
            for i in range(len(toki_pona_words)):
                if word == toki_pona_words[i]:
                    out_array[i] = out_array[i] + 1
                else:
                    pass
        # Original poem given
        print(self.poem)
        # All occurances of a word
        print(new_poem)

        return out_array

test1 = vectorization('Toki_Pona_Vectors.csv', 
                    'sina, sina la, ken ala mi la. pilin. ante. seme?')

print(test1.make_vectors())