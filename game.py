import pygame

STORY = {
    "start": {
        "text": "You wake up at a fork in the road.",
        "choices": [
            {"label": "Take the forest path", "next": "forest"},
            {"label": "Take the mountain path", "next": "mountain"},
        ],
    },
    "forest": {
        "text": "The forest is quiet. You see a glowing cave.",
        "choices": [
            {"label": "Enter the cave", "next": "treasure"},
            {"label": "Return to the fork", "next": "start"},
        ],
    },
    "mountain": {
        "text": "The mountain trail is steep. A storm approaches.",
        "choices": [
            {"label": "Find shelter", "next": "shelter"},
            {"label": "Keep climbing", "next": "summit"},
        ],
    },
    "treasure": {
        "text": "You find an ancient treasure chest. You win!",
        "choices": [],
    },
    "shelter": {
        "text": "You wait out the storm and make it home safely. You win!",
        "choices": [],
    },
    "summit": {
        "text": "Lightning strikes nearby. You retreat, but survive. The end.",
        "choices": [],
    },
}


def get_next_node(story, current_node, choice_index):
    choices = story[current_node]["choices"]
    if choice_index < 0 or choice_index >= len(choices):
        raise ValueError("Invalid choice index")
    return choices[choice_index]["next"]


def _key_to_choice_index(key):
    if key in (pygame.K_1, pygame.K_KP1):
        return 0
    if key in (pygame.K_2, pygame.K_KP2):
        return 1
    return None


def wait_for_choice(choice_count):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return None
                choice_index = _key_to_choice_index(event.key)
                if choice_index is not None and choice_index < choice_count:
                    return choice_index
        pygame.time.wait(50)


def run_game():
    pygame.init()
    pygame.display.set_caption("Choose Your Path")
    pygame.display.set_mode((400, 120))

    print("=== Choose Your Path ===")
    print("Use the game window, then press 1 or 2 to choose. Press ESC to quit.\n")

    current = "start"
    running = True

    while running:
        node = STORY[current]
        print(node["text"])

        if not node["choices"]:
            print("\nGame over. Thanks for playing!")
            break

        for index, choice in enumerate(node["choices"], start=1):
            print(f"  {index}. {choice['label']}")

        print("Choose: ", end="", flush=True)
        selected = wait_for_choice(len(node["choices"]))

        if selected is None:
            print("\nGame exited.")
            running = False
            continue

        print(selected + 1)
        current = get_next_node(STORY, current, selected)
        print()

    pygame.quit()


if __name__ == "__main__":
    run_game()
