from . import SipsTestCaseBase, get_data
from sippers.file import SipsFile, PackedSipsFile


class TestRegisteredClasses(SipsTestCaseBase):
    def test_registered_class(self):
        from sippers.parsers.parser import _PARSERS

        self.assertItemsEqual(_PARSERS.keys(), [
            'sippers.parsers.iberdrola.Iberdrola',
            'sippers.parsers.endesa.Endesa',
            'sippers.parsers.endesa.EndesaCons'
        ])


class TestParser(SipsTestCaseBase):
    def test_parse_ps(self):
        for dso in self.SIPS_DATA:
            sips_file = self.SIPS_DATA[dso]['file']
            lines = []
            with SipsFile(sips_file) as sf:
                for line in sf:
                    self.assertIn('ps', line)
                    self.assertIn('measures', line)
                    self.assertIn('orig', line)
                    lines.append(line['ps'])
            self.assertEqual(len(lines), 10)
        for dso in self.SIPS_PACKED_DATA:
            sips_file = self.SIPS_PACKED_DATA[dso]['file']
            with PackedSipsFile(sips_file) as psf:
                for sf in psf:
                    lines = []
                    for line in sf:
                        self.assertIn('ps', line)
                        self.assertIn('measures', line)
                        self.assertIn('orig', line)
                        lines.append(line['ps'])
                    self.assertEqual(len(lines), 10)