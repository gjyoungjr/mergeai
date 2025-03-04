import typer
from typing import Optional
from rich.console import Console
from conflict_detector import detect_merge_conflicts

console = Console()

## Test merge conflict detector
def main(
    command: str = typer.Argument(None),
    repo_path: Optional[str] = typer.Option(".", "--repo-path", "-r", help="Path to the repository")
):


    if command == "resolve":
        console.print(f"🔍 Scanning for merge conflicts in [bold cyan]{repo_path}[/bold cyan] ...")

        conflicted_files = detect_merge_conflicts(repo_path)
        
        if not conflicted_files:
            console.print("[green]✅ No merge conflicts found![/green]")
            return

        for file in conflicted_files:
            console.print(f"⚠ Found conflict in: [bold yellow]{file}[/bold yellow]")
            # conflicts = extract_conflicts(file)

            # for conflict in conflicts:
                # print(f"Conflict: {conflict}")
                # ai_resolution = resolve_conflict(conflict)
                # apply_fix(file, ai_resolution)

        console.print("\n[bold green]🎉 All conflicts resolved! Run `git add . && git commit` to save changes.[/bold green]")
    else:
        raise typer.BadParameter("Invalid command. Use 'resolve'.")

if __name__ == "__main__":
    typer.run(main)