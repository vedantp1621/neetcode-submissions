class Solution:
    def isPalindrome(self, s: str) -> bool:

        # palindrome: reads same forward as backward

        # case insensitive
        # ignores non alphanumeric

        # set everything to lowercase
        # check if non-alphanumeric (.isalnum)

        # preprocess:
        # set everything lower -> done
        # ignore alphanumeric -> TODO while we move pointers
        # remove spaces. replace() -> done

        # process:
        # two pointers 
        # stop once chars on each side dont match up, or when pointers overlap


        s = s.lower()
        s = s.replace(" ", "")


        left, right = 0, len(s)-1


        print(left, right)

        while left < right:
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue
            
            if s[left] != s[right]:
                return False
            
            left += 1
            right -= 1
            print(left)
            print(right)

        return True


        