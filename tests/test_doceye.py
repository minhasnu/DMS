from doceye import doceye

def test_image_to_text():
    assert doceye.image_to_text("test.jpg","thresh")=="Sample text here\n\x0c"
