from testing_assistant import digital_assistant


def test_show_note():
  actual = digital_assistant("how are you")
  expected = "I am well"
  assert  actual == expected
def Test_send_sms():
  actual = digital_assistant('YouTube')
  expected = "Here you go to Youtube\n"
  assert  actual == expected
def test_send_email():
  actual = digital_assistant('Google')
  expected = "Here you go to Google\n"
  assert  actual == expected
def test_open_google():
  actual = digital_assistant('show note')
  expected = "hello"
  assert  actual == expected
def test_read_text_from_image():
  actual = digital_assistant('stop')
  expected = 'Listening stopped'
  assert  actual == expected
