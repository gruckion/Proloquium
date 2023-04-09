# Makefile

# Stops Makefile echoing recipes unless in debug mode.
DBG_MAKEFILE ?=
ifeq ($(DBG_MAKEFILE),1)
	$(warning ***** starting Makefile for goal(s) "$(MAKECMDGOALS)")
	$(warning ***** $(shell date))
else
	# If we're not debugging the Makefile, don't echo recipes.
	MAKEFLAGS += -s
endif

# It's necessary to set this because some environments don't link sh -> bash.
SHELL := /usr/bin/env bash -o errexit -o pipefail -o nounset
BASH_ENV := ./hack/lib/logging.sh

# Define variables
SCRIPTS_DIR := scripts
SCRIPTS := run
# Sets help as the default target
default: help

# Define phony targets
.PHONY: help $(SCRIPTS)

# Define help target
help:
	@echo "Usage: make <target>"
	@echo ""
	@echo "Targets:"
	@echo " help Show this help message"
	@echo " run: Build and Run the application and its dependencies."


# Define individual script targets
.PHONY: $(SCRIPTS)
$(SCRIPTS):
	@echo "Running script: $@.sh"
	chmod +x ./$(SCRIPTS_DIR)/$@.sh
	./$(SCRIPTS_DIR)/$@.sh
