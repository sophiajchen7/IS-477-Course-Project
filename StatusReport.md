# Project Status Report By USGS Lifecycle Model Tasks

#### Plan: Evaluated and Completed
Based on our project plan, we followed the USGS Science Data Lifecycle Model. Completing the project plan was our successful collaboration on determining the trajectory and direction of our project and research question. After acquiring the data and initializing data processing, we considered reformulating our research question due to encountering difficulties with dataset merging, which we will discuss in the processing step. However, we overcame the difficulty and are going to continue to address the research question we initially crafted: Is there a relationship between the number of building permits issued and the number of building violations recorded in a given neighborhood or year?

#### Acquire: Completed
We initially attempted to acquire the datasets from the Chicago data portal with the framework we have used in the data acquisition lab and homework, however, we ran into an API authorization error and researched and acquired the App Token required on the Chicago data portal. Seen in the jupyter notebooks also committed in github, we used varying methods the requests library and also the sodapy library with Socrata that processes the API on the Chicago data portal. We successfully retrieved the datasets.

#### Process: In Progress
After data retrieval, we really had to consider what features were, firstly, feasible to attain from the datasets just because of the fact that there were not many convenient features to merge the datasets on. Secondly, we also had to consider what features we thought would be most logical to focus on in order to address our research question. We decided to centralize our focus onto “STREET_NAME” and  “ISSUE_DATE” in the building permits dataset and “street name” and “violation date” in the building violations dataset. Trying to figure out how to determine how to group the rows of each dataset by neighborhood (because zipcodes weren’t a column in both datasets), we settled on using streets to group the data for now. After, we standardized the columns to be lowercase. In order to merge the datasets, we split the street name from street type in the permits dataset to align with the format of street names in the violations dataset.

#### Analyze: In Progress
To analyze the data, we grouped permit issuances and violations by year then generated correlation matrices to see the relationship between the number of permits issued in a year and the number of violations committed that year. On top of that, we compared the number of violations recorded on a street compared to another street to identify possible problem areas, and also the number of permits issued on that street. The top violating streets were identified, and the top permit issued streets were identified as well. All analysis is done in Python with the pandas library and the libraries mentioned above. Matplotlib.pyplots is used to generate the visualizations so far, as well as seaborn. Future analysis may include grouping by ranges of longitude and latitude coordinates to get a different grouping and representation of what a “neighborhood” is. On top of that, we are considering doing spatial trend visualization by community area and performing more correlation analysis with other potential features we may want to engineer. 

#### Preserve: 
Ways we are preparing our data, analysis, and project for preservation are making sure we commit our work to GitHub and also using accessible and popular methods of data collection and analysis. This includes using popular Python libraries, labeling our project iterations in our Jupyter notebooks, and using common and stable file formats (.csv, .txt, .ipynb), and using the GitHub repository. 

We have a summary of the data we’re using in the project plan, which includes provenance, and we plan to create a data dictionary when we determine all of the columns and rows we need for our analysis. 

#### Publish/Share
Because we are not done with the analysis and fully answering our research question, the project is not ready for publication or sharing. However, we have discussed our work with other peers in our class and have been transparent with our findings and processes. Publication and or sharing will not be executed until visualizations, statistics, and a proper explanation for each iteration of our analysis are complete. Right now, we have two separate Jupyter notebooks for cleaning and merging the data, as we tested using different methods, but for the final report, these will be consolidated into a single notebook to ensure that it is clear and easy to understand for others.

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
Based on the feedback given for our project plan, we created a tag for easy navigation in our repository to reach the project plan and created a new tag for our status report. 

We also clarified our division of responsibilities to make individual roles more defined and aligned with the evaluation criteria. Sophia led the technical development, including data integration and analysis, while Samantha focused on documentation and quality management. Throughout the process, we both reviewed each other’s work and provided assistance where needed to maintain accuracy. To ensure the reproducibility of the analysis, Samantha will be documenting all of our work, and Sophia will be formatting the analysis clearly. Both people hold each other accountable to make the project transparent by consistently noting, mentioning, and recording their contributions. As discussed in previous sections above, the analysis of data and data collection and processing may branch to observe and draw insight from geographic trends, possibly in order to address the neighborhood element of our research question, which is still in progress of being finalized. 

# Team Member Contributions
**Sophia Chen**
Sophia led the technical development of the project, completing the majority of the data integration, cleaning, and preprocessing work. She wrote the API retrieval and process code based on the dataset and API research conducted by Samantha, structured the merging logic, created the idea of parsing street names, and produced the initial visualizations that were later built upon. All of Sophia’s coding analysis is documented in the status_report.ipynb notebook in the GitHub repository. She also organized the repository structure and drafted the initial outline for this status report that the team ended up following.

**Samantha Mean**
Samantha identified data acquisition methods with sodapy library in Python by researching Sodapy and the Chicago data portal website. They both conversed and agreed upon methods of merging the dataset and which features to focus on for our initial analysis. She followed up on Sophia’s initiation of data processing and analysis with the generation of correlation matrices found in the data_analysis.ipynb file in GitHub and attempted a new process of merging and data acquisition compared to Sophia to explore more ways of data analysis. As documentor of the project, Samantha wrote the status report portion based on some bullet points Sophia laid out for her to explicate further. 
