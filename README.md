# **Blackjack Challenge**

## Table of Contents
1. [About the Project](#About-The-Project)
2. [Assumptions and Choices](#Assumptions-and-Choices)
3. [What I Did Well](#What-I-Did-Well)
4. [Rationale/Tradeoffs on Design/Algorithmic Decisions](#Rationale/Tradeoffs-on-Design/Algorithmic-Decisions)
5. [What I Would Improve](#What-I-Would-Improve)
6. [Manual Tests](#Manual-Tests)
6. [Automated Tests](#Automated-Tests)


# About the Project
This simple interactive Blackjack game is built in Python and runs in terminal. The player can choose to either hit or stand by typing ‘H’ or ‘S’ when prompted. No dependencies need to be installed to play the game. 

# Assumptions and Choices 
The first assumption I made regards the instruction: 

> “Hit until the hand’s score is greater or equal to 17 [...]. Otherwise, at some point the dealer will stand.”
 
This directive was a little bit ambiguous to me as I originally interpreted this as: 

> “As soon as the Dealer’s hand sums to >= 17, they stop drawing cards.”

Excluding the possibility of an instant blackjack, there are two possible outcomes: the dealer’s hand summing up to be greater or equal to 17 can either be greater than the Player’s hand or less than or equal to the Player’s hand.  
1.  Player hand sum = 19, Dealer hand sum = 17

In Case #1, although the Dealer’s hand is greater than or equal to 17, the value of the Dealer’s hand is still lower than the Player’s hand. If I were to go along with my original interpretation, then the game would end and the Player would win since 19 >= 17. 

2.  Player hand sum = 18, Dealer hand sum = 19

In Case #2, when the Dealer’s hand is greater than the Player’s hand (and less than or equal to 21), then the Dealer will evidently win. 

The issue with this interpretation is that it is unrealistic. In Case #1, if the Dealer’s hand is greater or equal to 17 but less than the Player’s hand, realistically they would choose to hit (add another card to their sum) as this would give them a chance at winning. Otherwise, if the Dealer chooses to stand on 17 and end their turn regardless of the Player’s hand total, then the Dealer would have a 0% chance of winning if the Player’s hand is > 17. Therefore, I added the condition that the Dealer keeps drawing cards if the total sum of his cards is less than 17 or if his hand is less than or equal to the hand of the Player (**line 87**). The assumption that I made is thus: 
> “As long as the Dealer’s hand is < 17 or if the sum of the cards in his hand is less than that of the Player, the Dealer keeps hitting.” 

Under this interpretation, there would not be a tie outcome since the Dealer would either bust or reach a value greater than the Player’s hand.

In addition to this, since not all outputs for all cases were given in the project file: 
> (Player/Dealer Blackjack, Player/Dealer Bust → Player/Dealer wins! , Player/Dealer both valid → Player/Dealer wins!) 

I made a few assumptions with regards to how to print the hands. For instance, when either player busts, their hand is not re-printed and the statement is displated: 
> “Player busts with 25”

In the case where the player busts with 25, the output is immediately followed by: 

> “Dealer wins!”

Additionally, the comparison between the Player’s hand and Dealer’s hand is only printed when both hands are less than or equal to 21:
> “A 5 4 = 20 to Dealer’s K 6 A = 17”

# What I Did Well
The most important strength of this project was the modularized Object Oriented design. The program contained separate classes for the Cards, Deck, User and Game. Under this model, basic inheritance could be implemented - in the user class, both the Player and Dealer were considered a user and shared the property of having a hand with a score and being able to draw cards. This made it easier to debug the code since I could easily pinpoint the class that any errors came from. Object Oriented designs also allow for more flexibility through polymorphism. For instance, the action of drawing a card was available to both the Player and Dealer. 

Another key strength was carefully architecturing the program prior to coding. On a sheet of paper, I decided on different classes as well as their respective functionalities which allowed for a smoother coding process. 

Input check was also implemented as the program forces the user to enter a valid input: either ‘H’ or ‘S’. For the future, instead of reprinting the current hands, a short error message such as “Invalid input! Please try again” could be implemented. 

Finally, I added a couple tests to check the base functionality of the program. I also made use of a pdb debugger to confirm that the correct values were being passed in. Since time was limited, I wasn’t able to verify each action and feature. This will be further elaborated in the testing section of this README. 

# Rationale/Tradeoffs on Design/Algorithmic Decisions
The biggest consideration was deciding whether to program the game functionally or using an object-oriented approach. Ultimately, I decided on the latter because it helped simplify the code. As previously mentioned, I was able to split the game into several classes: Card, Deck, User and Game. Not only did this improve the readability of the code, but it also reduced code usage and allowed for inheritance and basic polymorphism. 

One of the most difficult concepts in the game was to determine whether or not the A (ace) card should take on the value of 1 or 11. 

First, we should understand the implementation of the card deck (class Card (**line 3**)). In this class, there is a static method that defines a map to store the literal values of the deck: 2-10, J, Q, K, A. Then, each of these cards is mapped to a value: 2-2, 3-3, 4-4, 5-5 [...],  

It is possible that either the Dealer or Player draws multiple A cards which could make calculating the optimal value difficult. For instance, if a hand were to be: 
> [A, 7, 2, A] → 11 + 7 + 2 + 1 = 21

The optimal value in this case would be 21 as shown above. However, there are three other options as each A can take on the value of 1 or 11. These options would be: 
> [A, 7, 2, A] → 1 + 7 + 2 + 1 = 11
>
> [A, 7, 2, A] → 1 + 7 + 2 + 11 = 21
>
> [A, 7, 2, A] → 11 + 7 + 2 + 11 = 31

If we were to have 3 A cards in our hand, we would have four different possibilities ([1,1,1], [1,1,11], [1,11,11], [11,11,11]). It is clear that the optimal value is the sum closest to 21 without surpassing it. We can then implement a greedy approach where A always takes on the larger value of 11, unless the sum of the hand is greater than 21 in which case it is 1. This is represented in the for loop in **lines 49-52**. We start off with the largest possible sum where each A has a value of 11. Then, for each A in the hand while the score is greater than 21, we subtract 10, giving it a value of 1. In this way, we are sure to obtain the optimal score. We return the closest value to 21 without being greater than it.  

# What I Would Improve
Given more time, I would definitely add more automated tests to verify all aspects of my program. The automated tests I implemented will be discussed below. I could have also made use of a Python linter to check syntactical and stylistic problems in the code. Additionally, I think that more documentation and comments throughout the code would have allowed for other readers to better understand. Ideally, each function would include its documented purpose, additional information, requirements, side effects and efficiency.  

# Manual Tests
Extensive manual testing was run on the code. Even prior to finishing the program, minor checks were done along the way to ensure that the correct values were being outputted and the deck contained all 52 cards. For instance, to test the process of choosing an optimal value of a hand with A in it, I manually set my hand to be [2, 3] and the card being added to the Player’s hand to be A. Then, I continuously added the card A to my hand and printed out the optimal score which resembled: 
> [2, 3, A] → 16
> 
> [2, 3, A, A] → 17
>
> [2, 3, A, A, A] → 18
>
> [...]

The case where the Player obtains a Blackjack was also manually tested as I tried multiple combinations that summed up to 21, including those that contained A. 
Finally once the program was finished, I ran it multiple times ensuring that I got every possible outcome: 
> (Player/Dealer Blackjack, Player/Dealer Bust → Player/Dealer wins! , Player/Dealer both valid → Player/Dealer wins!)

 once without A in the hand and once with one or more values of A in the hand. 

# Automated Tests
Finally, a few short automated tests were created to test the program which can be run by entering “python3 game.py --test”. These basic tests include:
1. Asserting Card() creates an instance of card with the correct corresponding value, 
2. Asserting that the completed deck contains all 52 cards 
3. Asserting that after dealing a card from the full deck, the size of the deck is 51. 

In the future more tests, both unit and integration, would be implemented to test for all in-game features and actions. 
