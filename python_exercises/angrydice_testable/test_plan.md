# AngryDice Test Plan

AngryDice functions:

* 'check_angry'
* 'check_roll'
* 'clean_input'
* 'game_controller'
* 'game_instructions'
* 'get_roll'
* 'is_cheat'
* 'print_roll'

## check_angry

* set both dice values to angry
 * function returns to true
* set both dice values to angry
 * user's current stage is set to stage 1
* set both dice values to anything but angry
 * current stage doesn't change
* set "a" dice to angry, other to any other value
 * current stage doesn't change
* set "b" dice to angry, other to any other value
 * current stage doesn't change

## check_roll

* check if we have met all stage exit conditions, move to next stage
* check if we don't move to the next stage if we haven't met all stage conditions.
    
## clean_input

* pass in random strings
* pass with multiple a & b
* always return a len(list) <= 2
* values of list can only be "a" or "b"
 
## game_instructions

* test input starts with a return key
* check instruction print output

## get_roll

* check if while loop ends when the input is `exit`
* check if parsed_input isn't a list, we don't fall apart at the seams.
* check if parsed_input is len 0
* check if parsed_input is len 1
* check if parsed_input is len 2
* check if return contains "a" if that was input, and "b" if that was input

## is_cheat

* check if user is holding 6, should return True
* check if user is holding any dice that are not part of the current stage's exit conditions
* check if user is holding a dice that is allowed, return False

## print_roll

* prints cheater if arg is set to true
* doesn't print cheater statment if arg is set to false
* prints correct dice values for dice a and dice