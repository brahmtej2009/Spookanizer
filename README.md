![Banner](media/banner.png)

This project has been submitted to [3am, Hack Club](https://3am.hackclub.com/)

---
# SPOOKANIZER

Its halloween season! This is a spooky themed project, for adding more "spook" to your everyday online chats, and to encrypt them so no one else can see or understand those! This is a Python tool to make your text spooky and encrypted so it looks scary to those who dont know about this. You can convert the spooky text back to original text through this same tool! Everytime you generate something, it gets salted, so the same input would give different outputs everytime you run it, but all those outputs would always convert back to the original message! You can also replace the keys and salt in this project through the .env file to customize the themes! Check it out!

---

### Excited? Try reading this!
```
🜕⚶🐀🝢🖤🜛🜙🝤♀⚰⚵♆🝘🜛🜏🝣🝙🝨🜟🧛🜃🜎👻🝰🜍🜘🜂🖤🖤🜅⚶🎭🔮🜟🧛🧙⚰🝱🜛🜔🜦🜟⛥👻🕸🜟🕸🜈🜇🜜🏺🤡♂,🜣🜟🖤🝞🜛⚰🜛🜞🜏🜟🗿†🧛🜎🝔🝧👻🖤🖤🔮🜉🪰🝞🜟👺🜛🜌🐸§🝖☽🜟⛥👻🕸⚲🝥🜟⧔👻⚶☣🖤,🝕⚲🝦⨂🜟🖤🏰🜛🜘🝥⚰🜛🜏🜟🜙🝨🧛👻♀🖤🖤🝔🔮🌘🝠🜟🜏🕸🖤🜟🔮🜏👻🜧⚴🕸♆🝰🝫🖤⧔🜟🜝🜄🜜🔮🖤🝲🌑⧔🜟⧔🜛🦉🜛🜏☽🜝🝤🝘🝧🜟🜋🪱⛥👻🜃🜔⨂🕸!🜟🖤🜛⚰🜛🜏🝘🗡🜝🜟🧛👻🖤🖤🐸🝢🝣🜔🔮🜟👹🔮🜕🝤🜘🩸🜇🜛🜟⛥👻🌘🐸🐸♂🕸🜢🝨🜢🜟🜨🜕🧟🜏⛥,🜟🜂🝪🝜♀🖤🜛⚰🜛🜏🜟🌌⁜🧛👻🖤🖤🜖🝕🔮🜃🏺🜟🝟🦉🔮⛥🜠🜟🜅🜝🜤🜉🧛👻👻⧔🎃🜅🜣🜨⛥🜛,🜟🖤🜛⚰🜛🜏🜟🧛👻🖤🖤☉⚶🔮🜟⚱🝲⚶🝦☽🝣🜛👺👺🝳🜟🜙🔮🜟👺🜔🝙🗿†🧙🜛🜟🔮🜡🝘🖤🜥⧔🜟🪦🜅🜊🕸🝚🝩🜏☽🝕🜟🝭⛥👻🎭🝮🕸!🜟👺👻⛓🜢🪱⚳👺🜟🧛🝟⚳🝰🜛☽🜟🜏🜌🝡🧙🧟🩸🌘🜄🐀🝠🜏👻👺👺🝳⁜🜛⧔🜋!
```
_Translate this by using SPOOKANIZER to convert to text!_

---
# Use your own Key+Salt Combination
If you want to use an encryption which no one else, except the receiver can understand, you can customize the keys and salts so it renders differently. Keys are in a specific format, the first 26 characters would be for a-z, the next 10 would be for 1-0, and 1 for space, making total of 37 Keys.

Salts are words used to make the encrypted output more complicated and strange, these do not store any data, and are taken out while decoding. You can add as many salts as you want, and its strength can be adjusted in .env settings.

To make your own encryption, follow this .env File Template:
```
KEY=
SALT=
salting=true
saltstrength=4
salt-length=4
```
- Enter 37 Keys, spaced by a comma (,).
- Enter a good amount of Salts (Atleast 10 Suggested).
- `salting` disables or enables salting through `false` or `true`.
- `saltstrength` is number between 0-5 for increasing chance of salt appearing after a character. Setting to 6 ensures salt after every character.
- `salt-length` is the maximum amount of salt characters which would be inserted after every real character.


---
# CONTRIBUTE
Feel free to contribute to this project! If you feel you have found a bug, or have suggestions to improve it, contact me or file a PR! 

---
# LICENSE
- ### **MIT**