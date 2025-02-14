all: js py lisp

js:
	@echo ''
	@echo '*** Javascript ***'
	node coroutines.js


py:
	@echo ''
	@echo '*** Python ***'
	python3 coroutines.py

lisp:
	@echo ''
	@echo '*** Lisp ***'
	sbcl --noinform --non-interactive --load coroutines.lisp --eval "(dispatcher)" --quit
