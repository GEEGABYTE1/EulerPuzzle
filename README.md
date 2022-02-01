# A Dynamic Solution to Euler's 243 Year old 'Impossible Puzzle' 🧩

Instead of using Quantum Algorithms and vectors, this puzzle can be seen as nothing but just pattern recognition! There were two "attempted" methods to solve this problem, but only one was successful due to space and time complexity, and the computer tangling itself up. 

It should be noted that there are multiple solutions to this puzzle, and mine is just one of many ways we can visualize a possible solution to the 6x6 board.

How I viewed the board was not by separate peices and their ranks, but each class and their ranks. Each number denotes a class, which involves upto a pawn, queen, king, bishop, rook, and a knight. The corresponding colours represent their ranks. 

The solution originally came to me when I was looking at the 5x5 board and realized something in common. A common pattern was that each class had the same colour diagonally when the board was solved. I then took that pattern into consideration and tried to extend it with a 6x6.

# Solution ✅

My solution consists of array itration. I had noticed that the peices do not repeat in their columns if you move the first element to the back at each array. This iteration was done relative to either 5 or 6 times depending on the length of the board. I intially started this iteration with colous, then with peices to illustrate that the solution was nothing more, than just patterns. 

After combining the colours and classes, we can notice that there is no repeating colour or class in any column. 

*Note*: Repetition in rows is not counted for as we assume each peice is different in a class with a different colour. This is our initial setup.

What had been seen is the same pattern noticed in the 5x5 puzzle, of which, the same classes were aligned with the same colour diagonally, which mean't that our solution worked. 

With a simple array iteration and outcomes from the Matrix Method, I have managed to solve the puzzle without any quantum algorithms.

# Matrix Method #️⃣

My first solution or method consisted of creating a matrix, which could be found under `script.py`. This method was more brute-force than pattern recognition. Instead of at a class as a whole, we looked at individual peices, which at the end, noticed that it was far more complex to work with. 

For each new peice, we would run two search algorithms, one for columns, and one for rows. Then we ran a few conditionals for the new peice, which consisted of:
 - If the whole row was empty
 - If this new peice was not in the current column 
 - If this new peice was not in the current row

Surprisingly, although having a time complexity of `n!`, where n was the length of the matrix, the method worked, but for only for half the board. What I ended up noticing with multiple trials and iterations, and even random sampling, was that the computer didn't know it was tangling itself up at times. It only considered the conditionals above, but not the future possiblities of the row.

For example, let's say we peices 3,4,5 (bishop, queen and king) that need to be put. All three of them are new peices in the row. However, there is a bishop in third column and a king in the 5th column. By my conditionals and my linear search algorithms for simplicity over performance, the computer would put the next peice that has not been put, in this case, the queen in the bishop's spot and the bishop in the queen's spot. This solution would work to permute the bishop and queen, but not for the king as the only spot left in the row was the king, which is already placed in the same column in another row. The result of this is the fact that the computer would tangle itself up and end up in an infinite loop. 

To reduce this error, I have tried possible permutation algorithms including tring to only permute the three top rows only for the bottom three to make it easier. It did work, however, just like how I stated above about each class having different peices, the matrix only showed two of peices of each set, and not all. If I did work with all 6 rows, the computer seems to get mixed up when approaching to the last row, as it starts to add multiple of the same ranks or peices. After a few trials, I realized it was because the computer's random sampling module was being exercised a lot. 

*Note*: After noticing these deffects, I had stopped working on this solution.

Though, it is possible to make my solution work. Maybe a cleaner, more dynamic approach by coming from two separate ends of the list and running 2 search algorithms on both the left side elements and the right side elements would have been more efficient. It would have also made the computer more aware of the possible outcomes of putting a certain element in a row at the time.

# Summary 🔮

My array-iteration solution is elementary, but it works. Array-iteration instead of quantum algorithms may break down when working with larger grids due to computation power. However, the dynamic approach possiblilities of the Matrix Method and noticing these patterns just through simpe computer science concepts depicts that computer science can also be an artistic method to solve such intriguing problems. 

I have not timed the solution, but it would be fairly slow compared to other languages. Moreover, my array-iteration solution came after working weeks with the Matrix Method and looking at the 5x5 solution for hours! 

Made in Python 🐍