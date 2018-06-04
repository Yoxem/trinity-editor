LIST_OF_ORIG_PY=$(shell find . -type f -name  "*.py" )

LIST_OF_UI=$(shell find . -type f -name "*.ui")
LIST_OF_UI_PY=$(patsubst %.ui,%.py,$(LIST_OF_UI))

LIST_OF_QRC=$(shell find . -type f -name "*.qrc")
LIST_OF_RC_PY=$(patsubst %.qrc,%_rc.py,$(LIST_OF_QRC))

LIST_OF_PY=$(LIST_OF_ORIG_PY)
LIST_OF_PY+=$(LIST_OF_UI_PY)
LIST_OF_PY+=$(LIST_OF_RC_PY)

LIST_OF_PYC:=$(patsubst %.py,%.pyc,$(LIST_OF_PY))

LIST_OF_PYCACHE=$(shell find . -type d -name "__pycache__")

main: $(LIST_OF_PYC) trinity-editor.pyc 
	chmod u+x trinity-editor.pyc

%.pyc: %.py
	python3 -m compileall -b $<

$(LIST_OF_RC_PY): %_rc.py: %.qrc
	pyrcc5 $< -o $@

$(LIST_OF_UI_PY): $(LIST_OF_UI)
	pyuic5 $< -o $@

clean:
	rm -rf $(LIST_OF_PYC) $(LIST_OF_UI_PY) $(LIST_OF_RC_PY) $(LIST_OF_PYCACHE)
