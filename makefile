# Microservices Project Make File
# author: Andrius Čekanauskas

VIRTUALENV = $(shell which virtualenv)

clean: shutdown
	rm -fr microservices.egg-info
	rm -fr venv

venv:
	$(VIRTUALENV) venv

install: clean venv
	. venv/bin/activate; python setup.py install
	. venv/bin/activate; python setup.py develop

launch: venv shutdown
	. venv/bin/activate; python  services/fibonaci.py

shutdown:
	ps -ef | grep "services/fibonaci.py" | grep -v grep | awk '{print $$2}' | xargs kill

