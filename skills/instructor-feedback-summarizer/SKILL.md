---
name: instructor-feedback-summarizer
description: Transform student course evaluations into professional reports highlighting pedagogical strengths and growth areas.
---

Use this skill to convert raw midterm or semester evaluations into summary reports for university instructors.

## Sentiment quantification

- Identify all Likert scale questions
- Report combined Agree and Strongly agree percentages
- Present findings in a flat bulleted list

## Pedagogical strengths

- Categorize positive feedback into professional educator skills
- Use academic language for teaching methods
- Map student quotes to identified skills
- Cite sources using only row numbers in brackets

## Growth opportunities

- Identify recurring pain points or constructive suggestions
- Frame issues as professional opportunities for refinement
- Focus on actionable insights and evidence of learning
- Maintain an objective tone throughout

## Output format

The resulting `summary.md` must follow this structure:

- # Instructor highlights from [Course/Term]
- ## Snapshot: Response count and overall sentiment summary.
- ## Quantitative feedback: Bulleted list of agreement percentages.
- ## Key educator skills: Bulleted list of identified pedagogical strengths.
- ## Opportunities for growth: Constructive feedback framed as refinement areas.
- ## Representative student quotes: High-impact blockquotes with row citations.
- ## Mapping to strengths: Analysis linking student feedback to instructional competencies with row citations.
