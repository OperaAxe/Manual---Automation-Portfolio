# DemoQA Elements — Manual Test Plan

**Target:** https://demoqa.com/elements  
**Prepared:** 27 October 2026  
**Scope:** the nine subsections under Elements only.

## Objective

Explore the visible behaviour of the Elements practice pages, record reproducible results, and separate application observations from expected demo behaviour. This is a portfolio exercise against a public training site, not a client engagement or a security certification.

## In scope

- Text Box
- Check Box
- Radio Button
- Web Tables
- Buttons
- Links
- Broken Links - Images
- Upload and Download
- Dynamic Properties
- Basic accessible-name checks for selected controls

## Out of scope

- Forms, Alerts, Widgets, Interactions, and Book Store Application sections
- Authentication or personal accounts
- Load/performance testing
- Production-like security claims
- Payment flows or destructive data changes outside temporary test rows

## Approach

1. Open each page and note its URL and visible controls.
2. Define the expected result before interaction.
3. Use synthetic values only.
4. Check resulting state, not only button response.
5. Record actual result and keep an evidence note.
6. Mark a test **Not Run** when the interaction was not completed.
7. Report only observed defects or clearly documented accessibility risks. Re-run them in a normal browser before submitting formal tickets.

## Initial results

The accompanying Excel pack contains 30 scenarios. In the initial observed session, 17 were marked Pass, 7 Fail, and 6 Not Run. The 7 failed observations are detailed in the workbook's Defect Log.

This does **not** mean 30 bugs were found. The workbook deliberately separates test scenarios from defect count. Some accessibility findings are based on DOM attributes and need confirmation with an accessibility tree or assistive technology. A browser automation timeout is recorded as a limitation, not a product failure.

## Test data

Use synthetic values like:
- Name: Test User
- Email: qa.test@example.com
- Current address: 10 Test Road
- Permanent address: 20 Example Street

For Web Tables, use a unique throwaway email and delete the test row after the scenario.

## Exit criteria for a stronger second pass

- Re-run all seven defect observations in a fresh browser session.
- Complete the six Not Run scenarios.
- Capture screenshots with the page URL and the relevant result visible.
- Verify accessibility-related observations using the browser accessibility tree and keyboard/screen-reader checks.
- Update the defect log with a confidence level, exact evidence, and current status.
