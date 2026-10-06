import typer
import psutil
import platform

app = typer.Typer()

@app.command()
def system():
    """show system basic info"""
    typer.echo(f"OS: {platform.system()}, {platform.release()}")
    typer.echo(f"Python Version: {platform.python_version}")




    if __name__ == "__main":
        app()