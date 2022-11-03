class RecurssionEx:
    def reverseArray(self, arr, l, r):
        if l >= r:
            print('reversed array: ', arr)
            return
        self.swap(arr, l, r)
        self.reverseArray(arr, l + 1, r - 1)

    def swap(self, arr, l, r):
        arr[l] = arr[r] + arr[l]
        arr[r] = arr[l] - arr[r]
        arr[l] = arr[l] - arr[r]

    #check if a string is palindrome

    def checkPalindrome(self, str, n, i=0):
        if i >=n/2:
            return True
        if str[i]!=str[n-i-1]:
            return False
        return self.checkPalindrome(str, n, i+1)



recurssionEx = RecurssionEx()

arr = [1,4,5,23,3]

recurssionEx.reverseArray(arr, 0, len(arr)-1)

print(recurssionEx.checkPalindrome('momos',len('moms')))