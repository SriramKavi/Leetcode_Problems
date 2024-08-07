class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        thousands = ["", "Thousand", "Million", "Billion"]
        res = ""
        idx = 0
        while num > 0:
            if num % 1000 != 0:
                ans = ""
                p = num % 1000
                if p >= 100:
                    ans += ones[p // 100] + " Hundred "
                    p = p % 100
                if p >= 20:
                    ans += tens[p // 10] + " "
                    p = p % 10
                if p > 0:
                    ans += ones[p] + " "
                ans += thousands[idx] + " "
                res = ans + res
            num //= 1000
            idx += 1
        return res.strip()
