---
name: worship-plan
description: Use this skill to generate, evaluate, or adapt a plan for a worship service
---

## Songs

When providing songs selections for a worship service. Describe reasoning behind song choices, and provide alternatives for each.

Always use Hymnary as the source for song information, and always link songs back to Hymnary. Links should be formatted as https://hymnary.org/text/{textAuthNumber}. Always use the song title as the link text. For example: [Blessed Assurance](https://hymnary.org/text/blessed_assurance_jesus_is_mine). Never guess song URLs and only use songs included in responses from Hymnary.

## Hymnary API

Lectionary weeks can be looked up to determine scripture references and suggested songs here: https://hymnary.org/browse/lectionary/02/08/2026 Replace the date in the URL as appropriate.

Hymns matching a query can be retrieved from hymnary as a csv file using curl.

### Examples

Hymns about the topic of heaven:

```
curl "https://hymnary.org/search?qu=topics%3Aheaven%20%20media%3Atext%20in%3Atexts&export=csv" > hymns.csv
```

Hymns about Genesis 1:1:

```
curl "https://hymnary.org/search?qu=scripture%3AGenesis%201:1%20media%3Atext%20in%3Atexts&export=csv" > hymns.csv
```

Hymns about John 1 and the topic of grace:

```
curl "https://hymnary.org/search?qu=topics%3AGrace%20scripture%3AJohn%201%20media%3Atext%20in%3Atexts&export=csv" > hymns.csv
```
