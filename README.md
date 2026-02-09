# Wavess 1.0 : LinkedIn Growth Solution (Task 1)

## Project Overview
This project is a small protoype created to analyse LinkedIn post performance and audience for the given LinkedIn post.
This project is used to extract relevant post features, analyse the audience and evalute if the current audience is the same as the defined Ideal Customer Profile(ICP).

## Given LinkedIn Post
Klarna - AI for Climate Resilience Program

https://www.linkedin.com/posts/klarna_klarnas-climate-resilience-program-activity-7346877091532959746-748v/?utm_source=share&utm_medium=member_desktop&rcm=ACoAAADnFyQBBmDIWAAFjnAInMjU44QmY2tSbC8

## Assumptions and Constraints
- LinkedIn API is restricted for general users, therefore, all the collected data is publically visible.
- Audience **sample** of users(Reactors/Commentators) and not the full audience.
- The Project prioritizes **business relevance** over prediction accuracy.
- Job roles and company types are gathered from profile titles and company information.
- Engagement performance is analysed using reactions(likes) and comments.
- If a profile lists more than one job role, the most recent job role is selected as a primary role. If there is full-time and part-time, the full-time position is selected as a primary role.

## Strategy Methods
### Audience Sample Collection
- Manual Collection of 25 Audience members
- Collection of: name, job title, company

### Post Features Extraction
- Text length metrics
- Emoji usage
- Hashtagb usage
- CTA keywords
- Topics
- Tone

These features are stored in 'outputs/post_features.csv'

### Audience Analysis
- Seniority derived from job_title
- Company type derived from company

The analytics is stored in 'outputs/audience_ranked.csv'

### Ideal Customer Profile (ICP)
- ICP companies were selected based on industry relevance
- ICP seniority is set to mid-senior

### ICP Scoring
Each audience member is scored on:
- Seniority
- Company Type
- Job role

Score is stored in 'output/audience_ranked.csv'

## Key Insights (Summary)
- The post primarily attracts professionals in leadership roles.
- Engagement is strongest among mid-to-senior level professionals.

## Automation & Scaling (Conceptual)
This workflow could be scaled by:
- Integrating LinkedIn APIs or approved data providers for automated data ingestion
- Automating NLP feature extraction and sentiment analysis pipelines
- Allowing customizable ICP definitions per client
- Benchmarking post performance across multiple posts and time periods
- Adding dashboards for real-time performance and audience relevance tracking

## How to run
### 1. Ensure Python is installed
### 2. Install dependencies
_pip install -r requirements.txt_
### 3. Run the scripts

## Notes
This project was made as a task to proceed with an internship application. It was NOT an original idea, however it was made by me.