from adventure.utils import read_events_from_file
from rich.console import Console
import random

console = Console()

def step(choice: str, events):
    random_event = random.choice(events)

    # only lowercase 'left' and 'right' are valid
    if choice == "left":
        text = f"You walk left. {random_event}"
    elif choice == "right":
        text = f"You walk right. {random_event}"
    else:
        text = "You stand still, unsure what to do. The forest swallows you."

    # colorful output for gameplay (not used in tests)
    if "left" in text:
        console.print(f"[green]{text}[/green]")
    elif "right" in text:
        console.print(f"[cyan]{text}[/cyan]")
    else:
        console.print(f"[red]{text}[/red]")

    return text

if __name__ == "__main__":
    events = read_events_from_file('events.txt')

    console.print("[bold yellow]You wake up in a dark forest.[/bold yellow] [magenta]You can go left or right.[/magenta]")
    while True:
        choice = console.input("[bold blue]Which direction do you choose? (left/right/exit): [/bold blue]")
        choice = choice.strip()
        if choice == 'exit':
            console.print("[bold magenta]Goodbye adventurer![/bold magenta]")
            break

        step(choice, events)
