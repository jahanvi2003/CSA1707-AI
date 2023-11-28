cat(fubby).
dog(figaro).
black_spots(fubby).
white_spots(figaro).

owns(mary,Pet):-cat(Pet),black_spots(Pet).
loves(Who,What):-owns(Who,What).