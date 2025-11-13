# Project Update By Lifestyle Task
#### Plan: Completed
Finalized in the project proposal with the research question:
Is there a relationship between the number of building permits issued and the number of building violations recorded in a given neighborhood or year?

#### Acquire: Completed
Successfully retrieved and storedthe records for both datasets. The columns were standardized to lowercase with underscores for consistency.

#### Process: In Progress
Both datasets were cleaned and filtered for the analysis period.

#### Analyze: In Progress
Yearly aggregation was doing using pandas.groupby(). The results were then merged on the year column. A visualization was also created with seaborn shows trends with permit issuance increasing while violations decreasing after 2018.

Next step: correlation analysis and spatial trend visualization by community area.

#### Preserve: 
- Keep the repository structured with clear folder organizations
- Generate data dictionary

#### Publish/Share
- Write final report
- Finalize figures and visualizations
- Tag final release on GitHub

# Updated Timeline
| **Task** | **Status** | **Target Completion** |
|-----------|-------------|------------------------|
| Plan | Completed | Oct 7 |
| Acquire | Completed | Nov 12 |
| Process | In Progress| Nov 20 |
| Analyze | In Progress| Nov 20 |
| Preserve | Waiting| Dec 10 |
| Publish/Share | Waiting| Dec 10 |

# Changes to Project Plan
- Incorporated clearer division of roles per feedback — Sophia leads documentation, reproducibility, Samantha leads data engineering and integration
- Expanded analysis scope to include geographic trends instead of only by year

# Team Member Contributions
Sophia Chen
- Retrieved both datasets via the Socrata API
- Developed the basics of the cleaning, merging, and visualization scripts
- Created documentation and structured repository organization

Samantha Mean
- Identified and verified the Socrata datasets from the Chicago Data Portal
- Helped define the API access and filtering strategy
- Assisted with integration planning
