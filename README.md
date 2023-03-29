# Design e implementazione di un avatar per applicazioni di Robotica Sociale

Repository contenente tutti i file citati nella tesi.


## Preparazione ambiente Blender e interprete Python

1. Installa UPBGE scaricando l'ultima release dal link https://upbge.org/#/download

2. Installa e abilita i seguenti plugin Blender:
* **BVH Retargeter**
* **Import Runtime MakeHuman Exchange 2**
* **Python Module manager**
* **ROS Human Bridge** (da abilitare in seguito al passo 3)

Per l'istallazione è sufficiente recarsi nelle preferenze di Blender e nella sezione Add-ons inserire i file .zip contenuti in `avatar/Blender/Plugin/`.

3. Aprire il menù di configurazione di **Python Module manager**, sempre all'interno della sezione per la gestione degli Add-ons, abilitare PIP mediate il tasto "Ensure PIP", installare poi i seguenti moduli:
* **rospy** module name: `--extra-index-url https://rospypi.github.io/simple rospy-all`
* **opencv** module name: `opencv-python`

4. È ora possibile abilitare il plugin **ROS Human Bridge**. Chiudendo le preferenze di Blender e tornando nella finestra principale contenente il *3D Viewport*, è ora possibile aprire il pannello di controllo dei plugin premendo sulla tastiera il tasto N.

## Preparazione workspace Catkin

1. Installa nel tuo workspace Catkin i pacchetti ROS contenuti in `avatar/ROS/`:
* sender
*  person_euler_msgs
* person_quaternion_msgs

2. Esegui il *source* del tuo workspace.

3. Compila mediante il comando `catkin_make`.

## Test funzionamento
All'interno del persorso `avatar/Blender/` vengono forniti un avatar e delle animazioni da me utilizzate per verificare il corretto funzionamento del *bridge* tra ROS e Blender. Per eseguire i test è necessario scaricare il contenuto delle due cartelle `Animation` e `models`, aprire il file .blend contenuto in quest'ultima e avviare il plugin **ROS Human Bridge** inserendo il topic ROS desiderato.
Basterà quindi poi avvare anche il nodo ROS *sender* il quale inizierà a inviare le informazioni di roto-traslazione al topic, tramutate dal plugin in effettivi movimenti dell'avatar nel *3D Viewport* di Blender. 
    
## Support 💬

Per supporto, scrivere al seguente indirizzo email andrea.tessarolo@studenti.unipd.it.


## Authors 👋

- [@Andrea Tessarolo](https://github.com/AndreaTss)
- [@Gloria Beraldo](https://github.com/GloriaB)
