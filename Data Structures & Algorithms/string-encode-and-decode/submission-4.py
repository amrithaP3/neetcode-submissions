class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += word + "#,"
        return res

    def decode(self, s: str) -> List[str]:
        res = s.split("#,")
        return res[0:len(res) - 1]
    # def encode(self, strs: List[str]) -> str:
    #     res = ""
    #     for i in range(len(strs)):
    #         res += strs[i]

    #         if i != (len(strs) - 1):
    #             res += "#WORD#"
        
    #     return res

    # def decode(self, s: str) -> List[str]:
    #     res = s.split("#WORD#")

    #     return res