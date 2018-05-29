main: UI/about.pyc UI/main.pyc trinity_resource_rc.pyc trinity-editor.pyc 
	chmod u+x trinity-editor.pyc

trinity-editor.pyc: trinity-editor.py
	python3 -m  compileall -b .

UI/about.pyc: UI/about.py

UI/main.pyc: UI/main.py

UI/main.py:    UI/main.ui
	pyuic5 $< -o $@

UI/about.py:    UI/about.ui
	pyuic5 $< -o $@

trinity_resource_rc.pyc: trinity_resource_rc.py

trinity_resource_rc.py: trinity_resource.qrc
	pyrcc5 $< -o $@

clean:
	rm -rf ./*.pyc __pycache__
	rm trinity_resource_rc.py
	cd MainWindow; rm -rf *.pyc __pycache__
	cd UI; rm -rf *.pyc *.py __pycache__
