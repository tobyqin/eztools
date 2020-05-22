# Release Guide

There are 2 options to release package.

## Run `publish.py` on development computer

Ensure `.pypirc` was configured in user profile. 
The package version will come from `VERSION` file, by default the package version will be auto increased.

## Create a tag and push to github, e.g. `v1.0.0`

The tag must be started with `v` and follow semantic versioning. Once tag created and pushed, 
the `.github/workflows/release.yml`, check there for the detail implementation.
The package version will use your tag version.