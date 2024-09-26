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
        print(f"{'Number of unique words:':<30} {total_unique_words:>02}\n")

    elif(int(user_input)==2):
        print(user_input)
    elif(int(user_input)==3):
        print(user_input)
    elif(int(user_input)==4):
        print(user_input)
    elif(int(user_input)==5):
        print(user_input)
    elif(int(user_input)==6):
        print(user_input)
    elif(int(user_input)==7):
        print(user_input)
    elif(int(user_input)==8):
        print(user_input)
    elif(int(user_input)==9):
        print(user_input)
    else:
        print("\033[31m>> Bruno:\033[0m No such task exist.")

