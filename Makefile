

TOPTARGETS := clean build clean-build s3 clean-s3 ckan clean-ckan info

SUBDIRS := source derived

$(TOPTARGETS): $(SUBDIRS)

$(SUBDIRS):
	$(MAKE) -C $@ $(MAKECMDGOALS)

.PHONY: $(TOPTARGETS) $(SUBDIRS)
	
install:
	pip install -r requirements.txt
	
index:
	mp index source
	mp index derived
