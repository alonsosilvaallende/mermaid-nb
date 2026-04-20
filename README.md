# mermaid-nb

## Create Mermaid diagrams in Python

## Installation

```sh
pip install mermaid-nb
```

or with [uv](https://github.com/astral-sh/uv):

```sh
uv add mermaid-nb
```

## Getting Started

In your notebook, run the following command:
```python
from mermaid_nb import Mermaid

Mermaid(diagram="flowchart LR\n  Hello --> World\n  Hello --> Name")
```
<img width="255" height="165" alt="image" src="https://github.com/user-attachments/assets/808c444e-12da-47cd-839a-fbb4d7a55cc3" />

## Create a Mermaid diagram in a Jupyter notebook
<img width="758" height="467" alt="image" src="https://github.com/user-attachments/assets/109265d8-9f4a-409a-81fa-675e0cc86b9c" />

## Create a Mermaid diagram in a marimo notebook or a marimo WebAssembly (WASM) notebook
<img width="719" height="467" alt="image" src="https://github.com/user-attachments/assets/a573ef71-ade6-4afe-bca4-12278bdd7dee" />

## Create a Mermaid diagram in a JupyterLite notebook
<img width="533" height="395" alt="image" src="https://github.com/user-attachments/assets/22e2d91c-36e1-4c64-806d-8e2589c7d042" />

## Development

We recommend using [uv](https://github.com/astral-sh/uv) for development.
It will automatically manage virtual environments and dependencies for you.

```sh
uv run jupyter lab example.ipynb
```

Alternatively, create and manage your own virtual environment:

```sh
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
jupyter lab example.ipynb
```

Open `example.ipynb` in JupyterLab, VS Code, or your favorite editor
to start developing. Changes made in `src/mermaid_nb/static/` will be reflected
in the notebook.
