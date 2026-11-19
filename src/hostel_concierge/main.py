"""

Hostel-Concierge
Main application entry point.

"""

def display_welcome() -> None:
    """ Display the application welcome message. """

    print("\n" + "=" * 45)
    print("       WELCOME TO HOSTEL-CONCIERGE")
    print("          Sunrise Hostel")
    print("=" * 45)
    print("\nHow can I help you today?")
    print("\nType 'exit' or 'quit' to leave.\n")

def start_conversation() -> None:
    """Start a basic interactive CLI conversation."""

    display_welcome()

    while True:
        try:
            user_input = input("You: ").strip()

            if user_input.lower() in ("exit", "quit"):
                print("\nHostel-Concierge: Goodbye! Have a great day.")
                break

            if not user_input:
                continue

            print(
                "\nHostel-Concierge: "
                "Thanks for your message! "
                "I'm still learning how to help you.\n"
            )
        except (KeyboardInterrupt, EOFError):
            print("\n\nHostel-Concierge: Goodbye!")
            break

def main() -> None:
    """Application entry point. """

    start_conversation()

if __name__ == "__main__":
    main()