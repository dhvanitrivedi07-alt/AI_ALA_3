"""
Library Management Chatbot (Rule-Based)
GMIU College Assignment - Python if-elif-else chatbot

NOTE: All timings, fines and borrowing limits below are ILLUSTRATIVE (sample data).
Change them to match your actual college library.
"""

# ---------------- Sample library data (edit to match your library) ----------------
LIBRARY_NAME = "GMIU Central Library"
OPEN_HOURS = "Monday to Saturday: 9:00 AM to 6:00 PM. Closed on Sundays and public holidays."
MAX_BOOKS = 3
BORROW_DAYS = 14
FINE_PER_DAY = 5  # rupees per book per day
LOCATION = "Ground floor, Main Academic Block, GMIU Campus."
CONTACT = "Email: library@example.edu | Phone: +91-00000-00000 (sample contact details)."

# A tiny sample catalogue: title -> (author, available copies)
BOOKS = {
    "python programming": ("John Zelle", 4),
    "let us c": ("Yashavant Kanetkar", 2),
    "data structures": ("Seymour Lipschutz", 0),
    "operating system concepts": ("Abraham Silberschatz", 3),
    "artificial intelligence": ("Stuart Russell", 1),
    "database system concepts": ("Henry Korth", 2),
}

HELP_TEXT = """You can ask me about:
  1. Library timings          (e.g. "What are the library hours?")
  2. Book availability        (e.g. "Is Python Programming available?")
  3. Issuing a book           (e.g. "How can I issue a book?")
  4. Returning a book         (e.g. "How do I return a book?")
  5. Renewing a book          (e.g. "Can I renew my book?")
  6. Membership / registration
  7. Maximum books allowed
  8. Borrowing duration
  9. Late return fines
 10. Library rules
 11. Search by title or author (e.g. "search Kanetkar")
 12. Library location
 13. Contact information
Type 'list' to see sample books, or 'exit' / 'quit' / 'bye' to end."""


def has_any(text, words):
    """Return True if any keyword from 'words' appears in 'text'."""
    for w in words:
        if w in text:
            return True
    return False


def search_books(text):
    """Look for a book title or author name inside the user's message."""
    results = []
    for title, (author, copies) in BOOKS.items():
        author_parts = author.lower().split()
        if title in text or has_any(text, author_parts):
            status = f"{copies} copies available" if copies > 0 else "currently NOT available"
            results.append(f"- {title.title()} by {author}: {status}")
    return results


def get_response(user_input):
    """Return the chatbot's reply for a given user message using if-elif-else rules."""
    text = user_input.lower().strip()

    if text == "":
        return "Please type a question. Type 'help' to see what I can do."

    # Exit
    elif text in ("exit", "quit", "bye", "goodbye"):
        return "Thank you for using the Library Chatbot. Happy reading! Goodbye."

    # Help
    elif text in ("help", "menu", "options") or "what can you do" in text:
        return HELP_TEXT

    # Greetings
    elif has_any(text, ["hello", "hi ", "hey", "good morning", "good afternoon", "good evening", "namaste"]) or text == "hi":
        return "Hello! Welcome to the Library Management Chatbot. How can I help you?"

    # Thanks
    elif has_any(text, ["thank", "thanks"]):
        return "You're welcome! Ask me anything else about the library."

    # List of books
    elif text in ("list", "list books", "show books", "catalogue", "catalog"):
        lines = [f"- {t.title()} by {a} ({c} available)" for t, (a, c) in BOOKS.items()]
        return "Sample books in the catalogue:\n" + "\n".join(lines)

    # Timings
    elif has_any(text, ["time", "timing", "hour", "open", "close", "closing", "opening"]):
        return f"{LIBRARY_NAME} timings (sample): {OPEN_HOURS}"

    # Fines (check before 'return' so "fine for late return" matches here)
    elif has_any(text, ["fine", "late", "penalty", "overdue", "delay"]):
        return (f"A late fine of Rs. {FINE_PER_DAY} per book per day is charged after the due date "
                "(sample value). Lost or damaged books must be replaced or paid for.")

    # Renewal
    elif has_any(text, ["renew", "extend", "extension"]):
        return (f"You can renew a book once for another {BORROW_DAYS} days if no one has reserved it. "
                "Bring the book and your library ID to the counter before the due date.")

    # Return
    elif has_any(text, ["return", "give back", "submit book"]):
        return ("To return a book, bring it to the library counter with your library ID. "
                "The librarian will scan it and update your record. Return on or before the due date to avoid fines.")

    # Issue
    elif has_any(text, ["issue", "borrow a book", "borrow book", "take a book", "get a book", "lend"]):
        return "Visit the library, select an available book, and present your valid library ID to the librarian."

    # Maximum books
    elif has_any(text, ["how many books", "maximum", "max", "limit"]):
        return f"A student can borrow a maximum of {MAX_BOOKS} books at a time (sample limit)."

    # Duration
    elif has_any(text, ["how long", "duration", "days", "period", "due date"]):
        return f"Books can be kept for {BORROW_DAYS} days from the date of issue (sample duration)."

    # Membership
    elif has_any(text, ["member", "registration", "register", "join", "library card", "library id", "sign up"]):
        return ("To become a member, fill the library registration form at the counter with your "
                "college ID card and one passport-size photo. Your library card will be issued after verification.")

    # Rules
    elif has_any(text, ["rule", "regulation", "policy", "allowed", "silence"]):
        return ("Library rules (sample):\n- Maintain silence.\n- Carry your library ID card.\n"
                "- No food or drinks inside.\n- Keep mobile phones on silent.\n"
                "- Handle books carefully; do not write in them.\n- Return books on time.")

    # Location
    elif has_any(text, ["where", "location", "located", "address", "find the library"]):
        return f"The library is located at: {LOCATION}"

    # Contact
    elif has_any(text, ["contact", "phone", "email", "librarian", "call"]):
        return CONTACT

    # Search / availability (title or author)
    elif has_any(text, ["available", "availability", "search", "find", "book", "author", "have"]) or search_books(text):
        results = search_books(text)
        if results:
            return "Here is what I found:\n" + "\n".join(results)
        else:
            return ("Sorry, I couldn't find that book in the sample catalogue. "
                    "Try a title or author name, or type 'list' to see available books.")

    # Unknown
    else:
        return "Sorry, I didn't understand that. Type 'help' to see the questions I can answer."


def main():
    """Run the chatbot in the terminal."""
    print("=" * 55)
    print("        Welcome to the Library Management Chatbot")
    print("=" * 55)
    print("Type 'help' to see options, or 'exit' to quit.\n")

    while True:
        try:
            user_input = input("You: ")
        except (EOFError, KeyboardInterrupt):
            print("\nBot: Goodbye!")
            break

        reply = get_response(user_input)
        print("Bot:", reply, "\n")

        if user_input.lower().strip() in ("exit", "quit", "bye", "goodbye"):
            break


if __name__ == "__main__":
    main()
