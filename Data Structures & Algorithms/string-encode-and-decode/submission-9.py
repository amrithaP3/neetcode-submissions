class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += word + "#WOW#"
        
        return res

    def decode(self, s: str) -> List[str]:
        res = s.split("#WOW#")
        
        return res[0:len(res) - 1]