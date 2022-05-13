import os
import struct
from sys import argv
from randomgen import ChaCha
import numpy as np

print(argv)

def initialGeneration() :
    NO_ROUNDS = int(argv[2])

    baseKeys = []
    for i in range(4) :
        baseKeys.append(os.urandom(4))
    baseKeys = list(map(lambda x : struct.unpack('i', x)[0], baseKeys))
    print(baseKeys)

    seed = 0
    for baseKey in baseKeys :
        seed = seed ^ baseKey
    seed &= 0x7FFFFFFF

    roundKeys = []

    rg = np.random.Generator(ChaCha(seed, rounds=20))
    for i in range(4*(NO_ROUNDS+2)) :
        roundKeys.append(rg.integers(0,2**32))
    
    res = np.append(np.array(baseKeys), np.array(roundKeys))
    np.savetxt("Keys.txt", res, fmt="%d", newline=" ")

def roundKeyGen() :
    NO_ROUNDS = int(argv[2])

    baseKeys = np.loadtxt("Keys.txt", dtype=np.int64)[:4]
    print(baseKeys)
    
    seed = 0
    for baseKey in baseKeys :
        seed = seed ^ baseKey
    seed &= 0x7FFFFFFF

    roundKeys = []

    rg = np.random.Generator(ChaCha(seed, rounds=20))
    for i in range(4*(NO_ROUNDS+2)) :
        roundKeys.append(rg.integers(0,2**32))
    
    np.savetxt("KeysDcryp.txt", roundKeys, fmt="%d", newline=" ")

if(argv[1] == '0') :
    initialGeneration()
else :
    roundKeyGen()