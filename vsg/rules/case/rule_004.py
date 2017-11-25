
from vsg.rules.case import case_rule


class rule_004(case_rule):
    '''Case rule 004 checks for a single space after the "when" keyword.'''

    def __init__(self):
        case_rule.__init__(self)
        self.identifier = '004'
        self.solution = 'Ensure a single space exists after the "when" keyword.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isCaseWhenKeyword:
                self._is_single_space_after('when', oLine, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._enforce_one_space_after_word(oFile.lines[iLineNumber], 'when')
