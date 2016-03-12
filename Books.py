#  File: Books.py

#  Description: Reads two books and compares their content

#  Student Name: Christina Nerona

#  Date Created: 05/04/2015

#  Date Last Modified: 05/06/2015


#Function to create global dictionary
def create_word_dict(book='words.txt'):
    word_book=open(book)
    word_list=[]
    
    #Creating a dictionary given the word file
    for line in word_book:
        line=line.strip()
        word_list.append(line)
    return(word_list)

#Function to parse/filter string
def parseString(st):
    #Filters through line to create words separated by spaces
    s=''
    st.replace("'s"," s")
    for ch in range(len(st)):
        if (st[ch]>='a' and st[ch]<='z') or (st[ch]>='A' and st[ch]<='Z') or (st[ch]=="'"):
            s+=st[ch]
            #If contraction exists, then 's is replaced with s

        else:
            s+=' '
    return s

#Function for getting statistical information on book content
def getWordFreq(name_book):
    #open the book
    book=open(name_book)

    #create an empty set for words
    word_set=set()

    #create a dictionary for word frequency
    word_dict={}

    #track total words
    total_words=0

    word_list=[]

    for line in book:
        line=line.strip()
        
        #prepping line and sending through filter
        line=parseString(line)
        line=line.split()
        for elt in line:
            word_list.append(elt)
    word_list.sort()

    #Check for Capitalized words
    global_dict=create_word_dict()
        
    #add words to the dictionary
    for word in word_list:
        word_set.add(word)
        total_words+=1

        #add words to dictionary
        if word in word_dict:
            word_dict[word]=word_dict[word]+1
        else:
            word_dict[word]=1
    capitals=[]
    for key in word_dict:
        if (key[0].isupper()):
            capitals.append(key)

    #Checking capitals
    capital_lets=capitals
    for word in capital_lets:
        if not (word.lower() in global_dict):
            total_words-=word_dict[word]
            word_dict.pop(word)
        else:
            if word.lower() in word_dict:
                word_dict.pop(word)
                word_dict[word.lower()]+=1
            else:
                word_dict.pop(word)
                word_dict[word.lower()]=1

    #close the file
    book.close()

    #Sets ratios
    num_unique_words=len(list(word_dict.keys()))
    word_ratio=num_unique_words/total_words
 
    
    #print the word frequency
    all_words=list(word_dict.keys())
    all_words.sort()

    #Returns key stats
    return [num_unique_words,total_words,word_ratio*100,word_dict,all_words]
    
def main():
    #Get input values
    book1=input('Enter name of first book: ')
    book2=input('Enter name of second book: ')
    print()

    #For testing purposes
    #book1='dickens.txt'
    #book2='hardy.txt'

    #Getting names of authors
    name1=input('Enter last name of first author: ')
    name2=input('Enter last name of second author: ')

    #For testing
    #name1='Dickens'
    #name2='Hardy'

    #separating values from fxn to indiv values
    list_values1=(getWordFreq(book1))
    unique1=(list_values1[0])
    total1=(list_values1[1])
    ratio1=(list_values1[2])
    dict1=(list_values1[3])
    all_words1=(list_values1[4])

    #separating values from fxn to indiv values
    list_values2=(getWordFreq(book2))
    unique2=(list_values2[0])
    total2=(list_values2[1])
    ratio2=(list_values2[2])
    dict2=(list_values2[3])
    all_words2=(list_values2[4])

    #Prints information for author1
    print()
    print(name1)
    print('Total distinct words =',unique1)
    print('Total words (including duplicates) =',total1)
    print('Ratio (% of total distinct words to total words) =',round(ratio1,10))
    
    #Finds words unique to author1
    distinct_words1=[]
    for word in dict1:
        if not (word in dict2):
            distinct_words1.append(word)
    distinct_words1.sort()

    #Assigns freq to each unique word to author1
    distinct_word_dict1={}
    for word in distinct_words1:
        distinct_word_dict1[word]=dict1[word]
    
    #Prints info for author1
    print()
    print(name2)
    print('Total distinct words =',unique2)
    print('Total words (including duplicates) =',total2)
    print('Ratio (% of total distinct words to total words) =',round(ratio2,10))


    #Finds unique words for author2
    distinct_words2={}
    for word in dict2:
        if not (word in dict1):
            distinct_words2[word]=dict2[word]

    #Prints Comparison stats
    print()
    print(name1,'used',str(len(distinct_words1)),'words that',name2,'did not use.')
    #Determines comparison stats
    sum_distinct1=sum(distinct_word_dict1.values())
    print('Relative frequency of words used by',name1,'not in common with',name2,'=',str(round(100*(sum_distinct1/(sum(dict1.values()))),10)))
    print('\n')

    #Prints Comparison stats
    print(name2,'used',str(len(list(distinct_words2.keys()))),'words that',name1,'did not use.')
    sum_distinct2=sum(distinct_words2.values())
    print('Relative frequency of words used by',name2,'not in common with',name1,'=',str(round(100*(sum_distinct2/(sum(dict2.values()))),10))) 
    print('\n')

main()
