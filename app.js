"use strict";
(() => {
  const search = document.querySelector("#search");
  const filters = document.querySelector("#themen");
  const status = document.querySelector("#result");
  const empty = document.querySelector("#empty");
  const cards = Array.from(document.querySelectorAll(".card"));
  if (!search || !filters || !status || !empty || !cards.length) return;
  const buttons = Array.from(filters.querySelectorAll("[data-filter]"));
  let category = "Alle";
  const normalise = text => text.normalize("NFC").toLocaleLowerCase("de");
  const filter = () => {
    const query = normalise(search.value.trim());
    let count = 0;
    for (const card of cards) {
      const matches = (category === "Alle" || card.dataset.category === category)
        && normalise(card.dataset.search || "").includes(query);
      card.hidden = !matches;
      if (matches) count += 1;
    }
    empty.hidden = count > 0;
    status.textContent = `${count} ${count === 1 ? "Beitrag" : "Beiträge"} entdecken`;
  };
  for (const button of buttons) button.addEventListener("click", () => {
    category = button.dataset.filter;
    for (const item of buttons) item.setAttribute("aria-pressed", String(item === button));
    filter();
  });
  search.addEventListener("input", filter);
  search.disabled = false;
  filters.hidden = false;
  filter();
})();
