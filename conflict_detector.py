import os
from git import Repo
from typing import List, Dict

def detect_merge_conflicts(repo_path: str = '.') -> Dict[str, List[str]]:
    print('checking conflicts..')
    # Convert to absolute path
    repo_path = os.path.abspath(repo_path)
    
    # Initialize the repository
    repo = Repo(repo_path)
    
    # Dictionary to store conflicts
    conflicts = {}
    
    # Check unmerged files
    for item in repo.index.unmerged_blobs():
        file_path = item[0]
        full_file_path = os.path.join(repo_path, file_path)
        
        try:
            with open(full_file_path, 'r') as f:
                content = f.read()
                # Check for conflict markers
                if '<<<<<<< ' in content:
                    # Extract conflict marker lines
                    conflict_lines = [
                        line for line in content.split('\n') 
                        if '<<<<<<< ' in line or '>>>>>>> ' in line or '=======' in line
                    ]
                    
                    # Store conflicts
                    conflicts[file_path] = conflict_lines
        
        except Exception as e:
            # Optional: log the error, but continue processing other files
            print(f"Error reading {file_path}: {e}")
    
    return conflicts