"""
// Time Complexity : O(M*N)
// Space Complexity : O(M*N)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : No

// Your code here along with comments explaining your approach
Algorithm Explanation
Given below
"""
from collections import deque
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        """
        Main idea - BFS/DFS
        1) Put the start position in the queue
        2) while queue is not empty
            - poll the position
            - Get the mines surrounding the position
            - If number of mines = 0
                 - update board value to 'B'(marking visited)
                - For all the 8 directions(within board range and not 'B')
                    - Add the position to queue
        3) return board
        Mines count
            - For all 8 directions, increment the mine count if value is 'M'
            - return the mine count
        """
        def get_mine_count(pos):
            count = 0
            directions = [[0,1],[1,0],[1,-1],[-1,1],[0,-1],[-1,0],[-1,-1],[1,1]]
            for dir in directions:
                new_x = dir[0] + pos[0]
                new_y = dir[1] + pos[1]
                if 0<= new_x < self.m and 0<= new_y < self.n and board[new_x][new_y]=='M':
                    count+=1
            
            return count
        
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board
        board[click[0]][click[1]] = 'B'
        q = deque([click])
        self.m = len(board)
        self.n = len(board[0])
        
        while q:
            pos = q.popleft()
            mines = get_mine_count(pos)
            if mines == 0:
                directions = [[0,1],[1,0],[1,-1],[-1,1],[0,-1],[-1,0],[-1,-1],[1,1]]
                for dirs in directions:
                    new_x = dirs[0] + pos[0]
                    new_y = dirs[1] + pos[1]
                    if 0 <= new_x < self.m and 0 <= new_y < self.n and board[new_x][new_y]=='E':
                        board[new_x][new_y] = 'B'
                        q.append([new_x,new_y])
            else:
                board[pos[0]][pos[1]] = str(mines)
        return board
        
        def dfs(pos):
            #logic
            mines = get_mine_count(pos)
            if mines > 0:
                board[pos[0]][pos[1]] = str(mines)
            else:
                board[pos[0]][pos[1]] = 'B'
                directions = [[0,1],[1,0],[1,-1],[-1,1],[0,-1],[-1,0],[-1,-1],[1,1]]
                for dir in directions:
                    new_x = dir[0] + pos[0]
                    new_y = dir[1] + pos[1]
                    if 0 <= new_x < self.m and 0 <= new_y < self.n and board[new_x][new_y]=='E':
                        dfs([new_x,new_y])
        
        
        dfs(click)
        return board