This program is a brute-force tool in Python. It finds several passwords from the list TARGETS. The program makes all possible combinations of characters from the alphabet until it finds each password. For each password, it shows the password, the number of tries, and the time it took. It also makes a graph that shows time versus tries. The graph updates for each password. The tries axis is in logarithmic scale.

Open the repository in VSCode.
Open a terminal in the folder where the file bruteforce.py is.
Run the program with:
python bruteforce.py
The program will try all combinations until it finds all passwords in the TARGETS list.
Each time it finds a password, it prints:
The password found
The number of tries
The time it took
It also shows a graph that updates for each password, showing time versus tries.
The program will try all combinations until it finds all passwords in the list TARGETS. Each time it finds a password, it prints the password, the number of tries, the time, and shows a graph.
Example output:

Brute-force for 5 passwords.
Password found: 123
Tries: 482370
Time: 1.397849 s

Password found: abc
Tries: 446646
Time: 0.745427 s

Password found: XYZ
Tries: 1020
Time: 0.120345 s

Password found: 456
Tries: 509163
Time: 2.006777 s
Password found: pass
Tries: 13299985
Time: 18.580420 s

Each password shows a graph with the progress of tries and time.
Reflection:
If the password is long (8 or more characters) and uses capital letters, numbers, and symbols, it will take a very long time to find it. 
For example, with 94 characters in the alphabet: a 3-character password has 94^3 combinations (~830,000), but an 8-character password has 94^8 combinations (~6.1 × 10^15). 
This is almost impossible to find with brute force. So this program works only with short and simple passwords.

Summary of steps in the code:

Make a list of passwords (TARGETS) and a character alphabet.

Use a while loop to find all 5 passwords.

Make all possible combinations for each length until each password is found.

Each time a password is found, print the password, the number of tries, the time, and show a graph.

Test with short passwords to see how time grows. It is very hard to use brute force for long passwords or passwords with symbols.
