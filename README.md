# Návštěvnost plovárny
Kód který sbírá data ohledně počtu návštěvníků, teploty vzduchu a teploty vody ze stránek městské plovárny Louka, tyto data jsou poté zapisovány do csv souboru, kde jsou následně uspořádány a následně je možné zobrazení v grafu, pro lepší přehled.
Kód je napsán tak, aby ho stačilo ráno v 10 spustit a v noci ve 21 se sám vypne, původně jsem chtěl, aby kód scrapnul data a byl ukončen a pomocí **taskschd.msc** jsem chtěl nastavit že by se zapínal každých deset minut, ale **taskschd.msc** mi vůbec nefungoval a proto jsem kód napsal takto.
