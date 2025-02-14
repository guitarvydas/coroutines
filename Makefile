all: lisp js py

js:
	node coroutines.js


py:
	python3 cor.py

lisp:
	sbcl --noinform --non-interactive --load cr.lisp --eval "(coroutine-manager)" --quit
