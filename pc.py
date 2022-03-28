import charge as c
import theme as t
from choose import choose_list
pcs = []

class PC():
    def __init__(self):
        pcs.append(self)
        self.name = ""
        self.skills = {}

        for skill in c.Charge.skills:
            self.skills[skill] = 0

        self.momentum = 2
        self.name = input("What is the name of your PC? ")

        self.dots = c.PC_START_DOTS

        print("Which of these 'themes' best describes your character?")
        self.theme = choose_list(t.themes)

        self.organization = False

        self.choose_skills()

        self.display()
    
    def display(self):
        print(f"{self.name}:")
        print(f"Theme: {self.theme}")
        print()
        print("Skills:")
        for action in c.Charge.skills:
            print(f"{action}: {self.skills[action]} dots")

    def choose_skills(self):
        to_assign = {}
        unassigned = self.dots
        for action in c.Charge.skills:
            num_dots = self.dots_for(action, unassigned)
            unassigned -= num_dots
            to_assign[action] = num_dots
        
        print("\nSkills:")
        for action in c.Charge.skills:
            print(f"{action}: {self.skills[action]}+{to_assign[action]} dots")

        if unassigned > 0:
            print("Warning: you have unassigned action dots remaining.")
            print("You will be able to assign them at the next milestone.")

        print("Is this correct?")
        if choose_list(["yes", "no"]) == "yes":
            for skill in to_assign.keys():
                self.skills[skill] += to_assign[skill]
            self.dots = unassigned
        else:
            self.choose_skills()


    def dots_for(self, skill, unassigned):
        if unassigned == 0:
            return 0

        print(f"{unassigned} unassigned skill dots")
        try:
            answer = int(input(f"Assign how many dots to {skill}? (max {c.MAX_SKILL_DOTS}) "))
        except:
            print("Invalid response")
            answer = self.dots_for(skill, unassigned)
        
        if answer > c.MAX_SKILL_DOTS:
            print("This system makes PCs be somewhat versatile by limiting the number of skill dots that can be assigned to one skill.")
            print(f"Please choose between 0 and {c.MAX_SKILL_DOTS} dots to assign to this skill.")
            answer = self.dots_for(skill, unassigned)

        if answer > unassigned:
            print("You do not have enough skill dots left for that.")
            answer = self.dots_for(skill, unassigned)

        if answer < 0:
            print("Quit messing with me. Skills can't be negative.")
            answer = self.dots_for(skill, unassigned)

        return answer

if __name__ == "__main__":
    pc = PC()