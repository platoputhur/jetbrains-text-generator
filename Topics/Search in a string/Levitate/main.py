spell = "Wingardium Leviosa"
sub = input()
try:
    print(spell.index(sub))
except ValueError:
    print("-1")
