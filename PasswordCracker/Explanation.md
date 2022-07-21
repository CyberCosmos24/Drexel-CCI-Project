# Brute Force Password Cracker
The brute force password cracker is `brute-password.py`.
It works by trying every possible combination of letters from the min password length up to the max password length.


# Brute Force Hash Cracker
The brute force hash cracker is `brute-hash.py`.
It works by trying every possible combination of letters from the min password length up to the max password length and hashing that to compare it with the input hash. 
If the user knows the hash algorithm that was used, they can put that in. Otherwise, they can select the UNKNOWN option and the program will try all of the available hash algorithms.


# Wordlist Password Cracker
The wordlist password cracker is `wordlist-password.py`.
The worlist password cracker works by using wordlists of the most common passwords to crack the password. It also tries common substitutions for letters such as in P@$$w0rd. 
* The user can select from 4 speed options:
```
|  Option   | Key | Password Variations | Time Est  |
|-----------|-----|---------------------|-----------|
| Very Slow |  V  |    15.5+ Billion    |   Days    |
|   Slow    |  S  |    124.5 Million    |  ~7 Min.  | 
|  Medium   |  M  |    18.45 Million    |  ~2 Min.  |
|   Fast    |  F  |    430 Thousand     |  ~2 Sec.  |
```
* They can also input a number of Brute Force Letters. The brute force letters are letters added to the end where the computer brute force guesses all of the options for those characters. This makes sure the program can find something like password7*, where the user just adds some random symbols or number onto the end of their password. (Note: Adding Brute Force letters will increase the time significantly.)

# Wordlist Hash Cracker
The wordlist hash cracker is `wordlist-hash.py`.
The worlist hash cracker works by using wordlists of the most common passwords and then hashing them to compare them with the input hash. It also tries common substitutions for letters such as in P@$$w0rd.
* If the user knows the hash algorithm that was used to hash the password, they can input it. Otherwise, they can select the UNKNOWN option which will try all of the available hash algorithms and let the user know which hash algorithm succeeded.
* The user can select from 4 speed options:
```
|  Option   | Key | Password Variations | Time Est  |
|-----------|-----|---------------------|-----------|
| Very Slow |  V  |    15.5+ Billion    |   Days    |
|   Slow    |  S  |    124.5 Million    |  ~7 Min.  | 
|  Medium   |  M  |    18.45 Million    |  ~2 Min.  |
|   Fast    |  F  |    430 Thousand     |  ~2 Sec.  |
```
* They can also input a number of Brute Force Letters. The brute force letters are letters added to the end where the computer brute force guesses all of the options for those characters. This makes sure the program can find something like password7*, where the user just adds some random symbols or number onto the end of their password. This is also helps in situations where the company may have added the first character or two of the users username to the end of the password before hashing it. (Note: Adding Brute Force letters will increase the time significantly.)
