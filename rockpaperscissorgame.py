import random
c=random.randint(0,2)
print("Welcome to the world of rock,paper and scissors.\n0 is for rock, 1 for paper and 2 for scissor.")
print("Choose your choice:")
i=input()
if i=='0':
    print("""
                            _______
                        ---'   ____)
                              (_____)
                              (_____)
                              (____)
                        ---.__(___)""")
    print("Computer chooses:")
    if c==0:
        print("""
                            _______
                        ---'   ____)
                              (_____)
                              (_____)
                              (____)
                        ---.__(___)""")
        print("It's a draw")
    if c==1:
        print("""
                             _______
                        ---'    ____)____
                                   ______)
                                  _______)
                                 _______)
                        ---.__________)""")
        print("You lose")
    if c==2:
        print("""
                            _______
                        ---'   ____)____
                                  ______)
                               __________)
                              (____)
                         ---.__(___)""")
        print("You win")

if i=='2':
    print("""
                            _______
                        ---'   ____)____
                                  ______)
                               __________)
                                  (____)
                            ---.__(___)""")
    print("Computer chooses:")
    if c==0:
        print("""
                            _______
                        ---'   ____)
                              (_____)
                              (_____)
                              (____)
                        ---.__(___)""")
        print("You lose")
    if c==1:
        print("""
                             _______
                        ---'    ____)____
                                   ______)
                                  _______)
                                 _______)
                        ---.__________)""")
        print("You win")
    if c==2:
        print("""
                            _______
                        ---'   ____)____
                                  ______)
                               __________)
                              (____)
                         ---.__(___)""")
        print("It's a draw")

if i=='1':
    print("""
                             _______
                        ---'    ____)____
                                   ______)
                                  _______)
                                 _______)
                        ---.__________)""")
    print("Computer chooses:")
    if c==0:
        print("""
                            _______
                        ---'   ____)
                              (_____)
                              (_____)
                              (____)
                        ---.__(___)""")
        print("You win")
    if c==1:
        print("""
                             _______
                        ---'    ____)____
                                   ______)
                                  _______)
                                 _______)
                        ---.__________)""")
        print("It's a draw")
    if c==2:
        print("""
                            _______
                        ---'   ____)____
                                  ______)
                               __________)
                              (____)
                         ---.__(___)""")
        print("You lose")
