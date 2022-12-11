#!/usr/bin/python3
""" Delete"""
from models.engine.file_storage import FileStorage
from models.state import State

fsd = FileStorage()

all_states = fsd.all(State)
print("All States: {}".format(len(all_states.keys())))
for state_key in all_states.keys():
    print(all_states[state_key])

new_state = State()
new_state.name = "California"
fsd.new(new_state)
fsd.save()
print("New State: {}".format(new_state))

all_states = fsd.all(State)
print("All States: {}".format(len(all_states.keys())))
for state_key in all_states.keys():
    print(all_states[state_key])

another_state = State()
another_state.name = "Nevada"
fsd.new(another_state)
fsd.save()
print("Another State: {}".format(another_state))

all_states = fsd.all(State)
print("All States: {}".format(len(all_states.keys())))
for state_key in all_states.keys():
    print(all_states[state_key])        

fsd.delete(new_state)

all_states = fsd.all(State)
print("All States: {}".format(len(all_states.keys())))
for state_key in all_states.keys():
    print(all_states[state_key])
    