class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False 

class Solution:
    def findWords(self, board1: List[List[str]], words: List[str]) -> List[str]:
        """
        create trie of words. go through each pos and check for word.
        if has letter matches turn black. back track on way out
        """

        board = board1
        res = []
        root = TrieNode()
        
        for word in words:
            self.insertWord(word, root, 0)

        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(r, c, root, curr):
            nonlocal board
            nonlocal dirs
            nonlocal res
            
            if board[r][c] in root.children and root.children[board[r][c]].is_end_of_word:
                res.append(curr + board[r][c])
                root.children[board[r][c]].is_end_of_word = False 
            
            if board[r][c] != '0' and board[r][c] in root.children:
                temp = board[r][c]
                board[r][c] = '0'
                
                for dx, dy in dirs:
                    if 0 <= r + dy < len(board) and 0 <= c + dx < len(board[0]):
                        dfs(r + dy, c + dx, root.children[temp], curr + temp)
                
                board[r][c] = temp  # RESTORE after exploring all neighbors

        for r in range(len(board)):
            for c in range(len(board[0])):
                dfs(r, c, root, '')

        return res

    def insertWord(self, word, root, i):
        if i == len(word):
            root.is_end_of_word = True
            return
        if word[i] in root.children:
            self.insertWord(word, root.children[word[i]], i + 1)
        else:
            root.children[word[i]] = TrieNode()
            self.insertWord(word, root.children[word[i]], i + 1)