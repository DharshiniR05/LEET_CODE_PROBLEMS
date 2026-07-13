class Solution(object):
    def checkIfPangram(self, sentence):
        
        #convert sentence into a set(unique letter)
        letters = set(sentence)

        #If there are 26 unique letter
        return len(letters) == 26

        