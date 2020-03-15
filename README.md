# Perceptron

Il percettrone venne proposto da Frank Rosenblatt nel 1958. La struttura è la seguente:
<br><br>
<img  src="./img/percettrone.JPG" height="280" width="500" style="text-align: center">
<br><br>\\
Considerando un numero p di predittori, il vettore X = [x1, x2, ... , xp] rappresenta l'input del percettrone. Quest'ultimo viene poi moltiplicato per il vettore dei pesi W = [w1, w2, ... , wp]. Detto ciò, l'output può essere espresso matematicamente dalla formula:
<br><br>
![first equation](https://latex.codecogs.com/gif.latex?%5Ctextit%7Boutput%7D%20%3D%20g%28%5Csum_%7Bp%3D1%7D%20%5E%7BP%7Dw_%7Bp%7Dx_%7Bp%7D%29)
<br><br>
in cui la funzione g() rappresenta la <i> funzione di attivazione </i>. Nella teoria del percettrone, la funzione utilizzata è la sigmoide


che rende il percettrone un classificatore binario.

  
   
  
  
  
  
