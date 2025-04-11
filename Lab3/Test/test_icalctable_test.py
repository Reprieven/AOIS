import unittest
from unittest.mock import patch
from ITableCalcMethod import (
    show_table_sdnf,
    calc_result_sdnf,
    sdnf_interface_table_calc,
    show_table_sknf,
    calc_result_sknf,
    sknf_interface_table_calc
)

class TestSDNF(unittest.TestCase):

    @patch('ITableCalcMethod.separate_terms_sdnf')
    @patch('ITableCalcMethod.form_table_sdnf')
    def test_show_table_sdnf(self, mock_form_table_sdnf, mock_separate_terms_sdnf):
        # Mocking the behavior of the dependencies
        mock_separate_terms_sdnf.return_value = ["A", "B", "C"]
        mock_form_table_sdnf.return_value = {
            "000": [0, 0, 0],
            "001": [0, 0, 1],
            "010": [0, 1, 0]
        }

        with patch('builtins.print') as mock_print:
            show_table_sdnf("A & B | C")
            mock_print.assert_called_once()  # Ensure the table is printed

    @patch('ITableCalcMethod.table_calc_sdnf')
    @patch('ITableCalcMethod.calc_SDNF')
    def test_calc_result_sdnf(self, mock_calc_SDNF, mock_table_calc_sdnf):
        # Mocking the behavior of the dependencies
        mock_table_calc_sdnf.return_value = {"000", "001"}
        mock_calc_SDNF.return_value = [{"000": 0, "001": 0, "010": 1}]

        result = calc_result_sdnf("A & B | C")
        self.assertEqual(result, {"000": 0, "001": 0})

    @patch('ITableCalcMethod.show_table_sdnf')
    @patch('ITableCalcMethod.calc_result_sdnf')
    @patch('ITableCalcMethod.replace_upper_case_with_inversion')
    def test_sdnf_interface_table_calc(self, mock_replace_inversion, mock_calc_result, mock_show_table):
        # Mocking the behavior of the dependencies
        mock_calc_result.return_value = {"A&B&C": 1}
        mock_replace_inversion.return_value = "¬A&B&¬C"

        with patch('builtins.print') as mock_print:
            sdnf_interface_table_calc("A & B | C")
            mock_print.assert_called_with("¬A&B&¬C")


class TestSKNF(unittest.TestCase):

    @patch('ITableCalcMethod.separate_terms_sknf')
    @patch('ITableCalcMethod.form_table_sknf')
    def test_show_table_sknf(self, mock_form_table_sknf, mock_separate_terms_sknf):
        # Mocking the behavior of the dependencies
        mock_separate_terms_sknf.return_value = ["A", "B", "C"]
        mock_form_table_sknf.return_value = {
            "000": [0, 0, 0],
            "001": [0, 0, 1],
            "010": [0, 1, 0]
        }

        with patch('builtins.print') as mock_print:
            show_table_sknf("A & B | C")
            mock_print.assert_called_once()  # Ensure the table is printed

    @patch('ITableCalcMethod.table_calc_sknf')
    @patch('ITableCalcMethod.calc_SKNF')
    def test_calc_result_sknf(self, mock_calc_SKNF, mock_table_calc_sknf):
        # Mocking the behavior of the dependencies
        mock_table_calc_sknf.return_value = {"000", "001"}
        mock_calc_SKNF.return_value = [{"000": 0, "001": 0, "010": 1}]

        result = calc_result_sknf("A & B | C")
        self.assertEqual(result, {"000": 0, "001": 0})

    @patch('ITableCalcMethod.show_table_sknf')
    @patch('ITableCalcMethod.calc_result_sknf')
    @patch('ITableCalcMethod.add_disjunction')
    @patch('ITableCalcMethod.replace_upper_case_with_inversion')
    def test_sknf_interface_table_calc(self, mock_replace_inversion, mock_add_disjunction, mock_calc_result, mock_show_table):
        # Mocking the behavior of the dependencies
        mock_calc_result.return_value = {"A+B+C": 1}
        mock_add_disjunction.return_value = "(A+B+C)"
        mock_replace_inversion.return_value = "¬A+¬B+¬C"

        with patch('builtins.print') as mock_print:
            sknf_interface_table_calc("A & B | C")
            mock_print.assert_called_with("¬A+¬B+¬C")


if __name__ == "__main__":
    unittest.main()