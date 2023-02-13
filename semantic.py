
import spacy



# spacy md model
nlp = spacy.load('en_core_web_md')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

"""From the results we can see 'cat' similar to 'monkey' by 0.5929929675536907 units.
   Then, 'banana' and 'monkey' similarity gives result of 0.40415016164997786, while
   'banana' and 'cat'  0.22358827466989753 . Interestingly, NLP can understand that cat and monkey  
   are animals, while comparison with banana obviously shows less similarity result. However, another 
   interesting point is differrence between banana and monkey, also banana and cat. 
   Here,  from general knowledge we can say some types of monkeys are known to consume fruits,
   priorly bananas, while all cats are meat eaters."""


# sm  Model
nlp = spacy.load('en_core_web_sm')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

"""Difference between sm and md models according to Userwarning is that sm model has no word vectors loaded.
    As well as according to documentations difference between all libraries are the statistical size.
    So, for more accurate result it is reommended to use larger models.
    As result of same word comparison we got:'cat'  and 'monkey'  0.6770566055016188,
    'banana' and 'monkey' 0.7276309976205778  and 'banana' and 'cat' 0.6806929905901463' .
    Which obviously makes less sense than results given by md model"""

#Ref: https://spacy.io/models/en

#Github
