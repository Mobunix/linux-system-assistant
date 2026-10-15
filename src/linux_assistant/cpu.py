import typer
import psutil
from rich import table
from src.linux_assistant.console import console

app = typer.Typer()

@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    """summary of information"""
    if ctx.invoked_subcommand is None:
        console.print(f"cpu percentage: {psutil.cpu_percent(interval=0.1)} \n cpu count: {psutil.cpu_count()}")
        
@app.command()
def cpu_percentage():
    """cpu percentage"""
    console.print(f"{psutil.cpu_percent(interval=0.1)}%")

@app.command()
def cpu_count():
    """the number of logical CPUs in the system"""
    console.print(f"{psutil.cpu_count()}")




if __name__ == "__main__":
    app()

