# aixcelerate-mood-guesser

## Project Description

Mood Guesser is a beginner-friendly Python project
that predicts whether a sentence expresses a Happy
or Sad mood.

It uses keyword matching and a simple word-scoring
learning method.

## Level 1: Counting Moods

The training dataset contains:
- Happy sentences: 8
- Sad sentences: 7

## Level 2: Guessing the Mood

The program uses 10 Happy clue words and
10 Sad clue words.

It ignores capital letters and punctuation.

When both mood counts are equal, the program
chooses Happy.

## Level 3: Testing

Accuracy on the 5 practice sentences: 100%

1. Which sentence went wrong (or was closest
to going wrong), and why?

My answer:
Today was a great day. It was closest to going
wrong because only one clue word, "great",
matched the Happy word list.

2. One change that would make my program better:

My answer:
I could improve the program by handling
negation words such as "not" and by adding
more training examples.

## Learning Questions

1. Total score of "good party today" and its mood:

+3, Happy.

2. Total score of "bad exam day" and its mood:

-3, Sad.

3. Why did "exam" get a score of 0, and is that good or bad?

It appeared once in a Happy sentence and once
in a Sad sentence. Therefore, its score became
zero. This is useful because it does not favour
either mood, although it may lose useful context.

4. Why is "not good" labelled Happy by this method,
and how could it be fixed?

The method gives "good" a positive score but
does not understand the meaning of "not".
It could be improved by detecting negation words.

## AI Declaration

I used an AI tool: NO

## Reflection
The hardest thing to organize all sub functions together in the right place and perform each respective level without any errors. 

[Write your own honest reflection here.]
