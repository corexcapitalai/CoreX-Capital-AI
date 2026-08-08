const examples = [
  {
    proposal: "BUY",
    confidence: "74%",
    governance: "CLEARED",
    risk: "LOW",
    reason: "Illustrative proposal passed all public-facing policy checks. No production execution is performed.",
    bad: false,
  },
  {
    proposal: "SELL",
    confidence: "81%",
    governance: "VETOED",
    risk: "HIGH",
    reason: "Illustrative deterministic risk gate vetoed the proposal despite high model confidence.",
    bad: true,
  },
  {
    proposal: "HOLD",
    confidence: "56%",
    governance: "HELD",
    risk: "MEDIUM",
    reason: "Illustrative context gate requested fresher information before publishing a final state.",
    bad: false,
  },
];

let exampleIndex = 0;
const button = document.querySelector("#simulateButton");
const proposal = document.querySelector("#proposalValue");
const confidence = document.querySelector("#confidenceValue");
const governance = document.querySelector("#governanceValue");
const risk = document.querySelector("#riskValue");
const reason = document.querySelector("#reasonText");
const year = document.querySelector("#year");

if (year) year.textContent = String(new Date().getFullYear());

button?.addEventListener("click", () => {
  exampleIndex = (exampleIndex + 1) % examples.length;
  const next = examples[exampleIndex];

  proposal.textContent = next.proposal;
  confidence.textContent = next.confidence;
  governance.textContent = next.governance;
  risk.textContent = next.risk;
  reason.textContent = next.reason;
  governance.classList.toggle("bad", next.bad);
  governance.classList.toggle("good", !next.bad);
});
