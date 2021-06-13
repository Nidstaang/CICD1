
from unittest import mock
from unittest.mock import patch
from main import bedchamber, laboratory, outside

def test_bedchamber(self):

    with mock.patch('builtins.input', return_value="1"):
        assert bedchamber() == """You lift the trapdoor. Stone stairs that never seem to end. You follow them and encounter a slightly open door.
        You go in and find yourself in an empty, dimly lit room. The stone walls seeem to have witnessed many centuries pass.
        There is shelves filled with books and weird objects that sparkle and make strange sounds. The floor is covered with more books and boxes filled with ingredients.
        You see Fane's empty desk at the end of the room. He is not there. His desk is filled with paper filled with scribbles. You see a polished crate.
        Complicated drawings and maps decorate the wall. You see a shelf with carved wooden details but you can't see what's on top of it.\n\n"""

    with mock.patch('builtins.input', return_value="2"):
        assert bedchamber() == "It seems to be locked through some weird lever mechanism. It won't bulge.\n Let's try the trapdoor."


def test_laboratory(self):

    with mock.patch('builtins.input', return_value="1"):
        assert laboratory() == """A pretty wooden crate sits on top of the desk.
        You open the crate. It's filled with ingredients. An emerald leather pouch grabs your attention.\n"""

    with mock.patch('builtins.input', return_value="3"):
        assert laboratory() == "You decide to go back upstairs. Maybe you missed something?"

def test_outside(self):

    with mock.patch('builtins.input', return_value="1"):
        assert outside() == "To be continued..."

    with mock.patch('builtins.input', return_value="2"):
        assert outside() == "To be continued..."