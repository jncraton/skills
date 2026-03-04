---
name: instructor-feedback-summarizer
description: Transform student course evaluations into professional reports highlighting pedagogical strengths and growth areas.
---

# Instructor Feedback Summarizer

Use this skill to convert raw midterm or semester evaluations into summary reports for university instructors.

## Process

1.  Quantify sentiment:
    - Identify Likert-style questions.
    - Report the percentage of "Agree" and "Strongly agree" responses as a bulleted list.

2.  Identify pedagogical strengths:
    - Categorize praise into professional educator skills (e.g., scaffolding, formative assessment, clear pacing).
    - Map student quotes to these skills using simple row citations like `[3]` or `[12-14]`.

3.  Frame growth opportunities:
    - Note recurring pain points or constructive suggestions.
    - Frame these as professional opportunities for refinement (e.g., "Strengthening alignment between lectures and exams").

## Output format

The resulting `summary.md` must follow this structure:

- # Instructor highlights from [Course/Term]
- ## Snapshot: Response count and overall sentiment summary.
- ## Quantitative feedback: Bulleted list of agreement percentages.
- ## Key educator skills: Bulleted list of identified pedagogical strengths.
- ## Opportunities for growth: Constructive feedback framed as refinement areas.
- ## Representative student quotes: High-impact blockquotes with row citations.
- ## Mapping to strengths: Analysis linking student feedback to instructional competencies with row citations.

## Guidelines

- Professional tone: Use academic language to describe teaching methods.
- Concise citations: Use `[row_number]` only. Omit filenames and range labels.
- Action-oriented: Focus on evidence of learning and actionable insights.

