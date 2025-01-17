"""Test Jac cli module."""
import io
import sys

from jaclang.cli import cmds
from jaclang.utils.test import TestCase


class ImportPassPassTests(TestCase):
    """Test pass module."""

    def setUp(self) -> None:
        """Set up test."""
        return super().setUp()

    def test_jac_cli_load(self) -> None:
        """Basic test for pass."""
        captured_output = io.StringIO()
        sys.stdout = captured_output

        # Execute the function
        cmds.load(self.fixture_abs_path("hello.jac"))  # type: ignore

        sys.stdout = sys.__stdout__
        stdout_value = captured_output.getvalue()

        # Assertions or verifications
        self.assertIn("Hello World!", stdout_value)

    def test_jac_cli_err_output(self) -> None:
        """Basic test for pass."""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        sys.stderr = captured_output

        # Execute the function
        try:
            cmds.run(self.fixture_abs_path("err.jac"), entrypoint="speak", args=[])  # type: ignore
        except Exception as e:
            print(f"Error: {e}")

        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__
        stdout_value = captured_output.getvalue()
        # print(stdout_value)
        # Assertions or verifications
        self.assertIn("*4:", stdout_value)
        self.assertIn("*7:", stdout_value)
