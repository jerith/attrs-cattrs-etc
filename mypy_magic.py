# This is copied verbatim from https://switowski.com/blog/creating-magic-functions-part2

from IPython.core.magic import register_cell_magic

@register_cell_magic('mypy')
def typechecker(line, cell):
    try:
        from mypy.api import run
    except ImportError:
        return "'mypy' not installed. Did you run 'pip install mypy'?"

    args = []
    if line:
        args = line.split()

    result = run(['-c', cell, *args])

    if result[0]:
        print('\nType checking report:\n')
        print(result[0])  # stdout

    if result[1]:
        print('\nError report:\n')
        print(result[1])  # stderr

    # Return the mypy exit status
    return result[2]
