##
## Bulid and load Metatab data packages
## for comments and course-enrollments
##


S3_BUCKET=library.metatab.org

PACKAGE_NAMES=\
ceden.waterboards.ca.gov-beachwatch-sandiego \
ceden.waterboards.ca.gov-tmdl-sandiego \
census.gov-counties-2017 \
census.gov-tracts-2017-sandiego \
noaa.gov-localclimate-200808_201807-san \
tidesandcurrents.noaa.gov-water_levels-la_jolla \
usngcenter.org-usng-ca11 \
waterservices.usgs.gov-stream_discharge-fashion_valley_sd 

# ---------

PACK_DIR=_build

.PHONY: $(PACK_DIR) clean packages s3 ckan list
	
default: packages ;
	
# List all of the targets
list:
	@$(MAKE) -pRrq -f $(lastword $(MAKEFILE_LIST)) : 2>/dev/null | awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$' | xargs
	
	

PACKAGE_MARKERS = $(patsubst %,$(PACK_DIR)/%.build,$(PACKAGE_NAMES))
S3_MARKERS = $(patsubst %,$(PACK_DIR)/%.s3,$(PACKAGE_NAMES))
CKAN_MARKERS = $(patsubst %,$(PACK_DIR)/%.ckan,$(PACKAGE_NAMES))

$(PACK_DIR):
	mkdir -p $(PACK_DIR)

# For the first build, when the last_build file doesn't yet exist. 
# I really don't understand make. 
%/_packages/last_build : $(PACK_DIR)
	@echo ======== BUILD $* from $* =======
	mp --exceptions build -f -z $* && touch $(PACK_DIR)/$*.build
	mp index $*

# Build a package file in the packages
# directory
$(PACK_DIR)/%.build :  %/metadata.csv
	@echo ======== BUILD $* from $* =======
	cd  $* && mp --exceptions build -f -z && cd .. && touch $(PACK_DIR)/$*.build
	mp index $* 	
	
$(PACK_DIR)/%.s3: $(PACK_DIR)/%.build
	@echo ======== S3 $* \( $@ \) =======
	mp s3 -s $(S3_BUCKET) $*  && touch $(PACK_DIR)/$*.s3
	touch -r $(PACK_DIR)/$*.build $*/metadata.csv # mp s3 updates the metadata, but we don't want to re-trigger build
	
$(PACK_DIR)/%.ckan: $(PACK_DIR)/%.s3
	@echo ======== CKAN $* \( $@ \) =======
	mp ckan  $* && touch $(PACK_DIR)/$*.ckan 
	touch -r $(PACK_DIR)/$*.build $*/metadata.csv # mp ckan updates the metadata, but we don't want to re-trigger build


# Make a package, using the packages'
# non-versioned names
$(PACKAGE_NAMES): %:$(PACK_DIR)/%.build ; 

# Make all packages 

clean: 
	echo

packages: $(PACKAGE_MARKERS) ;

s3: $(S3_MARKERS) ;
	
ckan: $(CKAN_MARKERS) ;
