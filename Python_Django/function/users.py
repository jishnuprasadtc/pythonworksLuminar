tweets="what a game , hats off to both teams . well done @benstokes38 @patcummins @berrlyarmy  @circketaus @ecbcircket"
word=tweets.split(" ")
for w in word:
    if w.startswith("@"):
        print(w)
