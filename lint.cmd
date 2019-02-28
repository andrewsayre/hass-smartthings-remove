@echo off
pip install isort --quiet
isort hass_smartthings_remove --recursive
pip install -r test-requirements.txt --quiet
pylint hass_smartthings_remove
flake8 hass_smartthings_remove
pydocstyle hass_smartthings_remove