from room import Room
class Map:
    def __init__(self):
        self.last_room = 0
        self.rooms = {}
        self.adj_rooms = {}

    def load_graph(self, room_graph):
        num_rooms = len(room_graph)
        rooms = [None] * num_rooms
        grid_size = 1
        for i in range(0, num_rooms):
            x = room_graph[i][0][0]
            grid_size = max(grid_size, room_graph[i][0][0], room_graph[i][0][1])
            self.rooms[i] = Room(f"Room {i}", f"({room_graph[i][0][0]},{room_graph[i][0][1]})",i, room_graph[i][0][0], room_graph[i][0][1])
        self.room_grid = []
        grid_size += 1
        self.grid_size = grid_size
        for i in range(0, grid_size):
            self.room_grid.append([None] * grid_size)
        # for room_id in room_graph:
        #     room = self.rooms[room_id]
        #     self.room_grid[room.x][room.y] = room
        #     if 'n' in room_graph[room_id][1]:
        #         self.rooms[room_id].connect_rooms('n', self.rooms[room_graph[room_id][1]['?']])
        #     if 's' in room_graph[room_id][1]:
        #         self.rooms[room_id].connect_rooms('s', self.rooms[room_graph[room_id][1]['?']])
        #     if 'e' in room_graph[room_id][1]:
        #         self.rooms[room_id].connect_rooms('e', self.rooms[room_graph[room_id][1]['?']])
        #     if 'w' in room_graph[room_id][1]:
        #         self.rooms[room_id].connect_rooms('w', self.rooms[room_graph[room_id][1]['?']])
        self.starting_room = self.rooms[0]