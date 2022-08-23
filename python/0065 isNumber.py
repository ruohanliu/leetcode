class Solution:
    def isNumber(self, s: str) -> bool:
        """
            #re

            -1.2E3
            ? 0 or 1
            decimal: (\d+\.(\d+)?)|(\.\d+)
            integer: \d+
        """
        a = re.match("^[\+-]?(((\d+\.(\d+)?)|(\.\d+))|(\d+))([eE][\+-]?\d+)?$",s)
        return True if a else False

    def isNumber(self, s: str) -> bool:
        def isDec(s):
            if not s:
                return False
            if s[0] in "+-":
                s = s[1:]
            if s.endswith("."):
                return s[:-1].isdigit()
            elif s.startswith("."):
                return s[1:].isdigit()
            else:
                spl = s.split(".")
                return len(spl) == 2 and spl[0].isdigit() and spl[1].isdigit()

        def isInt(s):
            if not s:
                return False
            if s[0] in "+-":
                s = s[1:]
            return s.isdigit()

        s = s.upper()
        if s.find("E")>=0:
            spl = s.split("E")
            return len(spl) == 2 and (isDec(spl[0]) or isInt(spl[0])) and isInt(spl[1])
        else:
            return isDec(s) or isInt(s)