import typer
import psutil
import platform
from src.linux_assistant.console import console
from src.linux_assistant import cpu

app = typer.Typer()
app.add_typer(cpu.app, name="cpu")


@app.command()
def system():
    """show system basic info"""
    console.print(f"Python Version: {platform.python_version()}")
    console.print(f"CPU percentage: {cpu.cpu_percentage()}")
    console.print(f"OS: {platform.system()}, {platform.release()}")



if __name__ == "__main__":
    app()