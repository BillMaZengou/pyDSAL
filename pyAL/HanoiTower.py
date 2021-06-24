def moveTower(height, fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height - 1, fromPole, withPole, toPole)
        moveDisk(fromPole, toPole)
        moveTower(height - 1, withPole, toPole, fromPole)

def moveDisk(fp, tp):
    print("Moving disk from", fp, "to", tp, ".")

def main():
    moveTower(2, "Pole 1", "Pole 3", "Pole 2")

if __name__ == '__main__':
    main()
