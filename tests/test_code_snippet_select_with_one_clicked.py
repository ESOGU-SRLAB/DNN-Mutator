import unittest
from unittest.mock import patch


# Select Code Snippets wit One Click
def code_snippet_select_with_one_clicked():
    try:
        clicked_item_text = self.ui.code_snippet_list.currentItem().text()

        with open(
            "code_snippets.json", encoding="utf-8"
        ) as code_snippets_from_json:
            code_snippets_name_list = json.load(code_snippets_from_json)

            added_snippet_regex_length = len(
                code_snippets_name_list["code_snippets"]
            )
            for i in range(0, added_snippet_regex_length):
                code_snippet_name = code_snippets_name_list["code_snippets"][i][
                    "Snippets"
                ]["Snippet_Name"]

                if clicked_item_text == code_snippet_name:
                    code_snippet_description = code_snippets_name_list[
                        "code_snippets"
                    ][i]["Snippets"]["Process"]
                    self.ui.textEdit_24.setPlainText(code_snippet_description)
    except AttributeError:
        pass

class TestCodeSnippetSelectWithOneClicked(unittest.TestCase):
    def test_code_snippet_select_with_one_clicked_with_valid_input(self):
        # Test if the function correctly selects the correct description with valid input
        with patch("builtins.open") as mock_open:
            with patch("json.load") as mock_load:
                mock_open.return_value.__enter__.return_value = [
                    {
                        "Snippets": {
                            "Snippet_Name": "My Snippet",
                            "Process": "This is my snippet.",
                        }
                    }
                ]
                self.ui.code_snippet_list.addItem("My Snippet")
                self.ui.code_snippet_list.setCurrentRow(0)
                code_snippet_select_with_one_clicked()
                # Check if the correct description is set
                self.assertEqual(self.ui.textEdit_24.toPlainText(), "This is my snippet.")