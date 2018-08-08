##
## Bulid and load Metatab data packages
## for comments and course-enrollments
##

.PHONY: sync packages default init 
default: packages ;


PACK_DIR=_build


PACKAGE_NAMES=\
sandiegodata.org-water_quality


PACKAGE_MARKERS = $(patsubst %,$(PACK_DIR)/%.build,$(PACKAGE_NAMES))
S3_MARKERS = $(patsubst %,$(PACK_DIR)/%.s3,$(PACKAGE_NAMES))
CKAN_MARKERS = $(patsubst %,$(PACK_DIR)/%.ckan,$(PACKAGE_NAMES))

$(PACK_DIR):
	mkdir -p $(PACK_DIR)


# Build a package file in the packages
# directory
$(PACK_DIR)/%.build :  $(PACK_DIR) %/_packages/last_build
	@echo ======== BUILD $* from $* =======
	mp --exceptions build -f -z $* && touch $(PACK_DIR)/$*.build
	mp index $* 	
	@echo ======== FINISHED BUILDING $* =======

$(PACK_DIR)/%.s3: $(PACK_DIR)/%.build
	@echo ======== S3 $* \( $@ \) =======
	mp s3 -s $(S3_BUCKET) $*  && touch $(PACK_DIR)/$*.s3
	
$(PACK_DIR)/%.ckan: $(PACK_DIR)/%.s3
	@echo ======== CKAN $* \( $@ \) =======
	mp s3 -s $(S3_BUCKET) $*  && touch $(PACK_DIR)/$*.ckan
	

# Make a package, using the packages'
# non-versioned names
$(PACKAGE_NAMES): %:$(PACK_DIR)/%.build ; 

# Make all packages 

packages: $(PACKAGE_MARKERS) ;

s3: $(S3_MARKERS) ;
	
ckan: $(CKAN_MARKERS) ;
