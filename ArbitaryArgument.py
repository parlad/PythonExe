def concat(*args, sep="/"):
    print(sep.join(args))
    return sep.join(args)

concat("earth", "mars", "venus")

concat("earth", "mars", "venus", sep=".")