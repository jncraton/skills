---
name: hymnary-recommendations
description: Use this skill for general song recommendations or worship planning
---

## Songs

Always use Hymnary as the source for song information, and always link songs back to Hymnary. Links should be formatted as https://hymnary.org/text/{textAuthNumber}. Always use the song title as the link text. For example: [Blessed Assurance](https://hymnary.org/text/blessed_assurance_jesus_is_mine). Only use songs included in responses from Hymnary. textAuthNumber is subject to change, and the only valid values are those just directly returned from live queries to Hymnary.

Describe reasoning behind song choices, and provide alternatives.

## Hymnary API

Hymns matching a query can be retrieved from hymnary as a csv file. Use curl to access these resources. Only recommend hymns that have be returned from a query to ensure they are fresh and accurate.

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
curl "https://hymnary.org/search?qu=hymnalNumber%3Accli2025+in%3Atext&export=csv" > ccli100.csv
```

Popular songs about the topic of heaven:

```
curl "https://hymnary.org/search?qu=topics%3Aheaven+all%3Accli+in%3Atexts&export=csv" > hymns.csv
```

Songs about Genesis 1:1:

```
curl "https://hymnary.org/search?qu=scripture%3AGenesis+1%253A1+in%3Atexts&export=csv" > hymns.csv
```

Songs about John 1 and the topic of grace:

```
curl "https://hymnary.org/search?qu=topics%3AGrace%20scripture%3AJohn%201%20in%3Atexts&export=csv" > hymns.csv
```

## Lectionary

Lectionary weeks can be looked up to determine scripture references and suggested songs here: https://hymnary.org/browse/lectionary/02/08/2026 Replace the date in the URL as appropriate.
