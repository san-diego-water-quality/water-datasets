# Combined Water Project Datasets

This package combines three other datasets for use in the water quality data
ptoject:

    * waterservices.usgs.gov-stream_discharge-fashion_valley_sd
    * tidesandcurrents.noaa.gov-water_levels-la_jolla#water_levels
    * noaa.gov-localclimate-200808_201807-san#lcd-san

The resulting dataset has daily values for rainfall, flow rate for the San
Diego river, and the max and min tide level at La Jolla.


See the [EDA
Notebook](https://github.com/san-diego-water-quality/water-datasets/blob/master/
sandiegodata.org-water_quality/notebooks/eda-tides_river_rain.ipynb) for
details of the structure of the data, in particular, the time coverage in the
Nulls section.