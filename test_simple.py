"""
This script tests the Bag of Holding

01219114 Computer Programming
Week 8, Test Case T1: The SIMPLE Test for the Bag of Holding Problem
(C) 2022 Chawanat Nakasan
Department of Computer Engineering, Kasetsart University
All rights reserved (proprietary, see reason at end of source file)

"""

# Scoring Guide:
# 0~p where p is max points = Your test has been scored for correctness.
# E = an exception occurred
# N = not tested

import traceback
import os
import sys
import re
from email.utils import parseaddr
import git
from pylint.lint import Run as run_pylint
from bag import Bag

class CheckPoint:
    """ Defines a single CheckPoint for testing purposes.
    """

    def __init__(self, cpid, cpname, cpscoremax, cpscoremin = 0):
        """ Creates a new CheckPoint.
            It requires the maximum score. All new CP's start at 0/cpscoremax.
            It also begins with "not graded" state. (special = "N")
        """
        if cpscoremax < cpscoremin:
            raise ValueError
        self.id = cpid
        self.name = cpname
        self.score = 0
        self.scoremax = cpscoremax
        self.scoremin = cpscoremin
        self.special = "N"

    def grade(self, score = None, unflagn = True):
        """ Grades the CheckPoint.
            The general use case is grade() which defaults to giving the CP the
            highest score possible. It also by default removes the "N" flag.
        """
        if score is None:
            self.score = self.scoremax
            self.special = None if unflagn else self.special
        elif self.score > self.scoremax:
            raise ValueError
        elif self.score < self.scoremin:
            raise ValueError
        else:
            self.score = score
            self.special = None if unflagn else self.special

    def set_special(self, s = None):
        """ Sets the special result character the argument s (default: None).
            Note that the program can't autodetect.
        """
        self.special = s

    def e(self):
        """ Shorthand for set_special('E') """
        self.set_special('E')

    def __str__(self):
        if self.special is None:
            return f"{self.score}/{self.scoremax}: {self.name}"
        return f"{self.special}/{self.scoremax}: {self.name}"

class CheckList:
    """ Contains multiple CheckPoints and allows summations.
    """

    def __init__(self):
        self.cp_list = []

    def add_cp(self, cp: CheckPoint):
        """ Adds a new CP, and returns it as a reference. """
        self.cp_list.append(cp)
        return cp

    def points(self):
        return sum([cp.score for cp in self.cp_list])

    def pointsmax(self):
        return sum([cp.scoremax for cp in self.cp_list])

    def printall(self):
        print("= Score Summary =")
        for cp in self.cp_list:
            print(cp)
        print(f"Total: {self.points()}/{self.pointsmax()}")
        print("\nEND")

cl = CheckList()

def shutdown(c = cl):
    """ Spits out all CP's so far (in the CL) and shuts down the test. """
    c.printall()
    sys.exit(0)

#
# CP01: Repo Exists
#

current_cp = cl.add_cp(CheckPoint(
        "01_valid_repo",
        "The submission is a valid git repository",
        5
        ))

try:
    pwd = os.path.dirname(os.path.realpath(__file__))
    repo = git.Repo(pwd)
    current_cp.grade()
except:
    current_cp.e()
    shutdown()

#
# CP02: Branch Correctness
#

current_cp = cl.add_cp(CheckPoint(
        "02_branch_name",
        "Git repo has the correct branch name ('master' XOR 'main')",
        5
        ))

has_master = repo.git.branch("-l", "master").strip() != ""
has_main = repo.git.branch("-l", "main").strip() != ""

try:
    assert has_master ^ has_main
    current_cp.grade()
    primary_branch = "master" if has_master else "main"
    repo.git.checkout(primary_branch)
except git.exc.GitcommandError:
    print("Git checkout failed. Please check your {primary_branch} branch.")
    current_cp.e()
    shutdown()
except AssertionError:
    print("ERROR: You may have only either master or main branch, not both!")
    current_cp.e()
    shutdown()


#
# CP03: File Correctness
#

current_cp = cl.add_cp(CheckPoint(
        "03_filenames",
        "The repository contains 'README.md' and 'bag.py'",
        5
        ))

try:
    to_check = ["README.md", "bag.py"]
    cp03_passed = all([os.path.exists(f) for f in to_check])
    if cp03_passed:
        current_cp.grade()
except:
    print("Some error occurred. It's probably on us. Here's your score card.")
    current_cp.e()
    shutdown()

#
# CP04: README.md
#

cp04a = cl.add_cp(CheckPoint(
        "04a_valid_fullname",
        "The file contains the full name on the 1st line",
        5
        ))
cp04b = cl.add_cp(CheckPoint(
        "04b_email_address",
        "The file contains the email address on the 2nd line",
        5
        ))
cp04c = cl.add_cp(CheckPoint(
        "04c_student_id",
        "The file contains the student ID on the 3rd line",
        5
        ))

PATTERN_NAME = '[a-zA-Z ]+'
PATTERN_ID = '[0-9]{10}'
readme_error = False # This flag prevents CP06 from grading as it requires
                     # user and email verification.

try:
    with open("README.md") as readme:
        readme_name, readme_email, readme_id = [l.strip() for l in readme.readlines()]
        name_match = re.search(PATTERN_NAME, readme_name)
        id_match = re.search(PATTERN_ID, readme_id)
        if name_match and name_match.group(0) == readme_name:
            cp04a.grade()
        if parseaddr(readme_email):
            cp04b.grade()
        if id_match and id_match.group(0) == readme_id:
            cp04c.grade()
except FileNotFoundError as e:
    print("ERROR: We didn't find README.md.")
    cp04a.e()
    cp04b.e()
    cp04c.e()
    readme_error = True
    print(traceback.format_exc())
except Exception as e:
    print("ERROR: Something went wrong during README file inspection.")
    cp04a.e()
    cp04b.e()
    cp04c.e()
    readme_error = True
    print(traceback.format_exc())

#
# CP05a-c: Code Completeness and Object Initialization
#

cp05a = cl.add_cp(CheckPoint(
        "05a_all_methods_correct",
        "The Bag class has all the required methods",
        5
        ))

cp05b = cl.add_cp(CheckPoint(
        "05b_all_attributes_correct",
        "The Bag class has all the required attributes",
        5
        ))

cp05c = cl.add_cp(CheckPoint(
        "05c_init",
        "The Bag.__init__ method is implemented correctly",
        5
        ))

required_methods = {"__init__", "add", "remove", "weight", "items", "dump"}
required_attributes = {"bagweight"}

if required_methods.issubset(set(dir(Bag))):
    cp05a.grade()

# If adding doesn't pass, then we can't do anything else.
add_passed = False

# Attributes created at init won't show up in the Class, so you need to init it
# first. This means we can't test 05b without 05c, sorry ...

try:
    b = Bag()
    cp05c.grade()
except:
    cp05c.e()
    shutdown()

if required_attributes.issubset(set(dir(b))):
    cp05b.grade()

#
# CP05d+i: Adding and Counting
#

cp05d = cl.add_cp(CheckPoint(
        "05d_add",
        "The Bag.add method is implemented correctly",
        5
        ))
cp05i = cl.add_cp(CheckPoint(
        "05i_count",
        "The Bag.count method is implemented correctly",
        5
        ))

try:
    # Basic Test
    b = Bag()
    try:
        for i in range(200):
            b.add(f"stick{i}", i)
    except Exception as e:
        print("ERROR: Exception caught from Bag.add method.")
        print("       Please know that the Bag.count method now cannot be tested.")
        cp05d.e()
        raise
    try:
        if b.count() == 200:
            cp05d.grade(2)
            cp05i.grade()
    except Exception as e:
        print("ERROR: Exception caught from Bag.count method.")
        print("       Neither .add nor .count can be scored. Please recheck.")
        cp05i.e()
        raise

    # Repeated Item Additions
    b = Bag()
    try:
        for i in range(10):
            b.add("egg", 2)
            add_passed = True
        if b.count() == 1:
            cp05d.grade()
    except Exception as e:
        print("ERROR: Exception caught from Bag.add method.")
        print("HINT : This happened while trying to add multiples of the same item.")
        cp05d.e()
        raise
except:
    print(traceback.format_exc())

#
# CP05ef: item removal and weighing
#

cp05e = cl.add_cp(CheckPoint(
        "05e_remove",
        "The Bag.remove method is implemented correctly",
        5
        ))

cp05f = cl.add_cp(CheckPoint(
        "05f_weight",
        "The Bag.weight method is implemented correctly",
        5
        ))

if add_passed:
    try:
        b = Bag(20)
        for i in range(1000):
            b.add(f"{i}", 1)
        try:
            if b.weight() == 1020:
                cp05f.grade()
            elif b.weight() == 1000:
                print("HINT : Did you implement the bag weight correctly?")
                cp05f.grade(2)
            elif b.weight() == 20:
                print("HINT : Did you implement the item weight correctly?")
                cp05f.grade(2)
            else:
                cp05f.grade(0)
        except:
            cp05f.e()
            print("HINT : Your code died somewhere around the Bag.weight test.")
            raise
        try:
            for i in range(1000):
                b.remove(f"{i}")
        except (IndexError, KeyError) as e:
            cp05e.e()
            print("HINT : Did you get your reference right when removing items?")
            raise
        if b.count() == 0:
            cp05e.grade()
    except Exception as e:
        print(traceback.format_exc())

#
# CP05g: items listing
#

cp05g = cl.add_cp(CheckPoint(
        "05g_items",
        "The Bag.items method is implemented correctly",
        5
        ))

if add_passed:
    try:
        b = Bag()
        b.add("potion", 3)
        b.add("egg", 0.2)
        b.add("cheese", 15)
        if sorted(b.items()) == ['cheese', 'egg', 'potion']:
            cp05g.grade()
        else:
            cp05g.grade(0)
    except:
        print("ERROR: Your code died somewhere around the Bag.items test.")
        print(traceback.format_exc())

#
# CP05h: dumping
#

cp05h = cl.add_cp(CheckPoint(
        "05h_dump",
        "The Bag.dump method is implemented correctly",
        5
        ))

if add_passed:
    try:
        b = Bag()
        for i in range(10000):
            b.add(f"{i}", 1)
        b.dump()
        if b.count() == 0:
            cp05h.grade()
        else:
            cp05h.grade(0)
    except:
        print("ERROR: Your code died somewhere around the Bag.dump test.")
        print(traceback.format_exc())

#
# CP05j: No PEP8 violations
#

# Your score will be rounded down.
# The score maxes out at 9, requiring 9.00/10.00 to obtain full marks.

CP05J_MAXSCORE = 9
cp05j = cl.add_cp(CheckPoint(
        "05j_pep8",
        "No PEP8 violations",
        CP05J_MAXSCORE
        ))

print("The following is a report from pylint, the code convention checker ...")
pylint_results = run_pylint(['bag.py'], do_exit = False)
pylint_score = min(int(pylint_results.linter.stats.global_note), CP05J_MAXSCORE)
cp05j.grade(pylint_score)
print("The report ends here.")

#
# CP06: Repository State Check
#

cp06a = cl.add_cp(CheckPoint(
            "06a_commits",
            "Repo contains at least 2 commits made by you.",
            10
            ))

cp06b = cl.add_cp(CheckPoint(
            "06b_msgs",
            "Those two commits contain commit messages at least 5 chars long.",
            6
            ))

if not readme_error:
    print()
    print("CP06: Git Commit Check")
    print(f"Your name in the readme file is {readme_name}")
    print(f"Email address: {readme_email}")
    print("This is the full git log.")
    gitlog = repo.git.log('--pretty=%h#%an#%ae#%s')
    print(gitlog)
    gitlog_lines = gitlog.split('\n')
    verified_name_email = 0
    verified_commit_msg = 0
    for line in gitlog_lines:
        line = line.split("#")
        if (line[1].lower() == readme_name.lower()
           and line[2].lower() == readme_email.lower()):
            verified_name_email += 1
            if len(line[3]) >= 5:
                verified_commit_msg += 1
    cp06a.grade(min(2,verified_name_email)*5)
    cp06b.grade(min(2,verified_commit_msg)*3)

else:
    print("CP06 not checked due to errors in readme file.")

#
# Final Summary
#

cl.printall()
