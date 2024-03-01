# Hate Speech Detection using ML and Python

This project is to detec Hate Speeches in tweets and classify into Hate Speech, Offensive Language or No Hate/Offensive tweets


## Explanations of Regular Expression Used in the Project

text = re.sub('\[.*?\]','',text)

The provided regular expression '\[.*?\]' is designed to match and remove text within square brackets. Here's a breakdown of the pattern:

\[ : Matches the opening square bracket.
.*? : Matches any character (except for a newline) zero or more times, but as few times as possible (non-greedy).
\] : Matches the closing square bracket.
So, this expression will find and replace anything within square brackets (including the brackets themselves) with an empty string.
This will remove the text within square brackets from the original text.

--text = re.sub('https?://\S+|www\.\S+','',text)

The regular expression https?://\S+|www\.\S+ is designed to match both HTTP and HTTPS URLs, as well as URLs starting with "www." Here's a breakdown of the pattern:

https?:// : Matches "http://" or "https://", where the "?" makes the "s" optional.
\S+ : Matches one or more non-whitespace characters.
| : Acts as an OR operator.
www\.\S+ : Matches URLs starting with "www." followed by one or more non-whitespace characters.
This expression will replace both HTTP(S) URLs and "www." URLs with an empty string.
This will remove both types of URLs from the original text.


--text = re.sub('<.*?>+','',text)

The goal of this code is to remove HTML tags from a text string.
<.*?>+: This is the regular expression pattern. Let's break it down:

<: Matches the opening angle bracket of an HTML tag.
.*?: Matches any character (except for a newline) in a non-greedy way. The *? means "zero or more occurrences, as few as possible."
>: Matches the closing angle bracket of an HTML tag.
+: Matches one or more occurrences of the preceding pattern.
So, the pattern <.*?>+ is designed to match and remove HTML tags in a non-greedy manner.

The purpose of this code is to remove all HTML tags from the text variable. After this line of code is executed, text will contain the original text without any HTML tags.

--text = re.sub('[%s]' % re.escape(string.punctuation),'',text)

%s: This is a placeholder in a string that is later filled by values provided to the string through the % operator. In this case, it's being used to insert the characters from string.punctuation into the pattern.

string.punctuation: This is a pre-defined string in the string module in Python, containing all ASCII punctuation characters.  !"#$%&'()*+, -./:;<=>?@[\]^_`{|}~

re.escape(string.punctuation): This escapes any special characters in the punctuation string so that they are treated literally in the regular expression pattern.

[%s]: This construct, after formatting, becomes a character class in a regular expression. It matches any single character that is in the set of characters represented by string.punctuation.

So, the overall purpose of this code is to use a regular expression to remove any characters in the text variable that belong to the set of ASCII punctuation characters. The %s is a way of making the pattern dynamic by inserting the actual punctuation characters into the character class.

--text = re.sub('\n','',text)

This line of code is using the re.sub function to replace newline characters (\n) with an empty string in the text variable.

\n: This is an escape sequence representing a newline character.

So, the pattern \n is used to match newline characters in the text variable, and the replacement is an empty string (''). This effectively removes all newline characters from the text.

--text = re.sub('\w*\d\w*','',text)

\w*: This matches zero or more word characters (alphanumeric characters plus underscore _).

\d: This matches a digit (0-9).

\w*: This again matches zero or more word characters.

So, the pattern \w*\d\w* is designed to match any substring that contains at least one digit. The entire matching substring is then replaced with an empty string (''), effectively removing any alphanumeric sequence that contains at least one digit.

After this line of code is executed, the text variable will contain the original text with any alphanumeric sequences containing digits removed.
After this line of code is executed, the text variable will contain the original text with all newline characters removed.

# UI screen

Some of the tweets have not been classified into Hate Speech or other classes. I used here DecisionTree and RandomForest still not getting proper classifications

[image]https://github.com/deeptivenugopal/ML_DL__AI_Projects/blob/main/End_To_End_Hate_Speech_Detection_StreamLit/Streamlit_UI_Pred.PNG?raw=true

