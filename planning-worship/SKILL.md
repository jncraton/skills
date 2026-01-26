---
name: planning-worship
description: Use this skill to generate a plan for a worship service
---

Hymnary is the source used for worship planning. All hymns and songs should link back to hymnary. Hymnary links should be formatted as https://hymnary.org/text/{textAuthNumber}. Always use the hymn title as the link text. For example: [Blessed Assurance](https://hymnary.org/text/blessed_assurance_jesus_is_mine)

## Hymnary API

Specific hymns matching a query can be retrieved from hymnary using curl as a CSV file.

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
