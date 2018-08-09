# Beachwatch Data, with Enhanced Features




# Elided Columns

This datasets excludes the const and empty columns from the source dataset.
These columns and their values are:


    program                      BeachWatch
    parentproject                BeachWatch_San Diego County
    project                      BeachWatch_San Diego County
    locationcode                 SurfZone
    collectiondepth              -88
    unitcollectiondepth          NR
    sampletypecode               Grab
    collectionreplicate          1
    resultsreplicate             1
    labsampleid                  Not Recorded
    matrixname                   samplewater
    mdl                          -88
    rl                           -88
    batchverification            NR
    compliancecode               NR
    eventcode                    WQ
    protocolcode                 Not Recorded
    collectionmethodname         Water_Grab
    collectiondevicedescription  Not Recorded
    calibrationdate              0000-00-00
    positionwatercolumn          Not Recorded
    preppreservationname         Not Recorded
    preppreservationdate         0000-00-00 00:00:00
    digestextractmethod          Not Recorded
    digestextractdate            0000-00-00
    analysisdate                 0000-00-00
    dilutionfactor               -88
    expectedvalue                0
    submissioncode               NR
    county                       San Diego
    county_fips                  73
    regional_board               San Diego
    rb_number                    9
    sampleid                     Not Recorded

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
    
    

