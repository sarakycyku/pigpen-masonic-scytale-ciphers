# pigpen-masonic-scytale-ciphers

## 1. Ekzekutimi i programit

Sigurohuni qe python eshte i instaluar:
python --version

Clone the repo:

git clone https://github.com/sarakycyku/pigpen-masonic-scytale-ciphers.git
cd pigpen-masonic-scytale-ciphers

Run the Program:

python -m main.main

Kur te ekzekutohet programi do te shfaqet nje menu ku duhet te zgjidhni algoritmin me te cilin deshironi te enkriptoni ose te dekriptoni:


CLASSICAL ENCRYPTION ALGORITHMS

1. Pigpen
2. Scytale
3. Masonic
4. Krahaso
5. Dil


Pasi te keni zgjedhur algoritmin duhet te zgjidhni nese doni te enkriptoni apo te dekriptoni:

1. Encrypt
2. Decrypt
Choose:

Ku enkriptimi e konverton plaintext ne ciphertext me algoritmin qe keni perzgjedhur, ndersa dekriptimi e kthen ciphertext ne plaintext.


Nese zgjidhni opsionin 4 qe eshte Krahaso i cili lejon qe nje tekst i vetem te enkriptohet me te tre algoritmet njekohesisht:

Pigpen Cipher
Scytale Transposition
Masonic Cipher

Nese zgjidhni opsionin 5 programi perfundon, ndersa nese zgjidhni opsione tjera te pa vlefshme programi shfaq error.

## 2. Pershkrimi i algoritmeve
#### 1. Pigpen Cipher

Pigpen Cipher eshte nje nga metodat me te vjetra te enkriptimit qe eshte perdorur kryesisht nga organizata sekrete si Freemasons ne shekujt e kaluar. Kjo metode nuk perdor zhvendosje apo riorganizim te shkronjave, por bazohet ne zevendesimin e tyre me simbole grafike.

Ne kete algoritem cdo shkronje e alfabetit anglez perfaqesohet nga nje simbol unik i ndertuar nga forma gjeometrike si kende, katrore dhe pika. Alfabeti zakonisht ndahet ne grupe dhe vendoset ne struktura te ngjashme me rrjeta (grid), ku cdo pozicion korrespondon me nje simbol te caktuar.

Per enkriptim, mesazhi merret dhe cdo shkronje zevendesohet me simbolin perkates nga tabela Pigpen. Si rezultat, teksti i enkriptuar perbehet vetem nga simbole dhe nuk mund te kuptohet lehte pa njohur sistemin.

Dekriptimi funksionon ne menyre te kundert: cdo simbol identifikohet dhe kthehet ne shkronjen perkates duke perdorur te njejten tabele. Pra, celesi i ketij algoritmi eshte njohja e lidhjes midis shkronjave dhe simboleve.

Ndryshe nga algoritmet e tjera me komplekse, Pigpen Cipher eshte nje metode e thjeshte dhe vizuale, qe perdoret me shume per qellime edukative dhe historike sesa per siguri reale.

#### 2. Scytale Transposition

Scytale transposition eshte nje nga metodat me te vjetra per enkriptim ku ne fillim eshte perdorur nga Spartanet ne Greqine e lashte per komunikime ushtarake. Te ky algoritem ne vend se te behet zevendesimi i shkronjave, ketu vetem nderrohet renditja e tyre.

Pajisja perbehet nga nje scytale shkop druri rreth te cilit mbeshtillet nje shirit pergamenti ose lekure ne menyre spirale. Pastaj mesazhi shkruhej ne menyre horizontale pergjate shiritit dhe kur shiriti largohej nga shkopi shkronjat dukeshin te perziera dhe nuk kishin kuptim. Si celes eshte perdorur diametri i shkopit pasi vetem nje shkop me te njejtin diameter mund ta bente dekriptimin e atij mesazhi.

Tek ky algoritem teksti organizohet ne nje matrice dhe celesi i cili tregon numrin e kolonave. Nese teksti nuk e mbushte matricen atehere shtohen karaktere plotesuese. Pas kesaj teksti i enkriptuar krijohet duke lexuar karakteret kolone pas kolone.

Dekriptimi funksionon ne menyre te kundert pra ciphertext vendoset perseri ne kolona sipas te njejtit celes dhe me pas lexohet rresht pas rresht per te rikthyer mesazhin origjinal.

#### 3.Masonic Cipher


## 3.Shembuj te rezultateve
#### 1. Pigpen Cipher
Ky program implementon Pigpen Cipher, një metodë klasike enkriptimi që zëvendëson çdo shkronjë me një simbol unik.
Si funksionon
Programi përdor dy struktura kryesore:
pigpen dictionary → për enkriptim (shkronjë ➝ simbol)
reverse dictionary → për dekriptim (simbol ➝ shkronjë)
Enkriptimi:
Funksioni encrypt(text):
Merr tekstin nga përdoruesi
E kthen në uppercase (A-Z)
Çdo shkronjë zëvendësohet me simbolin përkatës
Simbolet ndahen me hapësira për lehtësi në dekriptim
✅ Shembull:
Input:

hello

Output:

┼ ┴ ¬ ¬ ┘
Dekriptimi:
Funksioni decrypt(text):
Merr tekstin e enkriptuar (simbolet)
I ndan me split() sipas hapësirave
Çdo simbol kthehet në shkronjën përkatëse
✅ Shembull:
Input:

┼ ┴ ¬ ¬ ┘

Output:

HELLO
Kur programi ekzekutohet, përdoruesi zgjedh:
1 - Encrypt
2 - Decrypt
Nëse zgjedh 1 → fut tekst normal për enkriptim
Nëse zgjedh 2 → fut tekst të enkriptuar për dekriptim
Keshtu doket terminali kur te behet RUN kodi
<img width="987" height="400" alt="image" src="https://github.com/user-attachments/assets/1f14bd76-0c3d-4b80-bc16-296671903186" />


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
Edhe matrica per dekriptim do te jete e njejte
dhe teksti i dekriptuar eshte :THISISASCYTALETRANSPOSITIONEXAMPLEXXXXXX
<img width="620" height="423" alt="image" src="https://github.com/user-attachments/assets/236ef277-475f-420f-ac1a-b4f1b9e655fc" />

#### 3.Masonic Cipher

