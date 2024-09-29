from helper import get_file_contents, sentiment

# Your code goes 
user_input: str = 0

while(int(user_input)!=9):
    user_input: str = input("\033[31m>> Bruno:\033[0m What can I help you with today?\n--------- TEXT OPERATIONS ---------\n1: Analyze text\n2: Analyze sentiment in text\n3: Find similarities between texts\n4: Search for a word in text\n--------- FILE OPERATIONS ---------\n5: Analyze a file\n6: Analyze the sentiment of a file\n7: Find similarities between two files\n8: Search for a word in a file\n9: Exit\n\033[32m>> User: \033[0m")
    while(not user_input.isnumeric()):
        user_input: str = input("\033[31m>> Bruno:\033[0m Please enter a valid number\n\033[32m>> User: \033[0m")
    
    if(int(user_input)==1):
        user_text: str = input("\033[31m>> Bruno:\033[0m Sure, I can help you analyze your text. What is your text?\n\033[32m>> User: \033[0m")
        total_char: int  = len(user_text)
        unique_char_set: set[str] = set()
        word_list: list[str] = user_text.lower().split(" ")
        unique_word_set: set[str] = set(word_list)
        
        for each_char in user_text:
            unique_char_set.add(each_char.lower())
        
        unique_char: int = len(unique_char_set)
        total_words: int = len(word_list)
        total_unique_words: int = len(unique_word_set)
        print("\033[31m>> Bruno:\033[0m Here is the analysis\n")
        print(f"{'Total number of characters:':<30} {total_char:>02}")
        print(f"{'Number of unique characters:':<30} {unique_char:>02}")
        print(f"{'Total number of words:':<30} {total_words:>02}")
        print(f"{'Number of unique words:':<30} {total_unique_words:>02}")

    elif(int(user_input)==2):
        user_text: str = input("\033[31m>> Bruno:\033[0m Sure, I can help you analyze the sentiment in your text. What is your text?\n\033[32m>> User: \033[0m")
        word_list: list[str] = user_text.lower().split(" ")
        text_length: int = len(word_list)
        sentiment_counter: int = 0
        
        for each_word in word_list:
            sentiment_counter: int = sentiment_counter + sentiment.get(each_word, 0)
        
        sentiment_average = sentiment_counter/text_length
        
        if(sentiment_average == 0):
            print("\033[31m>> Bruno:\033[0m neutral")
        elif(sentiment_average > 0 and sentiment_average < 0.25):
            print("\033[31m>> Bruno:\033[0m somewhat positive")
        elif(sentiment_average > 0.25 and sentiment_average < 0.5):
            print("\033[31m>> Bruno:\033[0m positive")
        elif(sentiment_average >= 0.5):
            print("\033[31m>> Bruno:\033[0m very positive")
        elif(sentiment_average < 0 and sentiment_average > -0.25):
            print("\033[31m>> Bruno:\033[0m somewhat negative")
        elif(sentiment_average < -0.25 and sentiment_average > -0.5):
            print("\033[31m>> Bruno:\033[0m negative")
        elif(sentiment_average <= -0.5):
            print("\033[31m>> Bruno:\033[0m very negative")
        
    elif(int(user_input)==3):
        user_text_1: str = input("\033[31m>> Bruno:\033[0m Sure, I can help you find similarities between two texts. Please enter the first text.\n\033[32m>> User: \033[0m")
        user_text_2: str = input("\033[31m>> Bruno:\033[0m Please enter the second text.\n\033[32m>> User: \033[0m")
        characters_to_remove = ['!', ',', '.', '?', ':', ';', '-', '_']
        translation_table = str.maketrans('', '', ''.join(characters_to_remove))
        user_text_1_removed: list[str] = user_text_1.lower().translate(translation_table).split(" ")
        user_text_1_set: set[str] = set(user_text_1_removed)
        user_text_2_removed: list[str] = user_text_2.lower().translate(translation_table).split(" ")
        user_text_2_set: set[str] = set(user_text_2_removed)

        intersection_set: set[str] = user_text_1_set.intersection(user_text_2_set)
        union_set: set[str] = user_text_1_set.union(user_text_2_set)

        percent_similar: int = len(intersection_set)*100/len(union_set)

        if(round(percent_similar) == 0):
            print(f"\033[31m>> Bruno:\033[0m The two texts are {percent_similar:.2f}% similar. There are no common words")
        else:
            print(f"\033[31m>> Bruno:\033[0m The two texts are {percent_similar:.2f}% similar. The common words are:\n{intersection_set}")

    elif(int(user_input)==4):
        user_text: str = input("\033[31m>> Bruno:\033[0m Sure, I can help you search for a word in your text. Please enter the text:\n\033[32m>> User: \033[0m")
        user_word: str = input("\033[31m>> Bruno:\033[0m Please enter the word you want to search for:\n\033[32m>> User: \033[0m")
        characters_to_remove = ['!', ',', '.', '?', ':', ';', '-', '_']
        translation_table = str.maketrans('', '', ''.join(characters_to_remove))
        user_text_removed: list[str] = user_text.lower().translate(translation_table).split(" ")
        word_position: list[int] = []

        for i in range(len(user_text_removed)):
            if(user_text_removed[i]==user_word.lower()):
                word_position.append(i+1)
            i +=1
        if(not word_position==[]):
            print(f"\033[31m>> Bruno:\033[0m The word '{user_word.lower()}' was found at the following positions: {word_position}")
        else:
            print("\033[31m>> Bruno:\033[0m The word was not found")

    elif(int(user_input)==5):
        user_file: str = input("\033[31m>> Bruno:\033[0m Sure, I can help you analyze the text in your file. What is your text? Please enter the filename:\n\033[32m>> User: \033[0m")
        user_text: str = get_file_contents(user_file)
        total_char: int  = len(user_text)
        unique_char_set: set[str] = set()
        word_list: list[str] = user_text.lower().split(" ")
        unique_word_set: set[str] = set(word_list)
        
        for each_char in user_text:
            unique_char_set.add(each_char.lower())
        
        unique_char: int = len(unique_char_set)
        total_words: int = len(word_list)
        total_unique_words: int = len(unique_word_set)
        print("\033[31m>> Bruno:\033[0m Here is the analysis\n")
        print(f"{'Total number of characters:':<30} {total_char:>02}")
        print(f"{'Number of unique characters:':<30} {unique_char:>02}")
        print(f"{'Total number of words:':<30} {total_words:>02}")
        print(f"{'Number of unique words:':<30} {total_unique_words:>02}")  
    elif(int(user_input)==6):
        user_file: str = input("\033[31m>> Bruno:\033[0m Sure, I can help you analyze the sentiment in your file. Please enter the filename:\n\033[32m>> User: \033[0m")
        user_text: str = get_file_contents(user_file)
        word_list: list[str] = user_text.lower().split(" ")
        text_length: int = len(word_list)
        sentiment_counter: int = 0
        
        for each_word in word_list:
            sentiment_counter: int = sentiment_counter + sentiment.get(each_word, 0)
        
        sentiment_average = sentiment_counter/text_length
        
        if(sentiment_average == 0):
            print("\033[31m>> Bruno:\033[0m neutral")
        elif(sentiment_average > 0 and sentiment_average < 0.25):
            print("\033[31m>> Bruno:\033[0m somewhat positive")
        elif(sentiment_average > 0.25 and sentiment_average < 0.5):
            print("\033[31m>> Bruno:\033[0m positive")
        elif(sentiment_average >= 0.5):
            print("\033[31m>> Bruno:\033[0m very positive")
        elif(sentiment_average < 0 and sentiment_average > -0.25):
            print("\033[31m>> Bruno:\033[0m somewhat negative")
        elif(sentiment_average < -0.25 and sentiment_average > -0.5):
            print("\033[31m>> Bruno:\033[0m negative")
        elif(sentiment_average <= -0.5):
            print("\033[31m>> Bruno:\033[0m very negative")
    elif(int(user_input)==7):
        user_file_1: str = input("\033[31m>> Bruno:\033[0m Sure, I can help you find similarities between two files. Please enter the filename of the first file:\n\033[32m>> User: \033[0m")
        user_text_1: str = get_file_contents(user_file_1)
        user_file_2: str = input("\033[31m>> Bruno:\033[0m Please enter the filename of the second file.\n\033[32m>> User: \033[0m")
        user_text_2: str = get_file_contents(user_file_2)
        characters_to_remove = ['!', ',', '.', '?', ':', ';', '-', '_']
        translation_table = str.maketrans('', '', ''.join(characters_to_remove))
        user_text_1_removed: list[str] = user_text_1.lower().translate(translation_table).split(" ")
        user_text_1_set: set[str] = set(user_text_1_removed)
        user_text_2_removed: list[str] = user_text_2.lower().translate(translation_table).split(" ")
        user_text_2_set: set[str] = set(user_text_2_removed)

        intersection_set: set[str] = user_text_1_set.intersection(user_text_2_set)
        union_set: set[str] = user_text_1_set.union(user_text_2_set)

        percent_similar: int = len(intersection_set)*100/len(union_set)
        
        if(round(percent_similar) == 0):
            print(f"\033[31m>> Bruno:\033[0m The two texts are {percent_similar:.2f}% similar. There are no common words")
        else:
            print(f"\033[31m>> Bruno:\033[0m The two texts are {percent_similar:.2f}% similar. The common words are:\n{intersection_set}")

    elif(int(user_input)==8):
        user_file: str = input("\033[31m>> Bruno:\033[0m Sure, I can help you search for a word in a file. Please enter the filename:\n\033[32m>> User: \033[0m")
        file_contents: str = get_file_contents(user_file)
        user_word: str = input("\033[31m>> Bruno:\033[0m Please enter the word you want to search for:\n\033[32m>> User: \033[0m")
        characters_to_remove = ['!', ',', '.', '?', ':', ';', '-', '_']
        translation_table = str.maketrans('', '', ''.join(characters_to_remove))
        file_contents_removed: list[str] = file_contents.lower().translate(translation_table).split(" ")
        word_position: list[int] = []

        for i in range(len(file_contents_removed)):
            if(file_contents_removed[i]==user_word.lower()):
                word_position.append(i+1)
            i +=1
        if(not word_position==[]):
            print(f"\033[31m>> Bruno:\033[0m The word '{user_word.lower()}' was found at the following positions: {word_position}")
        else:
            print("\033[31m>> Bruno:\033[0m The word was not found")

    elif(int(user_input)==9):
        print("\033[31m>> Bruno:\033[0m This chat is now over.")
    else:
        print("\033[31m>> Bruno:\033[0m No such task exist.")
