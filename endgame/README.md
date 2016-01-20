#Codebreaking for Traditional Cipher Systems

* Information theory provides general insights about the security of various encryption schemes. However, cracking an "insecure" cipher often requires a lot of clever probabilistic inference, for instance in the form of sampling schemes like Gibbs sampling of the posterior distribution over encryption keys.

* Historically, cracking the German Enigma encryption machine was such a task, you can read about it in Section 18.4 of [MacKay]. More recently, Kevin Knight and colleagues has also written a number of papers on codebreaking from an explicitly Bayesian viewpoint (e.g., this one).

* If you like a programming challenge, you can also try to decipher the encrypted texts listed under this topic on Mathias' page and report on your findings.

#Codebreaking for Traditional Cipher Systems(Mathias Page)
This topic is a practical challenge: I provide a number of texts, each of which are encrypted using a different type of encryption scheme. Your task will be to squeeze information out of these ciphers by any means you want, documenting the methods you used and the successes and failures they led to. It is absolutely not necessary that you crack all of the ciphers, or even try to do so.

The encrypted texts are all in English, and they were snipped quite randomly out of Project Gutenberg books. In some cases, they were transformed to uppercase letters only. In other cases, they were preserved in the original form.

The resulting ciphers are the following:

* A substitution cipher.
* A permutation cipher.
* A running key cipher, here represented as the sum of two ASCII codes (e.g., A + Z = 65 + 90 = 155). Both the key and the encrypted text were converted to uppercase before encryption.
* An Enigma-style, periodic, polyalphabetic cipher.
* A cipher encrypted with both substitution and permutation.
* A Zodiac-style homophonic cipher encrypted by means of a Chinese restaurant process so that each letter can have several translations. The plaintext behind this cipher was converted to uppercase before encryption.