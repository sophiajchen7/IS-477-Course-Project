# Chicago Building Permits & Violations: A Data Integration and Trend Analysis

## Contributors

- Sophia Chen
- Samantha Mean

## Summary 
It’s important for urban environments to have compliant building safety practices and continuous monitoring from the city. However, building activities and building violations are often reported through different systems which make it difficult to understand how these activities relate across neighborhoods. In this project, we take a look at the relationship between Chicago building permits and Chicago building violations by integrating two large public datasets from the Chicago Data Portal. This was our research question that guided the decisions we made throughout this project: Is there a relationship between the number of building permits issued and the number of building violations recorded in a given neighborhood or year?

This project was completed as part of the IS 477 course on Data Management, Curation, and Reproducibility, where we followed the USGS Data Lifecycle from data acquisition through results dissemination. The workflow includes data acquisition by an API endpoint link to gain authorization to query the datasets’ data in our Python Jupyter Notebook, data cleaning and preprocessing by narrowing our datasets to year and location columns as well as feature engineering a community_area column to then integrate the data by merging the datasets and grouping by area and year, data visualization of with the columns to understand the correlation and relationship between year, permit issuances, violations, and community areas, and finally enabling workflow reproducibility by automating of the workflow in a shell script file. 

The datasets were acquired from the Chicago Data Portal by their API endpoint links via Python then cleaned and preprocessed extensively due to the lack of a shared unique identifier. The datasets were then narrowed down to “year” and “community_area” columns to focus on the research question. Initially, community_area was determined by “street_name” which was a limitation we documented, but still provided for meaningful analysis at an aggregated level. Later into the project, we used the geopandas library in Python and the “Boundaries - Community Areas” Chicago Data Portal dataset to group the permits and violations datasets by community areas defined by the Chicago Data Portal which provided for an accurate analysis of community area violations and permit issuances in Chicago.

After integration, we conducted exploratory visualizations to examine trends and relationships. We observed that the number of violations has overall gone down across community areas from 2006 to 2025, permit issues have increased exponentially beginning around 2023, and that there is little to no relationship between violations and permit issuances based on our visualizations explained later in our Findings section. 

To ensure full reproducibility, we created a Run-All shell script that executes the entire workflow from start to finish. Instead of manually running each Python script like we did when building this project, the Run-All script automatically performs our data acquisition, integrity check, cleaning and preprocessing, merging, and analysis code that we did throughout the course of our project execution. With the Run-All shell script file, others may fully reproduce our project in a single command with all required dependencies (libraries, etc.) installed. 

Below is the full documentation of all processes, findings, and forward thinking done in this data science workflow. By integrating the building violations, building permits, and community areas datasets from the Chicago Data Portal, we were able to identify that the permit issuance process is not directly correlated with violations in the context of year and community area in Chicago between 2006 and 2025.

## Data Profile

### Chicago Building Permits Dataset
Source: City of Chicago Data Portal<br>
Access Method: API endpoint JSON link 

The building permits dataset is a large and frequently updated dataset open data resource that is published by the City of Chicago that contains detailed records of construction activity across the city. Because it is released under a permissive open-data license and contains only building level information and not personal identifiers, it is ethically appropriate for us to use for public analysis. To address our research question, we used “ISSUE_DATE”, “STREET_NAME”, “LONGITUDE”, and “LATITUDE” columns in our data analysis. “ISSUE_DATE” was used to extract the years of the permit issuances to allow us to merge the violation records and permit issuance data then aggregate by year. “STREET_NAME” was used in our initial exploratory data analysis to aggregate the records somewhat geographically to see possible trends by street name. “LONGITUDE” and “LATITUDE” allowed us to use the geopandas library to then truly group the records by community area given the data in the “Boundaries - Community Areas” dataset explained below. There was a lot of information in this dataset and in the end, we kept only the attributes necessary for our analysis to ensure that the data set was both manageable and analytically focused for our objectives. In the initial exploratory data analysis, the dataset was accessed with Socrata from the sodapy library in Python and its unique Socrata identifier to query the dataset. For the final dataset usage, we used the API endpoint JSON link and the requests and pathlib Python libraries to acquire the dataset and download the csv locally. As a forewarning, the files were very large, so the shell script provided for someone to reproduce the project may take minutes to complete running. 

### Chicago Building Violations Dataset
Source: City of Chicago Data Portal<br>
Access Method: API endpoint JSON link 

The building violations dataset is significantly larger than the permits dataset and contains records of code enforcement issued throughout Chicago. Like the permits dataset, the violations dataset contains no personally identifying information and is published under an open-data license, making it ethically suitable for us to analyze. Several key attributes were especially important for our project. To address our research question, we used “VIOLATION DATE”, “STREET NAME”, “LONGITUDE” and “LATITUDE” columns in our data analysis. “VIOLATION DATE” was used to extract the year of each violation record to then merge with the permits dataset then group the records by year. “STREET NAME” was used during the initial exploratory data analysis to group the records in an attempt to group the records geographically so we could see if there were any trends across streets. “LONGITUDE” and”LATITUDE” allowed us to use the geopandas library to then truly group the records by community area given the data in the “Boundaries - Community Areas” dataset explained below. There was a lot of information in this dataset, but the features focused on were narrowed down to these couple of columns in order to answer the research question. By focusing on these specific fields, we were able to explore and identify specific patterns and trends related to building violations and permit issuances by year and neighborhood. Analysis on these focused columns allowed us to provide a foundational analysis for future analysis to be done on why the trends we found were the way they were. This data was accessed with its unique Socrata identifier and the sodapy Python library in the initial exploratory data analysis. For the final dataset usage, we used the API endpoint JSON link and the requests and pathlib Python libraries to acquire the dataset and download the csv locally. As a forewarning, the files were very large, so the shell script provided for someone to reproduce the project may take minutes to complete running. 


### Chicago Boundaries - Community Areas
Source: City of Chicago Data Portal<br>
Access Method: API endpoint JSON link 

This dataset provides the official geographic boundaries for the 77 designated community areas in the City of Chicago. Like the others, this dataset is publicly available, maintained by the City, and released under open-data access for public use. Its main attribute is a uniquely assigned community area number, which corresponds to each community area’s name and boundaries. The dataset includes polygon geometry describing the exact spatial boundaries of each community area. Using this dataset, we can map our permit and violation data into a visual. Because these community area boundaries seldom change, this dataset is good for our longitudinal comparisons across years without boundary-induced mistakes. In order to group the building permits and violations by the community areas the Chicago data portal defined, we use the “community” and  “area_numbe” columns in our data analysis. With these columns, we were able to join the permits and violations datasets with the community area dataset then group by the community areas given the longitude and latitudes of the record. This dataset greatly allowed to address the “neighborhood” aspect of our research question. 

### Integration Strategy
The permits and violations datasets do not share a common unique identifier, such as a building ID, yet we needed a reproducible way to combine them at a geographic level. Early in the project, we took a look at joining records by normalized street names, but this approach was not precise and prone to inconsistency. Our final integration strategy relied on geographic enrichment using the Chicago Community Areas dataset. For both permits and violations, we used latitude and longitude to convert each record into a GeoDataFrame and then performed a spatial join with the official community area boundary polygons to assign every record a community_area value. This made sure that each permit and violation was matched to one of Chicago’s stable geographic regions rather than relying on unreliable textual address fields. After community areas were assigned, we were able to extract the year from each record’s date field and aggregate counts of permits and violations by community_area and year. These summarized tables were then merged on their shared keys to create the final integrated analytical dataset used throughout our visualizations and findings. This combination provided an accurate, reproducible foundation for comparing activity across Chicago neighborhoods.

### Data Storage & Organization 
Our project is organized into a few main folders to keep everything clear and easy to find. The data folder contains a raw and processed folder. The raw folder contains the original files downloaded from the Chicago Data Portal. The processed folder holds the cleaned and transformed datasets, including the versions where each permit and violation has been assigned to a community area and the final merged table we used for analysis.

All graphs and visualizations created during the analysis step are saved in the results folder. We use simple, descriptive names for each file so it’s easy to understand what stage it belongs to and what it contains.

Because some of our data files are large, we also uploaded both the raw and processed datasets and all visualizations to a shared [Box folder](https://uofi.box.com/s/62z68mdfykj67as9al2aukour3vqq30e). This helps anyone running our project see the file sizes before downloading and avoids storage issues on devices with limited storage, while most people can still regenerate everything automatically using our run-all script.

## Data quality 

### Completeness
For the purposes of our project, the datasets we used contained all of the columns we needed to address our research question. All records had values for the columns we were focused on. Some street names were missing or inconsistent, but these were normalized or excluded. The permits dataset includes all permit issuances even if it has been suspended, revoked, or cancelled after issuance. 

### Consistency
To prepare for integration, we converted all street names to uppercase and stripped whitespace and standardized data formats. Violations and permits records were both aggregated at the year level to avoid granularity mismatches. No standardized procedure is provided for the inputting of the permit issuance and violations data nor permit granting process and violation definition process. However, codes and types are briefly explained in the column descriptions.

### Accuracy
For the most part, all datasets used for this data analysis are accurate. There are inconsistent street naming conventions for the permits and violations datasets and some placeholding values. The permits dataset “ISSUE_DATE” represents “For most permit types, date when City determined permit was ready to issue subject to payment of permit fees; For Express Permit Program, date when permit issued based on full payment of applicable permit fee” (Chicago Data Portal).

### Timeliness
The permits and violations datasets are updated daily and are dated from 2006 to present. Because our analysis uses year-level aggregations, small reporting delays do not significantly affect our results, but a disclaimer for users to be aware that the datasets may not reflect real-time activity is provided. Our results pull a snapshot in time through the API, so our results may differ from future runs if new records are added after or project submission but the checksum provides the integrity check of our data being the exact set it is we used for the duration of our project.

### Limitations
Joining on street names results in a many-to-many join with possible over-counting, however, we move on from this method of grouping records to doing a much more reliable and accurate geopandas grouping of records with defined community areas. 

## Findings
In our initial exploratory data analysis, we found that grouping by street name provided way too granular grouping of permit issuances and violations. While we developed visualizations on total permits and violations by street (seen in the “status_report.ipynb” file in the notebooks folder), these results and groupings don’t really help at all in answering our research question. 
From looking at our final data visualizations from doing the proper grouping of records with the community area dataset, we found that, ultimately, there is a near to none relationship between building permit issuances and building violations in Chicago with a 0.051 correlation. However, when looking at the correlation matrix, we observed a small positive correlation of 0.2 between year and permit issuance. In the line plot of permit issuances by community area over time, we see that permit issuances actually decrease in the top ten community areas for permit issuance which may indicate that other areas that had less permit issuances are beginning to develop more, industrially and socioeconomically, and require for more permit issuances. In the correlation matrix, we also observed a moderate negative correlation of -0.34 between year and violation frequency. This correlation can be seen in the line plot of violation frequency by community area over time. This line plot also shows how the year 2020 was a year with exceptionally low violations which could most logically be explained by the global COVID-19 pandemic, but it may also mean that some development in building violation evaluation or inspection because the frequency of violations stayed fairly level in the subsequent years. 
Decrease in building violation frequency can also be seen in the box plots of violations by year. Outliers max from around 11,500 violations in 2006 to around 8,000 in 2016 to only around 3,800 in 2025 so far. A final proof of a collective decrease in building violations can be given by the heatmap of violation frequency by community area over time. 

The increase in building permits could be attributed to construction and industrial expansion or population growth, a faster permit issuance process, or even economic growth and infrastructure investment.  

Based on the geographic distribution of violations and permits in the community areas visualization, we observe that building violations are highly frequent in the west and south side of Chicago. These areas may experience higher inspection frequency, ageing structures, or socioeconomic barriers to properly maintaining their buildings. Conversely, building permit issuances are highly frequent in the North side which can indicate more redevelopment, investment, and construction in that area. The combination of these visualizations can conclude that building permits and violations reflect different dynamics in Chicago’ s urban landscape. 
Overall, permit and violation frequency are not correlated, but if observed over time and across community areas in Chicago separately, significant insight on the development and state of Chicago is drawn through our data analysis.

## Future work 
One of the most valuable improvements we could make to this project involves strengthening reproducibility and long-term accessibility. A next step would be packaging the entire workflow into a Docker container. Right now, users must install Python, set up a virtual environment, and ensure that their dependencies match ours. This can create inconsistencies across machines and operating systems. By containerizing the workflow with Docker, every user would run the project inside the exact same environment, with the same Python version, library versions, and system configuration. This would eliminate setup issues and make the project fully portable, ensuring that the workflow behaves identically regardless of whether someone is using macOS, Windows, or Linux. Minimizing the size of the dataset only what was necessary too first with Socrata then downloading locally would also increase the portability of the workflow. 

Another important improvement would be publishing our cleaned datasets, results, and code to an archival repository such as Zenodo. Zenodo would assign a permanent DOI (digital object identifier), which allows our work to be formally cited and preserved long-term. This would support FAIR principles by making the project findable, accessible, interoperable, and reusable beyond the scope of this course. Using a DOI also provides version control for future updates and ensures that anyone referencing our project is accessing a stable, publicly available snapshot of the work.

A final way future scientists, analysts, or researchers may expand upon our project is by exploring the results described in our findings. Many conclusions I drew based on the findings of the analysis are ideas or assumptions and can definitely be verified or rebuttalled with additional contextual information and research done on things like the socioeconomic environment of the community areas or the construction developments and policy changes of Chicago. Even things like natural disasters that happened or major happenings that could have happened within a city or community that may further explain why violation frequency or permit issuance was high, low, or stagnant for certain community areas or years. Doing this analysis with a team to research the context of these statistics would greatly build upon our foundational data analysis and more data analysis can spawn through a deeper dive on some of the findings we had for this project. 

Overall, our project is already strong and fully functional, but these enhancements would make it even more reproducible and accessible for future users.

## Reproducing
This section provides all instructions and information needed to fully reproduce our project from start to finish. It includes how to acquire the data, verify integrity, install dependencies, run the automated workflow, and locate all outputs.

### 1. Clone the Repository
git clone https://github.com/sophiajchen7/IS-477-Course-Project.git<br>
cd IS-477-Course-Project

This will create the full project directory on your machine, including the scripts, data, and results folders.

### 2. Set Up the Environment (Required Before Running Anything)
All dependencies are listed in **requirements.txt** 

To install them, first create a virtual environment:

**macOS/Linux:**

python3 -m venv venv<br>
source venv/bin/activate<br>
pip install -r requirements.txt

**Windows (PowerShell):**

python -m venv venv<br>
venv\Scripts\Activate.ps1<br>
pip install -r requirements.txt

### 3. Optional: Using the [Box Folder](https://uofi.box.com/s/62z68mdfykj67as9al2aukour3vqq30e)
We provide a Box folder containing our original raw datasets, processed datasets, and final visualizations. These files are only needed if your computer has limited storage or if the run_all.sh workflow cannot complete successfully.

The recommended method is to run the full workflow using our run_all script (Step 4), which automatically downloads and recreates everything.

If you choose to download files manually, place them as follows:
- Raw files → data/raw/
- Processed files → data/processed/
- Plots → results/plots/

We still include the Box folder for convenience, but most users will not need it.

### 4. Running the Automated Workflow
Our project includes a Run-All script that performs every step of the analysis pipeline in the correct order:
- Data acquisition
- Checksum validation
- Cleaning and preprocessing
- Spatial joins with community areas
- Integration and aggregation
- Full analysis and visualization generation

**macOS/Linux:**

chmod +x run_all.sh<br>
./run_all.sh

**Windows (PowerShell):**

bash run_all.sh

Running this script will internally call:
1. acquire_data.py
    - Downloads permits and violations dataset
    - Saves as raw CSVs
2. check_integrity.py
    - Computes checksums for the two raw files
3. clean_data.py
    - Cleans permits and violations
    - Loads community area boundaries directly via GeoJSON request
4. merge_data.py
    - Performs spatial joins with community areas
    - Aggregates counts by year and neighborhood
5. analyze.py
    - Generates visualizations and stores them in the results folder

No additional user interaction is required.

### 5. Expected Outputs
Raw Folder Contains:
- permits.csv
- violations.csv

Processed Folder Contains:
- permits_with_ca.csv
- violations_with_ca.csv
- merged_counts.csv

Results Folder Contains:
- Heatmaps
- Line charts
- Boxplots
- Side-by-side maps
- Correlation visuals

### 6. Notes on Reproducibility
- The Box folder preserves the exact data snapshot used during our project.
- All scripts reference directory paths consistently so the workflow runs the same way on any machine.

## References 
City of Chicago | Data Portal | City of Chicago | Data Portal. (n.d.). Chicago.<br>
    https://data.cityofchicago.org 

Socrata Developers | Socrata. (2018). Socrata.com.<br>
    https://dev.socrata.com 
