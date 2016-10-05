import os
from subprocess import check_call
from shlex import split

def post_save(model, os_path, contents_manager):
    """post-save hook for doing a git commit / push"""
    if model['type'] != 'notebook':
        return # only do this for notebooks
    workdir, filename = os.path.split(os_path)
    if filename.startswith('Scratch') or filename.startswith('Untitled'):
        return # skip scratch and untitled notebooks
    # now do git add / git commit / git push
    check_call(split('git add {}'.format(filename)), cwd=workdir)
    check_call(split('git commit -m "notebook save" {}'.format(filename)), cwd=workdir)
    check_call(split('git push'), cwd=workdir)

c.FileContentsManager.post_save_hook = post_save
