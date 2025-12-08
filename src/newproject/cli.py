# src/alphacomplexbenchmarking/cli.py
import logging
from pathlib import Path
import typer
from rich import print

from newproject.logging_config import setup_logging



app = typer.Typer(help="Simulation + TDA pipeline")


@app.callback()
def main(
    verbose: bool = typer.Option(
        False,
        "--verbose",
        "-v",
        help="Enable verbose (DEBUG) logging",
    ),
):
    """
    Global CLI options, executed before any subcommand.
    """
    level = logging.DEBUG if verbose else logging.INFO
    setup_logging(log_dir=Path("logs"), level=level)
    logger = logging.getLogger(__name__)
    logger.debug("CLI started with verbose=%s", verbose)


@app.command("run-pipeline")
def run_pipeline():
    """
    Full pipeline:

    """
    logger = logging.getLogger(__name__)
    logger.info(f"log initial variables here")

    # 1) first step


    # 2) second step


    # 3) etc


    logger.info(f"Ocassional logging here")
    print("[bold green]Pipeline complete.[/bold green]")


@app.command("self-check")
def self_check():
    """
    Run a small in-memory pipeline to check that the core steps still work.
    Prints step-by-step status; exits with code 0 on success, 1 on error.
    """
    logger = logging.getLogger(__name__)
    logger.info("Running self-check")

    ok = True

    # --- Step 1: ---
    # try:
        
    # --- Step 2: ---
    # etc

    # --- Step 3: ---
    # etc


if __name__ == "__main__":
    app()