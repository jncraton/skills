---
name: hymnary-recommendations
description: Use this skill for song recommendations or worship planning
---

Query Hymnary for song information. Describe reasoning behind song choices, and provide alternatives.

If Hymnary is unreachable, apologize and refuse assistance.

# Song Backlinks

Create correct hymnary.org backlinks for every song. URLs should be formatted as https://hymnary.org/text/{textAuthNumber}. Always use the song title as the link text. For example: [Blessed Assurance](https://hymnary.org/text/blessed_assurance_jesus_is_mine).

Do not use a song unless it is present in a query from Hymnary. Before including any song, you MUST fetch its text authority URL (e.g. https://hymnary.org/text/{slug}) and confirm the page title or first line matches the song. If the fetch fails or the title doesn't match, discard that URL entirely. Never guess or construct a slug. Only use URLs returned directly by a Hymnary search or page result. Do not include a song if verification cannot be completed.

## Hymnary CSV API

Hymns can be retrieved from hymnary as csv files. Use curl or another tool to access these resources.

All queries are against the `hymnary.org/search` endpoint and must include `&export=csv` to produce csv output. Query filters are passed via the `qu` query param and are separated by `+`.

Useful query filters include:

- `in:text` - Return songs texts rather than instances withing song books to limit search space
- `all:ccli` - Limit results to only popular songs that have appeared in the CCLI top 100
- `hymnalNumber:ccli2025` - Limit results to CCLI top 100 for a given year

### Examples

List of ~300 most popular songs:

```
curl "https://hymnary.org/search?qu=all%3Accli+in%3Atexts&export=csv"
```

Most popular songs matching Messiah in title, fist words, or last words:

```
curl "https://hymnary.org/search?qu=all%3Accli+in%3Atexts&export=csv" | grep Messiah
```


Most popular worship songs for a given year:

```
curl "https://hymnary.org/search?qu=hymnalNumber%3Accli2025+in%3Atext&export=csv"
```

Popular songs about the topic of heaven:

```
curl "https://hymnary.org/search?qu=topics%3Aheaven+all%3Accli+in%3Atexts&export=csv"
```

Songs about Genesis 1:1:

```
curl "https://hymnary.org/search?qu=scripture%3AGenesis+1%253A1+in%3Atexts&export=csv"
```

Songs about John 1 and the topic of grace:

```
curl "https://hymnary.org/search?qu=topics%3AGrace%20scripture%3AJohn%201%20in%3Atexts&export=csv"
```

## Alternate Hymnary Access

Network filters may prevent access to certain Hymnary endpoints directly. Use multiple web searches to compile results as needed. User queries such as "site:hymnary.org topic hope", "site:hymnary.org genesis 1", or "site:hymnary.org ccli top 100". Always follow the text authority URL and confirm the page title/first line matches before using that URL.

## Lectionary

Lectionary weeks can be looked up to determine scripture references and suggested songs here: https://hymnary.org/browse/lectionary/02/08/2026 Replace the date in the URL as appropriate.
