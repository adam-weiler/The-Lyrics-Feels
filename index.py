# import matplotlib.pyplot as plt
# plt.plot([1, 2, 3, 4])
# plt.ylabel('some numbers')
# plt.show()



import csv  # Needed to open csv files.
# import string  # Needed to strip punctuation from unfiltered_lyrics.
import re  # Ditto
# from collections import OrderedDict 

file = open('./TestFile.csv', 'r')
librareader = csv.reader(file)

# unfiltered_lyrics = 'happiness Happy Vacation always fun enjoyment a about across'
unfiltered_lyrics = "There must be some way out of here Said the joker to the thief There's too much confusion I can't get no relief Businessmen, they drink my wine Plowmen dig my earth None of them along the line Know what any of it is worth No reason to get excited The thief, he kindly spoke There are many here among us Who feel that life is but a joke But you and I, we've been through that And this is not our fate So let us not talk falsely now The hour is getting late All along the watchtower Princes kept the view While all the women came and went Barefoot servants too Outside, in the distance A wildcat did growl Two riders were approaching The wind began to howl"
#Need to remove special characters, punctuation.
#Maybe remove duplicate characters?
#Need to remove -ing, -ly suffixes
# Edge case - princes removed but prince is valid word, riders removed but rider is valid word, same for servants and servant, same for women and woman
common_words = ['a', 'ah', 'about', 'above', 'across', 'after', 'again', 'ago', 'all', 'along', 'already', 'always', 'am', 'an', 'and', 'another', 'any', 'anyone', 'anything', 'are', 'around', 'as', 'at', 'away', 'be', 'before', 'behind', 'below', 'besides', 'best', 'better', 'between', 'both', 'but', 'by',   'can\'t',   'colour', 'course', 'down', 'each', 'early', 'either', 'else', 'enough', 'even', 'ever', 'every', 'everyone', 'everybody', 'except', 'extremely', 'false', 'far', 'fast', 'few', 'for', 'from', 'front', 'further', 'goodbye', 'half', 'he', 'hello', 'her', 'here', 'hers', 'him', 'his', 'how', 'i', 'if', 'in', 'inside', 'into', 'is', 'it', 'its', 'just', 'kept', 'la', 'last', 'lately', 'left', 'less', 'long', 'lot', 'lower', 'mah', 'many', 'mark', 'me', 'more', 'most', 'much', 'my', 'near', 'nearly', 'neighbour', 'neither', 'never', 'next', 'no', 'none', 'nor', 'not', 'nothing', 'now', 'of', 'off', 'often', 'oh', 'on', 'only', 'ooh', 'oooh', 'or', 'our', 'out', 'outside', 'over', 'own', 'per', 'please', 'plenty', 'probably', 'quite', 'rah', 'really', 'ro', 'said', 'same', 'several', 'she', 'should', 'since', 'so', 'some', 'someone', 'something', 'sometimes', 'soon', 'still', 'such', 'sudden', 'than', 'that', 'the', 'their', 'them', 'then', 'there', 'therefore', 'these', 'they', 'this', 'though', 'through', 'to', 'today', 'together', 'tomorrow', 'tonight', 'too', 'true', 'twice', 'under', 'until', 'up', 'usually', 'very', 'was', 'we', 'were', 'well', 'what', 'when', 'where', 'which', 'while', 'who', 'why', 'with', 'without', 'yesterday', 'yet', 'you', 'your', 'zero']  # Adding ah, be, kept, la, mah, oh, ooh, oooh, rah, ro, said, them, they, through
# contractions = ["aren't", "can't", "couldn't", "didn't", "doesn't", "don't", "hadn't", "hasn't", "haven't", "he'd", "he'll", "he's", "I'd", "I'll", "I'm", "I've", "isn't", "let's", "mightn't", "mustn't", "shan't", "she'd", "she'll", "she's", "shouldn't", "that's", "there's", "they'd", "they'll", "they're", "they've", "we'd", "we're", "we've", "weren't", "what'll", "what're", "what's", "what've", "where's", "who's", "who'll", "who're", "who's", "who've", "won't", "wouldn't", "you'd", "you'll", "you're", "you've"]

if (unfiltered_lyrics):
    total_mean_valence = 0
    total_mean_arousal = 0
    total_mean_dominance = 0
    index = 0
    unique_words = []

    # lyrics_list = unfiltered_lyrics.strip(string.punctuation)

    # lyrics_list = unfiltered_lyrics" ".join(re.split('\W+', s))

    # lyrics_list = "".join(OrderedDict.fromkeys(unfiltered_lyrics)) 
    lyrics_list = re.sub('[^A-Za-z0-9\']+', ' ', unfiltered_lyrics)  # Removes all special characters from text.

    lyrics_list = lyrics_list.lower().split()  # Takes input, puts all in lowercase, splits into a list.
    lyrics_list = list(set(lyrics_list))

    lyrics_list.sort()  # Sorts list alphabetically.

    for word in common_words:  # For each word in common_words.
        if word in lyrics_list:  # If a common word is in lyrics_list, it is removed.
            lyrics_list.remove(word)
            print(f'Removing common word: {word}')

        # if word in contractions:
        #     lyrics_list.remove(word)
        #     print(f'Removing contraction: {word}')  # This isn't working yet.

    # print(string.punctuation)



    length = len(lyrics_list)

    print(lyrics_list)

    for line in librareader:  # For each line in CSV file.
        word=line[1]  # Takes word from B column of CSV file.

        if word in lyrics_list:  # If current word of CSV file matches the word in the index file.
            print(f'Word found: {word}')
            unique_words.append(word)

            valence_mean_sum=float(line[2])
            arousal_mean_sum=float(line[5])
            dominance_mean_sum=float(line[8])
            
            print(f'valence: {valence_mean_sum}')
            print(f'arousal: {arousal_mean_sum}')
            print(f'dominance: {dominance_mean_sum}\n')

            total_mean_valence += valence_mean_sum
            total_mean_arousal += arousal_mean_sum
            total_mean_dominance += dominance_mean_sum
            index += 1

            if index == length:  # If all the words from lyrics_list are found, breaks out of the loop early.
                break
    
    total_emotions = total_mean_valence + total_mean_arousal + total_mean_dominance

    print(f'valence average: {total_mean_valence / length}')         # Low is Sad        # High is happy     
    print(f'arousal average: {total_mean_arousal / length}')         # Low is bored      # High is excited
    print(f'dominance average: {total_mean_dominance / length}')     # Low is Fear       # High is Angry
    print(f'emotions average: {total_emotions / length}\n')

    print(unique_words)

# sad = 5 - (total_mean_valence / length)
# happy = (total_mean_valence / length) - 5
# bored = 5 - (total_mean_arousal / length)
# excited = (total_mean_arousal / length) - 5
# fear = 5 - (total_mean_dominance / length)
# angry = (total_mean_dominance / length) - 5

# print(f'sad: {sad}')
# print(f'happy: {happy}')
# print(f'bored: {bored}')
# print(f'excited: {excited}')
# print(f'fear: {fear}')
# print(f'angry: {angry}')
