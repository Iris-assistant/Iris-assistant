from testing_assistant import digital_assistant


def test_how_are_you():
  actual = digital_assistant("how are you")
  expected = "I am well"
  assert  actual == expected
def test_open_youtube():
  actual = digital_assistant('YouTube')
  expected = "Here you go to Youtube\n"
  assert  actual == expected
def test_open_google():
  actual = digital_assistant('Google')
  expected = "Here you go to Google\n"
  assert  actual == expected
def test_show_note():
  actual = digital_assistant('show note')
  expected = "hello"
  assert  actual == expected
def test_stop_assistant():
  actual = digital_assistant('stop')
  expected = 'Listening stopped'
  assert  actual == expected
def test_missed_voice():
  actual = digital_assistant('dgfdg')
  expected = "Sorry! can you repeat .. "
  assert  actual == expected
