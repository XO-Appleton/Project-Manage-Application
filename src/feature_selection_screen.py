class FeatureSelectionScreen:

    def __init__(self):
        pass

    def display_options(self, branch_names: list):
        print("The following branches are available:")
        for name in branch_names:
            print(name)

    def get_branch_choice(self) -> str:
        return input("Select one branch, type in the name exactly as displayed:\n")