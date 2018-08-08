# Beachwatch Data, with Enhanced Features




# Elided Columns

This datasets excludes the const and empty columns from the source dataset.
These columns and their values are:


|    | Column Name                 | Constant Value              |
|---:|:----------------------------|:----------------------------|
|  0 | program                     | BeachWatch                  |
|  1 | parentproject               | BeachWatch_San Diego County |
|  2 | project                     | BeachWatch_San Diego County |
|  3 | locationcode                | SurfZone                    |
|  4 | collectiondepth             | -88                         |
|  5 | unitcollectiondepth         | NR                          |
|  6 | sampletypecode              | Grab                        |
|  7 | collectionreplicate         | 1                           |
|  8 | resultsreplicate            | 1                           |
|  9 | labsampleid                 | Not Recorded                |
| 10 | matrixname                  | samplewater                 |
| 11 | mdl                         | -88                         |
| 12 | rl                          | -88                         |
| 13 | batchverification           | NR                          |
| 14 | compliancecode              | NR                          |
| 15 | eventcode                   | WQ                          |
| 16 | protocolcode                | Not Recorded                |
| 17 | collectionmethodname        | Water_Grab                  |
| 18 | collectiondevicedescription | Not Recorded                |
| 19 | calibrationdate             | 0000-00-00                  |
| 20 | positionwatercolumn         | Not Recorded                |
| 21 | preppreservationname        | Not Recorded                |
| 22 | preppreservationdate        | 0000-00-00 00:00:00         |
| 23 | digestextractmethod         | Not Recorded                |
| 24 | digestextractdate           | 0000-00-00                  |
| 25 | analysisdate                | 0000-00-00                  |
| 26 | dilutionfactor              | -88                         |
| 27 | expectedvalue               | 0                           |
| 28 | submissioncode              | NR                          |
| 29 | county                      | San Diego                   |
| 30 | county_fips                 | 73                          |
| 31 | regional_board              | San Diego                   |
| 32 | rb_number                   | 9                           |
| 33 | sampleid                    | Not Recorded                |

The dataset also excludes these Null columns:

* observation
* samplecomments
* collectioncomments
* resultscomments
* batchcomments
* groupsamples
* occupationmethod
* startingbank
* distancefrombank
* unitdistancefrombank
* streamwidth
* unitstreamwidth
* stationwaterdepth
* unitstationwaterdepth
* hydromod
* hydromodloc
* locationdetailwqcomments
* channelwidth
* upstreamlength
* downstreamlength
* totalreach
* locationdetailbacomments
* huc8
* huc8_number
* huc10
* huc10_number
* huc12
* huc12_number
* waterbody_type


# Notes


The most prevalent measure code in this dataset is 24 for Enterococcus (analyte) meaured with Enterolert (methodname) in units of MPN/100 mL. This is probably because in 2004, the [EPA changed recomendations to use Enterococcus as a primary indicator bacteria in coastal waters:](https://www.federalregister.gov/documents/2004/11/16/04-25303/water-quality-standards-for-coastal-and-great-lakes-recreation-waters)

    EPA subsequently recommended the use of E. coli or enterococci for fresh
    recreational waters and enterococci for marine recreational waters because
    levels of these organisms more accurately predict acute gastrointestinal
    illness than levels of fecal coliforms.
    
    

