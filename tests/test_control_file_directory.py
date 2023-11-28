import unittest


def control_file_directory(file_name):
    """Check the file directory for the unwanted characters"""
    banned_characters = ["(", ")", "[", "]", "?", "<", ">", "\\", "|"]
    for i in file_name:
        if i in banned_characters:
            return False
    return True

class TestControlFileDirectory(unittest.TestCase):
    def test_control_file_directory_with_banned_characters(self):
        # Test if the function correctly detects banned characters
        file_name_with_banned_characters = "my/file?name"
        result = control_file_directory(file_name_with_banned_characters)
        self.assertFalse(result)

    def test_control_file_directory_without_banned_characters(self):
        # Test if the function correctly allows file names without banned characters
        file_name_without_banned_characters = "my_file_name"
        result = control_file_directory(file_name_without_banned_characters)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
