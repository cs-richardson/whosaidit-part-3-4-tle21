import string
import math

#Get_Counts
#The function takes in a file name, opens it and and splits the whole text into indivisual words
#The function counts the amount of word that has been said and how many times each word has been said
translator =  str.maketrans('','',string.punctuation) #Removes all punctuations after the string so "heart", "heart." and "heart," counts as the same word
def get_counts(file_name):     

    counts = dict() 
    
    file = open(file_name,'r') 
    
    amount = 0 
    
    for line in file:
        text = file.read() 
        text = text.translate(translator)
        raw_words = text.split() 
        
        for i in range(0, len(raw_words)):  
            words = raw_words[i].lower()
            if words in counts: 
                counts[words] = counts[words] + 1
                amount = amount + 1 
            else:
                counts[words] = 1 
                amount = amount + 1 
        

    counts.update({'_total': amount}) 
    return (counts) 
    file.close() 

hamlet = get_counts("hamlet-full.txt") 
sense_and_sensibility = get_counts("sense-and-sensibility.txt")

#Get_score
#Get_score takes a word and a dictionary and gives a score on how close the word is to the dictionary.
#The higher the score is, the closer it is to the dictionary 
def get_score(word, counts):
    denominator = float(1 + counts["_total"])
    if word in counts:
        return math.log((1 + counts[word]) / denominator)
    else:
        return math.log(1 / denominator)     

#Raw user text is split into indivisual words
#The length of user_text is stored inside user_text_length
raw_user_text = input("Please Enter Your Text: ")
user_text = raw_user_text.split()
user_text_length = len(user_text)

#predict
#The predict function takes the user text and uses get_score to give a score to see how close it is to a dictionary of words from a shakespeare work and a Jane Austen work
#If the score for the shakespeare dictionary is higher it will print "I think that was written by Shakespeare", and vice versa

def predict(user_text, shakespeare, jane_austen):
    score_shakespeare = float(0)
    score_janeausten = float(0)
    for i in range (0, user_text_length):
        score1 = get_score(user_text[i], shakespeare)
        score_shakespeare = score_shakespeare + score1
        score2 = get_score(user_text[i], jane_austen)
        score_janeausten = score_janeausten + score2
    if float(score_shakespeare) > float(score_janeausten):
        return ("I think that was written by Shakespeare.")
    if float(score_janeausten) > float(score_shakespeare):
        return ("I think that was written by Jane Austen.")
       

print(predict(user_text, hamlet, sense_and_sensibility)) #Calling the function predict 




    

    
