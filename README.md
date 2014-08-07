Oulipean Glitching
==================
This project performs semantic glitching on JPEG files. The main script is written in Python. Semantic glitching is a way of filtering the several hundreds of thousands of characters that form the representation of a typical digital image. About one in every 10 characters is in the ASCII range 101 - 172 (e.g., the alphabet!). I build up these characters into a string and then search the string for English words occuring in sequence. This 'semantic' content is then shifted and deformed in various ways and the JPEG is re-saved with the changed information. This produces a glitching effect.

The bell control character is also used to produce pitched sounds (Windows only).
