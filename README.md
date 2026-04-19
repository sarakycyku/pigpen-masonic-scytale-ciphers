# pigpen-masonic-scytale-ciphers

Ky eshte nje program per perdorimin e algoritmeve klasike te enkriptimit dhe dekriptimit.Ne menyre qe porgrami te perdoret me lehte perdoret nje menu ku perdoruesi mund te zgjedhe mes disa algoritmeve. 

## 1. Ekzekutimi i programit
Hape CMD ose Terminal.
Sigurohuni qe python eshte i instaluar:

``python --version``

Clone the repo:

``git clone https://github.com/sarakycyku/pigpen-masonic-scytale-ciphers.git``

``cd pigpen-masonic-scytale-ciphers``

Run the Program:

``python -m main.main``

Kur te ekzekutohet programi do te shfaqet nje menu:


<img width="291" height="244" alt="image" src="https://github.com/user-attachments/assets/fd33ec53-9720-48b9-9a4a-50c51788905a" />

Prej kesaj menu  duhet te zgjedhni algoritmin me te cilin deshironi te enkriptoni ose te dekriptoni

Pasi te keni zgjedhur algoritmin duhet te zgjidhni nese doni te enkriptoni apo te dekriptoni:

<img width="339" height="362" alt="image" src="https://github.com/user-attachments/assets/a1b8a969-3ada-49d1-9ef7-292d92cb3c45" />


Ku enkriptimi e konverton plaintext ne ciphertext me algoritmin qe keni perzgjedhur ndersa dekriptimi e kthen ciphertext ne plaintext.


Nese zgjidhni opsionin 4 qe eshte Krahaso i cili lejon qe nje tekst i vetem te enkriptohet me te tre algoritmet njekohesisht:

<img width="348" height="390" alt="image" src="https://github.com/user-attachments/assets/028e979f-2f95-44af-ac96-d340a2072262" />


Nese zgjidhni opsionin 5 programi perfundon ndersa nese zgjidhni opsione tjera te pa vlefshme programi shfaq error.

## 2. Pershkrimi i algoritmeve
#### 1. Pigpen Cipher

Pigpen Cipher eshte nje nga metodat me te vjetra te enkriptimit qe eshte perdorur kryesisht nga organizata sekrete si Freemasons ne shekujt e kaluar. Kjo metode nuk perdor zhvendosje apo riorganizim te shkronjave por bazohet ne zevendesimin e tyre me simbole grafike.

Ne kete algoritem cdo shkronje e alfabetit anglez perfaqesohet nga nje simbol unik i ndertuar nga forma gjeometrike si kende katrore dhe pika. Alfabeti zakonisht ndahet ne grupe dhe vendoset ne struktura te ngjashme me rrjeta (grid) ku cdo pozicion korrespondon me nje simbol te caktuar.

Per enkriptim mesazhi merret dhe cdo shkronje zevendesohet me simbolin perkates nga tabela Pigpen. Si rezultat teksti i enkriptuar perbehet vetem nga simbole dhe nuk mund te kuptohet lehte pa njohur sistemin.

Te dekiriptimi cdo simbol identifikohet dhe kthehet ne shkronjen perkates duke perdorur te njejten tabele. Pra celesi i ketij algoritmi eshte njohja e lidhjes midis shkronjave dhe simboleve.

Ndryshe nga algoritmet e tjera me komplekse Pigpen Cipher eshte nje metode e thjeshte dhe vizuale qe perdoret me shume per qellime edukative dhe historike sesa per siguri reale.
<img width="1024" height="464" alt="rsirGNhjrGdsKvGfbTVzu37fUieCcTnrACEME71Rifgaxay7IMFEFNTcrM-cxcEsP03CsTqOnN6bf4nG7utS4QWbsGWJsXG5bzNbzZNdCrjkFd7l84phrM-UrsX-8QOAhOoSw4HaL9wfy08kT4IvINe4GAbaEu3IujuNWs3-7ARo72XKeuIUWEBPUQATcny0" src="https://github.com/user-attachments/assets/40d0a003-0b64-4d89-8cd1-4f56a1155bff" />


#### 2. Scytale Transposition

Scytale transposition eshte nje nga metodat me te vjetra per enkriptim ku ne fillim eshte perdorur nga Spartanet ne Greqine e lashte per komunikime ushtarake. Te ky algoritem ne vend se te behet zevendesimi i shkronjave, ketu vetem nderrohet renditja e tyre.

Pajisja perbehet nga nje scytale shkop druri rreth te cilit mbeshtillet nje shirit pergamenti ose lekure ne menyre spirale. Pastaj mesazhi shkruhej ne menyre horizontale pergjate shiritit dhe kur shiriti largohej nga shkopi shkronjat dukeshin te perziera dhe nuk kishin kuptim. Si celes eshte perdorur diametri i shkopit pasi vetem nje shkop me te njejtin diameter mund ta bente dekriptimin e atij mesazhi.

Tek ky algoritem teksti organizohet ne nje matrice dhe celesi i cili tregon numrin e kolonave. Nese teksti nuk e mbushte matricen atehere shtohen karaktere plotesuese. Pas kesaj teksti i enkriptuar krijohet duke lexuar karakteret kolone pas kolone.

Ndersa te dekirptimi ciphertext vendoset perseri ne kolona sipas te njejtit celes dhe me pas lexohet rresht pas rresht per te rikthyer mesazhin origjinal.

<img width="347" height="145" alt="download" src="https://github.com/user-attachments/assets/9676e29c-9a26-42f1-aadb-97ec01c88ce1" />

#### 3.Masonic Cipher
Masonic Cipher eshte nje cipher qe perdoret per enkriptim dhe dekriptim te tekstit. Ky algoritem perdor tri rrjeta te ndryshme per te paraqitur te gjitha shkronjat e alfabetit.

Rrjeti i pare perdoret per shkronjat A-I dhe i ka simbolet pa pika. Rrjeti i dyte perdoret per shkronjat J-R dhe i ka te njejtat simbole por me nje pike brenda. Rrjeti i trete perdoret per shkronjat S-Z dhe i ka simbolet diagonale.

Per enkriptim, teksti konvertohet ne shkronja te medha, pastaj cdo shkronje zevendesohet me simbolin perkates. Hapesirat mbeten te pandryshuara dhe simbolet ndahen me hapesira per lehtesi ne dekriptim.

Dekriptimi funksionon ne menyre te kundert: cdo simbol identifikohet dhe kthehet ne shkronjen perkatese duke perdorur te njejten tabele.


## 3.Shembuj te rezultateve
#### 1. Pigpen Cipher
Ky program implementon Pigpen Cipher nje metode klasike enkriptimi qe zevendeson cdo shkronje me nje simbol unik.

Si funksionon

Programi përdor dy struktura kryesore:

pigpen dictionary -> per enkriptim (shkronje -> simbol)

reverse dictionary -> per dekriptim (simbol -> shkronje)

Enkriptimi:

Mirret teksti nga perdoruesi
E kthen në uppercase dhe cdo shkronje zevendesohet me simbolin perkates,
Simbolet ndahen me hapesira per lehtesi ne dekriptim

si shembull eshte:

Input:

hello

Output:

┼ ┴ ¬ ¬ ┘

Dekriptimi:


Mirret teksti i enkriptuar (simbolet) dhe ndanen me split() sipas hapesirave
Cdo simbol kthehet ne shkronjen perkatese,
Shembull:

Input:

┼ ┴ ¬ ¬ ┘

Output:

HELLO

Kur programi ekzekutohet, përdoruesi zgjedh:

1 - Encrypt

2 - Decrypt

Nese zgjedh 1  futet tekst normal per enkriptim

Nese zgjedh 2 futet tekst i enkriptuar per dekriptim

Por ky algoritem enkeripton vetem shkronjat dhe nese jepet nje numer ose ndonej simbol tjeter programi shfaq error
<img width="368" height="373" alt="image" src="https://github.com/user-attachments/assets/ecba3391-67da-4e0c-8c67-0f5e2a54d0b0" />


Keshtu doket terminali kur te behet RUN kodi:

<img width="398" height="482" alt="image" src="https://github.com/user-attachments/assets/061f3ca4-9238-4c6f-b4fa-02c12e53da79" />



#### 2. Scytale Transposition
Per algoritmin scytale si tekst marrim "This is a scytale transposition example" prej te ciles largohen hapesirat dhe  te gjitha shkronjat shnderrohen ne  uppercase. 

"THISISASCYTALETRANSPOSITIONEXAMPLE" nese numri i rreshtave eshte 10 dhe gjatesia e tektit eshte 35 atehere numri i kolonave do te jete 35/10 =3.5=4 kolona dhe do

te fitohet matrica :

```
T H I S
I S A S
C Y T A
L E T R
A N S P
O S I T
I O N E
X A M P
L E X X
X X X X
```
dhe teksti i enkriptuar eshte:TICLAOIXLXHSYENSOAEXIATTSINMXXSSARPTEPXX

Ndersa gjate dekriptimit padding X qe jane largohen dhe fitohet THISISASCYTALETRANSPOSITIONEXAMPLE
<img width="563" height="502" alt="image" src="https://github.com/user-attachments/assets/4a2816c3-d8e6-4e69-9655-90ca5196f9d4" />


#### 3.Masonic Cipher
Per algoritmin Masonic cipher si tekst marrim "HELLO WORLD". Teksti konvertohet ne shkronja te medha dhe hapesirat mbeten te pandryshuara.

"HELLO WORLD" do te thote qe cdo shkronje zevendesohet me simbolin perkates nga rrjete perkatese:

H -> ┴ (nga rrjeta 1)

E → ┼ (nga rrjeta 1)

L -> ┐• (nga rrjeta 2)

L -> ┐• (nga rrjeta 2)

O -> ┤• (nga rrjeta 2)

(hapesire) -> (hapesire)

W -> ◢ (nga rrjeta 3)

O -> ┤• (nga rrjeta 2)

R -> ┘• (nga rrjeta 2)

L -> ┐• (nga rrjeta 2)

D -> ├ (nga rrjeta 1)

dhe teksti i enkriptuar eshte: ┴ ┼ ┐• ┐• ┤• ◢ ┤• ┘• ┐• ├

Per dekriptim cdo simbol identifikohet nga tabela dhe kthehet ne shkronjen perkatese. Simbolet ndahen me hapesira dhe hapesirat mbeten hapesira.

Teksti i dekriptuar eshte: HELLO WORLD    
<img width="538" height="477" alt="image" src="https://github.com/user-attachments/assets/943b9f39-d7be-41f2-a551-d2c76f221a0b" />



