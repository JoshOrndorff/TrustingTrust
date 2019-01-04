Reflections on Trusting Trust
-----------------------------

These programs are basic python implementations of the compilers and other programs from Ken Thompson's [Turing Award Lecture](https://www.archive.ece.cmu.edu/~ganger/712.fall02/papers/p761-thompson.pdf). I encourage you to read the three-pager and consider the problems he suggests before looking at my solutions.

Programs
--------
Spoiler Warning: **Quine** is the first challenge that Thompson presents. It is a program that exactly reproduces its own source code.

**HonestLogin** is a correctly-written python program to let a user enter if they know the secret password. This program is ultimately the target of our attack.

**TrojanLogin** is a backdoored version of the Honest Login. Because the code is obviously malicious, it would be easy to detect and the attack would likely not succeed.

**Honest Compiler** is a very simple string processor. So simple in fact that it's only job is to output the exact same string that it took in.

Spoiler Warning: **Trojan Compiler** is an intentionally incorrect version of the honest compiler that works correctly in most cases, but not when compiling the honest login or the honest compiler. Thus it conceals its identity.


Authors
-------

Joshy Orndorff

Isaac Defrain
