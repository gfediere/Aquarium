# HowTo
Editez le fichier pompe_doseuse.conf en mettant les numeros des PINs cables sur le raspberry, ex:
```
[gpio_id]
ca: 14
mg: 18
sel: 22
```
Vous pouvez ensuite lancer le script (ou le croner) en passant en parametre le produit (ca|mg|sel...) et le volume, ex:
```
python pompe_doseuse.py ca 10
```
