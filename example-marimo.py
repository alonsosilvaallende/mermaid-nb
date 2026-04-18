import marimo

__generated_with = "0.23.1"
app = marimo.App()


@app.cell
def _():
    from mermaid_nb import Mermaid

    Mermaid()  # default diagram
    return (Mermaid,)


@app.cell
def _(Mermaid):
    Mermaid(
        diagram="""
    flowchart LR
      A[Start] --> B{Decision}
      B -->|Yes| C[Continue]
      B -->|No| D[Stop]
    """,
        theme="forest",
        look="handDrawn",
        theme_variables={"nodeTextColor": "#0000ff", "fontFamily": "Caveat, cursive"}
    )
    return


if __name__ == "__main__":
    app.run()
