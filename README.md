# Perceptron

Il percettrone venne proposto da Frank Rosenblatt nel 1958. La struttura è la seguente:
<br><br>
<img  src="./img/percettrone.JPG" height="250" width="450" style="text-align: center">
<br><br>
Considerando un numero p di predittori, il vettore <i> X = [x1, x2, ... , xp] </i> rappresenta l'input del percettrone. Quest'ultimo viene poi moltiplicato per il vettore dei pesi <i> W = [w1, w2, ... , wp] </i>. Detto ciò, l'output può essere espresso matematicamente dalla formula:
<br><br>
![first equation](https://latex.codecogs.com/gif.latex?%5Ctextit%7Boutput%7D%20%3D%20g%28%5Csum_%7Bp%3D1%7D%20%5E%7BP%7Dw_%7Bp%7Dx_%7Bp%7D%29)
<br><br>
in cui la funzione g(), detta <i> funzione di attivazione </i>, è spesso rappresentata dalla funzione sigmoidea matematicamente esprimibile in questo modo:

![first equation](https://latex.codecogs.com/gif.latex?%5Csigma%28x%29%20%3D%20%5Cfrac%7B1%7D%7B%281&plus;e%5Ex%29%7D)

La funzione sigmoidea ha un dominio di valori nel range [0,1] rendendo così il percettrone un classificatore binario. In particolare,.


  
   
  
  
  
  
