import random, sys
QUESTIONS = [
    {'question': "How many times can you take 2 apples from a pile of 10 apples?",
  'answer': "Once. Then you have a pile of 8 apples.",
  'accept': ['once', 'one', '1'],
  'options' : ['twice','two', 'six','once', 'one', '1']
  },
  {'question': 'What begins with "e" and ends with "e" but only has one letter in it?',
  'answer': "An envelope.",
  'accept': ['envelope'],
  'options' : ['box,', 'eye', 'envelope']
  },
 {'question': "Is it possible to draw a square with three sides?",
  'answer': "Yes. All squares have three sides. They also have a fourth side.",
  'accept': ['yes']},
  {'question': "How many times can a piece of paper be folded in half by hand without unfolding?",
 'answer': "Once. Then you are folding it in quarters.",
 'accept': ['one', '1', 'once'],
 'options' : ['two','one', '1', 'once','2']
 },
 {'question': "What does a towel get as it dries?",
  'answer': "Wet.",
 'accept': ['wet'],
  'options' : ['water', 'moist', 'wet']
 },
  {'question': "What does a towel get as it dries?",
  'answer': "Drier.",
  'accept': ['drier', 'dry'],
   'options' : ['water', 'drier', 'dry','moist', 'wet',]
  },
  {'question': "Imagine you are in a haunted house full of evil ghosts. What do you have to do to stay safe?",
  'answer': "Nothing. You're only imagining it.",
  'accept': ['nothing', 'stop'],
  'options' : ['gun', 'nothing', 'stop', 'pause',]
  },
  {'question': "A taxi driver is going the wrong way down a one-way street. She passes ten cops but doesn't get a ticket. Why not?",
  'answer': "She was walking.",
  'accept': ['walk'],
   'options' : ['hop', 'walk', 'run', 'fly',]
  },
  {'question': "What does a yellow stone thrown into a blue pond become?",
  'answer': "Wet.",
 'accept': ['wet'],
   'options' : ['wet', 'flooded', 'dry',]
 },
  {'question': "How many miles does must a cyclist bike to get to training?",
  'answer': "None. They're training as soon as they get on the bike.",
  'accept': ['none', 'zero', '0'],
   'options' : ['two', 'none', 'three', 'zero',]
  },
  {'question': "What building do people want to leave as soon as they enter?",
  'answer': "An airport.",
  'accept': ['airport', 'bus', 'port', 'train', 'station', 'stop'],
   'options' : ['school', 'airport', 'market', 'station',]
  },
  {'question': "If you're in the middle of a square house facing the west side with the south side to your left and the north side to your right, which side of the house are you next to?",
  'answer': "None. You're in the middle.",
  'accept': ['none', 'middle', 'not', 'any'],
    'options' : ['none', 'front', 'midddle', 'back',]
  },
  {'question': "How much dirt is in a hole 3 meters wide, 3 meters long, and 3 meters deep?",
  'answer': "There is no dirt in a hole.",
  'accept': ['no', 'none', 'zero'],
   'options' : ['none', 'four', 'zero', 'six',]
  },
  {'question': "A girl mails a letter from America to Japan. How many miles did the stamp move?",
  'answer': "Zero. The stamp was in the same place on the envelope the whole time.",
  'accept': ['zero', '0', 'none', 'no'],
   'options' : ['twenty', 'none', 'sixteen', 'no',]
  },
  {'question': "What was the highest mountain on Earth the day before Mount Everest was discovered?",
  'answer': "Mount Everest was still the highest mountain of Earth the day before it was discovered.",
  'accept': ['everest'],
   'options' : ['everest', 'kilimonjanro', 'savana']
  },
]
CORRECT_TEXT = ['Correct!', 'That is right.', "You're right.",
 'You got it.', 'Righto!']
INCORRECT_TEXT = ['Incorrect!', "Nope, that isn't it.", 'Nope.',
'Not quite.', 'You missed it.']

print('''
 Can you figure out the answers to these trick questions?
 (Enter QUIT to quit at any time.)
''')

input('Press Enter to begin...')

random.shuffle(QUESTIONS)
score = 0

for questionNumber, qa in enumerate(QUESTIONS): 
   print(f'Question: {questionNumber + 1}')
   print(f'Score: {score} / {len(QUESTIONS)}')
   print(f"QUESTION: {qa['question']}")
   print(f"option: {qa['options']}")
   response = input(' ANSWER: ').lower()
   if response == 'quit':
      print('Thanks for playing!')
      sys.exit()
   correct = False
   for acceptanceWord in qa['accept']:
      if acceptanceWord in response:
         correct = True
         if correct:
            text = random.choice(CORRECT_TEXT)
            print(text, qa['answer'])
            score += 1
         else:
            text = random.choice(INCORRECT_TEXT)
            print(text, 'The answer is:', qa['answer'])
            response = input('Press Enter for the next question...').lower()
            if response == 'quit':
               print('Thanks for playing!')
               sys.exit() 
            print("That's all the questions. Thanks for playing!")    

