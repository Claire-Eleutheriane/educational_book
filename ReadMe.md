#ReadMe

## Bibliographie

Techno à utiliser : JupyterBook https://jupyterbook.org/intro.html.

JupyterBook est développé par le projet *Executable Books* en parallèle de MyST, MyST Parser, Sphinx Book Theme, etc.
Plusieurs exemples de livres interactifs :
- https://github.com/executablebooks/quantecon-mini-example
- https://github.com/executablebooks/quantecon-example
Intérêt du JupyterBook : il peut être écrit en Markdown (plus précisément en MyST, un Markdown adapté pour Sphinx).

La techno utilisée par M. Tiller dans MBE est un plus antique (Python 2), basée sur Sampledoc (https://matplotlib.org/sampledoc/extensions.html).
Elle permet d'inclure une fonction Matplotlib dans un document ReST.

## Prochaines actions

Ce que je pensais faire : des *ipywidgets*. On donne une valeur, et ça simule derrière avec iPython.
Ça ne semble pas correctement compatible avec JupyterBook : il y a officiellement des *issues* car les ipywidgets ont besoin d'un kernel Python en parallèle du JavaScript.
https://jupyterbook.org/interactive/interactive.html conseille d'utiliser la techno Thebe pour faire marcher quelques widgets, via Binder ; chez moi Binder ne marche pas.
Conclusion : JupyterBook pas ouf pour l'instant !
