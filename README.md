# Project 3 Text Analysis

### Name

Muneeb Azfar Nafees

### Introspection

**Challenges Faced:**
1. _Project Simplicity_: The overall project was relatively straightforward. However, there were a few elements I wasn’t familiar with, such as using the `str.translate` function, for which I referred to resources for assistance.
2. _Formatting Issues_: The most challenging part of the project was formatting the text, particularly for the first and fifth menu options. This process was time-consuming and required multiple adjustments to get it right.

**Lessons:**
1. _Resource Utilization_: When faced with unfamiliar functions or approaches, I effectively used external resources to learn and apply them.
2. _Patience with Formatting_: I learned the importance of being patient and thorough with formatting, as even small errors can lead to significant time delays.


### Resources

1. https://builtin.com/data-science/python-f-string
2. https://www.toppr.com/guides/python-guide/references/methods-and-functions/methods/dictionary/get/python-dictionary-get/#:~:text=You%20can%20access%20the%20values,it%20returns%20a%20default%20value.
3. https://stackoverflow.com/questions/9285086/access-dict-key-and-return-none-if-doesnt-exist
4. https://sparkbyexamples.com/python/python-remove-multiple-characters-from-string/#:~:text=5.-,Using%20filter()%20and%20join()%20Methods,characters%20into%20a%20new%20string.

### *DO NOT EDIT BELOW THIS LINE*
---

## Goal

The goals of this project are:
* Use loops, dictionaries, sets, and lists more extensively
* Begin with rudimentary NLP tasks - sentiment analysis, similarity, and search

## Description

In this project, you will process text. You will be re-using some of the structure of your code from the previous project to create a menu but instead of doing math and string operations, all options will process text, analyze emotions, find similarities, and search.


Following are the main tasks for the project and you implement them in sequence:


### `chatbot.py` file

I have provided the `chatbot.py` for you. All your code must go here. **Make sure NOT to delete the code that already exists** 


### Endless interaction

Last time, the interactions with the chatbot ran only once i.e., after the chatbot performed one operation, the program ended. This time ensure that unless the user chooses the option to exit, the interactions should start from the meny option. After completing the first operation, the chatbot should prompt the user with the menu again asking what else they want to do today.

### Personalization, Persona, and Menu

In the previous project, I let you choose the chatbot's persona. This time, I want the chatbot to have a helpful and neutral tone. However, I want _you_ to choose the name of the chatbot. In the following examples, I am calling my chatbot to be "Alex", you should **choose a different name**.

In this project, the menu options will be fixed for everyone to ensure uniformity. Consider the following example as a guide for tone, the menu options to include, and their formatting :

```bash
>> Alex: What can I help you today with?
--------- TEXT OPERATIONS ---------
1: Analyze text
2: Analyze sentiment in text
3: Find similarities between texts
4: Search for a word in text
--------- FILE OPERATIONS ---------
5: Analyze a file
6: Analyze the sentiment of a file
7: Find similarities between two files
8: Search for a word in a file
9: Exit
```

### Menu Option #1: Analyze Text

In the first menu option, the user will provide a text via the `input` prompt. After this prompt, you need provide the user with: 

* Count of total characters in the text.
* Count of *unique* characters in the text.
* Count of words in the text.
* Count of unique words in the text.

Note when counting unique characters and words, they should be case-insensitive i.e., consider `a` and `A` as the same character and `hello` and `HelLo` as the same word.

```bash
>> Alex: What can I help you today with?
--------- TEXT OPERATIONS ---------
1: Analyze text
2: Analyze sentiment in text
3: Find similarities between texts
4: Search for a word in text
--------- FILE OPERATIONS ---------
5: Analyze a file
6: Analyze the sentiment of a file
7: Find similarities between two files
8: Search for a word in a file
9: Exit
>> User: 1
>> Alex: Sure, I can help you analyze your text. What is your text?
>> User: How are you doing today? Are you good?
>> Alex: Here is the analysis

Total number of characters:     38
Number of unique characters:    15
Total number of words:          08
Number of unique words:         06
```

### Menu Option #2: Analyze Sentiment

Sentiment analysis is a fundamental task in NLP. Understanding the emotion of a text has a variety of applications, such as - understanding people's opinions about a movie/restaurant, their mood in a chat, or predicting their actions. In this option, we will implement a very rudimentary sentiment analyzer. Later in the course, we will look at a more sophisticated version of sentiment analysis.

A simple way of analyzing a sentiment is to identify the proportion of positive and negative words. For example - "good" has a positive sentiment whereas "bad" has a negative sentiment. If I describe a movie as - "The movie was really good", then you can infer from the "good" that sentence has a positive sentiment. Similarly, if I describe a movie as "The movie was pretty bad", then you would understand that the sentence has a negative sentiment. We can also have neutral sentiment. For example: "The first half of the movie was good but the ending was bad". Since we have both the "good" and the "bad", we can say that the sentiment is neutral.

Using this idea of the proportion of positive and negative sentiment words, we will identify the sentiment of text. You will be provided a dictionary called `sentiment` that contains some common words with their sentiments. These sentiment values are as follows: 

* -2 for negative sentiment
* -1 for somewhat negative sentiment
* 0 for neutral sentiment
* 1 for somewhat positive sentiment
* 2 for positive sentiment.

Here are some of the words and their sentiment value from the `sentiment` dictionary:

```python
sentiment: dict[str, int] = {
  "horrific": -2,
  "unpleasant": -1,
  "wonderful": 2,
  "typical": 1,
  "ok": 0
}
```

To analyze the sentiment of a text, identify the **average sentiment** of the sentence. If the value of the average is

*  0, then it has a "neutral" sentiment,
*  between 0 and 0.25 (excluding), then it has a "somewhat positive" sentiment,
*  between 0.25 and 0.50 (excluding), then it has a "positive" sentiment,
*  greater than or equal to 0.5, "very positive" sentiment,
*  between 0 and -0.25 (excluding), then it has a "somewhat negative" sentiment,
*  between -0.25 and -0.50 (excluding), then it has a "negative" sentiment,
*  less than -0.5 or equal to, then it has a "very negative" sentiment

**If the word does not exist in the `sentiment` dictionary, assume its sentiment as 0.**

Here are some examples of sentences and their sentiment:

```
sentence: It was an unpleasant movie
sentiment: Somewhat negative

sentence: It was an ok movie
sentiment: neutral

sentence: It was an unpleasant and horrific movie
sentiment: negative

sentence: Wonderful movie
sentiment: Very positive
```

Here is an example of what the interaction with the chatbot could look like:

```bash
>> Alex: What can I help you today with?
--------- TEXT OPERATIONS ---------
1: Analyze text
2: Analyze sentiment in text
3: Find similarities between texts
4: Search for a word in text
--------- FILE OPERATIONS ---------
5: Analyze a file
6: Analyze the sentiment of a file
7: Find similarities between two files
8: Search for a word in a file
9: Exit
>> User: 2
>> Alex: Sure, I can help you analyze the sentiment in your text. What is your text?
>> User: It was an unpleasant and horrific movie
>> Alex: Somewhat negative
```

### Menu Option #3: Find similarities between texts

Identifying similarity between documents is another rudimentary task in Natural Language Processing (NLP). It's widely used in applications like plagiarism detection, recommendation systems, and document clustering. In this menu option, you will implement a simple method to compute the similarity between two texts provided by the user.

We will use the Jaccard Similarity coefficient to measure the similarity between the two texts. The Jaccard Similarity is defined as the size of the intersection divided by the size of the union of two sets. In this case, the sets are the unique words from each text.

The Jaccard similarity between two sets $(A)$ and $(B)$ is defined as:

$$[
J(A, B) = \frac{|A \cap B|}{|A \cup B|}
]
$$

where: 
- $(|A \cap B|)$ is the number of elements in the intersection of sets $(A)$ and $(B)$.
- $(|A \cup B|)$ is the number of elements in the union of sets $(A)$ and $(B)$.

To implement text similarity when the user selects this menu option, ask them to input the first text and then the second text. Then, convert both texts to lowercase to ensure case-insensitive comparison, remove all punctuation from the texts. You can use the `str.translate()` method along with `str.maketrans()` to remove punctuation.  Next, convert the string into a set of unique words. Lastly, to calculate the Jaccard index:

* find the set of words common to both texts (i.e., their intersection).
* find the set of all unique words from both texts (i.e., their union).
* divide the size of the intersection by the size of the union.

Print the result using `f-string`. Remember to use the `{:.Nf}` syntax to round numbers up to `N` places. Review the Jupyter notebooks from previous weeks.

Here is an example interaction

```bash
>> Alex: What can I help you today with?
--------- TEXT OPERATIONS ---------
1: Analyze text
2: Analyze sentiment in text
3: Find similarities between texts
4: Search for a word in text
--------- FILE OPERATIONS ---------
5: Analyze a file
6: Analyze the sentiment of a file
7: Find similarities between two files
8: Search for a word in a file
9: Exit
>> User: 3
>> Alex: Sure, I can help you find similarities between two texts. Please enter the first text.
>> User: Apple banana cherry
>> Alex: Please enter the second text.
>> User: Coconut cherry mango tomato
>> Alex: The two texts are 16.66% similar. The common words are:
['cherry']
```


### Menu Option #4: Search for a word in texts

Searching for specific words within a text is a common task in text processing. In this menu option, you will implement a feature that allows the user to search for a particular word within a text they provide. If the word exists in the text, your program should inform the user and specify the positions where the word occurs.

A couple of things to note:

* The search should be case-insensitive, meaning that searching for "Apple" should find instances of "apple", "Apple", "APPLE", etc.
* If the word is found, the program should provide the positions (indices) of the word within the text.
* Ensure that you are searching for whole words, not substrings within other words. For example, searching for "cat" should not match "concatenate".
* Note that you need to specify the position and not the index
* If the word is not found, simple state "The word was not found"

(Psst: The `index` method will fail, do you know why?)

Following is an example interaction:

```bash
>> Alex: What can I help you today with?
--------- TEXT OPERATIONS ---------
1: Analyze text
2: Analyze sentiment in text
3: Find similarities between texts
4: Search for a word in text
--------- FILE OPERATIONS ---------
5: Analyze a file
6: Analyze the sentiment of a file
7: Find similarities between two files
8: Search for a word in a file
9: Exit
>> User: 4
>> Alex: Sure, I can help you search for a word in your text. Please enter the text:
>> User: The quick brown fox jumps over the lazy dog.
>> Alex: Please enter the word you want to search for:
>> User: the
>> Alex: The word 'the' was found at the following positions: [1, 7]
```

### Menu Options #5-#8: File Operations

All the operations you do for text, you should also do for a file. In this project, you are be provided with a function `get_file_contents` that returns you the content of a file. You only need to ask the user for the filename(s) and use this function to get its content as a `string`. Assume that the file exists and is within this repo.

Here is an example interaction with the chatbot for option #8

`sample3.txt`
```txt
Data science is an interdisciplinary field that uses scientific methods, processes, algorithms and systems to extract knowledge and insights from data. Data is the new oil.
```

```bash
>> Alex: What can I help you today with?
--------- TEXT OPERATIONS ---------
1: Analyze text
2: Analyze sentiment in text
3: Find similarities between texts
4: Search for a word in text
--------- FILE OPERATIONS ---------
5: Analyze a file
6: Analyze the sentiment of a file
7: Find similarities between two files
8: Search for a word in a file
9: Exit
>> User: 8
>> Alex: Sure, I can help you search for a word in a file. Please enter the filename:
>> User: sample3.txt
>> Alex: Please enter the word you want to search for:
>> User: data
>> Alex: The word 'data' was found at the following positions: [1, 15]
```

### Output

Note that output of the chatbot is strongly formatted. Whenever user provides an input, it is on a new line and next to the `>> User:` string. Similarly, when the chatbot is saying something it is prepended with the string `>> Alex:`. 


## Rubric

* Analyze text - 10 points
* Analyze sentiment in text - 15 points
* Find similarities between texts - 15 points
* Search for a word in texts - 15
* Analyze file - 5 points
* Analyze sentiment in a file - 10 points
* Find similarities between files - 10 points
* Search for a word in file - 10 points
* Endless interaction - 5 points
* Formatted output - 5 points

## Tips On How To Excel


* Start early!
* Ask for help when stuck. Remember the 30 minute rule? No? Look into the syllabus.
* Break down the task into smaller tasks and try to implement them in Jupyter Notebook. Once implemented in the notebook successfully, transfer it into `.py` file.
* Run the `.py` file to make sure the new addition did not break any changes.
* After implementing each small task, commit changes.
* Review the notebooks from classes available on GitHub if you cannot remember syntax for anything.
* Run your code multiple times and vary the inputs to ensure it works as intended. 

## Feedback
- [10] Analyze text
- [15] Analyze sentiment in text
- [15] Find similarities between texts
- [15] Search for a word in texts
- [5] Analyze file
- [10] Analyze sentiment in a file
- [10] Find similarities between files
- [9] Search for a word in file
- [5] Endless interaction
- [5] Formatted output
- Project 3: 99 points
- Feedback: Amazing job with the project! The point off is in option #8, you do not account for word at beginning of new line such as 'it' (13rd word) in sample4.txt. Besides, keep up the good work!
