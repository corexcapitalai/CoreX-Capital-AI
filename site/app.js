const year = document.querySelector("#year");
if (year) year.textContent = String(new Date().getFullYear());

const sectionLinks = [...document.querySelectorAll('nav a[href^="#"]')];
const sections = sectionLinks
  .map((link) => document.querySelector(link.getAttribute("href")))
  .filter(Boolean);

if ("IntersectionObserver" in window && sections.length) {
  const observer = new IntersectionObserver(
    (entries) => {
      const visible = entries
        .filter((entry) => entry.isIntersecting)
        .sort((a, b) => b.intersectionRatio - a.intersectionRatio)[0];

      if (!visible) return;

      sectionLinks.forEach((link) => {
        const active = link.getAttribute("href") === `#${visible.target.id}`;
        link.setAttribute("aria-current", active ? "location" : "false");
      });
    },
    { rootMargin: "-30% 0px -55%", threshold: [0.1, 0.35, 0.6] },
  );

  sections.forEach((section) => observer.observe(section));
}
