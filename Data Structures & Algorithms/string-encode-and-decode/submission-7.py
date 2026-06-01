class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += word + "#WORD#"
        
        return res

    def decode(self, s: str) -> List[str]:
        res = s.split("#WORD#")
        return res[0:len(res) - 1]