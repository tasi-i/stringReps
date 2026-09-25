# Frequent Words — Python package starter

Implement two functions for analyzing text (such as DNA sequences):

- `PatternCount(text, pattern)`: count occurrences, including overlapping matches.
- `FrequentWords(text, k)`: find all most frequent length-`k` substrings.

Both functions start as TODO stubs that raise `NotImplementedError`. Their
docstrings describe the expected behavior and assumptions.

## Package layout

```text
pyproject.toml                  # Package metadata and build configuration
src/
    frequent_words/
        __init__.py             # Makes both functions available to import
        pattern_count.py        # Implement PatternCount here
        frequent_words.py       # Implement FrequentWords here
```

Separate `.py` files are called **modules**. A directory of related modules
with an `__init__.py` file forms a Python **package**. Putting these functions
in separate modules is valid Python practice; related small functions can
also share a module.

Python convention normally uses `pattern_count` and `frequent_words` for
function names. This starter keeps `PatternCount` and `FrequentWords` to
match the algorithm names used in class, while using lowercase module names.

## Set up

Use Python 3.10 or newer. From this repository's root directory:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e .
```

On Windows, activate with `.venv\Scripts\activate` in Command Prompt or
`.venv\Scripts\Activate.ps1` in PowerShell instead.

An editable install (`-e`) means edits to the source files take effect without
reinstalling the package. There are no runtime dependencies.

## Use your implementations

After completing the TODOs, try this in Python:

```python
from frequent_words import FrequentWords, PatternCount

print(PatternCount("AAAA", "AA"))  # Expected: 3
print(FrequentWords("ATAT", 2))    # Expected: {"AT"}
```

All package imports are already set up. Students only need to replace the
TODO comments and `raise NotImplementedError(...)` lines with their code.
Inside `FrequentWords`, call `PatternCount(text, pattern)` directly; its
import is already included at the top of the file:

```python
from .pattern_count import PatternCount
```

The leading dot means “from another module in this package.” Leave this
line and `__init__.py` as provided. After setup, start Python with `python`
in the terminal and use the example above to call your functions. Running
the individual source files directly is not how this package is used.

Check overlapping matches, ties, empty text, and patterns or words longer
than the text. Set output order is not guaranteed.
