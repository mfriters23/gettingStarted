#Questions:
#"In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?":
#"Are encoding and encryption the same? - Yes/No":
#"Is it possible to decrypt a message without a key? - Yes/No":
#"Is it possible to decode a message without a key? - Yes/No":
#"Is a hashed message supposed to be un-hashed? - Yes/No":
#"What is the SHA256 hashing value of your NYU email and use the answer in your code - ":
#"Is MD5 a secured hashing algorithm? - Yes/No":
#"What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number":
#"What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an integer number":

def welcome_assignment_answers(question):
    if question == "In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?":
        answer = "pcap"
    elif question == "Are encoding and encryption the same? - Yes/No":
        answer = "No"
    elif question == "Is it possible to decrypt a message without a key? - Yes/No":
        answer = "No"
    elif question == "Is it possible to decode a message without a key? - Yes/No":
        answer = "Yes"
    elif question == "Is a hashed message supposed to be un-hashed? - Yes/No- ":
        answer = "No"
    elif question == "Is MD5 a secured hashing algorithm? - Yes/No":
        answer = "No"
    elif question == "What is the SHA256 hashing value of your NYU email and use the answer in your code - ":
        answer = "466f5a951421f8e5b0ee60a55aad1b2a"
    elif question == "What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number":
        answer = "3"
    elif question == "What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an integer number":
        answer = "2"
    else:
        answer = "This is not my beautiful wife! This is not my beautiful car! How did I get here?"
    return(answer)

if __name__ == "__main__":
    #use this space to debug and verify that the program works
    debug_question = ("In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?")
    print(welcome_assignment_answers(debug_question))