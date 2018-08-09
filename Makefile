

TOPTARGETS := clean build clean-build s3 clean-s3 ckan clean-ckan

SUBDIRS := source derived

$(TOPTARGETS): $(SUBDIRS)

$(SUBDIRS):
	$(MAKE) -C $@ $(MAKECMDGOALS)

.PHONY: $(TOPTARGETS) $(SUBDIRS)