# pigpen-masonic-scytale-ciphers

## 1. Ekzekutimi i programit

Sigurohuni qe python eshte i instaluar:
python --version

Clone the repo:
git clone https://github.com/sarakycyku/pigpen-masonic-scytale-ciphers.git
cd pigpen-masonic-scytale-ciphers

Run the Program:
python -m main.main

Kur te ekzekutohet programi do te shfaqet nje menu ku duhet te zgjdihni algoritmin me te cilin deshironi te enkriptoni ose te dekriptoni:

========================================
CLASSICAL ENCRYPTION ALGORITHMS
========================================
1. Pigpen
2. Scytale
3. Masonic
4. Exit
========================================

Pasi qe keni zgjedhur algoritmin duhet te zgjedhni si a doni te enkriptoni apo te dekriptoni:

1. Encrypt
2. Decrypt
Choose:

Ku enkriptimi e konverton plaintext ne ciphertext me algoritmin qe keni perzgjedhur ndersa dekriptimi e kthen ciphertext ne plaintext.

Nese zgjidhni opsionin 4 programi perfundon ndersa nese zgjidhni 5 ose me shume pragrami shfaq error.

##2.Pershkrimi i algoritmeve

1.Pigpen
2.Masonic
3.Scytale transposition

Scytale transposition eshte nje nder metodat per me te vjetra per enkriptim ku ne fillim eshte perdoru nga Spartanet ne Greqine e lashte per komunikime ushtarake. Te ky algoritem ne vend se te behet zevendesimi i shkronjave ketu vetem nderrohet renditja e tyre.

Pajisja perbehet nga nje scytale shkop druri rreth te cilit mbeshtillet nje shirit pergamenti ose lekure ne menyre spirale. Pastaj mesazhi shkruhej ne menyre horizontale pergjate shiritit dhe kur shiriti largohej nga shkopi shkronjat dukeshin te perziera dhe nuk kishin kuptim. Si celes eshte perdorur diametri i shkopit pasi vetem nje shkop me te njejtin diameter mund ta bente dekriptimin e atij mesazhi.

Tek ky algoritem teksti organizohet ne nje matrice dhe celesi i cili tregon numrin e kolonave. Nese teksti nuk e mbushte matricen atehere shtohen karaktere plotesues. Pas kesaj teksti i enkriptuar krijohet duke lexuar karakteret kolone pas kolone.

Dekriptimi funksionon ne menyre te kundert pra ciphertext vendoset perseri ne kolona sipas te njejtit celes dhe me pas lexohet rresht pas rreshti per te rikthyer mesazhin origjinal.
