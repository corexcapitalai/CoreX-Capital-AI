// Minimal browser/Node-style example for the local public mock API.
// The endpoint is synthetic and read-only.

const baseUrl = "http://127.0.0.1:8787";

async function getExampleSignal() {
  const response = await fetch(`${baseUrl}/v1/signals/example`);
  if (!response.ok) throw new Error(`HTTP ${response.status}`);
  return response.json();
}

getExampleSignal()
  .then((signal) => {
    console.log({
      proposal: signal.proposal.action,
      governance: signal.governance.state,
      synthetic: signal.synthetic,
    });
  })
  .catch((error) => console.error("Public mock request failed:", error.message));
