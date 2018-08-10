
NS = sandiegodata.org
VERSION = latest

REPO = water-datasets
NAME = water-datasets
INSTANCE = default
DOCKER ?= docker



VOLUMES=  -v datapackages:/opt/datapackages

.PHONY: build push shell run start stop restart reload rm rmf release

build:
	$(DOCKER) build -t $(NS)/$(REPO):$(VERSION) .


shell:
	$(DOCKER) run --rm -i -t $(PORTS) $(VOLUMES) $(ENV) $(NS)/$(REPO):$(VERSION) /bin/bash

attach:
	$(DOCKER) exec  -ti $(NAME) /bin/bash

run:
	$(DOCKER) run --rm --name $(NAME) $(PORTS) $(VOLUMES) $(ENV) $(NS)/$(REPO):$(VERSION)

logs:
	$(DOCKER) logs -f $(NAME) 


rmf:
	$(DOCKER) rm -f $(NAME)

rm:
	$(DOCKER) rm $(NAME)

release: build
	make push -e VERSION=$(VERSION)

default: build