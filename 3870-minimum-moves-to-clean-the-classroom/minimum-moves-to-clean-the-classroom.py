from collections import deque

class Solution(object):
    def minMoves(self, classroom, energy):
        m = len(classroom)
        n = len(classroom[0])

        litter_id = {}
        start_row = start_col = 0
        litter_count = 0

        for row in range(m):
            for col in range(n):
                if classroom[row][col] == 'S':
                    start_row, start_col = row, col
                elif classroom[row][col] == 'L':
                    litter_id[(row, col)] = litter_count
                    litter_count += 1

        target_mask = (1 << litter_count) - 1
        if target_mask == 0:
            return 0

        queue = deque()
        queue.append((start_row, start_col, 0, energy, 0))

        # Stores maximum remaining energy for each position and litter mask.
        best_energy = {
            (start_row, start_col, 0): energy
        }

        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        while queue:
            row, col, mask, remaining, moves = queue.popleft()

            if remaining == 0:
                continue

            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc

                if (new_row < 0 or new_row >= m or
                        new_col < 0 or new_col >= n or
                        classroom[new_row][new_col] == 'X'):
                    continue

                new_energy = remaining - 1
                new_mask = mask
                cell = classroom[new_row][new_col]

                if cell == 'R':
                    new_energy = energy

                if cell == 'L':
                    index = litter_id[(new_row, new_col)]
                    new_mask |= (1 << index)

                if new_mask == target_mask:
                    return moves + 1

                state = (new_row, new_col, new_mask)

                if best_energy.get(state, -1) >= new_energy:
                    continue

                best_energy[state] = new_energy
                queue.append(
                    (new_row, new_col, new_mask, new_energy, moves + 1)
                )

        return -1
        