## Overview
The overall goal of this project is to identify, if one exists, between the number of building permits issued and the number of building violations recorded in a given neighborhood or year. By inspecting the relationship between building violations and building permit issuance, we may be able to identify trends in the terms of the permit issuance that may be attributed to building violations. Patterns in permit issuance conditions or status like it being expired, revoked, having unpaid fees, waived fees, type of violation, as well as what neighborhoods and years have similar trends in their violation and permit data on top of other factors may be telling of the inefficiencies or flaws that are in the building permit acquisition process. On the other hand, insight on common building violations may be inspected by this data processing and analysis project in general. Overall, this project is to bring insight to the building permitting process and to find possible correlations between permit status and building violations in the City of Chicago.
We decided to follow the US Geological Survey Data Lifecycle because of its straightforward and all-encompassing flow that’s conducive for the goals of this project. Rather than trying to continue a cycle using data in this project, we are trying to draw conclusions and gain new understanding by the utilization of the datasets we’ll be looking at. Therefore, the USGS Data Lifecycle is effective for our project because it is moving in one direction and not necessarily demanding to loop around again. We will be accessing the data with an API and performing analysis with Python pandas, seaborn, and matplotlib libraries. Analysis will be dealing heavily with correlations between data points and visualizations will be demonstrating such with a correlation matrix, line chart, and other applicable visualizations. Reporting and all project developments are for the purposes of informing building management for the City of Chicago with the aspiration of improving the building permit granting process, and minimizing building violations upon inspection.

## Research Question
Is there a relationship between the number of building permits issued and the number of violations recorded in a given neighborhood or year?

## Team
Samantha will be in charge of data acquisition coding, integration, and data cleaning. 
Sophia will be in charge of keeping us on track of documentation, reproducibility, and transparency.
Throughout the project, both Sophia and Samantha will be consistently holding each other accountable for ethical data handling, recording proper documentation, and ensuring security. Most, if not all, of the project requirements will be completed together. This includes data cleaning, workflow automation and provenance, data integration, reproducibility, and elements of the USGS Data Lifecycle like backup and security, managing quality, documentation, analysis, and publishing & sharing. 

## Datasets
1. [Building Permits from Chicago Data Portal](https://data.cityofchicago.org/d/ydr8-5enu)  
This dataset contains the details of all building permits within the City of Chicago. Each record includes information such as the permit number, issue date, permit type, address, latitude, longitude, and more. This dataset is important for us to understand patterns in construction activity and development in Chicago. The data is updated daily and covers data from 2006 to the present.

    We will use this building permits data set to quantify construction activity across communities and over time. It will also be good for identifying patterns in permit types and permit fees. Compared against the building violations data, we will be able to assess how new development or renovation trends relate to code compliance.

2. Building Violations from Chicago Data Portal
   (https://data.cityofchicago.org/Buildings/Building-Violations/22u3-xenr/about_data)
This dataset contains details of all building violations issued from 2006 to the present in the City of Chicago. The violations are always associated with an inspection. Each observation in the dataset is a single violation record, therefore, more than one observation can be associated with one inspection record. The dataset does not necessarily contain completely accurate representations of the current condition of the building and more for informational purposes. Features we will most likely extract for the purposes of this project are: 
- Violation ordinance
- Inspector ID
- Inspection category 
- Address
- Property group 
- Violation location
- Violation description
- Violation status
- Violation data
- id


## Timeline
<img width="700" height="250" alt="image" src="https://github.com/user-attachments/assets/1ead0bb1-601b-4f75-8550-ba22ec9584d3" />

Every step in the timeline will be done with an equal split between Sophia and Samantha.

#### Plan
- Finalize research question
- Identify datasets
- Take a look at ethical and data privacy considerations

#### Acquire
- Download both datasets either as CSV or through api
- Store data in organized folders

#### Process
- Clean missing values, standardize addresses
- Covenant dates and location fields into consistent formats
- Assess data quality

#### Analyze
- Integrate datasets by community area or address
- Compute metrics
- Perform exploratory data analysis
- Test for correlations between the datasets

#### Preserve
- Keep the repository structured with clear folder organizations
- Generate data dictionary

#### Publish/Share
- Write final report
- Finalize figures and visualizations
- Tag final release on GitHub

## Constraints
1. Missing Fields in Data: Some records have incomplete information, such as incomplete addresses or missing fees, which require cleaning and could affect certain analyses.
2. Challenge Matching Addresses: To integrate these datasets together, the addresses will need to be standardized, and handling abbreviations like “Street” vs “St.” is something that we may need to address.
3. Time Inconsistencies: Since our datasets have data that trace back to almost two decades ago, older records may be less comparable to recent ones as permitting policies and reporting standards could have changed over time.
4. Large Data Volume: Both datasets contain hundreds of thousands of entries which may slow down our processing and analysis if not properly filtered.
5. Geographic Precision: Some records lack the precise latitude and longitude coordinates which can make our spatial visualizations less accurate.

## Gaps
1. Dataset Merging: We have not yet determined how the datasets with be merged together, whether it is by census area or latitude and longitude. Each options has its trade offs in terms of accuracy and completeness.
2. Scope of Time Period: Because the data covers many years, the range of years for our analysis will depend on data volume and efficiency of data cleaning.
3. Permit Categorization: Additional reach will need to be done for us to classify and group together different permit types.
4. Quality Assessment Criteria: The specific criteria and metrics that we will be using for evaluating data quality will be determined once the data is loaded and explored.
5. Correlation and Causality: While relationships between permits and violations can be identified, it may be challenging for us to determine whether the high violation counts are caused by new development in the area or other socioeconomic factors.
