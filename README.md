# Christian David — QA Portfolio

Manual QA testing built on engineering discipline, automation added where it earns its place.

[LinkedIn](https://linkedin.com/in/davidchristianj) | [X](https://x.com/0x_Opera) | [Upwork](https://www.upwork.com/freelancers/~010e703beaa0687103) | [Fiverr](https://www.fiverr.com/s/P2PmoBo)

---

## Value Proposition

A green checkmark doesn't mean your app works. It means the script did what you told it to do. I find what the script wasn't told to check: the form that breaks when a user pastes instead of types, the button that's clickable a half-second before the API call finishes, the flow that only fails on a slow connection. Manual and exploratory testing is where I catch that, because a human mind still notices what an assertion doesn't. Once I know what actually breaks, I automate the checks worth repeating, Playwright suites wired into CI, so the bug I found once doesn't have to be found twice. Thorough first. Fast second. Never the other way round.

---

## 1. Professional Summary

I test software the way I was trained to think about materials under stress: everything has a failure point, the job is finding it before it costs someone else. My core discipline is manual testing: functional, exploratory, regression, run by hand, thinking like a real user and like someone hunting for the exact condition that breaks the thing. Automation extends that work rather than replacing it. Playwright and TypeScript suites wired into GitHub Actions, Python tooling that turns a plain-language spec into structured test scenarios. The manual pass tells me what's worth automating. It never gets skipped to save time.

---

## 2. Technical Skills Matrix

**Manual Testing (Core)**

| Skill | Level | Notes |
|---|---|---|
| Functional Testing | Proficient | Full user flows, multi-step forms, state-dependent UI |
| Exploratory Testing | Proficient | Unscripted, session-based, chasing edge cases a test plan won't predict |
| Regression Testing | Proficient | Manual verification pass before and after a fix ships |
| Bug Reporting | Proficient | Reproducible steps, expected vs actual, severity, environment specifics |
| Jira | Proficient | Ticket triage, bug lifecycle tracking, from live Upwork QA work |

**Automation & Tooling (Extension)**

| Skill | Level | Notes |
|---|---|---|
| Playwright | Proficient | E2E suites, role-based locators over brittle CSS selectors, wired into GitHub Actions CI |
| Python | Proficient | Test tooling, AI-assisted test case generation from plain-language specs |
| Postman | Proficient | API testing, request chaining, response schema checks |
| TypeScript / JavaScript | Familiar | Used alongside Playwright for test logic |
| SQL | Familiar | Querying test data state directly, not just trusting the UI |
| n8n / Zapier | Proficient | Workflow automation, adjacent skill for process-level QA |

**Note:** keep every rating honest to what you can defend live in an interview. "Proficient" means you can work unsupervised with it under pressure, not that you've read the docs once.

---

## 3. Bug Reports Showcase — ⚠️ NEEDS REAL CONTENT

This is where manual testing expertise gets proven, not claimed. A resume says you can find bugs. A well-written bug report shows how you think. Currently empty. Fill with 3-5 real ones before this portfolio goes live anywhere.

**Bug Report Template:**
```
Title: [Short, specific description of the defect]
Environment: [Browser/OS/device, app version]
Steps to Reproduce:
1.
2.
3.
Expected Result: [What should happen]
Actual Result: [What actually happens]
Severity: [Critical / High / Medium / Low]
Root cause hypothesis (optional): [race condition, validation gap, state mismatch, etc.]
Screenshot/Evidence: [attach]
```

**Action for you:** pick 2-3 public web apps or open-source projects, test them for real using a session-based exploratory technique, not a checklist. Look specifically for state bugs (things that break on back-button, refresh, or double-submit), timing bugs (race conditions between UI and network), and boundary bugs (empty states, max-length inputs, special characters). Those three categories separate a real tester from someone who clicked through the happy path. This is the highest-leverage gap in the whole portfolio; everything else is secondary until this section has real content.

---

## 4. Test Case Samples — ⚠️ NEEDS REAL CONTENT

Lead with manual test case design, then show how a subset became automated.

Must include:
- Manual functional test cases (happy path, 1-2 examples only; this isn't where the skill shows)
- Manual boundary and negative test cases; this is where manual expertise actually shows: what happens at zero, at max, at malformed input, at unauthorized access
- 1-2 examples of a manual test case that became a Playwright automated check, with a short note on why that specific one earned automation (high repetition, high regression risk, low judgment required)

**Action for you:** pull real cases from your own testing work. The manual-to-automated pairing is your sharpest differentiator; it shows you don't automate by default, you automate by decision.

---

## 5. Automation Projects (Extension of Manual Work)

**Automated E2E Test Suite**
Playwright + TypeScript, wired into GitHub Actions CI, running regression checks on every push. Built after identifying which manual regression checks were repetitive enough and low-judgment enough to justify automating instead of running by hand every cycle.
`[link to repo]`

**AI-Assisted Test Case Generator**
Python tool converting plain-language feature specs into structured test scenarios and Playwright test stubs. Speeds up the scaffolding work. Every generated case still gets a manual review pass before it merges, because AI output is a draft, not a verdict.
`[link to repo]`

**API Test Automation Framework**
API testing suite with structured, readable reporting, request/response validation, and schema checks for coverage visibility across a team.
`[link to repo]`

**Action for you:** each project needs its own README, what it tests, which framework, and why it exists, not just that it exists. A repo with no README reads as abandoned, not proof.

---

## 6. Certifications and Learning

- AI Fluency Certificate — Anthropic Academy
- AI-assisted testing — ShiftSync

## 7. Project Context

**QA Tester — Upwork (Current)**
Strictly manual QA testing sourced through Upwork. Functional and exploratory testing, Jira for bug tracking, reproduction steps written precise enough that a developer fixes on the first read, never has to ask what triggered it.

**VoiceGuard — Dev3Pack Global Hackathon (2026)**
Industry: Fintech/crypto. Built a QA process from scratch for a voice-first crypto transaction safety assistant under real hackathon time pressure, no room for a second pass. Manual test case design for the voice-capture and transaction-confirmation flow, the two places where a silent failure would have cost the demo. Delivered a stable live with zero last-minute failures.

**Independent QA Tester — uTest (2026)**
Manual and exploratory testing on live production software across real-world products, not staging environments; real users' real data on the other side of every bug found.

---

## AI QA Skills (2026 differentiator)

- **AI-assisted test case generation:** built a Python tool converting plain-language specs into structured Playwright test stubs. Treats AI as a first draft generator, not a decision-maker.
- **Knowing what AI gets wrong:** [Action for you: this is the one line that matters most in this section. Write a real example: a time AI-generated tests reported a false pass, or missed an edge case entirely, and how your manual pass caught what the model didn't. One honest sentence here beats ten lines claiming "AI-powered testing" as a buzzword.]
- **Manual judgment as the check on automation:** every automated suite here traces back to a manual test case designed by hand first. The order is the point. Automation without a manual origin is just untested guessing at scale.

---

## What's Left To Do (in order)

1. Find and document 3-5 real bugs (Section 3), highest priority; this is where manual expertise gets proven instead of claimed
2. Pull 5-10 real test cases from your own testing, including at least one manual-to-automated pairing (Section 4)
3. Add READMEs to your three project repos (Section 5)
4. Write the "AI got it wrong once, manual caught it" example (AI QA Skills section)
5. Publish the repo as public on GitHub, link from LinkedIn Featured, Upwork portfolio, and Fiverr gig gallery
