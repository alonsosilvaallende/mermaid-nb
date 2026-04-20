[![PyPI version](https://badge.fury.io/py/mermaid-nb.svg)](https://badge.fury.io/py/mermaid-nb)
[![License: Apache2.0](https://img.shields.io/badge/License-Apache2.0-yellow.svg)](https://opensource.org/licenses/Apache2.0)

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

Here is a [basic example](https://marimo.app/?slug=pn13uf) of a marimo WebAssembly (WASM) notebook.

## Create a Mermaid diagram in a JupyterLite notebook
<img width="556" height="395" alt="image" src="https://github.com/user-attachments/assets/750a7f24-6ce3-47a8-a4ed-b84e957adcb8" />

Here is a [basic example](https://alonsosilvaallende.github.io/my-jupyterlite-site/lab/index.html?tempNotebook=1&path=temp.ipynb&openAsNotebook=1#notebook=N4IgtgpgLghgJjWIBcoDWEBOA7CAbAZwAcIBjFUbGSFEIgTygAsB7bEAGhDgEti8Y9APpUayEAAVGrbAAIAFFJa84EAJScQA7AHMArjB0RaDZmxABfLtv2GIQntgBmLCiFLKIYHpkwtMQmCebqLG4qYymgBuWAQ85sgAzFYgTjx49hAAHlAQ2HEJIAB0DJrekFD0JLS5OQD0WQC0EeZcoSbSrSDYAEYe2DGYUELZRP65mB1m7FwMOpDYUARCGVlYtDwt2InRsfHs4olFAByWKb0umGCIgY7+KACsbT2X11AoACxcpPiEKADaoB4cFoxwAjAA2ABMAE4YQAGUiNGAQh4QxofY4fJE9SEAdkaD0S8JhMGJuLgYPI31+Qkq1XEHlUmgILD0mB+tAApERNrJHARYHg8LJIFcYMCRD0ytB4IgYG4oJg9IKICDkEq9BAUmyoEQ9EsAQBdLjZMgG-ZCDx6RYobB6YVWIHqkB4kkw45wD4PDEQSEYl5I47wv2NCCJSn4iDwqnwzQ-YV0qphdzBLis9mc8ROPxgUVYa6S3r8sBjIayACyBYlcAAOth61XxcD5LxDJhqABeWupPAsADupCYMHLABkAEq1+uyWQACV+LFkjUaAD5ZAB1fx4OvTucLper2QAOWoEB7Gi4FTlSFQIE1qvVmu1XF1+sNyH+JpAZtIFrYVrZW1kHtR0OGdWhSUSGFEkSCBjkaPEIDxRIMXhHofRgUg4B6RoIR6D5EgI0gYTBGEnGlGlE3pFMmWMdM2Q5FMZVgBAb1Ae9ckfZVnxAV8DQIY1TTWX8oEta0gJAvALCNCwgA) of a JupyterLite notebook.

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
