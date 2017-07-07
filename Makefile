make develop:
	virtualenv myenv && . myenv/bin/activate && python setup.py develop

make test:
	. myenv/bin/activate && pytest tests

make clean:
	rm -rf myenv && rm -rf build && rm -rf dist && rm -rf *.egg-info
