# Autocomplete System

* this project takes prefix from the user and provide suggestions for possible  words.
* You can run the program using the instructions in *To Run* below.
* You can test technical correctness by running the unit tests as in the section *To Test* below.

### To Run

* `python3 autocomplete/trie.py`
* follow the input prompts to use the auto suggestion
* you can enter one letter and hit enter to see if there are suggestions for the entered prefix

### To Test

* To run all the unittests: `python3 -m unittest tests/test_auto_complete.py`
* To run a specific step's unittest: `python3 -m unittest tests.test_auto_complete.MyTestCase.test_prefix_found`
