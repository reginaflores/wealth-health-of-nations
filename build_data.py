"""Build data/data.json from Gapminder CSVs (life expectancy, GDP/capita PPP, population)."""
import csv, json, sys, os
raw = sys.argv[1]
def series(fn):
    d = {}
    for r in csv.DictReader(open(os.path.join(raw, fn))):
        y = int(r['time'])
        if 1810 <= y <= 2020:
            v = list(r.values())[2]
            if v: d.setdefault(r['geo'], {})[y] = float(v)
    return d
lex = series('lex_91fc7aa957.csv'); inc = series('inc_06a60c6ba0.csv'); pop = series('pop_76a31f00dd.csv')
ent = {r['country']: r for r in csv.DictReader(open(os.path.join(raw, 'ddf--entities--geo--country.csv')))}
OCEANIA = {'aus','nzl','png','fji','slb','vut','wsm','ton','kir','fsm','mhl','plw','nru','tuv'}
CONT = {'africa':'Africa','americas':'Americas','asia':'Asia','europe':'Europe'}
out = []
for g in sorted(set(lex) & set(inc)):
    e = ent[g]
    cont = 'Oceania' if g in OCEANIA else CONT[e['world_4region']]
    ys = list(range(1810, 2021))
    def arr(s, nd): return [round(s[g][y], nd) if y in s.get(g, {}) else None for y in ys]
    NAMES = {'UAE':'United Arab Emirates','UK':'United Kingdom','USA':'United States'}
    out.append({'id': g, 'name': NAMES.get(e['name'], e['name']), 'continent': cont,
                'lex': arr(lex, 2), 'gdp': arr(inc, 0), 'pop': arr(pop, 0)})
json.dump({'startYear': 1810, 'endYear': 2020, 'countries': out}, open('data/data.json', 'w'), separators=(',', ':'))
print(len(out), 'countries;', sum(1 for c in out if c['pop'][-1] is None), 'missing 2020 pop')
