#!/bash/sh

all:

	@echo \\n\\n"| A* sizelab = Tiny | Heuristic = Manhattan | "\\n\\n

	python pacman.py -l mediumMaze -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic -z .5

	@echo \\n\\n"| A* sizelab = Big | Heuristic = Euclidean | "\\n\\n

	python pacman.py -l bigMaze -p SearchAgent -a fn=astar,heuristic=euclideanHeuristic -z .5

	@echo \\n\\n"| Uniform Cost Search | sizelab = Medium | Heuristic = none | "\\n\\n

	python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs

	@echo \\n\\n"| Hill Climbing | sizelab = tiny | Heuristic = Manhattan | "\\n\\n

	python pacman.py -l tinyMaze -p SearchAgent -a fn=hcl,heuristic=manhattanHeuristic -z .5

	@echo \\n\\n"| Hill Climbing | sizelab = Medium | Heuristic = Euclidean | "\\n\\n

	python pacman.py -l mediumMaze -p SearchAgent -a fn=hcl,heuristic=euclideanHeuristic -z .5

	@echo \\n\\n"| Simulated Annealing | sizelab = tiny | Heuristic = none | "\\n\\n

	python pacman.py -l mediumMaze -p SearchAgent -a fn=san -z .5

a*tinyM:

	@echo \\n\\n"| A* sizelab = Tiny | Heuristic = Manhattan | "\\n\\n
	python pacman.py -l mediumMaze -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic -z .5

a*bigE:

	@echo \\n\\n"| A* sizelab = Big | Heuristic = Euclidean | "\\n\\n
	python pacman.py -l bigMaze -p SearchAgent -a fn=astar,heuristic=euclideanHeuristic -z .5

ucsM:

	@echo \\n\\n"| Uniform Cost Search | sizelab = Medium | Heuristic = none | "\\n\\n
	python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs

hcltinyM:

	@echo \\n\\n"| Hill Climbing | sizelab = tiny | Heuristic = Manhattan | "\\n\\n
	python pacman.py -l tinyMaze -p SearchAgent -a fn=hcl,heuristic=manhattanHeuristic -z .5

hclmediumE:

	@echo \\n\\n"| Hill Climbing | sizelab = Medium | Heuristic = Euclidean | "\\n\\n
	python pacman.py -l mediumMaze -p SearchAgent -a fn=hcl,heuristic=euclideanHeuristic -z .5

sanmedium:

	@echo \\n\\n"| Simulated Annealing | sizelab = tiny | Heuristic = none | "\\n\\n
	python pacman.py -l mediumMaze -p SearchAgent -a fn=san -z .5

help:

	@echo \\n\\n"command: a*tinyM 	| to A* with tiny maze and Manhattan Heuristic"
	@echo "command: a*bigE  		| to A* with big maze and Euclidean Heuristic"
	@echo "command: ucsM			| to Uniform Cost Search with medium maze"
	@echo "command: hcltinyM		| to Hill Climbing with tiny maze and Manhattan Heuristic"
	@echo "command: hclmediumE		| to Hill Climbing with medium maze and Euclidean Heuristic"
	@echo "command: sanmedium		| to Simulated Anneling with medium maze"

	@echo \\n\\n"but you can also run all by executing the command: run"\\n\\n