
from vsg.rules import case_rule
from vsg import utils


class rule_016(case_rule):
    '''
    Entity rule 016 checks the when keyword has proper case.
    '''

    def __init__(self):
        case_rule.__init__(self, 'case', '016', 'isCaseWhenKeyword', self._extract_when_keyword)
        self.solution = 'Change when keyword to ' + self.case + 'case'

    def _extract_when_keyword(self, oLine):
        return utils.extract_word(oLine.line, 'when')
