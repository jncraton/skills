---
name: instructor-feedback-summarizer
description: Create a summary.md file from raw student course evaluations, focusing on highlighting instructor strengths and actionable feedback for university courses.
---

# Instructor Feedback Summarizer

Use this skill to transform raw midterm or semester student feedback into a structured `summary.md` report for university instructors.

## Input requirements

- A data file (e.g., `midterm-survey.csv`) containing student responses.
- Responses typically include Likert-style ratings on instruction, course materials, and open-ended feedback on what is working or should change.

## Process

1. **Analyze quantitative data**:
   - Identify Likert-style questions (e.g., "Strongly agree" to "Strongly disagree").
   - Calculate the percentage of students who "Agree" or "Strongly agree" for each statement.
   - Present these as a bulleted list in a "Quantitative feedback" section to provide a high-level snapshot of student sentiment.

2. **Identify educator skills**:
   - Review open-ended responses to identify specific pedagogical strengths (e.g., scaffolding, formative assessment, clarity, responsiveness, or effective use of technology).
   - Look for themes related to specific course components like labs, lectures, or quizzes.

3. **Select representative quotes**:
   - Pick 3-5 quotes that illustrate the most common student perspectives.
   - Prioritize quotes that offer specific evidence of learning or engagement.
   - Always cite the source file and line number using the format `file.csv:line`.

4. **Map to instructor strengths**:
   - Create a concluding section that explicitly maps student feedback to recognized instructional strengths.
   - Translate student praise (e.g., "I like the quizzes") into professional educator skills (e.g., "Effective use of low-stakes formative assessment to support retrieval").

5. **Identify opportunities for growth**:
   - Note any constructive suggestions or recurring pain points (e.g., exam preparation, clarity of instructions, or pacing).
   - Frame these as "Opportunities for growth" rather than failures.

## Output format

The resulting `summary.md` should follow this structure:

- **Title**: Instructor highlights from [Course/Term] feedback.
- **Snapshot**: Metadata including response count and overall sentiment.
- **Quantitative feedback**: Percentages of agreement for key instructional metrics.
- **Key educator skills**: Bulleted list of themes identified from qualitative responses.
- **Opportunities for growth**: Constructive feedback and suggested improvements.
- **Representative student quotes**: Blockquotes with citations to the raw data.
- **Mapping to strengths**: Detailed analysis linking feedback to specific instructional competencies.

## Guidelines

- Use professional, academic language when describing instructional practices.
- Focus on highlights and actionable insights that support instructor growth.
- Ensure all percentages are accurate based on the total number of valid responses.
- Maintain citations for every quote to allow for verification.
