train_data = [
    ("I got full marks in the test today!", "Happy"),
    ("We won the college cricket match", "Happy"),
    ("My friends planned a surprise party for me", "Happy"),
    ("The food in the canteen was really tasty", "Happy"),
    ("I am so excited for the weekend trip", "Happy"),
    ("Our project got selected for the exhibition", "Happy"),
    ("I finally learned how to ride a bicycle", "Happy"),
    ("Mom made my favourite sweets today", "Happy"),
    ("I lost my phone on the bus", "Sad"),
    ("I failed in the mathematics exam", "Sad"),
    ("My best friend is moving to another city", "Sad"),
    ("It rained and our picnic was cancelled", "Sad"),
    ("I missed the last bus and felt very upset", "Sad"),
    ("My laptop stopped working before the submission", "Sad"),
    ("I felt lonely during the long holidays", "Sad")
]
def clean_sentence(sentence):
    cleaned = ""

    for char in sentence.lower():
        if char.isalnum() or char.isspace():
            cleaned += char
        else:
            cleaned += " "

    return cleaned.split()


#LEVEL 1


def count_moods(data):

    happy_count = 0
    sad_count = 0

    for sentence, mood in data:

        if mood == "Happy":
            happy_count += 1

        elif mood == "Sad":
            sad_count += 1

    return happy_count, sad_count


print("LEVEL 1: COUNTING MOODS")

print("Mood Count:", count_moods(train_data))


#LEVEL 2

happy_words = [
    "full",
    "won",
    "friends",
    "surprise",
    "tasty",
    "excited",
    "selected",
    "learned",
    "favourite",
    "great"
]

sad_words = [
    "lost",
    "failed",
    "moving",
    "rained",
    "cancelled",
    "missed",
    "upset",
    "stopped",
    "lonely",
    "laptop"
]


def guess_mood(sentence):

    words = clean_sentence(sentence)

    happy_count = 0
    sad_count = 0

    for word in words:

        if word in happy_words:
            happy_count += 1

        if word in sad_words:
            sad_count += 1

    if happy_count > sad_count:
        return "Happy"

    elif sad_count > happy_count:
        return "Sad"

    else:
        # neutral or unclear words alone do not
        return "Happy"


print("\nLEVEL 2: MOOD GUESSER")

print("Example 1:", guess_mood("I won a prize today!"))
print("Example 2:", guess_mood("I lost my phone!"))

#LEVEL 3

practice_data = [
    ("I won a medal in the sports meet", "Happy"),
    ("I lost my notebook before the exam", "Sad"),
    ("My friends gave me a lovely surprise", "Happy"),
    ("The train was late and I felt upset", "Sad"),
    ("Today was a great day", "Happy")
]


def test_program(data):

    correct = 0

    print("\nLEVEL 3: TESTING RESULTS")

    for sentence, actual_mood in data:

        predicted_mood = guess_mood(sentence)

        print("\nSentence:", sentence)
        print("Actual Mood:", actual_mood)
        print("Predicted Mood:", predicted_mood)

        if predicted_mood == actual_mood:
            correct += 1

    accuracy = (correct / len(data)) * 100

    print("\nCorrect Predictions:", correct)
    print("Total Sentences:", len(data))
    print("Accuracy:", accuracy, "%")

    return accuracy


level2_accuracy = test_program(practice_data)


def learn_scores(data):

    scores = {}

    for sentence, mood in data:

        words = clean_sentence(sentence)

        for word in words:

            if word not in scores:
                scores[word] = 0

            if mood == "Happy":
                scores[word] += 1

            elif mood == "Sad":
                scores[word] -= 1

    return scores


word_scores = learn_scores(train_data)

def guess_mood_learned(sentence):

    words = clean_sentence(sentence)

    total_score = 0

    for word in words:

        total_score += word_scores.get(word, 0)

    if total_score > 0:
        return "Happy"

    else:
        return "Sad"


def test_learned_model(data):

    correct = 0

    print("\nBONUS: LEARNED MODEL RESULTS")

    for sentence, actual_mood in data:

        predicted = guess_mood_learned(sentence)

        print("\nSentence:", sentence)
        print("Actual:", actual_mood)
        print("Predicted:", predicted)

        if predicted == actual_mood:
            correct += 1

    accuracy = (correct / len(data)) * 100

    print("\nLearned Model Accuracy:", accuracy, "%")

    return accuracy


learned_accuracy = test_learned_model(practice_data)



print("\nMODEL COMPARISON")

print("Level 2 Accuracy:", level2_accuracy, "%")

print("Learned Model Accuracy:", learned_accuracy, "%")
