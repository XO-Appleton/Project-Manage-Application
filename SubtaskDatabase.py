from __future__ import annotations
import json
from os.path import *
from datetime import date

from Subtask import Subtask

class SubtaskDatabase:

    __json_dump_file_name = "progress_db.json"
    __subtask_count: int = None
    __subtask_count_key = "subtask_count"
    __subtasks: dict = None
    __subtasks_key = "subtasks"

    __instance: SubtaskDatabase = None

    def __init__(self):
        self.load_database()

    def add_subtask(self, project_id: int, subtask: Subtask):
        project_id = str(project_id)
        subtask.uid = self.__subtask_count
        self.__subtask_count += 1
        if project_id not in self.__subtasks:
            self.__subtasks[project_id] = []
        self.__subtasks[project_id].append(subtask)
        self.save_database()

    def get_subtasks(self, project_id: int) -> list:
        project_id = str(project_id)
        if not project_id in self.__subtasks:
            return []
        return [subtask.copy() for subtask in self.__subtasks[project_id]]

    def get_subtask(self, project_id: int, subtask_id: int) -> Subtask:
        results = [subtask for subtask in self.get_subtasks(str(project_id)) if subtask.uid == subtask_id]
        if len(results) > 0:
            return results[0].copy()

    def remove_subtasks(self, project_id: int):
        self.__subtasks[str(project_id)] = []
        self.save_database()

    def remove_subtask(self, project_id: int, subtask_id: int):
        project_id = str(project_id)
        subtasks = self.__subtasks[project_id]
        for i in range(len(subtasks)):
            if subtasks[i].uid == subtask_id:
                subtasks.pop(i)
                return

    def modify_subtask(self, project_id: int, subtask: Subtask):
        project_id = str(project_id)
        subtasks = self.__subtasks[project_id]
        for i in range(len(subtasks)):
            if subtasks[i].uid == subtask.uid:
                subtasks.pop(i)
                subtasks.append(subtask)
                return

    def toggle_subtask(self, project_id: int, subtask_id: int):
        old = self.get_subtask(project_id, subtask_id)
        old.completed = not old.completed
        self.modify_subtask(project_id, old)

    def load_database(self):
        self.__subtasks = {}
        if not isfile(self.__json_dump_file_name):
            with open(self.__json_dump_file_name, "w") as fp:
                json.dump({self.__subtask_count_key: 0, self.__subtasks_key: {}}, fp)
        
        with open(self.__json_dump_file_name) as fp:
            raw = json.load(fp)
        self.__subtask_count = raw[self.__subtask_count_key]
        subtask_records = raw[self.__subtasks_key]
        for project_id in subtask_records:
            self.__subtasks[project_id] = [Subtask.reconstruct(d) for d in subtask_records[project_id]]

    def save_database(self):
        json_ready_dict = {}
        for project_id in self.__subtasks:
            json_ready_dict[project_id] = [subtask.get_dict() for subtask in self.__subtasks[project_id]]
        raw = {
            self.__subtask_count_key: self.__subtask_count,
            self.__subtasks_key: json_ready_dict
        }
        with open(self.__json_dump_file_name, "w") as fp:
            json.dump(raw, fp)


    @staticmethod
    def get_instance() -> SubtaskDatabase:
        if SubtaskDatabase.__instance == None:
            SubtaskDatabase.__instance = SubtaskDatabase()
        return SubtaskDatabase.__instance


if __name__ == "__main__":
    sdb = SubtaskDatabase.get_instance()
    # s = Subtask(0, "a", date.today(), False, False, False)
    # sdb.add_subtask(0, s)
    print(sdb.get_subtasks(0)[0].get_dict())