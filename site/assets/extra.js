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
