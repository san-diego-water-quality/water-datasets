##
## Bulid and load Metatab data packages
## for comments and course-enrollments
##

.PHONY: sync packages default init 
default: packages ;


SOURCE_PACKAGE_NAMES=\
ceden.waterboards.ca.gov-beachwatch-sandiego \
ceden.waterboards.ca.gov-tmdl-sandiego \
census.gov-counties-2017 \
census.gov-tracts-2017-sandiego \
noaa.gov-localclimate-200808_201807-san \
tidesandcurrents.noaa.gov-water_levels-la_jolla \
usngcenter.org-usng-ca11 \
waterservices.usgs.gov-stream_discharge-fashion_valley_sd 


SOURCE_PACKAGES = $(patsubst %,packages/%.zip,$(SOURCE_PACKAGE_NAMES))

PACK_DIR=packages
DOC_DIR=documentation

init:
	mkdir -p $(PACK_DIR)

##
## Load Eagle Apps Targets
##

# Build a package file in the packages
# directory
packages/%.zip: init  %/metadata.csv
	@echo ======== BUILD $* \( $@ \) =======
	mp --exceptions build -f -z -n $* -D $(PACK_DIR)
	mp index $(PACK_DIR)
	@echo ======== FINISHED BUILDING $* =======


# Make a package, using the packages'
# non-versioned names
$(SOURCE_PACKAGE_NAMES): %:packages/%.zip ; 

# Make all packages 

packages: $(SOURCE_PACKAGES) ;
