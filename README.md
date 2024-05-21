Motor_Vehicles_Insights
===============================

## Project architecture
![arquitecture_.png](images%2Farquitecture_.png)
## Objective
This repository contains the code for an end-to-end data pipeline.

The goals of the project are:

- develop end-to-end data pipeline that will help to organize data processing in a batch manner;
- develop dbt models to prepare data for the required analytical purposes;
- build analytical dashboard that will make it easy to discern the trends and digest the insights;
The period of the data processing will cover from 2020 to 2023.
### Dataset

The data is compination of three datasets:  
[The Motor Vehicle Collisions](https://data.cityofnewyork.us/Public-Safety/Motor-Vehicle-Collisions-Crashes/h9gi-nx95/about_data) dataset provides comprehensive information on traffic accidents occurring on city streets within New York City. Each entry in the dataset corresponds to a single collision event. The data includes reports from all police-recorded motor vehicle accidents throughout NYC.

To trigger a police report (MV104-AN), a collision must meet specific criteria: it involves injuries or fatalities, or results in property damage exceeding $1000.

[The Motor Vehicle Collisions - Vehicles](https://data.cityofnewyork.us/Public-Safety/Motor-Vehicle-Collisions-Vehicles/bm4k-52h4/about_data) dataset furnishes detailed records for each vehicle involved in a crash. Each entry represents a distinct motor vehicle participant.

Similarly, the [Motor Vehicle Collisions - Person](https://data.cityofnewyork.us/Public-Safety/Motor-Vehicle-Collisions-Person/f55k-p6yu) dataset presents information about individuals involved in accidents. Each record pertains to a person—be it a driver, passenger, pedestrian, cyclist, or other party—affected by a collision.


Problem description and purposes
===============================
The project is related Motor Vehicle Collisions in New York and is based on data from 3 datasets.

Need to analyze: what types of cars most often get into collisions, for what reasons collisions took place, at what time of the day accidents most often occur, the age and gender of the drivers involved in collisions.

### Mage(orchestration): 

The project utilizes Mage, an orchestration tool, for uploading data into PostgreSQL databases. Leveraging Mage's capabilities,seamlessly integrated a data loader mechanism, allowing for the efficient ingestion of data from external sources via links. This loader is designed to not only upload the data but also perform crucial tasks such as renaming columns and adjusting data types to ensure compatibility and consistency within the database. Once the data has been successfully loaded and refined, Mage facilitates the exporting process, directing the refined dataset to a specified PostgreSQL database, complete with predefined schema and dataset configurations. This orchestrated workflow ensures the integrity and reliability of the data pipeline, empowering seamless data management and analysis within PostgreSQL environment
![DAG.PNG](images%2FDAG.PNG)
### DBT  

In order to clean and transform the data and also create new tables so After uploading the data to postgres i used dbt (data build tool) for transforming the data stored in PostgreSQL.i crafted SQL queries within dbt to orchestrate the transformation of the data into structured and analyzable formats. constructed sophisticated data transformation pipelines that efficiently processed the data within PostgreSQL.  
The core tables are:
- `mvc_sum_2020, mvc_sum_2021, mvc_sum_2022`
- `crashes_per_hour`
  
### Dashboard: Metabase  
For creating the Dashboard Metabse was the choosen tool which can integrates easily with postgres to grap the data and by using the sql quiry feature in metabse to play with the data.  

![Dashboard_1.png](images%2FDashboard_1.png)
![Dashboard_2.png](images%2FDashboard_2.png)
