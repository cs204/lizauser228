import itertools
import random

class Minesweeper():
    def __init__(self, height=8, width=8, mines=8):
        self.height = height
        self.width = width
        self.mines = set()
        self.board = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(False)
            self.board.append(row)
        while len(self.mines) != mines:
            i = random.randrange(height)
            j = random.randrange(width)
            if not self.board[i][j]:
                self.mines.add((i, j))
                self.board[i][j] = True
        self.mines_found = set()

    def is_mine(self, cell):
        i, j = cell
        return self.board[i][j]

    def nearby_mines(self, cell):
        count = 0
        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):
                if (i, j) == cell:
                    continue
                if 0 <= i < self.height and 0 <= j < self.width:
                    if self.board[i][j]:
                        count += 1
        return count

    def won(self):
        return self.mines_found == self.mines


class Sentence():

    def __init__(self, cells, count):
        self.cells = set(cells)
        self.count = count

    def __eq__(self, other):
        return self.cells == other.cells and self.count == other.count

    def __str__(self):
        return f"{self.cells} = {self.count}"

    def known_mines(self):
        if len(self.cells) == self.count and self.count != 0:
            return self.cells
        else:
            return set()

    def known_safes(self):
        if self.count == 0:
            return self.cells
        else:
            return set()

    def mark_mine(self, cell):
        if cell in self.cells:
            self.cells.remove(cell)
            self.count -= 1

    def mark_safe(self, cell):
        if cell in self.cells:
            self.cells.remove(cell)

class MinesweeperAI():

    def __init__(self, height=8, width=8):
        self.height = height
        self.width = width
        self.moves_made = set()
        self.mines = set()
        self.safes = set()
        self.knowledge = []

    def mark_mine(self, cell):
        self.mines.add(cell)
        for sentence in self.knowledge:
            sentence.mark_mine(cell)

    def mark_safe(self, cell):
        self.safes.add(cell)
        for sentence in self.knowledge:
            sentence.mark_safe(cell)

    def add_knowledge(self, cell, count):
        self.moves_made.add(cell)
        self.mark_safe(cell)
        new_sentence_cells = set()
        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):
                if (i, j) == cell:
                    continue
                if (i, j) in self.safes:
                    continue
                if (i, j) in self.mines:
                    count = count - 1
                    continue
                if 0 <= i < self.height and 0 <= j < self.width:
                    new_sentence_cells.add((i, j))
        self.knowledge.append(Sentence(new_sentence_cells, count))
        knowledge_changed = True
        while knowledge_changed:
            knowledge_changed = False
            safes = set()
            mines = set()
            for sentence in self.knowledge:
                safes = safes.union(sentence.known_safes())
                mines = mines.union(sentence.known_mines())
            if safes:
                knowledge_changed = True
                for safe in safes:
                    self.mark_safe(safe)
            if mines:
                knowledge_changed = True
                for mine in mines:
                    self.mark_mine(mine)
            empty = Sentence(set(), 0)
            self.knowledge[:] = [x for x in self.knowledge if x != empty]
            for sentence_1 in self.knowledge:
                for sentence_2 in self.knowledge:
                    if sentence_1.cells == sentence_2.cells:
                        continue
                    if sentence_1.cells == set() and sentence_1.count > 0:
                        raise ValueError
                    if sentence_1.cells.issubset(sentence_2.cells):
                        new_sentence_cells = sentence_2.cells - sentence_1.cells
                        new_sentence_count = sentence_2.count - sentence_1.count
                        new_sentence = Sentence(new_sentence_cells, new_sentence_count)
                        if new_sentence not in self.knowledge:
                            knowledge_changed = True
                            self.knowledge.append(new_sentence)

    def make_safe_move(self):
        safe_moves = self.safes - self.moves_made
        if safe_moves:
            return random.choice(list(safe_moves))
        return None

    def make_random_move(self):
        moves = {}
        MINES = 8
        num_mines_left = MINES - len(self.mines)
        spaces_left = (self.height * self.width) - (len(self.moves_made) + len(self.mines))
        if spaces_left == 0:
            return None
        basic_prob = num_mines_left / spaces_left
        for i in range(0, self.height):
            for j in range(0, self.width):
                if (i, j) not in self.moves_made and (i, j) not in self.mines:
                    moves[(i, j)] = basic_prob
        if moves and not self.knowledge:
            move = random.choice(list(moves.keys()))
            return move
        elif moves:
            for sentence in self.knowledge:
                num_cells = len(sentence.cells)
                count = sentence.count
                mine_prob = count / num_cells
                for cell in sentence.cells:
                    if moves[cell] < mine_prob:
                        moves[cell] = mine_prob

            move_list = [[x, moves[x]] for x in moves]
            move_list.sort(key=lambda x: x[1])
            best_prob = move_list[0][1]
            best_moves = [x for x in move_list if x[1] == best_prob]
            move = random.choice(best_moves)[0]
            return move