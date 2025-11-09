const fs = require("fs");
const url = "https://gist.githubusercontent.com/ongkiii/b40620d8d4a98ab17642858dce4cb2ec/raw/04031ccf177079e8730cdf77664ec685886d915e/IPA-Sources.md";

async function fetchAndWrite() {
  const res = await fetch(url);
  if (!res.ok) throw new Error(`Fetch failed: ${res.status}`);
  const text = await res.text();
  fs.writeFileSync("side/repos.md", text, "utf8");
  console.log("Wrote side/repos.md");
}

fetchAndWrite().catch(err => {
  console.error(err);
  process.exit(1);
});


document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll(".md-typeset .grid.cards li").forEach(card => {
    const link = card.querySelector("a[href]");
    if (link) {
      card.style.cursor = "pointer";
      card.addEventListener("click", () => {
        window.location.href = link.href;
      });
    }
  });
});