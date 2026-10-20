# Library Rule-Based Chatbot
# Created using Python if-elif-else conditions

print("=" * 45)
print("       WELCOME TO THE LIBRARY CHATBOT")
print("=" * 45)
print("Hello! I can help you with library-related questions.")
print("Try asking about: timings, books, membership, issue, return, fine, or help.")
print("Type 'bye' or 'exit' to end the conversation.\n")

while True:
    user_input = input("You: ").strip().lower()

    if user_input in ["bye", "exit", "quit", "goodbye"]:
        print("Bot: Thank you for visiting the library chatbot. Have a great day!")
        break

    elif user_input in ["hello", "hi", "hey", "hii"]:
        print("Bot: Hello! Welcome to the library. How can I help you?")

    elif "help" in user_input or "what can you do" in user_input:
        print("Bot: I can answer questions about library timings, books, membership,")
        print("     borrowing and returning books, and library fines.")

    elif "timing" in user_input or "opening" in user_input or "hours" in user_input:
        print("Bot: The library is open Monday to Saturday, from 9:00 AM to 6:00 PM.")
        print("     Please check with the library staff for holiday timings.")

    elif "book" in user_input and ("available" in user_input or "find" in user_input or "search" in user_input):
        print("Bot: You can search for a book by its title, author, or subject in the library catalogue.")
        print("     If you cannot find it, please ask the librarian for help.")

    elif "membership" in user_input or "member" in user_input or "join" in user_input:
        print("Bot: To become a library member, visit the library desk with your student ID")
        print("     and complete the membership form.")

    elif "issue" in user_input or "borrow" in user_input or "take a book" in user_input:
        print("Bot: To issue a book, show your library ID to the librarian.")
        print("     Eligible members can usually borrow books according to library rules.")

    elif "return" in user_input or "submit a book" in user_input:
        print("Bot: Please return borrowed books at the library counter on or before the due date.")

    elif "fine" in user_input or "late" in user_input or "overdue" in user_input:
        print("Bot: A late-return fine may apply if a book is returned after its due date.")
        print("     Please ask the librarian to confirm the current fine amount.")

    elif "location" in user_input or "where is" in user_input or "address" in user_input:
        print("Bot: The library is on the college campus. Please check the campus directory")
        print("     or ask the reception desk for its exact location.")

    elif "thank" in user_input:
        print("Bot: You're welcome! Happy reading!")

    else:
        print("Bot: Sorry, I don't understand that question.")
        print("     Please ask about timings, books, membership, issuing, returning, or fines.")
