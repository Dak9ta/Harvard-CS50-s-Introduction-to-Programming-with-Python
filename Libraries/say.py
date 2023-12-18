import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.fox("hello, " + sys.argv[1])
    
'''
This is a list of commands you can play with to change the displayed animal
['beavis', 'cheese', 'cow', 'daemon', 'dragon', 'fox', 'ghostbusters', 'kitty',
'meow', 'miki', 'milk', 'octopus', 'pig', 'stegosaurus', 'stimpy', 'trex', 
'turkey', 'turtle', 'tux']
'''