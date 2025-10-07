## Overview
The overall goal of this project is to identify, if one exists, between the number of building permits issued and the number of building violations recorded in a given neighborhood or year. By inspecting the relationship between building violations and building permit issuance, we may be able to identify trends in the terms of the permit issuance that may be attributed to building violations. Patterns in permit issuance conditions or status like it being expired, revoked, having unpaid fees, waived fees, type of violation, as well as what neighborhoods and years have similar trends in their violation and permit data on top of other factors may be tellin

## Research Question(s)
Is there a relationship between the number of building permits issued and the number of violations recorded in a given neighborhood or year?

## Team
Samantha will be in charge of data acquisition coding, integration, and data cleaning. Throughout the project, both Sophia and Samantha will be consistently holding each other accountable for ethical data handling, recording proper documentation, and ensuring security. Most, if not all, of the project requirements will be completed together .

## Datasets
1. [Building Permits from Chicago Data Portal](https://data.cityofchicago.org/d/ydr8-5enu)  
This dataset contains the details of all building permits within the City of Chicago. Each record includes information such as the permit number, issue date, permit type, address, latitude, longitude, and more. This dataset is important for use to understand patterns in construction activity and development in Chicago. The data is updated daily and covers data from 2006 to the present.

    We will use this building permits data set to quantify construction activity across communities and over times. It will also be good for identifying patterns in permit types and permit fees. Compared agains the building violaitons data we will be able to assess how new development or renovation trends relate to code compliance.

2. Building Violations from Chicago Data Portal

## Timeline
Document the plan and timeline for implementing your project including who will complete each task.
<img width="700" height="250" alt="image" src="https://github.com/user-attachments/assets/1ead0bb1-601b-4f75-8550-ba22ec9584d3" />

## Constraints
1. Missing Fields in Data: Some records have incomplete information such as incomplete addresses or missing fees which requires cleaning and could imit certain analyses.
2. Challenge Matching Addresses: To integrate these datasets together, the addresses will need to be standardized and handling abbreviations like “Street” vs “St.” is something that we may need to address.
3. Time Inconsistencies: Since our datasets have data that trace back to almost two decades ago, older records may be less comparable to recents ones as permitting policiesa dn reporting standards could have changed over time.

## Gaps
1. Dataset Merging: We have not yet determined how the datasets with be merged together, whether it is by census area or latitude and longitude. Each options has its trade offs in terms of accuracy and completeness.
2. Scope of Time Period: Because the data covers many years, the range of years for our analysis will depend on data volume and efficiency of data cleaning.
3. Permit Categorization: Additional reach will need to be done for us to classify and group together different permit types.
