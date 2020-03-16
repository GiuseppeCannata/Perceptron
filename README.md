# Perceptron

<b> 1. Introduzione </b>
<br><br>
Il percettrone venne proposto da Frank Rosenblatt nel 1958. La struttura è la seguente:
<br><br>
<img  src="./img/percettrone.JPG" height="250" width="450" Hspace="220">
<br>
Considerando un numero p di predittori, il vettore <i> X = [x1, x2, ... , xp] </i> rappresenta l'input del percettrone. Quest'ultimo viene poi moltiplicato per il vettore dei pesi <i> W = [w1, w2, ... , wp] </i>. Detto ciò, l'output può essere espresso matematicamente dalla formula:
<br><br>
<img  Hspace="160">
![output neurone](https://latex.codecogs.com/gif.latex?%5Ctextit%7Boutput%7D%20%3D%20g%28%5Csum_%7Bp%3D1%7D%20%5E%7BP%7Dw_%7Bp%7Dx_%7Bp%7D%29)
<br><br>
in cui la funzione g(), detta <i> funzione di attivazione </i>, è spesso rappresentata dalla funzione sigmoidea matematicamente esprimibile in questo modo:
<br><br>
<img  Hspace="170">
![funzione sigmoide](https://latex.codecogs.com/gif.latex?%5Csigma%28x%29%20%3D%20%5Cfrac%7B1%7D%7B%281&plus;e%5Ex%29%7D)
<br><br>
Quest'ultima ha un dominio di valori nel range [0,1] rendendo così il percettrone un classificatore binario. In particolare, supponendo di avere due classi A e B, il valore ritornato dalla funzione sigmoidea esprime la probabilità di appartenenza dell'esempio X alla classe A o B.
<br><br>
Di estrema importanza è il vettore dei pesi W. Il loro valore viene determinato durante la fase di apprendimento <i> (training) </i>, in maniera tale che la differenza (target - output) sia la più piccola possibile. Ma quanto piccola? Considerando (target - output) come la funzione di loss, l'obiettivo è quello di raggiungere il <i> minimo globale </i>. In particolare con il termine target ci riferiamo al valore con cui labelliamo l'osservazione X <i> (valore atteso) </i>, al contrario, con il termine output ci riferiamo al valore restituito dal percettrone <i>(predizione) </i>. 
<br>
I pesi vengono determinati attraverso la regola di aggiornamento <i> delta rule </i> (discesa del gradiente). Considerando un solo neurone (appunto il percettrone) possiamo esprimere la delta rule in questo modo:
<br><br>
<img  Hspace="170">
![delta rule](https://latex.codecogs.com/gif.latex?%5CDelta%7BW%7D%20%3D%20%5Ceta%20%28t%20-%20o%29%20X)
<br><br>
el i conseguente aggiornamento del vettore peso:
<br><br>
<img  Hspace="170">
![aggiornamento pesi](https://latex.codecogs.com/gif.latex?W_%7Bnew%7D%20%3D%20W_%7Bold%7D%20&plus;%20%5CDelta%7BW%7D)
<br><br><br>
<b> 2. Regressione </b>
<br><br>
Modificando la funzione di attivazione possiamo ottenere un modello regressivo. In particolare, sostituiamo la funzione sigmoidea con la funzione ReLU. Quest'ultima viene ad esprimersi matematicamente:
<br><<br>
<img  Hspace="170">
![formula relu](https://latex.codecogs.com/gif.latex?ReLU%28x%29%20%3D%20max%280%2Cx%29)
<br><br>
Detto ciò, il nostro percettrone costituirà un modello definito dal seguente hyperpiano:
<br><br>
<img  Hspace="150">
![hyperpiano](https://latex.codecogs.com/gif.latex?y_%7Bpred_%7Bi%7D%7D%20%3D%20w_%7B0%7D%20&plus;%20w_%7B1%7Dx_%7Bi1%7D&plus;%20...%20&plus;%20w_%7Bp%7Dx_%7Bip%7D)
<br><br>
in cui <i> w0 </i> rappresenta l'intercetta mentre w1, ... , wp le relative pendenze.
<br><br><br>
<b> 3. Plot residui </b>
<br><br>
Di seguito posto il plot dei residui calcolato sul training set sia del percettrone sia eseguendo una LinearRegression. Il dataset utilizzato è <a href="https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_boston.html">Boston house-prices</a> 
<table>
        <tr><td><b>Perceptron</b></td><td><b>LinearRegression</b></td></tr>
        <tr><td><img  src="./img/plot_residui.png" width="320" height="230"></td><td><img  src="./img/.png" width="320" height="230"></td></tr>
</table>
