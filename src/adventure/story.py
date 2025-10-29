from adventure.utils import read_events_from_file
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
import random

console = Console()

def step(choice: str, events):
    random_event = random.choice(events)

    if choice == "left":
        return left_path(random_event)
    elif choice == "right":
        return right_path(random_event)
    else:
        return "You stand still, unsure what to do. The forest swallows you."

def left_path(event):
    return "You walk left. " + event

def right_path(event):
    return "You walk right. " + event

if __name__ == "__main__":
    events = read_events_from_file("events.txt")

    console.print(
        Panel.fit(
            "[bold cyan]You wake up in a dark forest.[/bold cyan]\nYou can go [bold]left[/bold] or [bold]right[/bold].",
            title=" Adventure Begins ",
            border_style="green",
        )
    )

    while True:
        choice = Prompt.ask(
            "[bold yellow]Which direction do you choose?[/bold yellow]",
            choices=["left", "right", "exit"],
            default="exit",
        )

        if choice == "exit":
            console.print(
                Panel.fit(
                    f"[bold magenta]You leave the forest safely, adventurer! Goodbye![/bold magenta]",
                    title=" Farewell ",
                    border_style="red",
                )
            )
            break



        result = step(choice, events)
        console.print(Panel(result, border_style="blue"))