document.addEventListener("DOMContentLoaded", function () {
  const btn = document.getElementById("toggle-theme");
  const html = document.documentElement;
  const STORAGE_KEY = "theme";

  // 1️⃣ Aplicar tema guardado al cargar
  const savedTheme = localStorage.getItem(STORAGE_KEY);
  if (savedTheme) {
    html.setAttribute("data-bs-theme", savedTheme);
  }

  // 2️⃣ Toggle + persistencia
  btn.addEventListener("click", function () {
    const current = html.getAttribute("data-bs-theme") || "light";
    const next = current === "dark" ? "light" : "dark";

    html.setAttribute("data-bs-theme", next);
    localStorage.setItem(STORAGE_KEY, next);
  });
});
