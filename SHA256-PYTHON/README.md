# Implementation of SHA-256

## Sample test 
$ python hash.py
Type or copy your message here: Hello
Your message:  Hello
Hash:  0001100001011111100011011011001100100010011100011111111000100101111101010110000110100110111111001001001110001011001011100010011001000011000001101110110000110000010011101101101001010001100000000000011111010001011101100100100000100110001110000001100101101001
Length:  256

## A beginner's script to implement the SHA-256 in Python from scratch.

SHA256 is a special tool that helps us keep our secrets safe. Just like how you have a secret password to access your phone or computer, there are secrets that we want to keep safe when we send them over the internet or store them on a computer.

SHA256 takes in any kind of message, like a sentence or a file, and turns it into a unique code called a "hash". This hash code is like a digital fingerprint that uniquely identifies the message. No two messages can have the same hash code, just like no two fingerprints are exactly the same.

SHA256 does this by taking the input message and chopping it up into small pieces called "blocks". Then it uses a series of complicated mathematical operations to scramble these blocks up in a way that is very hard to reverse. Think of it like a puzzle where you have to put the pieces back together, but it's very hard to do so because the pieces have been mixed up in a complicated way.

Once SHA256 has scrambled up all the blocks, it produces a hash code that is unique to the input message. This hash code is a fixed length of 256 bits, which means it's a string of 256 binary digits. This code can be used to verify that the message hasn't been changed, tampered with, or hacked during transmission or storage.

In summary, SHA256 is a tool that helps us keep our secrets safe by turning them into unique codes that are very hard to reverse or hack. It does this by chopping up the message into blocks and scrambling them up in a complicated way, resulting in a fixed-length hash code that is unique to the input message.