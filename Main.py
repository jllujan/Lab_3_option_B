# Lab 3 option B : AVL Trees and Red-Black Trees
# Name: Jose Lujan
# ID: 80572649
# class: cs2302
# class time 10:30-11:50

from AVL_Node import Node
from AVL_Tree import AVLTree
from Red_Black_Node import RBTNode
from Red_Black_Tree import RedBlackTree


# Function creates an AVL tree holding values inside of given file
def create_avl(file_name):
    english_words = AVLTree()

    # Open file and read first line
    file = open(file_name, "r")
    line = file.readline()

    # Loop will go trough every line in the file
    while line:
        # Add each word, lowercased, to avoid searching errors
        new_word = Node(line.rstrip().lower())
        english_words.insert(new_word)
        line = file.readline()

    # Returns AVL Tree
    return english_words


# Function creates a Red-Black tree holding values inside of given file
def create_red_black(file_name):
    english_words = RedBlackTree()

    # Open file and read first line
    file = open(file_name, "r")
    line = file.readline()

    # Loop will go trough every line in the file
    while line:
        # Add each word, lowercased, to avoid searching errors
        english_words.insert(line.rstrip().lower())
        line = file.readline()

    # Returns Red-Black Tree
    return english_words


# Function that prints every node in tree, from left to right, recursively
def print_tree(tree_node):
    if tree_node is None:
        print("Your tree is empty.")
        return
    # Print left sub-tree
    if tree_node.left is not None:
        print_tree(tree_node.left)
    print(tree_node.key)
    # Print right sub-tree
    if tree_node.right is not None:
        print_tree(tree_node.right)


# Function that generates all possible permutations from a given word
def get_perms(word):
    if len(word) <= 1:
        return word
    else:
        perm_list = []
        for perm in get_perms(word[1:]):
            for i in range(len(word)):
                perm_list.append(perm[:i] + word[0:1] + perm[i:])
        return perm_list


# Function that prints all valid anagrams from a given word
def print_anagrams(word, tree):
    permutations = get_perms(word)

    for i in range(len(permutations)):
        if tree.search(permutations[i]):
            print(permutations[i])
    return


# Function that returns the number of valid anagrams from a given word
def count_anagrams(word, tree):
    permutations = get_perms(word)
    count = 0

    for i in range(len(permutations)):
        if tree.search(permutations[i]):
            count += 1

    return count


# Function that returns the word with the most possible anagrams from a given file
def most_anagrams(file_name, tree):
    try:
        if tree.root is None:
            print("Your tree is empty.")
            return None
        # Open file and read first line
        file = open(file_name, "r")
        line = file.readline()

        highest_anagrams = line.rstrip().lower()  # Variable that holds word with most possible anagrams
        highest_count = count_anagrams(highest_anagrams, tree)

        # Loop will go trough every line in the file
        while line:
            new_word = line.rstrip().lower()
            new_count = count_anagrams(new_word, tree)
            if new_count > highest_count:
                highest_anagrams = new_word
                highest_count = new_count
            line = file.readline()

        # Returns word with the most anagrams
        return highest_anagrams
    except FileNotFoundError:
        print("File not found. Please try again.")


# Main function
# It is asked to the user what operation he/she wishes to perform.
def main():
    print("Please select the type of binary search tree you would like to create: ")
    print()
    tree = input("Press 1 for AVL Tree.\nPress 2 for Red-Black Tree.\n")

    if tree == '1':
        print("Generating your AVL Tree.")
        avl_tree = create_avl("words.txt")
        keep_going = True
        while keep_going:
            print("Please type the number of the operation you would like to perform:")
            print("   1. Get the number of possible anagrams from a given word.")
            print("   2. Compare a list of words from a given file and obtain the word with the most possible anagrams.")
            print("   3. Print all possible anagrams from a given word.")
            print("   4. ")
            answer = input()

            if answer == '1':
                word = input("Please type the word to search for anagrams: ")
                print(count_anagrams(word, avl_tree))
            elif answer == '2':
                file = input("Please type the name of the file: ")
                highest_anagrams = most_anagrams(file, avl_tree)
                print("The word with the most anagrams is:", highest_anagrams)
            else:
                print("Option you typed, is not listed")

            loop = input("\nNew operation? y/n\n")

            if loop == 'y':
                keep_going = True
            elif loop == 'n':
                keep_going = False
            else:
                print("please try again.")


    elif tree == '2':
        print("Generating your Red-Black Tree.")
        red_black = create_red_black("words.txt")
        keep_going = True
        while keep_going:
            print("Please type the number of the operation you would like to perform:")
            print("   1. Get the number of possible anagrams from a given word.")
            print("   2. Compare a list of words from a given file and obtain the word with the most possible anagrams.")

            answer = input()

            if answer == '1':
                word = input("Please type the word to search for anagrams: ")
                print(count_anagrams(word, red_black))
            elif answer == '2':
                file = input("Please type the name of the file: ")
                highest_anagrams = most_anagrams(file, red_black)
                print("The word with the most anagrams is:", highest_anagrams)
            else:
                print("Option you typed is not listed")

            loop = input("\nNew operation? y/n\n")

            if loop == 'y':
                keep_going = True
            elif loop == 'n':
                keep_going = False
            else:
                print("Please try again.")
    else:
        print("You type an input which is not available, please run the program again.")


main()