from typing import Any, Optional, TYPE_CHECKING
from docutils.statemachine import StringList

from sphinx.application import Sphinx
from sphinx.ext.autodoc import FunctionDocumenter, ModuleDocumenter, bool_option
from sphinx.util import inspect

import logging

if TYPE_CHECKING:
    from sphinx.ext.autodoc import Options

logger = logging.getLogger(__name__)

class TestDocumenter(FunctionDocumenter):
    objtype = 'test'
    directivetype = FunctionDocumenter.objtype
    priority = 10 + FunctionDocumenter.priority
    option_spec = dict(FunctionDocumenter.option_spec)

    @classmethod
    def can_document_member(cls, member: Any, membername: str, isattr: bool, parent: Any) -> bool:
        """Check if member can be documented as a test function."""
        try:
            if not FunctionDocumenter.can_document_member(member, membername, isattr, parent):
                return False

            logger.debug("Evaluating test documenter for: %s", membername)
            return membername.startswith('test_') and callable(member)

        except Exception as e:
            logger.warning("Error checking test member %s: %s", membername, e)
            return False

    def add_directive_header(self, sig: str) -> None:
        """Add the directive header and options to the generated content."""
        domain = 'test'
        directive = 'test'
        name = self.format_name()
        sourcename = self.get_sourcename()

        # Remove 'test_' prefix to match domain expectations
        display_name = name[5:] if name.startswith('test_') else name

        # Generate directive with proper formatting
        self.add_line(f'.. {domain}:{directive}:: {display_name}{sig}', sourcename)

    def add_content(self, more_content: Optional[StringList], no_docstring: bool = False) -> None:
        """Add content including pytest marks as suite information."""

        if hasattr(self.object, 'pytestmark') and self.object.pytestmark:
            suite_names = [mark.name for mark in self.object.pytestmark if hasattr(mark, 'name')]
            if suite_names:
                suite_line = f":suite: {','.join(suite_names)}"
                self.add_line(suite_line, self.get_sourcename())

        super().add_content(more_content)


def setup(app: Sphinx) -> dict[str, Any]:
    """Setup the autodoc test extension."""
    app.setup_extension('sphinx.ext.autodoc')  # Require autodoc extension
    app.add_autodocumenter(TestDocumenter)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
