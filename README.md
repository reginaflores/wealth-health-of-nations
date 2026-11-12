# The Wealth & Health of Nations, 1810–2020

An animated bubble chart of income per person (GDP/capita, PPP, log scale) against life expectancy for 195 countries.
Bubble size = population, color = continent. Hover for details, press play to animate through time, pause or drag the slider to inspect any year.

**Live:** https://reginaflores.github.io/wealth-health-of-nations/

- `index.html` — the visualization (D3 v7, no build step)
- `data/data.json` — merged dataset
- `build_data.py` — rebuilds `data/data.json` from Gapminder CSVs (life expectancy, income per person, population; Gapminder systema_globalis)

Continents follow Gapminder's four world regions, with Pacific island nations, Australia and New Zealand split out as Oceania.
