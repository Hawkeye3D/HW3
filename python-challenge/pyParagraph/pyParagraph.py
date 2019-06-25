import csv
import os
import re  #regular Expressions 
#For Testing Purposes
def gettextfile(name):
    with open(name,'r') as infile:
        Paragraph = infile.read()        
        return Paragraph # pass it back for whatever

filename1 = "paragraph_1.txt"
filename2 = "paragraph_2.txt"
#filename1 = os.path.join("..","raw_data","paragraph_1.txt")  #this technique NEVER works for me!!
#filename2 = os.path.join("..","raw_data","paragraph_2.txt")
#print(filename1)
#print(filename2)
Paratext1 =(gettextfile(filename1))
Paratext2 = (gettextfile(filename2))
print("EXAMPLE ONE")
print(Paratext1)
Sentencecnt = Paratext1.split(".")
sentRE = re.split("(?<=[.!?]) +", Paratext1)
print(len(Sentencecnt))
print(len(sentRE))
print("EXAMPLE TWO")
print(Paratext2)
Sentencecnt = Paratext2.split(".")
sentRE = re.split("(?<=[.!?]) +", Paratext2)
print(len(Sentencecnt))
print(len(sentRE))
#Well, the little test I ran above truly points out the problem with RE!
#in the first paragraph there are 6 periods, no question marks and no !
#Python split command sees them all.
#RE apparently ignores the last one and reports only 6.
#The second paragraph is even worse, RE sees 2 of 12, but in fact there are only 11 sentences.
#Python counts an abbreviation; an exception to the logic.

#conclusion, use Python.  Someone,once said of Regular Expressions, "If you have a problem and you decide to use RE to help solve that problem, all you have accomplished is that you now have TWO problems."
#I whole-heartedly agree with that sentiment, not that they can't be made to work, but they are so sytax sensitive, that they would tax anyone's temper. It is generally a waste of time to try and craft a perfect
#RE solution if one is not already at hand. (Of which there are many, but even finding that can take some time.)

#One of the lessons to be learned with this exercise is that logic needs to be tested against different data sets.
#Also, sometimes the best that one can do is get an approximate solution to a complex problem.  In this case the 
#complex problem is parsing written human language.

#I won't bother going through with the rest of the exercise, it is a matter of setting up a loop to 
#split sentences into words (whitespace splitting -- default split behavior), then report the word count for each sentence, and then to a length of each
#word and divide by the number of words for an average.  If I were interested in this problem I would do further analysis by counting prepositions and subtractings them from the word
#count, so as to get an better idea of just how large the words are that are being used to describe the ideas.
      