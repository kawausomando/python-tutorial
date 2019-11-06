def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
        print("-" * 40)
        keys = sorted(keywords.keys())
        for kw in keys:
            print(kw, ":", keywords[kw])
            
cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

# 出力
# -- Do you have any Limburger ?
# -- I'm sorry, we're all out of Limburger
# It's very runny, sir.
# ----------------------------------------
# client : John Cleese
# shopkeeper : Michael Palin
# sketch : Cheese Shop Sketch
# It's really very, VERY runny, sir.
# ----------------------------------------
# client : John Cleese
# shopkeeper : Michael Palin
# sketch : Cheese Shop Sketch