import random

# Basic story templates for logic-based generation
story_templates = [
    "The {adj} {noun} {verb} through the enchanted forest.",
    "Once upon a time, a {adj} {noun} {verb} under the starry sky.",
    "In a mystical land, the {adj} {noun} {verb} with great joy!",
    "The entire town was amazed as the {adj} {noun} {verb} like never before!"
]

def generate_logic_story(noun, adj, verb):
    """Generate a story using a random template."""
    template = random.choice(story_templates)
    return template.format(noun=noun, adj=adj, verb=verb)

def display_welcome_message():
    """Display the welcome message."""
    print("🎭 Welcome to the Fun Mad Libs Story Generator! 📖")
    print("Create a unique and fun-filled story using your own words!\n")

def get_user_input():
    """Get user input for noun, adjective, and verb."""
    noun = input("Enter a noun (e.g., dragon 🐉): ").strip()
    adjective = input("Enter an adjective (e.g., gigantic 🌟): ").strip()
    verb = input("Enter a verb (e.g., dances 💃): ").strip()
    return noun, adjective, verb

def main():
    display_welcome_message()
    
    while True:
        noun, adjective, verb = get_user_input()
        
        if not all([noun, adjective, verb]):
            print("🚨 Oops! Please fill in all fields to generate your story.")
            continue
        
        print("\nGenerating your logic-based story... 🎭")
        story = generate_logic_story(noun, adjective, verb)
        
        print("\n🎉 Your magical story is ready!\n")
        print(story)
        
        play_again = input("\nDo you want to create another story? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("\nThanks for playing! Goodbye! 👋")
            break

if __name__ == "__main__":
    main()