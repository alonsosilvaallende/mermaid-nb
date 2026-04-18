import mermaid from "https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs";
import rough from "https://cdn.jsdelivr.net/npm/roughjs@4/bundled/rough.esm.js";

window.rough = rough;

async function render({ model, el }) {
  const diagram = model.get("diagram");
  const look    = model.get("look");
  const theme   = model.get("theme");
  const themeVariables = model.get("theme_variables");

  mermaid.initialize({
    startOnLoad: false,
    look: look,
    theme: theme,
    themeVariables: themeVariables
  });

  const graphContainer = document.createElement("div");
  el.appendChild(graphContainer);

  const id = "mermaid-" + Math.random().toString(36).slice(2);

  try {
    const { svg } = await mermaid.render(id, diagram);
    graphContainer.innerHTML = svg;
  } catch (err) {
    graphContainer.innerText = "Render error: " + err.message;
    console.error("Mermaid render error:", err);
  }
}

export default { render };
