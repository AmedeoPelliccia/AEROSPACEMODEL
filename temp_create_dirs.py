import os
root = r'c:\Users\amate\OneDrive\Documentos\OneDrive\Desktop\AEROSPACEMODEL-ASIT-ASIGT.worktrees\copilot-worktree-2026-02-10T17-51-05'
os.makedirs(os.path.join(root, 'src', 'aerospacemodel', 'pipeline'), exist_ok=True)
os.makedirs(os.path.join(root, '.github', 'workflows'), exist_ok=True)
with open(os.path.join(root, 'src', 'aerospacemodel', 'pipeline', '__init__.py'), 'w') as f:
    f.write('')
with open(os.path.join(root, '.github', 'workflows', '.gitkeep'), 'w') as f:
    f.write('')
print('Done')
