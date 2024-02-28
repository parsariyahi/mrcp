# **MRCP**
Morse code Protocol written in python, this project is for sake of learning and fun and does not have real-world use cases except that you want to talk to your friends with **Morse code**. <br>
This project has all the features that a simple protocol has, **request format**, **encoder**, **decoder**. <br>
**MRCP** is working on top of **TCP** connections, and the structure is ``Request``-``Response``.

## Request Format
Morep request example:
```
Chunk-Size = 47
Morse-Code = 0100.111.0001.0/1011.111.001./1000.01.1000.1011
```

### Chunk-Size
**Chunk-Size** represent the **lenght** of the morse code that sent with this request, this value will tell ``MRCP`` how many bytes need to read to get the full request data, You need to send this value as ``Integer``.

### Morse-Code
**Morse-Code** is the actual data that sent over ``MRCP`` protocol, This value contains: [``0``, ``1``, ``.``, ``/`` ], You need to send this value as ``String``.

## Translation Rules
First of all, we translate the ``words`` into ``morse code`` and send it over ``MRCP``, Rules are:

### **0** - **Zero**
**Morse code** use ``.`` as one of it's component, in ``MRCP`` we use ``0`` to represent that.

### **1** - **One**
**Morse code** use ``-`` as one of it's component, in ``MRCP`` we use ``1`` to represent that.

### **.** - **Dot**
**Morse code** use ``Space`` for seperating the characters from eachother, we use ``.`` to represent that.

### **/** - **Slash**
**Morse code** use ``/`` for seperating the words from eachother, we use ``/`` to represent that.

### Example
```
Real Morse code: .-.. --- ...- . / -.-- --- ..- / -... .- -... -.--
MRCP Format: 0100.111.0001.0/1011.111.001./1000.01.1000.1011
```

## Encoder, Decoder
Encoder will encode the words into ``MRCP`` style ``Morse code`` and decoder will decode the ``MRCP`` style ``Morse code`` into words.