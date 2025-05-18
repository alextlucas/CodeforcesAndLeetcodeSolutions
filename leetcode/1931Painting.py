class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        mod = 10**9 + 7

        valid = dict()

        #finding ternary numbers for valid rows
        for mask in range(3**m):
            color = []
            temp_mask = mask
            for i in range(m):
                color.append(temp_mask % 3)
                temp_mask //= 3
            if any(color[i] == color[i + 1] for i in range(m - 1)):
                continue
            valid[mask] = color
        
        #for each mask, check which other masks would be valid if adjacent
        adjacent = defaultdict(list)
        for mask1, color1 in valid.items():
            for mask2, color2 in valid.items():
                if not any(x == y for x, y in zip(color1, color2)):
                    adjacent[mask1].append(mask2)
        
        
        #dp state compression
        f = [int(mask in valid) for mask in range(3**m)]
        for i in range(1, n):
            g = [0] * (3**m)
            for mask1 in valid.keys():
                for mask2 in adjacent[mask1]:
                    g[mask1] = (g[mask1] + f[mask2]) % mod
            
            #space optimization, only two arrays needed
            f = g
        
        return sum(f) % mod




