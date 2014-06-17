"""TO-DO: Write a description of what this XBlock is."""

import pkg_resources

from xblock.core import XBlock
from xblock.fields import Scope, Integer, String
from xblock.fragment import Fragment

class pdfXBlock(XBlock):
    """
    TO-DO: document what your XBlock does.
    """
    # Fields are defined on the class.  You can access them in your code as
    # self.<fieldname>.
    # TO-DO: change the default href so it is included as a resource in the xblock, not an url
    href = String(display_name="href",
                  default="http://www.upv.es/miw/infoweb/vcamp/info/plano-upv-es.pdf",
                  scope=Scope.content,
                  help="PDF file that will be shown in the XBlock")

    display_name = String(display_name="Display Name",
                          default="PDF File",
                          scope=Scope.settings,
                          help="Name of the component in the edxplatform")

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")


    def student_view(self, context=None):
        """
        The primary view of the pdfXBlock, shown to students
        when viewing courses.
        """
        html = self.resource_string("static/html/pdf.html")
        frag = Fragment(html.format(self=self))
        frag.add_css(self.resource_string("static/css/pdf.css"))
        return frag


    def studio_view(self, context=None):
        """
        The primary view of the paellaXBlock, shown to students
        when viewing courses.
        """
        html = self.resource_string("static/html/pdf_edit.html")
        frag = Fragment(html.format(self=self))
        frag.add_javascript(self.resource_string("static/js/src/pdf_edit.js"))
        frag.initialize_js('pdfXBlock')
        return frag

    @XBlock.json_handler
    def save_pdf(self, data, suffix=''):
        """
        An example handler, which increments the data.
        """
        self.href = data['href']
        self.display_name = data['display_name']

        return {
            'result': 'success',
        }

    # TO-DO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("pdfXBlock",
             """<vertical_demo>
                <pdf/>
                </vertical_demo>
             """),
        ]