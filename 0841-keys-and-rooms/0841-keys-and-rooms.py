class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        visited = set()
        visited.add(0) 
        
        def dfs(room):
            for key in rooms[room]:
                if key not in visited:
                    visited.add(key)
                    dfs(key) 
        
        dfs(0)
        

        return len(visited) == len(rooms)
            
        