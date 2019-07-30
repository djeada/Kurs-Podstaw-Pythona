from string import Template 
  
t = Template('$x jest bratem $y') 

slownik1 = {'x': 'James', 'y': 'Tunczyka'}

print(t.substitute(slownik1))

slownik2 = {'x': 'Lol', 'y': 'Lola'}

print(t.substitute(slownik2)) 
