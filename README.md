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

========================================
CLASSICAL ENCRYPTION ALGORITHMS
========================================
1. Pigpen
2. Scytale
3. Masonic
4. Krahaso
5. Dil
========================================

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

3. Pershkrimi i algoritmeve
1. Pigpen
2. Masonic
3. Scytale transposition
1. Pigpen Cipher

Pigpen Cipher eshte nje nga metodat me te vjetra te enkriptimit qe eshte perdorur kryesisht nga organizata sekrete si Freemasons ne shekujt e kaluar. Kjo metode nuk perdor zhvendosje apo riorganizim te shkronjave, por bazohet ne zevendesimin e tyre me simbole grafike.

Ne kete algoritem cdo shkronje e alfabetit anglez perfaqesohet nga nje simbol unik i ndertuar nga forma gjeometrike si kende, katrore dhe pika. Alfabeti zakonisht ndahet ne grupe dhe vendoset ne struktura te ngjashme me rrjeta (grid), ku cdo pozicion korrespondon me nje simbol te caktuar.

Per enkriptim, mesazhi merret dhe cdo shkronje zevendesohet me simbolin perkates nga tabela Pigpen. Si rezultat, teksti i enkriptuar perbehet vetem nga simbole dhe nuk mund te kuptohet lehte pa njohur sistemin.

Dekriptimi funksionon ne menyre te kundert: cdo simbol identifikohet dhe kthehet ne shkronjen perkates duke perdorur te njejten tabele. Pra, celesi i ketij algoritmi eshte njohja e lidhjes midis shkronjave dhe simboleve.

Ndryshe nga algoritmet e tjera me komplekse, Pigpen Cipher eshte nje metode e thjeshte dhe vizuale, qe perdoret me shume per qellime edukative dhe historike sesa per siguri reale.

2. Scytale Transposition

Scytale transposition eshte nje nga metodat me te vjetra per enkriptim ku ne fillim eshte perdorur nga Spartanet ne Greqine e lashte per komunikime ushtarake. Te ky algoritem ne vend se te behet zevendesimi i shkronjave, ketu vetem nderrohet renditja e tyre.

Pajisja perbehet nga nje scytale shkop druri rreth te cilit mbeshtillet nje shirit pergamenti ose lekure ne menyre spirale. Pastaj mesazhi shkruhej ne menyre horizontale pergjate shiritit dhe kur shiriti largohej nga shkopi shkronjat dukeshin te perziera dhe nuk kishin kuptim. Si celes eshte perdorur diametri i shkopit pasi vetem nje shkop me te njejtin diameter mund ta bente dekriptimin e atij mesazhi.

Tek ky algoritem teksti organizohet ne nje matrice dhe celesi i cili tregon numrin e kolonave. Nese teksti nuk e mbushte matricen atehere shtohen karaktere plotesuese. Pas kesaj teksti i enkriptuar krijohet duke lexuar karakteret kolone pas kolone.

Dekriptimi funksionon ne menyre te kundert pra ciphertext vendoset perseri ne kolona sipas te njejtit celes dhe me pas lexohet rresht pas rresht per te rikthyer mesazhin origjinal.
