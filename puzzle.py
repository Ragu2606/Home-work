from msilib import knownbits
from multiprocessing.pool import IMapIterator
from pkgutil import ImpImporter
from socket import IOCTL_VM_SOCKETS_GET_LOCAL_CID
from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # A is either a Knight or a Knave.
    Or(AKnight, AKnave),
    # If A is a knight, He is not a Knave.
    Implication(AKnight, Not(AKnave)),
    #If A is a knave, He is not a Knight.
    Implication(AKnave, Not(AKnight)),
    # A translated: If and only if i'm a Knight and also a Knave.
    Biconditional(AKnight, And(AKnight,AKnave)) 
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And( 
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Implication(AKnight, Not(AKnave)),
    Implication(AKnave, Not(AKnight)),
    Implication(BKnight, Not(BKnave)),
    Implication(BKnave, Not(BKnight)),
    Biconditional(AKnight, And(AKnave,BKnave))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Implication(AKnight, Not(AKnave)),
    Implication(AKnave, Not(AKnight)),
    Implication(BKnight, Not(BKnave)),
    Implication(BKnave, Not(BKnight)),   
    Biconditional(AKnight, Or(And(AKnight, BKnight),
                              And(AKnave, BKnave)),
    Biconditional(BKnight, Or(And(AKnight, BKnave),
                              And(AKnave, BKnight)))
    ))
# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Or(CKnight, CKnave),
    Implication(AKnight,Not(AKnave)),
    Implication(AKnave, Not(AKnight)),
    Implication(BKnight,Not(BKnave)),
    Implication(BKnave, Not(BKnight)), 
    Implication(CKnight,Not(CKnave)),
    Implication(CKnave, Not(CKnight)),   
    Biconditional(Or(AKnight, AKnave), Or(AKnight, AKnave)),
    Biconditional(BKnight, Biconditional(AKnight, AKnave)),
    Biconditional(BKnight, CKnave),
    Biconditional(CKnight, AKnight)
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
